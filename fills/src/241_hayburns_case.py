"""Fill for 241_hayburns_case. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/2/409/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"When Congress told federal circuit courts to decide veterans' pension claims subject to revision by the Secretary of War and Congress, five Justices on circuit refused, writing that Congress may not assign Article III courts non-judicial duties or make their decisions subject to executive or legislative revision; the Supreme Court itself never reached the merits (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="In April 1792, the Circuit Court for the District of Pennsylvania")],
  "Procedural History": [SEC("Facts and Procedural History", frm="In April 1792, the Circuit Court for the District of Pennsylvania")],
  "Judicial Votes": [
    N(r"The Supreme Court issued \textbf{no merits judgment}. It divided \textbf{3--3} and denied Attorney General Randolph's \textit{ex officio} mandamus motion, then held his renewed motion on Hayburn's behalf under advisement until Congress's Act of February 28, 1793, mooted it (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Opinion of the Court:} None; the report is a procedural entry by reporter Alexander Dallas, with a footnote reprinting the circuit-court letters to President Washington (2 U.S.\ at 410--414 n.*).
    \item \textbf{Views on the Merits:} Five of the six sitting Justices---Chief Justice Jay and Justices Cushing, Wilson, Blair, and Iredell---stated their constitutional objections in circuit-court letters: the New York Circuit (Jay, Cushing, and District Judge Duane), the Pennsylvania Circuit (Wilson, Blair, and District Judge Peters), and the North Carolina Circuit (Iredell and District Judge Sitgreaves).
    \item \textbf{Concurring and Dissenting Opinions:} None in the modern sense.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{The Circuit-Court Letters (No Opinion of the Court)}"), SEC("Reasoning"),
    N(r"\subsection{Differences Among the Three Circuit Courts}"),
    SEC("Concurring and Dissenting"),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Core Judicial Power"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Unconstitutional): Executive Veto of Court Awards.}", glue=" "),
    S(r"Congress enacts the ``Cyber-Compensation Act,'' directing federal district courts to adjudicate private claims for federal cyber-attack relief and enter monetary awards, but providing that the Secretary of Homeland Security may ``review and vacate any district court award that the Secretary deems inconsistent with national fiscal priorities.''", glue=" "),
    S(r"Unconstitutional under \textit{Hayburn's Case} and \textit{Plaut v. Spendthrift Farm}. Congress may assign public-benefit claims to an executive agency in the first instance (with subsequent Article III judicial review), but it cannot vest an Article III court with adjudicatory authority while making the court's judgment subject to executive revision or veto."),
    N(r"\item \textbf{Same-Side (Unconstitutional): Advisory Rulings on Pending Bills.} To reduce litigation over new laws, Congress directs the D.C. Circuit to review any bill passed by one House, at the request of a committee chair, and to issue a ruling on whether it would be constitutional if enacted. No party is injured, no one is sued, and the ruling binds no one. The duty is not ``properly judicial'' or performed ``in a judicial manner,'' in the words of the New York circuit judges: it asks a court to advise the legislature rather than decide a case between adverse parties. Under the advisory-opinion bar that \textit{Hayburn's Case} founded and \textit{Muskrat v.\ United States} applied, Congress cannot impose this assignment on an Article III court."),
    N(r"\item \textbf{Opposite-Side (Constitutional): Terminating Prospective Injunctions After a Change in Law.} Suppose Congress enacts", glue=" "),
    S(r"(a) a statute amending substantive federal environmental law prospectively and directing federal courts to terminate ongoing \textit{prospective} injunctions that no longer satisfy the new statutory standard", glue=""),
    N(r".", glue=" "),
    S(r"Under \href{https://www.law.cornell.edu/supremecourt/text/99-224}{\textit{Miller v. French}, 530 U.S. 327 (2000)}, modifying or terminating \textit{prospective} equitable decrees based on changed underlying law does not retroactively reopen final money judgments in violation of \textit{Hayburn's Case} or \textit{Plaut}."),
    N(r"\item \textbf{Opposite-Side (Constitutional): Judges Serving Voluntarily on a Commission.} Suppose Congress enacts", glue=" "),
    S(r"(b) a statute creating an independent advisory commission on federal judicial ethics on which three federal appellate judges may voluntarily serve in their individual capacities without adjudicating cases", glue=""),
    N(r". Under", glue=" "),
    S(r"\textit{Mistretta} and the New York circuit judges' ``commissioner'' distinction in \textit{Hayburn's Case}, voluntary extrajudicial service by individual judges on a non-adjudicatory commission does not assign non-judicial duties to Article III courts or compromise judicial finality."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Judgments Payable Only if Congress Appropriates.} Congress allows veterans to sue in federal district court for wrongly denied disability benefits, but provides that any judgment may be paid only from funds Congress appropriates each year for that purpose. After a court enters a final judgment for a veteran, Congress declines to fund that award. On one view, the judgment itself remains final and binding, and Congress has merely exercised its power of the purse, which \textit{Hayburn's Case} did not address. On another, a judgment that Congress can decline to honor case by case is effectively ``liable to a reversion, or even suspension, by the Legislature itself,'' which the North Carolina judges said the Constitution forbids. Where the line falls is unsettled."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{The Irony", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: Chapter line, provisions list, FJC link, metadata vote/author lines (restated in Judicial Votes).",
  "Legacy section: lead-in paragraph (most-cited framing, judicial-review priority claim); 'Core Judicial Power and the Administrative State Through 2026' item (Stern v. Marshall, SEC v. Jarkesy, 2026 litigation) - tangential, and its quoted phrase is not from Hayburn's Case. Kept: Plaut item; Muskrat/California v. Texas/Mistretta item.",
  "Exam Hypotheticals: headings and 'Analysis:' labels; Hypothetical 2's 'By contrast, suppose Congress enacts two separate measures' lead-in and 'Both provisions are constitutional' sentence (split into Examples 3 and 4).",
 ],
 "notes": [
  "Judicial Votes does not name the sixth sitting Justice because the original brief does not.",
 ],
}

emit(__file__, FILL)
