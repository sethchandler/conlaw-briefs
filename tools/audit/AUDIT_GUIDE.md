# Audit guide: verifying the briefs against primary sources

You are auditing LaTeX case briefs in `/home/user/conlaw-briefs/briefs/` for Seth J. Chandler's Constitutional Law **Briefing Book** (never "casebook"; never write "Spring 2027"). For each brief assigned to you there is an issue packet:

```
SCRATCH/packets/<brief>.json
```

Packet fields: `quote_issues`, `inline_not_found`, `recent_unverified`, `recent_dropped`, `concerns`, and sometimes `note`.

**You do not edit any file in the repository and you do not run git.** You write one results file (format below). The person running the audit applies and checks every correction.

## Your sources

1. **Official opinion text, already downloaded**, one file per case: `SCRATCH/sources/<case number>.json`. The case number is the number before the first underscore in the brief name. Search it with:
   ```
   python3 /home/user/conlaw-briefs/tools/audit/grep_source.py SCRATCH/sources NUM "phrase"
   python3 /home/user/conlaw-briefs/tools/audit/grep_source.py SCRATCH/sources NUM --page 514
   ```
   - Matching ignores punctuation and line breaks. Pages are U.S. Reports pages for official PDFs and PDF pages for slip opinions.
   - The text of older volumes is OCR, so small character glitches ("regu late") are the scan, not the brief.
   - `--page` prints the page as printed. Use it to copy exact wording and confirm pin cites. The file holds the majority, concurrences and dissents.
2. **CourtListener**, for any other decision. Load the tools with `ToolSearch` query `select:mcp__CourtListener__search,mcp__CourtListener__search_document,mcp__CourtListener__read_document`, then use `search` (court `scotus` or a circuit) and `search_document`.
3. **The web via curl**: `www.law.cornell.edu` (statutes and the Constitution), `www.supremecourt.gov`, `www.govinfo.gov`, `tile.loc.gov`. Justia blocks automated access, so don't use it.

## What to do with each packet item

**`quote_issues`**: Key Quotations, or inline quotes, that were not matched exactly to the case's own opinion text.
- `WORDING`: there are word-level differences; `differences` shows them.
  - Check the page.
  - If the brief dropped, added or changed words without an ellipsis or brackets, correct the quote to the opinion's exact words. Mark omissions with ` \dots{} ` and alterations with `[ ]`.
  - If the "difference" is only a running head, a footnote number or OCR noise, record it under `resolved_ok`.
- `NOTFOUND`: the quote isn't in this case's text.
  - Search the case's text for a distinctive shorter phrase.
  - Then check whether the passage is quoting another decision, using CourtListener.
  - If it comes from a different case, fix the attribution.
  - If you can't find it anywhere, it may be fabricated. Replace the whole quote block with a real passage from the same opinion making the same point, copied exactly with its correct attribution and page. If no suitable passage exists, delete the block, as long as at least three quotations remain.
- `pin` `WRONG` / `OFF_BY_1`: `us_pages` is where the quote actually appears. Confirm with `--page`, then correct the pin cite in the attribution.

**`inline_not_found`**: quotations in the body of the brief that aren't in this case's own opinion. Most quote another case, a statute or a scholar, which is fine.
- If the surrounding sentence attributes the quote to *this* case, it's an error. Find the real wording or remove the quotation marks and paraphrase.
- If it's attributed to another Supreme Court decision, spot-check it with CourtListener when practical.
- Don't spend long on scholarly quotations. List any you can't resolve under `unresolved`.

**`recent_unverified`**: a 2024–26 decision cited in the current brief that wasn't matched automatically. The list includes false hits, such as an old case next to an unrelated 2026 date; mark those `resolved_ok`.
- For real citations, confirm the case exists and that the brief's description (court, date, vote, holding) is right.
- Correct errors.
- If a cited decision can't be found at all, remove or rewrite that sentence.

**`recent_dropped`**: 2024–26 decisions that appeared in the original draft (`originals/briefs/<brief>.tex`) but were dropped during conversion.
- Determine whether each is real.
- Recommend restoring one only if it is a **Supreme Court** decision that overruled, narrowed, or squarely applied this case's holding, so that a student needs it to state current law. Lower-court decisions are not restored.
- Give the verbatim original passage, where it should go, and your verification, under `restore`.

**`concerns`**: possible errors the conversion agents noticed in the original drafts. Verify each one against the sources. If it's a real error in the current brief, correct it; otherwise record it under `resolved_ok`.

## Rules for corrections

- `find` must be copied **exactly** from the current `briefs/<brief>.tex`, keeping LaTeX intact. It must be at least 20 characters long and must occur **exactly once** in that file. Check this with `grep -c -F`.
- Keep corrections minimal. Fix the error; don't restyle.
- Never put quotation marks around words you have not verified in a primary source.
- Never change `\section{...}` headings. Never change the start of an example label (`\textbf{Same-Side (`, `\textbf{Opposite-Side (`, `\textbf{Fence-Sitter (`).
- Escape `& % $ # _` in new text. Use ``` ``...'' ``` for quotation marks.
- Every correction needs a `source`: a URL, or "official opinion text, U.S. page N".

## Output: one JSON file at the path given in your instructions

```json
[
 {"brief": "18_buck_v_bell",
  "corrections": [{"find": "...", "replace": "...", "category": "quote|pin|attribution|recent_case|fact|other",
                   "severity": "CRITICAL|MODERATE|MINOR", "reason": "...", "source": "..."}],
  "restore": [{"passage": "<verbatim from originals/briefs/...>", "place": "...", "reason": "...", "verification": "..."}],
  "resolved_ok": ["short note per item checked and found fine"],
  "unresolved": ["item and why"]}
]
```

Include every assigned brief, even when it has nothing to correct. Write the file with Python (`json.dump(..., ensure_ascii=False)`) so the LaTeX backslashes are escaped correctly, then run `python3 -c "import json; json.load(open(PATH))"` to confirm it parses.
