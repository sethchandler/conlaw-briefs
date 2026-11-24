# Group B → Group A conversion: pilot report (3 briefs)

All three briefs now use the Group A / `/case-briefer` nine-section structure and the main Group A preamble (centered title, "Case Brief"). Each compiles cleanly with pdflatex: no errors, no warnings.

| Brief | Words moved verbatim | New words | Pages |
|---|---|---|---|
| 166 *Ex parte McCardle* (1869) | 1,722 | 618 | 7 |
| 167 *Cooper v. Aaron* (1958) | 1,723 | 620 | 7 |
| 177 *West Virginia v. EPA* (2022) | 2,466 | 571 | 9 |

**How the text was handled.** `tools/assemble.py` builds each brief from a list of parts. A part either copies text from Neon's original or is marked as new text. Copied text is checked character for character against the original, and the build fails if it doesn't match. The only change made to copied text is lowercasing one first letter after a new subject (for example, "Justice Kagan criticized…"), used twice in *West Virginia*.

## Where each Group A section comes from

| Group A section | Source |
|---|---|
| Memory Jogger | **New**: one sentence, about 50 words |
| Detailed Case Facts / Procedural History | Neon's combined section, split at the first procedural event; no rewording |
| Judicial Votes | **New** list built from Neon's Case Metadata (majority and joins, concurrences, dissents, disposition) |
| Holding | Neon's Issue(s) Presented (as "Questions Presented") + Neon's Holding, verbatim |
| Analysis of Opinions | Neon's Reasoning and separate opinions, verbatim, under per-opinion subheadings. Kept legacy items go in a final **Subsequent Developments** subsection. |
| Examples: Future Applications | 2 same-side, 2 opposite-side, 1 fence-sitter. Neon's hypotheticals are reused where they fit; the rest are **new**. |
| Critique | Neon's critique bullets, verbatim, turned into bold-labeled paragraphs (Group A style) |
| Key Quotations | Verbatim |

## Modern-legacy material: kept only where directly on point

- ***McCardle*.** Kept *Yerger*/*Felker*, *Klein*, *Boumediene*, and the *Patchak v. Zinke* sentence. Dropped the intro paragraph, *Santos-Zacaria*, and the 2026 Court-reform aside.
- ***Cooper*.** Kept the *Nixon* / *City of Boerne* item. Dropped the *Trump v. CASA* / *Trump v. Barbara* / 2024–25 law-review item as tangential.
- ***West Virginia*.** Kept *Biden v. Nebraska* and *Learning Resources v. Trump* (2026), which apply the doctrine directly. Dropped the *Loper Bright* / *Consumers' Research* item. *Consumers' Research* is still cited in one example that came from Neon. The *Learning Resources* item is long, so you may want to trim it.

## Other material dropped (listed in `fills` and visible in each `.diff`)

- Case Metadata extras: argument dates, term, Chapter/Topic line, duplicate printed URLs, consolidated docket numbers. The main Justia and Cornell links remain in Judicial Votes.
- Neon's "Opposite Side Contrast" passages in *McCardle* and *Cooper*, which are exam tips rather than hypotheticals and repeat the critiques. *West Virginia*'s contrast is a real hypothetical and is reused as Example 3.

## New text that needs independent checking (the safeguard step)

- Memory Joggers (3), Judicial Votes lists (3), and the new examples:
  - *McCardle* 1, 2, 4, 5
  - *Cooper* 2, 3, 4, 5
  - *West Virginia* 2, 4, 5
- Cases cited in the new text: *Felker v. Turpin*, 518 U.S. 651 (1996); *Boumediene v. Bush*, 553 U.S. 723 (2008); *Dobbs v. Jackson Women's Health Org.*, 597 U.S. 215 (2022); *Biden v. Nebraska* (by name only).
- **Links not yet tested.** This cloud environment's network policy blocks supreme.justia.com and www.law.cornell.edu, so no link in the new text has been tested. All of them follow Justia's and Cornell's standard URL patterns.

## Not changed: needs your call before the full run

1. **Quotation attribution style.** Group B puts the pin cite inside the quote block, e.g. `(74 U.S. at 514)`. Group A puts it on a `\noindent ---` line after the quote. The conversion can be done by script, but it moves text around, so it isn't done here.
2. **Length.** Converted Group B briefs are still about 15–20% shorter than Group A briefs, mainly because the facts sections are thinner. The pilot adds no facts; adding them would be new writing.
