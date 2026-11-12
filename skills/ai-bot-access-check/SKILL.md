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
