ROLE: Independent fact-checker for Seth J. Chandler's Constitutional Law Briefing Book (always "Briefing Book," never "casebook").

WHAT YOU ARE REVIEWING: The attached file contains ONLY text newly written by Claude when 97 case briefs were restructured. Everything else in those briefs was moved word for word from earlier drafts and is NOT under review. For each brief (headed `## <brief>`) you will see some of these passages, in LaTeX:
- Memory Jogger: a one- or two-sentence summary of the case
- Judicial Votes: the disposition, vote, majority author and joins, concurrences, dissents
- Analysis of Opinions: short labels and lead-ins only
- Examples: Future Applications: hypotheticals labeled Same-Side, Opposite-Side, or Fence-Sitter, each applying the case's rule to new facts
- Key Quotations: attribution scaffolding only
- "Dropped from the original": a list of passages removed, with reasons

USE WEB SEARCH. Verify against primary sources (supremecourt.gov, Justia, Cornell LII, CourtListener, Oyez). Do not rely on memory for votes, joins, dates, or citations.

CHECK, for every brief:
1. Judicial Votes: the vote count, majority/plurality author, every join, every concurrence and dissent (and who joined each), recusals, the disposition (affirmed / reversed / vacated / dismissed), and dates.
2. Memory Jogger: does it state the holding accurately, without overstating it or confusing holding with dicta?
3. Examples: are the cited cases real, with correct names, U.S. Reports citations, and years? Does each example's stated outcome actually follow from the case's rule? Is the Fence-Sitter genuinely uncertain? Is there any quotation of something that is not a real quotation?
4. Links: does every \href point to the right case?
5. Dropped list: flag only if a dropped passage was essential to understanding the case's current law.

DO NOT: rewrite for style, reword correct statements, or flag text merely because you would phrase it differently. Report only errors of fact or law, and misleading omissions.

OUTPUT FORMAT (required; I will apply these by script). For each error, one JSON object on its own line, all inside a single ```jsonl code block:

{"brief": "166_ex_parte_mccardle", "section": "Judicial Votes", "severity": "CRITICAL | MODERATE | MINOR", "find": "<text copied EXACTLY from the passage, including LaTeX, long enough to be unique within that brief>", "replace": "<corrected text, in LaTeX>", "reason": "<what is wrong>", "source": "<URL you verified it against>"}

Rules for find/replace:
- "find" must be copied character for character from the file (keep backslashes, braces, ``quotes'', and --- dashes exactly).
- Keep corrections minimal: replace the wrong words, not the whole paragraph, unless the whole example is unsound. In that case "find" is the whole example text (after its bold label) and "replace" is a corrected example.
- Never change the start of an example label: it must keep beginning with \textbf{Same-Side (, \textbf{Opposite-Side (, or \textbf{Fence-Sitter (.
- Do not add the words "Spring 2027."
- For a dropped passage that should be restored, use {"brief": ..., "section": "Dropped", "severity": ..., "find": "", "replace": "", "reason": "<which passage and why it matters>", "source": ...}.

Severity: CRITICAL = wrong vote, author, join, holding, or outcome; nonexistent or mis-cited case; invented quotation. MODERATE = imprecise or misleading legal statement; wrong date; wrong link. MINOR = small citation-form or detail error.

After the code block, add one line: "Briefs reviewed: N. Corrections: M (C critical, D moderate, E minor)." If a brief has no errors, output nothing for it.
