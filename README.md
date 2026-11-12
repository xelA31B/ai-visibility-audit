# AI Visibility Audit PRO — Claude plugin

Everything in the free **ai-visibility-audit**, plus live checks: the plugin asks **ChatGPT** and **Perplexity** the buyer questions directly through their APIs and compares their real answers and cited sources with Claude's view.

## What's inside

| Part | What it does |
|------|--------------|
| **ai-visibility-audit** skill | Full audit with a 3-engine table: ChatGPT / Perplexity / Claude, mentions, positions, competitors, sources, score 0–100, action plan |
| **ai-bot-access-check** skill | robots.txt rules for AI bots, llms.txt, sitemap, JS rendering |
| **ai-readiness-fixes** skill | Ready-to-paste llms.txt, robots rules, schema.org, FAQ, About text |
| **ai-engines** server | Tools `ask_chatgpt`, `ask_perplexity`, `check_engine_keys` (no extra installs, uses Python 3) |

## Setup: API keys (once)

1. Get keys:
   - OpenAI: platform.openai.com → API keys (add a small balance, e.g. $5)
   - Perplexity: perplexity.ai → Settings → API (add a small balance)
2. Create the file `~/.ai-visibility-pro/keys.json` (in your home folder):

```json
{
  "openai": "sk-...",
  "perplexity": "pplx-..."
}
```

One key is enough; the audit uses whichever engines are configured. Alternatively set environment variables `OPENAI_API_KEY` and `PERPLEXITY_API_KEY`.

Optional: `"openai_model"` (default `gpt-5.6`) and `"perplexity_model"` (default `sonar`).

3. Restart Claude and ask: "check engine keys". It should report both as configured.

Keys stay on your computer and are sent only to OpenAI and Perplexity. Never paste keys into a chat.

## Install

Upload the `ai-visibility-audit-pro.plugin` file in the Claude desktop app or Claude Code. Requires Python 3 on the computer (preinstalled on macOS and most Linux; on Windows install from python.org).

## Usage

"Сделай про-аудит видимости в ИИ для [company], [site], [what and where]"

## Cost

About 1–5 cents per question per engine. A typical 10-question audit on two engines costs well under $1.

## License

MIT
