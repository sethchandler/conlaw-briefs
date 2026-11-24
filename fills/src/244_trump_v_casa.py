"""Fill for 244_trump_v_casa. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/606/24a884/"
C = "Concurring and Dissenting"
P = "Pedagogical"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Challengers to the 2025 birthright-citizenship executive order won nationwide injunctions in three district courts; without reaching the order's legality, the Court held 6--3 that universal injunctions likely exceed federal courts' equitable authority under the Judiciary Act of 1789, limiting relief to what is needed to give each plaintiff with standing complete relief (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Individuals (including pregnant mothers)")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Individuals (including pregnant mothers)")],
  "Judicial Votes": [
    N(r"By a \textbf{6--3} vote, the Supreme Court \textbf{granted} the Government's applications for \textbf{partial stays} of the three universal preliminary injunctions. The applications were argued May 15, 2025, and decided June 27, 2025 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/24A884}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Barrett delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Thomas, Alito, Gorsuch, and Kavanaugh.
    \item \textbf{Concurring Opinions:} Justice Thomas filed a concurring opinion, joined by Justice Gorsuch. Justice Alito filed a concurring opinion, joined by Justice Thomas. Justice Kavanaugh filed a concurring opinion.
    \item \textbf{Dissenting Opinions:} Justice Sotomayor filed a dissenting opinion, joined by Justices Kagan and Jackson. Justice Jackson filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Question Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Barrett)}"),
    N(r"\subsubsection{The Judiciary Act of 1789 and Historical Equity}"),
    SEC("Reasoning", frm="Justice Barrett grounded", to=r"\subsection{Rejection of the Bill"),
    N(r"\subsubsection{Rejection of the Bill-of-Peace Analogy and Rule 23}"),
    SEC("Reasoning", frm="The Court rejected respondents'", to=r"\subsection{Complete Relief"),
    N(r"\subsubsection{Complete Relief vs.\ Universal Relief and Stay Factors}"),
    SEC("Reasoning", frm=r"Distinguishing ``complete relief''"),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC(C, frm="Emphasized that the complete-relief", to=r"\item \textbf{Justice Alito", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Alito)}"), N("Justice Alito", glue=" "),
    SEC(C, frm="Warned of two potential", to=r"\item \textbf{Justice Kavanaugh", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Kavanaugh)}"), N("Justice Kavanaugh", glue=" "),
    SEC(C, frm="Highlighted that", to=r"\item \textbf{Justice Sotomayor", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Sotomayor)}"), N("Justice Sotomayor", glue=" "),
    SEC(C, frm="Condemned the Government's", to=r"\item \textbf{Justice Jackson", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Jackson)}"), N("Justice Jackson", glue=" "),
    SEC(C, frm="Argued that focusing", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{The Class-Action Route Applied:} Granting certiorari before judgment in \textit{Trump v.\ Barbara}, No.~25-365 (June 30, 2026), the Court affirmed a preliminary injunction that a provisionally certified nationwide class had obtained against Executive Order No.~14160, holding that the order violates the Citizenship Clause. Chief Justice Roberts wrote for five Justices; Justice Kavanaugh concurred in the judgment and dissented in part; Justices Thomas, Alito, and Gorsuch dissented."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Universal Scope Stayed): Two Plaintiffs Challenge a Wire-Transfer Surcharge.}", glue=" "),
    S(r"The President issues an executive order directing the Treasury to impose a 10\% surcharge on all international wire transfers sent by U.S.\ residents. Two individual plaintiffs sue in federal district court, alleging the order violates Article I's Taxing Clause, without moving for Rule 23 class certification or naming any agency rule under the APA. Finding the order patently unconstitutional, the district court enters a universal preliminary injunction barring enforcement nationwide.", glue=" "),
    S(r"Under \textit{CASA}, the universal scope must be stayed. Enjoining the Treasury from collecting the surcharge on the two named plaintiffs' transfers affords them complete relief; extending protection to nonparties exceeds the district court's equitable authority under the Judiciary Act of 1789."),
    N(r"\item \textbf{Same-Side (Relief Limited to the Plaintiff): A Contractor Challenges a Speech Condition.} An executive order bars all federal contractors from making public statements about a pending trade negotiation. One software contractor sues, alleging a First Amendment violation, and the district court, finding the order likely unconstitutional, enjoins its enforcement against every federal contractor in the country. Under \textit{CASA}, the injunction is broader than necessary: an order barring the Government from enforcing the condition against the plaintiff fully redresses \emph{its} injury, and nothing about the relief is indivisible. The injunction must be narrowed to the plaintiff. Other contractors may file their own suits or seek certification of a Rule 23(b)(2) class (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Pathways \textit{CASA} Leaves Open): APA Vacatur and a Certified Class.}", glue=" "),
    S(r"Suppose instead that (a) a trade association sues under the Administrative Procedure Act, 5 U.S.C.\ \S\ 706(2), to ``hold unlawful and set aside'' a final Treasury regulation implementing the surcharge, OR (b) the individual plaintiffs satisfy Rule 23(a) and 23(b)(2) and obtain certification of a nationwide class of all U.S.\ senders subject to the surcharge before seeking a classwide injunction.", glue=" "),
    S(r"Unlike \textit{CASA}, neither remedy is barred by \textit{CASA}'s holding. Footnote 10 explicitly carved out APA \S\ 706(2) vacatur (which lower courts through 2026 continue to apply universally), and the majority itself identified a properly certified Rule 23(b)(2) class action as the lawful modern descendant of the English bill of peace---provided the district court conducts the ``rigorous analysis'' demanded by \textit{Wal-Mart} and Justice Alito's concurrence."),
    N(r"\item \textbf{Opposite-Side (Indivisible Relief): Noise From a Federal Firing Range.} A homeowner sues the Defense Department, alleging that a new nighttime live-fire training schedule at a neighboring base creates a nuisance and violates federal law. The district court enjoins nighttime firing altogether. The injunction benefits every neighbor of the base, not just the plaintiff, but \textit{CASA} does not require it to be narrowed. Justice Barrett explained that a court may award relief that incidentally benefits nonparties when indivisible relief is needed to redress the plaintiff's own injury, and she used a neighbor's nuisance as her example. There is no way to stop the noise at one house while letting it continue next door, so the scope of the injunction is consistent with the complete-relief principle."),
    N(r"\item \textbf{Fence-Sitter (State Plaintiffs): A Benefits Rule and Cross-Border Students.} A State sues to block an executive order that would bar federal student-aid eligibility for children of certain noncitizens. It argues that an injunction limited to its own residents would not give it complete relief, because students constantly move into the State from elsewhere, and its universities would have to verify each student's eligibility under a patchwork of rules. \textit{CASA} acknowledged that the inquiry for state plaintiffs is ``more complicated'' and remanded for the lower courts to decide whether narrower relief would suffice. Justice Thomas, by contrast, warned that complete relief is a ``ceiling'' and that nonparty-benefiting remedies must remain rare, and Justice Alito flagged lax state standing as a loophole. Whether the State can justify relief extending beyond its borders is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(P, frm=r"  \item \textbf{Statutory Originalism", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: consolidated docket numbers, Briefing Book placement, filing date, SupremeCourt.gov page-proof link (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section (restated after independent review: one new sentence on Trump v. Barbara (June 30, 2026), verified on CourtListener, now under Subsequent Developments): CRS Report framing and all three 2025--2026 items (remand class actions, Barbara v. Trump / Trump v. Barbara merits ruling, Tincher v. Noem, Ninth and First Circuit state-plaintiff remand rulings, Louisiana v. FDA / City of Columbus APA-vacatur rulings). These are lower-court applications or a later ruling on the executive order's merits rather than on CASA's remedial holding, and none could be verified for this pass.",
  "Exam Hypotheticals 'Analysis:' labels; their text is reused in Examples 1 and 3.",
 ],
}

emit(__file__, FILL)
