# Session Summary: Constitutional Law Briefing Book

This session took 247 Constitutional Law case briefs (1792 to November 2026) from an inconsistent draft set to an audited Briefing Book in four editions: full, Four-Page, Two-Page, and One-Page.

## 1. Planning and the template problem

We started by planning a low-cost audit. While planning, we found that the briefs used two different templates.

- **Group A** (files 1–165) followed the case-briefer format. Its nine sections are Memory Jogger, Detailed Case Facts, Procedural History, Judicial Votes, Holding, Analysis of Opinions, Examples: Future Applications, Critique, and Key Quotations. The Examples section has five examples: two Same-Side, two Opposite-Side, and one Fence-Sitter.
- **Group B** (files 166–262) had been generated without that skill and used an improvised structure, including a "modern legacy" section.

Group A was confirmed as the correct template.

## 2. Converting Group B

After a three-brief pilot, the remaining Group B briefs were converted to the Group A template. The conversion system reuses the original wording wherever possible:

- each brief has a "fill" script that marks every passage as either new text or verbatim source text;
- an assembler checks that all moved text is verbatim;
- corrections are stored separately and applied automatically;
- a checker confirms the nine sections, five labeled examples, attributed quotations, a cap on new words, and a clean LaTeX compile.

"Modern legacy" material was kept only where it was clearly relevant.

## 3. Standardizing quotations

All briefs were converted to the Group A quotation style: a block quotation followed by an attribution line. Some quotations were cited only by page. We checked whether any came from per curiam opinions, found that none did, and added the speaker to each.

All 247 briefs now share one preamble and a centered title block.

## 4. Independent review by ChatGPT

The newly written text was exported in four parts for review by ChatGPT. ChatGPT returned its corrections as JSONL files, which were evaluated and applied, with each decision logged in `reports/review_results/`.

## 5. Audit against primary sources

Every brief was checked against official opinion text: Library of Congress U.S. Reports scans, GovInfo, and Supreme Court slip opinions and preliminary prints. Official text was found for 246 of 247 cases. The audit tools in `tools/audit/` check:

- each quotation's wording (exact, scanning noise, wording difference, or not found);
- pin cites;
- citations to 2024–2026 decisions;
- 215 concerns flagged during conversion.

The audit made 147 corrections (19 moderate, 128 minor). Per instruction:

- the quotation marks in *Chae Chan Ping* were removed;
- all 13 unsourced or unverifiable quotations and items were deleted.

The report is `reports/audit/AUDIT_REPORT.md`. The full Briefing Book compiles cleanly at 1,746 pages.

## 6. Condensed editions

### Pilot

Three cases (*Hemani*, *Carolene Products*, *Egbert v. Boule*) were condensed into 4-, 2-, and 1-page versions. The pilot was accepted with one caution: *Carolene Products* must quote Footnote Four, the passage the case is known for.

### Choosing the key quotation automatically

Rather than fixing cases like *Carolene* by hand, the quotations are ranked automatically:

1. **Candidates** come from the full brief's verified Key Quotations. An agent may also nominate one famous passage, but only after finding it in the official text.
2. **Citation counts.** Each candidate's best-known phrase is searched on CourtListener to count how many opinions quote it. Phrases that predate the case are excluded.
3. **Judgment fallback.** If the highest count is below 10 (typical for very recent cases), the passage stating the rule, or the one the scholarship treats as central, ranks first.

The method was validated on nine known cases, and each produced the expected passage:

| Case | Passage | Opinions quoting it |
|---|---|---|
| *Carolene Products* | Footnote Four | 222 |
| *Marbury* | "province and duty" | 946 |
| *McCulloch* | "let the end be legitimate" | 255 |
| *Youngstown* | Jackson's "diffuses power" | 126 |

Rankings run only once per case and are saved to `condensed/signature/<case>.json`, so later runs reuse them instead of searching CourtListener again.

### Rules for each edition

| Edition | Sections | Examples | Quotations |
|---|---|---|---|
| Four-Page | All 9 | 5 | Top 3 |
| Two-Page | All 9, compact | 3 | Rank 1 |
| One-Page | 9 bold run-in labels | 3 | Rank 1 |

All editions use only content from the audited full brief. Every quotation must appear verbatim in it.

### Production

A workflow ran 13 parallel agents, about 19 cases each, following `condensed/CONDENSE_GUIDE.md`. Each agent ranked the quotations, wrote the three editions, and ran `tools/condense_check.py` until it passed. The checker verifies:

- exact page counts, with a reasonably full last page;
- required headings;
- no LaTeX warnings or overlong lines;
- verbatim quotations;
- the required ranked quotations.

**Results:**

- all 247 cases pass when re-checked independently;
- 191 cases were ranked by citation count and 56 by judgment;
- spot checks look right, such as *Mathews v. Eldridge*'s three-factor test (2,808 opinions) and *Tinker*'s "schoolhouse gate" (450).

### Books

Three Briefing Books were built with the existing builder:

| Edition | Pages |
|---|---|
| Four-Page | 837 |
| Two-Page | 533 |
| One-Page | 286 |

Each title page names its edition. The books reflow the text in the book's 11pt typeface, so individual cases can run slightly over or under their target length; the standalone files are the exact-length versions.

## Where things are

**GitHub** (`sethchandler/conlaw-briefs`):

| Location | Contents |
|---|---|
| `briefs/` | The 247 audited full briefs |
| `condensed/4page/`, `condensed/2page/`, `condensed/1page/` | The condensed editions |
| `condensed/signature/` | Quotation rankings |
| `condensed/SIGNATURE_LOG.md` | The rank-1 quotation for every case |
| `condensed/CONDENSATION_SPEC.md`, `SIGNATURE_QUOTE_METHOD.md`, `CONDENSE_GUIDE.md` | Rules and method |
| `reports/audit/`, `reports/review_results/` | Audit and review records |
| `tools/` | Conversion, audit, checking, and build scripts |

**PDFs** are not stored in the repository. To rebuild them:

- condensed books: run `tools/build_condensed_books.sh`;
- full book: run `tools/update_briefing_book.py --compile`.
