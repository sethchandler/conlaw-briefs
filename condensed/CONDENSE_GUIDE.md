# Guide for condensing agents

Repo: `/home/user/conlaw-briefs`. For each brief assigned to you (stem such as `78_marbury_v_madison`), you produce four files:

```
condensed/signature/<stem>.json   quotation ranking (step 1)
condensed/4page/<stem>.tex        Four-Page Edition
condensed/2page/<stem>.tex        Two-Page Edition
condensed/1page/<stem>.tex        One-Page Edition
```

The source is the audited full brief, `briefs/<stem>.tex`. Before your first case, read `condensed/CONDENSATION_SPEC.md` (the rules for each edition), `condensed/SIGNATURE_QUOTE_METHOD.md`, and the finished examples for `139_united_states_v_carolene_products`, `228_egbert_v_boule`, and `142_united_states_v_hemani` in all four locations. Copy their preambles and layout exactly.

**If `condensed/signature/<stem>.json` already exists, do not search again: use it.** Write nothing outside these four files. Do not run git. Other agents are working in the same repo at the same time.

## Step 1: rank the quotations (once per case)

1. **Candidates.** Take the Key Quotations in `briefs/<stem>.tex`, which were verified against the official reports.
   - You may nominate one famous passage the brief lacks. Use it only after finding it in the official opinion text: `python3 tools/audit/grep_source.py /tmp/claude-0/-home-user-conlaw-briefs/28d280af-ab16-5d32-aa6f-2586863fbe44/scratchpad/sources <case number> "phrase"`.
   - Copy a nominated passage exactly as printed, and record `"source": "nominated"` and `"verified_in"` (the page).
2. **Count citations.** Load CourtListener with `ToolSearch` query `select:mcp__CourtListener__search`.
   - For each candidate, search its best-known phrase, the words courts actually quote, in quotation marks: `{"q": "\"phrase\"", "num_results": 1, "fields": ["caseName"]}`. The result's `count` is the number of opinions quoting it.
   - Use 5–10 distinctive words. Never use stock language that predates the case.
   - If a count looks low for a famous passage, try one more phrase from it and keep the higher count.
   - **Pace yourself:** one search at a time. Stop searching a case once one candidate has at least three times the count of every other.
   - If a search errors or times out, wait about a minute (do other work meanwhile), then retry once. If it fails again, rank that case by judgment.
3. **Judgment fallback.** If the top count is below 10 (typical for 2024–2026 decisions), rank by judgment: put first the passage that states the case's rule or test, or that the scholarship discussed in the brief's Critique treats as central. Record a one-line `reason` for each.
4. **Write `condensed/signature/<stem>.json`:**

```json
{"brief": "<stem>", "method": "citation_count" or "judgment",
 "candidates": [{"rank": 1, "text": "<opening words of the quotation, copied exactly; at least 12 words>",
                 "speaker": "...", "phrases": ["..."], "counts": [123], "score": 123,
                 "source": "brief" or "nominated", "verified_in": "U.S. page (nominated only)", "reason": "(judgment only)"}],
 "notes": "..."}
```

   A candidate's `text` must be words that will appear verbatim in your editions. If you will quote only part of a long passage, as the 1-page *Carolene* quotes only the "prejudice against discrete and insular minorities" clause of Footnote Four, the `text` should be the part you will use.

## Step 2: write the three editions

Follow `condensed/CONDENSATION_SPEC.md`.
- **Use only the full brief's content.** No new facts, cases, holdings, characterizations, or citations.
- **Quotation marks only around words that appear verbatim in the full brief,** or around your verified nominated passage.
- **Quotations by edition:**
  - 1-page and 2-page: the **rank-1** quotation.
  - 4-page: the **top three**, in rank order.
- **Keep the analytical spine:** holding and rule, vote, majority reasoning, main separate opinions, examples covering both sides plus a close case, leading critiques.
- **Fill the pages.** 4-page: four pages, the last at least a third full. 2-page: two pages. 1-page: one page, about 85% full.
- **Shortening a long rank-1 quotation** for the 1-page edition: quote a contiguous verbatim excerpt of it (bracketing a changed first letter, as in `[P]rejudice`), and make that excerpt the candidate's `text`.

## Step 3: check and fix

```
cd /home/user/conlaw-briefs && python3 tools/condense_check.py <stem>
```

Fix and re-run until it prints `"pass": true`.
- If an edition runs over its page count, cut lower-priority material: critique first, then example detail, then analysis detail.
- If a page is too empty, restore substance from the full brief.
- Give up after about five attempts on one case, and report its remaining problems.

## Return

For each assigned brief, report: stem, pass (true or false), method, the rank-1 quotation's opening words and score, and any remaining problems.
