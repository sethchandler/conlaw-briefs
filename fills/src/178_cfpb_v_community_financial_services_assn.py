"""Fill for 178_cfpb_v_community_financial_services_assn. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/601/22-448/"
SO = "Concurring and Dissenting"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Rejecting payday lenders' challenge, the Court held 7--2 that the CFPB's standing funding mechanism---drawing a capped amount each year from the Federal Reserve System's combined earnings---satisfies the Appropriations Clause, because an appropriation need only be a law identifying a source of public funds and authorizing their expenditure for designated purposes (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Two trade associations representing")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Two trade associations representing")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} the Fifth Circuit by a \textbf{7--2} vote. The case was argued on October 3, 2023, and decided on May 16, 2024 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Thomas delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Sotomayor, Kagan, Kavanaugh, Barrett, and Jackson.
    \item \textbf{Concurring Opinions:} Justice Kagan filed a concurring opinion, joined by Justices Sotomayor, Kavanaugh, and Barrett. Justice Jackson filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Alito filed a dissenting opinion, joined by Justice Gorsuch.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Thomas)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Kagan)}"), N("Justice Kagan", glue=" "),
    SEC(SO, frm="Joined the majority in full", to=r"  \item \textbf{Justice Jackson", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Jackson)}"), N("Justice Jackson", glue=" "),
    SEC(SO, frm="Agreed that the plain text", to=r"  \item \textbf{Justice Alito", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Alito)}"), N("Justice Alito", glue=" "),
    SEC(SO, frm="Argued that ``Appropriations''", to=r"\end{itemize}", lc=True),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Valid Appropriation): A Fee-Funded Agency.} Congress creates a federal trademark registry and provides by permanent statute that the registry may spend, without annual appropriations, the filing fees it collects, up to a fixed amount each year, to examine and register marks. Firms denied registration argue that the agency escapes the annual control of the purse. Under \textit{CFPB v.\ CFSA}, the statute is a law that identifies a source of public funds (the fees) and designates the purposes for which they may be spent; the Clause demands nothing more. The arrangement closely tracks the fee-funded Customs Service and Post Office that the First and Second Congresses established and that the majority relied on, and the cap leaves the agency discretion only to spend less (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Valid Appropriation): A Permanent ``Such Sums'' Benefits Program.} A permanent statute provides that the Secretary of Veterans Affairs shall pay, from the general Treasury, such sums as are necessary to provide a specified monthly education stipend to every eligible veteran, with no expiration date and no annual vote. A taxpayer group argues that a perpetual, open-ended draw on the Treasury is not a true appropriation. The statute names a source (the general Treasury) and a designated purpose (the stipend), so it satisfies the \textit{CFPB v.\ CFSA} test; nothing in the Clause requires annual renewal or a fixed sum. Justice Kagan's concurrence emphasized that standing appropriations of this kind fund a large share of the modern federal budget, which is why a contrary rule would have unsettled programs such as Social Security and Medicare."),
    N(r"\item \textbf{Opposite-Side (Violates the Constitution): A Standing Draw for the Army.} Congress gives a new Army Modernization Office permanent authority to draw from the Treasury, each year and without further legislation, whatever the Office's Director deems necessary to equip soldiers, subject to an inflation-adjusted cap. Unlike the CFPB's mechanism, this one runs into an express constitutional limit: Article~I, \S~8, cl.~12 provides that no appropriation of money to raise and support armies shall be for a longer term than two years. The majority in \textit{CFPB v.\ CFSA} relied on that Army Clause to show by negative implication that civilian appropriations need not be time-limited; by the same reasoning, a perpetual army appropriation is invalid."),
    N(r"\item \textbf{Opposite-Side (No Appropriation at All): Spending Without a Statute.} After Congress declines to fund a proposed border-technology program, the Secretary of Homeland Security directs the Treasury to pay \$200 million to contractors to build it, citing only the President's general Article~II responsibility to protect the Nation. \textit{CFPB v.\ CFSA} keeps the Clause's core requirement intact: money may leave the Treasury only under a law that identifies a source and authorizes the expenditure for designated purposes. Here no statute authorizes the payment at all, so it violates the Appropriations Clause regardless of the program's merits. \href{https://supreme.justia.com/cases/federal/us/496/414/}{\textit{Office of Personnel Management v.\ Richmond}, 496 U.S.\ 414 (1990)}, likewise held that payments of money from the Treasury must be authorized by statute."),
    N(r"\item \textbf{Fence-Sitter (Open Question): An Uncapped Perpetual Draw for an AI Safety Agency.}", glue=" "),
    S(r"Suppose Congress enacts the ``National AI Safety Authority Act,'' authorizing a single-director agency to draw ``whatever amounts the Director deems necessary, without any dollar or percentage cap, from the general Treasury of the United States in perpetuity, to promote safe artificial intelligence.'' Regulated AI firms challenge the funding mechanism under the Appropriations Clause.", glue=" "),
    S(r"\textbf{Government's Argument (Under \textit{CFPB v. CFSA}):} The statute satisfies Justice Thomas's two-part test: it identifies a source (the general Treasury) and a designated purpose (promoting safe AI). Neither durational limits nor numerical caps are textually required outside the Army Clause, and Congress has long enacted standing ``sums necessary'' mandatory appropriations (as Justice Kagan highlighted).", glue=" "),
    S(r"\textbf{Opposite Side Contrast (Distinguishing \textit{CFPB v. CFSA}):} Challengers can exploit the majority's repeated emphasis on the CFPB's \textit{statutory cap} (``Congress determined the amount of the Bureau's annual funding by imposing a statutory cap,'' 601~U.S.~at~438) and its analogy to early ``sums not exceeding'' grants. Unlike the CFPB or the fee-funded Post Office/Customs Service, an \textit{uncapped} draw from the \textit{general Treasury} paired with an open-ended statutory mandate (``promote safe AI'') combines an Appropriations Clause defect with a severe Article~I nondelegation problem---a separate constitutional constraint that Justice Thomas explicitly left open (601~U.S.~at~440--441).", glue=" "),
    N(r"The majority used the cap to answer the amount objection to the CFPB's particular appropriation, while stating a source-and-purpose test and recognizing standing appropriations. A separate unresolved question is whether this uncapped authority and broad objective delegate too much discretion."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\textbf{Critiques:}", to=r"\textbf{Exam Hypothetical:}", strip=r"\textbf{Critiques:} ")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, lower-court citation line, Chapter/Topic line, SupremeCourt.gov slip-opinion link (Justia link kept in Judicial Votes).",
  "Legacy section in full (no Subsequent Developments subsection): introductory paragraphs on fiscal consequences and methodology; FCC v. Consumers' Research item (cites CFSA in passing on nondelegation, does not apply its holding); 2025-2026 'combined earnings' statutory litigation (lower-court statutory dispute, blog sources); impoundment debates item (scholarly/litigant commentary).",
 ],
 "notes": [
  "Neon's single exam hypothetical, which argues both sides, is reused as the Fence-Sitter (Example 5) with one new closing sentence.",
 ],
}

emit(__file__, FILL)
