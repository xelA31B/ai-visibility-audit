# AI Visibility & GEO Audit — Claude plugin

**GEO (Generative Engine Optimization) / AEO audit.** Find out how your brand shows up in AI assistants (ChatGPT, Claude, Perplexity, Gemini) and get a concrete plan to be mentioned and recommended more often.

## What it does

| Skill | What you get |
|-------|--------------|
| **ai-visibility-audit** | Full audit: buyer questions to AI, whether the brand is mentioned, competitors, cited sources, site readiness, score 0–100, prioritized action plan. Simple mode (business owner) or Pro mode (marketer / agency, client-ready). |
| **ai-bot-access-check** | 2-minute technical check: which AI crawlers your robots.txt allows or blocks, llms.txt, sitemap, JavaScript-only rendering. |
| **ai-readiness-fixes** | Ready-to-paste fixes: llms.txt, robots.txt rules, schema.org JSON-LD, FAQ, "About" text, directory checklist. |

## Install

**Claude app (web, desktop):** Plugins → add a marketplace from a GitHub repository → `xelA31B/ai-visibility-audit` → install **AI Visibility & GEO Audit**. Once approved in the Claude directory, search for **AI Visibility & GEO Audit** in Plugins.

**Claude Code (VS Code or terminal):**

```
/plugin marketplace add xelA31B/ai-visibility-audit
/plugin install ai-visibility-audit@ai-visibility-audit
```

## Commands

Type `/` in Claude and pick a command:

| Command | What it does |
|---|---|
| `/geo-audit [company] [website] [market]` | AI visibility (GEO) audit of a brand |
| `/geo-bot-check [website]` | Check which AI bots can access a website |
| `/geo-fixes [website or audit]` | Ready-to-paste GEO fixes: llms.txt, schema, FAQ, robots.txt |

## How to use

Just ask Claude, in any language:

- "Audit AI visibility for Acme Dental, acmedental.com, dentist in Budapest"
- "Сделай аудит видимости в ИИ для компании …"
- "Check if AI bots can access example.com"
- "Create llms.txt and schema markup for my site"

## Limitations

- The plugin runs inside Claude and cannot query ChatGPT, Perplexity or Gemini directly. It uses web search and Claude's own knowledge, and you can paste answers from other assistants to include them in the report.
- AI answers vary between sessions and models; treat results as a snapshot and re-check monthly.
- Every finding is labelled as checked, user-provided or estimate. Nothing is invented.

## Requirements

Web search and web fetch enabled in Claude. No API keys or accounts needed.

## License

MIT
