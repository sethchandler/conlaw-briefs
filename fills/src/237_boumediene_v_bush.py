"""Fill for 237_boumediene_v_bush. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/553/723/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Holding 5--4 that the Suspension Clause has full effect at Guantanamo Bay, the Court struck down \S~7 of the Military Commissions Act because the Detainee Treatment Act's review of CSRT determinations was not an adequate and effective substitute for habeas corpus (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The D.C. Circuit (476 F.3d 981")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The D.C. Circuit (476 F.3d 981")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} the D.C. Circuit by a \textbf{5--4} vote. The case was argued on December 5, 2007, and decided on June 12, 2008 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supct/html/06-1195.ZO.html}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Kennedy delivered the opinion of the Court, joined by Justices Stevens, Souter, Ginsburg, and Breyer.
    \item \textbf{Concurring Opinion:} Justice Souter filed a concurring opinion, joined by Justices Ginsburg and Breyer.
    \item \textbf{Dissenting Opinions:} Chief Justice Roberts filed a dissenting opinion, joined by Justices Scalia, Thomas, and Alito. Justice Scalia filed a dissenting opinion, joined by Chief Justice Roberts and Justices Thomas and Alito.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kennedy)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Souter)}"),
    SEC("Concurring and Dissenting", frm="Justice Souter emphasized", to=r"\textbf{Chief Justice Roberts"),
    N(r"\subsection{Dissenting Opinion (Chief Justice Roberts)}"),
    SEC("Concurring and Dissenting", frm="Chief Justice Roberts argued", to=r"\textbf{Justice Scalia (Dissenting"),
    N(r"\subsection{Dissenting Opinion (Justice Scalia)}"),
    SEC("Concurring and Dissenting", frm="Writing in sharp originalist"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Limits on Extraterritorial Reach:}", to=r"  \item \textbf{Deferential Post-"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Cabining the Suspension Clause", to=r"  \item \textbf{Habeas and Custody Challenges"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Suspension Clause Applies): A Leased Atoll Outside Any War Zone.}", glue=" "),
    S(r"Suppose the United States signs a 99-year lease with a Pacific island nation granting ``exclusive U.S. administrative control'' over a remote atoll used to detain noncitizens suspected of cyber-terrorism, and Congress strips federal habeas jurisdiction while substituting an internal military review board that bars counsel and newly discovered exculpatory evidence.", glue=" "),
    S(r"Under \textit{Boumediene}'s three factors---(1) contested status with weak process, (2) long-term exclusive \textit{de facto} U.S. control outside an active war zone, and (3) minimal practical obstacles---the Suspension Clause applies, and the jurisdiction-stripping statute is an unconstitutional suspension unless Congress invokes Rebellion or Invasion or provides an adequate judicial substitute."),
    N(r"\item \textbf{Same-Side (Inadequate Substitute): Judicial Review Without the Power to Order Release.} After \textit{Boumediene}, Congress again strips district courts of habeas jurisdiction over Guantanamo detainees and substitutes review in the D.C. Circuit. The new statute lets detainees have counsel, see the evidence against them, and present newly discovered exculpatory evidence, and it authorizes the court to declare a detention unlawful. But it provides that the court may only recommend release to the Secretary of Defense, who retains final authority. \textit{Boumediene} held that an adequate substitute for habeas must include, at a minimum, the power to order the conditional release of a person unlawfully detained. Because the reviewing court cannot order release, the substitute remains inadequate and the statute operates as an unconstitutional suspension of the writ."),
    N(r"\item \textbf{Opposite-Side (Suspension Clause Does Not Apply): A Forward Operating Base in an Active Combat Zone.}", glue=" "),
    S(r"A foreign national captured and held by U.S. forces at a temporary forward operating base inside an active foreign combat zone lacks a constitutional habeas right because the United States lacks permanent exclusive control and judicial review would create severe practical and military obstacles."),
    N(r"\item \textbf{Opposite-Side (Outside the Core of the Writ): Expedited Removal at the Border.}", glue=" "),
    S(r"A noncitizen apprehended 25 yards inside the U.S. border who seeks habeas review not to obtain release from custody, but to compel a second asylum hearing and remain in the country, cannot invoke \textit{Boumediene} because such relief falls outside the historical 1789 core of the writ."),
    N(r"\item \textbf{Fence-Sitter (Close Call): A Detention Facility on an Allied Nation's Military Base.} Under a long-term status-of-forces agreement, the United States operates a detention facility on a military base in an allied country far from any active hostilities, holding noncitizens captured in a distant conflict; the host nation retains sovereignty and its law formally applies on the base, though U.S. forces run the facility. Congress bars habeas review and provides only military status hearings. Two \textit{Boumediene} factors favor the detainees: the process for determining their status is weak, and there is no war-zone friction. But the site factor points the other way, because unlike Guantanamo, the United States lacks complete and indefinite control, and a court order might create friction with the host government. How courts weigh that mix is uncertain under \textit{Boumediene}'s functional test."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Indeterminacy", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: consolidated docket numbers, rehearing grant date, constitutional-provision line, syllabus link.",
  "Legacy section: introductory paragraph; 'Deferential Post-Boumediene Guantanamo Review' item (remand outcome and D.C. Circuit evidentiary standards, Al-Hela); 'Habeas and Custody Challenges Through 2026' item (2025--2026 district-court litigation). Kept: Al Maqaleh and Thuraissigiam items.",
  "Exam Hypothetical 2: lead-in sentence 'Contrast Boumediene with two opposite side scenarios...' and the bold sub-labels; the two scenarios are reused as Examples 3 and 4.",
 ],
 "notes": ["Neon's second hypothetical contained two separate fact patterns; each is used as one Opposite-Side example."],
}

emit(__file__, FILL)
