# AI Visibility Audit — Claude plugin

Find out how your brand shows up in AI assistants (ChatGPT, Claude, Perplexity, Gemini) and get a concrete plan to be mentioned and recommended more often.

## What it does

| Skill | What you get |
|-------|--------------|
| **ai-visibility-audit** | Full audit: buyer questions to AI, whether the brand is mentioned, competitors, cited sources, site readiness, score 0–100, prioritized action plan. Simple mode (business owner) or Pro mode (marketer / agency, client-ready). |
| **ai-bot-access-check** | 2-minute technical check: which AI crawlers your robots.txt allows or blocks, llms.txt, sitemap, JavaScript-only rendering. |
| **ai-readiness-fixes** | Ready-to-paste fixes: llms.txt, robots.txt rules, schema.org JSON-LD, FAQ, "About" text, directory checklist. |

## Install

Add it from the Claude directory (claude.ai/directory) once published, or upload the `.plugin` file from the Releases page.

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
