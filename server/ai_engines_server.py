#!/usr/bin/env python3
"""AI Engines MCP server (stdio, no dependencies).

Lets Claude ask ChatGPT (OpenAI Responses API + web_search) and Perplexity (Sonar API)
the same buyer questions a customer would ask, and returns their real answers with cited sources.

API keys are read from (first match wins):
  1. Environment variables OPENAI_API_KEY / PERPLEXITY_API_KEY
  2. ~/.ai-visibility-pro/keys.json  ->  {"openai": "sk-...", "perplexity": "pplx-..."}
Optional overrides: OPENAI_MODEL (default gpt-5.6), PERPLEXITY_MODEL (default sonar),
or "openai_model" / "perplexity_model" in keys.json.
"""
import json
import os
import sys
import urllib.error
import urllib.request

SERVER_NAME = "ai-engines"
SERVER_VERSION = "0.1.0"
KEYS_FILE = os.path.join(os.path.expanduser("~"), ".ai-visibility-pro", "keys.json")
TIMEOUT = 120


def load_config():
    cfg = {}
    try:
        with open(KEYS_FILE, encoding="utf-8") as f:
            cfg = json.load(f) or {}
    except (OSError, ValueError):
        cfg = {}
    return {
        "openai": os.environ.get("OPENAI_API_KEY") or cfg.get("openai"),
        "perplexity": os.environ.get("PERPLEXITY_API_KEY") or cfg.get("perplexity"),
        "openai_model": os.environ.get("OPENAI_MODEL") or cfg.get("openai_model") or "gpt-5.6",
        "perplexity_model": os.environ.get("PERPLEXITY_MODEL") or cfg.get("perplexity_model") or "sonar",
    }


def http_post(url, key, payload):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:500]
        raise RuntimeError(f"HTTP {e.code}: {body}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error: {e.reason}")


def ask_chatgpt(prompt, country=None):
    cfg = load_config()
    if not cfg["openai"]:
        raise RuntimeError(f"No OpenAI API key. Set OPENAI_API_KEY or add \"openai\" to {KEYS_FILE}.")
    tool = {"type": "web_search"}
    if country:
        tool["user_location"] = {"type": "approximate", "country": country.upper()[:2]}
    data = http_post(
        "https://api.openai.com/v1/responses",
        cfg["openai"],
        {"model": cfg["openai_model"], "tools": [tool], "input": prompt},
    )
    texts, sources = [], []
    for item in data.get("output", []):
        if item.get("type") != "message":
            continue
        for part in item.get("content", []):
            if part.get("type") == "output_text":
                texts.append(part.get("text", ""))
                for ann in part.get("annotations", []) or []:
                    if ann.get("type") == "url_citation" and ann.get("url"):
                        sources.append({"title": ann.get("title", ""), "url": ann["url"]})
    seen, uniq = set(), []
    for s in sources:
        if s["url"] not in seen:
            seen.add(s["url"])
            uniq.append(s)
    return {"engine": "ChatGPT", "model": cfg["openai_model"], "answer": "\n".join(texts).strip(), "sources": uniq}


def ask_perplexity(prompt, country=None):
    cfg = load_config()
    if not cfg["perplexity"]:
        raise RuntimeError(f"No Perplexity API key. Set PERPLEXITY_API_KEY or add \"perplexity\" to {KEYS_FILE}.")
    payload = {"model": cfg["perplexity_model"], "messages": [{"role": "user", "content": prompt}]}
    if country:
        payload["web_search_options"] = {"user_location": {"country": country.upper()[:2]}}
    data = http_post("https://api.perplexity.ai/chat/completions", cfg["perplexity"], payload)
    answer = ""
    choices = data.get("choices") or []
    if choices:
        answer = (choices[0].get("message") or {}).get("content", "")
    sources = []
    for r in data.get("search_results") or []:
        if r.get("url"):
            sources.append({"title": r.get("title", ""), "url": r["url"]})
    if not sources:
        sources = [{"title": "", "url": u} for u in (data.get("citations") or [])]
    return {"engine": "Perplexity", "model": cfg["perplexity_model"], "answer": answer.strip(), "sources": sources}


PROMPT_SCHEMA = {
    "type": "object",
    "properties": {
        "prompt": {"type": "string", "description": "The buyer question, exactly as a customer would type it."},
        "country": {"type": "string", "description": "Optional 2-letter country code to localize search, e.g. HU, DE, US."},
    },
    "required": ["prompt"],
}

TOOLS = [
    {
        "name": "ask_chatgpt",
        "description": "Ask ChatGPT (OpenAI API with web search) a question and get its real answer plus cited sources.",
        "inputSchema": PROMPT_SCHEMA,
    },
    {
        "name": "ask_perplexity",
        "description": "Ask Perplexity (Sonar API) a question and get its real answer plus cited sources.",
        "inputSchema": PROMPT_SCHEMA,
    },
    {
        "name": "check_engine_keys",
        "description": "Report which AI engine API keys are configured (never reveals the keys).",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def call_tool(name, args):
    if name == "check_engine_keys":
        cfg = load_config()
        return {
            "openai_configured": bool(cfg["openai"]),
            "perplexity_configured": bool(cfg["perplexity"]),
            "openai_model": cfg["openai_model"],
            "perplexity_model": cfg["perplexity_model"],
            "keys_file": KEYS_FILE,
        }
    prompt = (args or {}).get("prompt", "").strip()
    if not prompt:
        raise RuntimeError("Missing 'prompt'.")
    country = (args or {}).get("country")
    if name == "ask_chatgpt":
        return ask_chatgpt(prompt, country)
    if name == "ask_perplexity":
        return ask_perplexity(prompt, country)
    raise RuntimeError(f"Unknown tool: {name}")


def send(msg):
    sys.stdout.write(json.dumps(msg, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def handle(req):
    method, rid = req.get("method"), req.get("id")
    if rid is None:
        return  # notification
    if method == "initialize":
        pv = (req.get("params") or {}).get("protocolVersion", "2025-06-18")
        send({"jsonrpc": "2.0", "id": rid, "result": {
            "protocolVersion": pv,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        }})
    elif method == "ping":
        send({"jsonrpc": "2.0", "id": rid, "result": {}})
    elif method == "tools/list":
        send({"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}})
    elif method == "tools/call":
        p = req.get("params") or {}
        try:
            result = call_tool(p.get("name"), p.get("arguments"))
            send({"jsonrpc": "2.0", "id": rid, "result": {
                "content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}]}})
        except Exception as e:  # report as tool error, keep server alive
            send({"jsonrpc": "2.0", "id": rid, "result": {
                "content": [{"type": "text", "text": f"Error: {e}"}], "isError": True}})
    else:
        send({"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": f"Method not found: {method}"}})


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except ValueError:
            continue
        handle(req)


if __name__ == "__main__":
    main()
