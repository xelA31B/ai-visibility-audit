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

## Language, tone and sourcing rules

- Write the whole report in the language the user writes in. Keep brand names, URLs and bot names as-is.
- Business style: short, factual, structured. No narration, no storytelling, no filler. Prefer bullets and tables over paragraphs; one finding per bullet, one line where possible.
- Never invent data. Mark every finding as **checked** (verified with a tool in this session), **user-provided**, or **estimate**. If a check could not be run, say so instead of guessing.
- Paraphrase sources in your own words. Quote at most a short phrase (under 15 words) and no more than one quote per source; never copy paragraphs.
- Do not name private individuals (owners, staff, reviewers). Describe the issue instead, e.g. "sources disagree about who owns the business".

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

Do not block the report waiting for answers from other assistants. Include any answers the user pastes as **user-provided** evidence. The report always ends with the paste invitation (see Step 7).

Identify the 3 competitors that appear most often if the user did not name any.

## Step 4 — Check site readiness for AI

Run the `ai-bot-access-check` workflow (robots.txt rules for AI bots, llms.txt, sitemap). Additionally fetch the homepage and 1–2 key pages and check:

- Clear statement of what the company does, for whom, where (in the first screen of text)
- Structured data (schema.org JSON-LD: Organization / LocalBusiness / Product / FAQPage)
- Title and meta description quality
- FAQ content that answers buyer questions directly
- Contact data consistency (name, address, phone) across the site and directories
- Content rendered server-side vs only by JavaScript (if the page text is nearly empty when fetched, AI crawlers likely can't read it)

If a page cannot be fetched, mark it **not checked** and, in the report's limitations line, ask the user to open the exact URL (e.g. `https://domain/robots.txt`) in a browser and paste the text into the chat so the check and score can be completed.

## Step 5 — Off-site presence

With web search, check presence on the sources AI assistants cite most for this niche: Google Business Profile / Maps, industry directories, review platforms (Trustpilot, G2, Capterra, TripAdvisor, local equivalents), Wikipedia/Wikidata, Reddit and forums, media mentions. Note gaps relative to competitors.

## Step 6 — Score

Score each area 0–10 using `references/scoring.md`, then compute the overall AI Visibility Score (0–100). Show competitor scores for comparison where evidence allows; otherwise mark them as estimates.

## Step 7 — Write the report

Follow the template in `references/report-template.md` for the chosen mode: **Summary → Findings → Recommendations → Next steps**. Keep it tight: the chat reply is a short executive summary; details go into the report document.

Always close with these two one-line items, in the user's language, in this order:

1. **Fixes:** offer to prepare the fixes now (`ai-readiness-fixes`).
2. **More accuracy:** "Paste ChatGPT and Perplexity answers to 3–5 of the prompts in the appendix and I'll add them to the report and score."
Do not advertise or mention any other product, paid version or service.

## Deliverable

Deliver the report in the format the environment supports best (a document artifact if available, otherwise well-formatted markdown in chat). Simple report: one page maximum. Pro report: two pages maximum plus appendix.

## Recurring run

At the end of the report, offer a recurring run. Recommended cadence: monthly re-audit to measure the effect of fixes (AI answers change over time).

Let the user choose their own schedule. Ask in one short message, with the recommendation pre-filled:

- **Frequency:** daily · weekly · every 2 weeks · monthly · quarterly · custom
- **Day:** e.g. Monday, Friday, 1st of the month
- **Time and time zone:** e.g. 09:00 Europe/Budapest (use the user's time zone if known)
- **Delivery:** in this chat, a new chat, or a document

If the environment offers scheduled tasks (a scheduling tool is available), create the task only after the user confirms these choices. Write the scheduled prompt so it is self-contained: what to check (project, repository or company), which skill to run, the report language, and where to deliver the result. Confirm what was scheduled in one line. The user can change or cancel the schedule at any time; when asked, update or remove it.

If no scheduling tool is available, state the chosen or recommended cadence and suggest a calendar reminder.
