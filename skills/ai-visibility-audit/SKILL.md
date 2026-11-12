---
name: ai-visibility-audit
description: >
  This skill should be used when the user asks to "audit AI visibility", "check how my brand
  appears in ChatGPT", "does AI recommend my company", "GEO audit", "AEO audit",
  "AI search audit", "how do AI assistants see my business", "compare my brand with competitors
  in AI answers", or wants a report on a company's presence in AI assistants
  (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews). Also triggers on the same requests
  in Russian ("аудит видимости в ИИ", "что ChatGPT говорит о моей компании") or Hungarian.
metadata:
  version: "0.1.0"
---

# AI Visibility Audit

Produce an evidence-based report on how a brand appears in AI assistants and what to change so AI assistants mention, cite and recommend it more often.

## Language and tone

- Write the whole report in the language the user writes in. Keep brand names, URLs and bot names as-is.
- Never invent data. Mark every finding as **checked** (verified with a tool in this session), **user-provided**, or **estimate**. If a check could not be run, say so instead of guessing.

## Step 1 — Collect inputs

Ask in one short message only for what is missing:

1. Brand / company name (required)
2. Website URL (required)
3. What it sells and where (niche + city/country/market)
4. Up to 3 known competitors (optional — find them in Step 3 if not given)
5. Report mode:
   - **Simple** — for a business owner: plain words, no jargon, top-5 actions.
   - **Pro** — for a marketer or agency: full tables, scores, evidence, client-ready.
   Default to Simple if the user does not choose.

## Step 2 — Build the buyer prompt set

Write 8–12 realistic questions a potential customer would ask an AI assistant, in the market's language. Mix four types:

- **Category**: "best [category] in [city]", "top [category] for [need]"
- **Problem**: "how to solve [problem the product solves]"
- **Comparison**: "[brand] vs [competitor]", "alternatives to [competitor]"
- **Brand**: "is [brand] good", "[brand] reviews", "what is [brand]"

Show the list to the user in the report appendix.

## Step 3 — Check AI answers

For each prompt:

1. Use web search to see which pages and brands surface for the query — AI assistants with search (ChatGPT search, Perplexity, Gemini, Claude) rely heavily on these results.
2. Answer the prompt as a neutral assistant from your own knowledge, then note whether the brand would be mentioned, at what position, and in what tone.
3. Record: brand mentioned (yes/no), position, competitors mentioned, sources that appear (directories, review sites, Wikipedia, Reddit, media, the brand's own site).

Then tell the user: "I can't query ChatGPT, Perplexity or Gemini directly. For a fuller picture, paste their answers to 3–5 of these prompts and I'll add them to the report." Include pasted answers as **user-provided** evidence. Do not block the report waiting for them.

Identify the 3 competitors that appear most often if the user did not name any.

## Step 4 — Check site readiness for AI

Run the `ai-bot-access-check` workflow (robots.txt rules for AI bots, llms.txt, sitemap). Additionally fetch the homepage and 1–2 key pages and check:

- Clear statement of what the company does, for whom, where (in the first screen of text)
- Structured data (schema.org JSON-LD: Organization / LocalBusiness / Product / FAQPage)
- Title and meta description quality
- FAQ content that answers buyer questions directly
- Contact data consistency (name, address, phone) across the site and directories
- Content rendered server-side vs only by JavaScript (if the page text is nearly empty when fetched, AI crawlers likely can't read it)

If a page cannot be fetched, ask the user to paste its content or skip that check and mark it **not checked**.

## Step 5 — Off-site presence

With web search, check presence on the sources AI assistants cite most for this niche: Google Business Profile / Maps, industry directories, review platforms (Trustpilot, G2, Capterra, TripAdvisor, local equivalents), Wikipedia/Wikidata, Reddit and forums, media mentions. Note gaps relative to competitors.

## Step 6 — Score

Score each area 0–10 using `references/scoring.md`, then compute the overall AI Visibility Score (0–100). Show competitor scores for comparison where evidence allows; otherwise mark them as estimates.

## Step 7 — Write the report

Follow the template in `references/report-template.md` for the chosen mode. Always end with a prioritized action list: what to do, why, effort (low/medium/high), expected impact.

Offer next steps in one line: generate fixes now (run `ai-readiness-fixes`), or re-run the audit in 30 days to measure change.

## Deliverable

Deliver the report in the format the environment supports best (a document artifact if available, otherwise well-formatted markdown in chat). Keep Simple reports to roughly one page; Pro reports may be longer.
