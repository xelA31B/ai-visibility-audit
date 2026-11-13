---
name: ai-readiness-fixes
description: >
  This skill should be used when the user asks to "fix my AI visibility", "create llms.txt",
  "write schema markup for my business", "generate FAQ for AI search", "update robots.txt for AI bots",
  "make my site readable for ChatGPT", or after an ai-visibility-audit or ai-bot-access-check
  when the user wants the recommended fixes prepared.
metadata:
  version: "0.1.0"
---

# AI Readiness Fixes

Turn audit findings into ready-to-paste assets. Use facts from the audit and the website only; ask the user to confirm any fact not found on the site (address, prices, founding year, etc.). Never invent reviews, awards, statistics or customer names.

## Assets to offer

Ask which ones the user wants (default: the first four):

1. **llms.txt** — Markdown file for the site root:
   - `# Brand name`
   - `> One-paragraph summary: what, for whom, where.`
   - Sections (`## Services`, `## About`, `## Contact`) with links to key pages and one-line descriptions.
2. **robots.txt rules for AI bots** — allow search and user-triggered AI bots; ask the user whether to allow or block training bots (business choice). Show only the lines to add, plus where the sitemap line goes.
3. **schema.org JSON-LD** — `Organization` or `LocalBusiness` (with name, url, logo, address, telephone, sameAs links to official profiles), plus `FAQPage` built from item 4. Output as a `<script type="application/ld+json">` block.
4. **FAQ block** — 6–10 questions taken from the audit's buyer prompts, each answered in 2–3 factual sentences that name the brand, the service and the location.
5. **"About" summary** — a 60–100 word paragraph for the homepage stating what the company does, for whom, where and what makes it different.
6. **Directory & review checklist** — the specific platforms where competitors are present and the brand is not, with links.

## Output rules

- Write texts in the website's language (ask if unclear); keep code blocks valid and copy-paste ready.
- For each asset add one line: where to put it and who usually does it (site admin, developer, CMS plugin).
- For WordPress, Wix, Shopify and Tilda, add a one-line hint on how to add the asset without a developer.
- Offer to bundle all assets into one document for handover to the client or developer.

## Branded document

Start the deliverable with a header block, translated into the document language: plugin name with ✦, document title, then subject · version · date · owner · status (draft or current). Follow with a 2–3 line summary and numbered sections; use tables for structured content and code blocks for anything to paste.

If the environment can render HTML artifacts or files, present it as a static HTML page (no scripts) in the house style: header band with a navy #1C1E4E to teal #0E7480 gradient and white text, meta details as small rounded pills, light background #F6F7FB, white rounded cards with a #E3E6EF border, summary card with a gold #FFC448 left accent, dark code blocks. Otherwise deliver the same structure as a document artifact or markdown.
