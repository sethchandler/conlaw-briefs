# Converting a Group B brief to the Group A template

Repo root: `/home/user/conlaw-briefs`. You convert briefs by writing **one Python file per brief**, `fills/src/<stem>.py`, that says where each piece of the Group A brief comes from. You never edit a `.tex` file yourself.

```
python3 tools/check_brief.py <stem>        # builds briefs/<stem>.tex and runs every check
```

Repeat until it prints `"pass": true`. Do **not** edit anything in `originals/`, `tools/`, or other briefs' files, and do **not** run git.

## Worked examples (read all three before starting)
- `fills/src/166_ex_parte_mccardle.py`, `fills/src/167_cooper_v_aaron.py`, `fills/src/177_west_virginia_v_epa.py`
- Compare each with its original `originals/briefs/<stem>.tex` and its result `briefs/<stem>.tex`.
- Helpers are documented in `tools/fillkit.py`: `N()` = new text, `S()` = exact text from the original, `SEC()` = verbatim slice of an original section, `ITEMS()` = slice with list items turned into bold-labeled paragraphs. `glue=" "` continues a paragraph; `glue="\n"` is a line break.

## The target: Group A / case-briefer sections, in this order

| Group A section | Source in the Group B brief | New text? |
|---|---|---|
| Memory Jogger | — | **New**: 1–2 sentences, at most ~60 words, capturing the case's essence (who, what rule). May end with the brief's main Justia link. |
| Detailed Case Facts | first part of "Facts and Procedural History" | No: `SEC(..., to=<anchor>)` |
| Procedural History | the rest of it, from the first procedural event (suit filed, lower-court ruling, appeal) | No: `SEC(..., frm=<anchor>)`. Splitting mid-paragraph at a sentence start is fine. If the original has a `\subsection{Procedural History}` heading or a `\textbf{Procedural History:}` lead-in, start after it (`strip=`). |
| Judicial Votes | Case Metadata + separate-opinions section | **New** list in the pilot format: disposition and vote, then Majority / Concurring / Dissenting items with authors and joins. Use only facts stated in the original brief. A sentence from the original may be moved in with `S()`. |
| Holding | Issue(s) Presented + Holding | `N(r"\textbf{Questions Presented:}")`, `SEC("Issue")`, `N(r"\textbf{Holding:}", glue=" ")`, `SEC("Holding")`. Drop the `Holding:` label if the original Holding already starts with one. |
| Analysis of Opinions | Reasoning + separate opinions | `N(r"\subsection{Majority Opinion (Justice X)}")` (or Plurality / Per Curiam / Opinion of the Court) + `SEC("Reasoning")`; one `\subsection{...}` per separate opinion with its text moved verbatim. If moved text starts with a bare verb ("Criticized…"), put `N("Justice Kagan", glue=" ")` before it and use `lc=True`. |
| (end of Analysis) Subsequent Developments | "Doctrinal/Constitutional Significance and Modern Legacy" | See the legacy rule below. |
| Examples: Future Applications | Neon's exam hypothetical(s) + new ones | Exactly 5 `\item`s in `\begin{enumerate}`, in this order and with labels that **start** exactly: `\textbf{Same-Side (...)`, `\textbf{Same-Side (...)`, `\textbf{Opposite-Side (...)`, `\textbf{Opposite-Side (...)`, `\textbf{Fence-Sitter (...)`. |
| Critique | critique items in "Pedagogical Critiques…" | No: `ITEMS(...)` (or `SEC` if they are prose) |
| Key Quotations | Key Quotations | See the quotation rule below. |

## Rules

**Moved text is verbatim.** `S()` text must appear character-for-character in the original; the builder rejects anything else. Never "fix" Neon's wording inside `S()`/`SEC()`. If you notice something in the original that looks wrong (a date, a vote, a holding), do not change it: report it in `concerns`.

**Legacy material ("Modern Legacy") is kept only when directly on point**: a later decision that overruled, narrowed, extended, or squarely applied *this case's* holding, which a student must know to state current law. Drop: intro and framing paragraphs, scholarship debates, tangential recent cases, "through 2026" commentary. Kept items move verbatim (`SEC` slices or `S`) inside `N(r"\subsection{Subsequent Developments}")`, `N(r"\begin{itemize}")`…`N(r"\end{itemize}")`. Usually 0–3 items; if none qualify, omit the subsection. You may move one sentence out of an item with `S()` under a short new label (see McCardle's *Patchak* item). List every drop in `dropped`.

**Examples.** Reuse Neon's hypotheticals when they are genuine hypotheticals: a new bold label (`N(..., glue=" ")`) followed by the moved fact pattern and analysis (`S(..., glue=" ")`). "Opposite Side Contrast" passages that are exam tips rather than fact patterns are dropped and listed in `dropped`. Each new example: 90–150 words, a concrete fact pattern, then *why* it comes out that way under this case's rule. The fence-sitter must be genuinely uncertain and say why.

**Accuracy in new text.**
- Cite only real Supreme Court cases you are certain of, with the correct U.S. Reports citation; prefer cases the brief already discusses.
- Never put quotation marks around anything that is not a verbatim quote already appearing in the brief (or the statutory text the brief quotes).
- Links: reuse a URL already in the brief, or use `https://supreme.justia.com/cases/federal/us/VOL/PAGE/` only for a case whose volume and page you are sure of. When unsure, give no link.
- Do not describe events after 2023 unless the original brief already does; never invent later history.

**Key Quotations.**
- If the stem is **not** in `tools/manual_quotes.txt`: use `SEC("Key Quotations")`; the checker converts attributions automatically.
- If it **is** listed (list-style quotations): rebuild each quote in Group A style from verbatim pieces, keeping every quote and adding none:
  ```python
  N(r"\begin{quote}", glue="\n"), S(r"``quote text exactly as in the original''", glue="\n"),
  N(r"\end{quote}", glue="\n"), N(r"\noindent ---", glue=" "), S(r"Justice Harlan, 188 U.S.\ at 363 (\href{...}{Justia})"),
  ```
  If the attribution is a label before the quote (e.g. `\item \textbf{Adoption of ... (Roberts, J., 297 U.S.\ at 66):}`), move just the attribution part, e.g. `S(r"Roberts, J., 297 U.S.\ at 66")`, and add a closing period with `N(".")` if needed.

**House style.** It is a "Briefing Book", never a "casebook". Never write "Spring 2027". No amsmath-only macros (`\tfrac`, `\dfrac`, `\mathbb`, `\operatorname`, `\text{}`). Escape `& % $ # _` in new text. New text per brief is capped at 1,100 words.

**What to record in the fill:** `"dropped"` (each original passage left out and why) and `"notes"` (anything a reviewer should know).
