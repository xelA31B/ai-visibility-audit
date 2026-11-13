---
name: ai-bot-access-check
description: >
  This skill should be used when the user asks to "check if AI bots can access my site",
  "is my site blocking ChatGPT", "check robots.txt for AI crawlers", "do I have llms.txt",
  "can Claude/Perplexity read my website", or needs a quick technical check of a website's
  readiness for AI crawlers and AI agents. Also used as Step 4 of the ai-visibility-audit skill.
metadata:
  version: "0.1.0"
---

# AI Bot Access Check

Quick technical check (about 2 minutes) of whether AI assistants and their crawlers can reach and read a website. Report in the user's language.

## Steps

1. **Get the domain.** Normalize to `https://domain`.
2. **Fetch `/robots.txt`.** For each bot in `references/ai-bots.md`, determine: allowed, blocked (whole site or key sections), or not mentioned (= allowed by default unless `User-agent: *` blocks it). Note `Crawl-delay` and `Sitemap:` lines.
3. **Fetch `/llms.txt`** (and `/llms-full.txt`). Record present / absent; if present, check it has a title, a one-paragraph summary and links to key pages.
4. **Check the sitemap** (from robots.txt or `/sitemap.xml`): present / absent, roughly how many URLs.
5. **Fetch the homepage.** If the fetched text is nearly empty or only shows loading placeholders, flag "content likely rendered by JavaScript only — many AI crawlers will not see it".

If any fetch fails (blocked by the tool or the site), ask the user to open the URL in their browser and paste the content, or mark the item **not checked**. Never guess robots.txt contents.

## Interpretation rules

- Blocking **training** bots (GPTBot, Google-Extended, CCBot, Applebot-Extended, etc.) is a legitimate business choice and does not stop the site appearing in AI answers. Present it neutrally.
- Blocking **search/retrieval** and **user-triggered** bots (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User) directly reduces visibility in AI answers — flag as a problem.
- A firewall/CDN can block bots even when robots.txt allows them; mention this as a possibility if pages fail to load for fetches but load for the user.

## Output

A table: Bot | Company | Purpose (training / search / user-triggered) | Status (allowed / blocked / not mentioned) | Impact on AI visibility.
Then 3 lines: llms.txt status, sitemap status, rendering status.
Finish with up to 3 concrete fixes and offer to generate them with `ai-readiness-fixes`.

## When a page or file cannot be fetched

Some Claude apps only open URLs that appear in the conversation or in search results, and refuse addresses Claude builds itself (for example `https://site/robots.txt`). When a fetch is refused:

1. In Claude Code, use the environment's web fetch or an HTTP GET from the terminal instead.
2. Otherwise, try to reach the same page through web search and fetch the result link.
3. If that also fails, give the user the exact links in one message and ask them to open them and paste the content; continue with what is available meanwhile.
4. Mark every item that could not be checked as **not checked** in the report, never as passed, and exclude it from the score.

## Branded report

If the environment can render HTML artifacts or files, deliver the full report using `references/report-template.md` (fill the placeholders, keep the design and colours; use the score ring for the main score and status chips for pass / warn / fail / not checked). Otherwise use the markdown format above. Keep the chat reply to a short summary either way.
