"""Fill for 192_jackson_v_metropolitan_edison. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/419/345/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"A privately owned, heavily regulated electric monopoly that cut off a customer's power without notice or a hearing was not a state actor: the Court required a close nexus between the State and the specific challenged act, and confined the public-function doctrine to powers traditionally exclusively reserved to the State (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Jackson sued Metropolitan in the United States")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Jackson sued Metropolitan in the United States")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Third Circuit by a \textbf{6--3} vote. The case was argued on October 15, 1974, and decided on December 23, 1974 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Rehnquist delivered the opinion of the Court, joined by Chief Justice Burger and Justices Stewart, White, Blackmun, and Powell.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Douglas, Justice Brennan, and Justice Marshall each filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Rehnquist)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Douglas)}"),
    SEC("Concurring and Dissenting", frm="Justice Douglas attacked", to=r"\subsection{Justice Brennan"),
    N(r"\subsection{Dissenting Opinion (Justice Brennan)}"),
    SEC("Concurring and Dissenting", frm="Justice Brennan declined", to=r"\subsection{Justice Marshall"),
    N(r"\subsection{Dissenting Opinion (Justice Marshall)}"),
    SEC("Concurring and Dissenting", frm="Justice Marshall agreed"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Consolidation (1978--1999):}", glue=" "),
    S(r"The Court extended \emph{Jackson}'s exclusivity and compulsion limits across private economic and social-welfare disputes in \href{https://supreme.justia.com/cases/federal/us/436/149/}{\emph{Flagg Bros., Inc. v. Brooks}}, 436 U.S. 149 (1978) (warehouseman's UCC lien sale), \href{https://supreme.justia.com/cases/federal/us/457/991/}{\emph{Blum v. Yaretsky}}, 457 U.S. 991 (1982) (Medicaid-funded nursing homes), \href{https://supreme.justia.com/cases/federal/us/457/830/}{\emph{Rendell-Baker v. Kohn}}, 457 U.S. 830 (1982) (publicly funded private school), \href{https://www.law.cornell.edu/supremecourt/text/457/922}{\emph{Lugar v. Edmondson Oil Co.}}, 457 U.S. 922 (1982) (two-part fair-attribution test), and \href{https://www.law.cornell.edu/supremecourt/text/526/40}{\emph{American Manufacturers Mutual Insurance Co. v. Sullivan}}, 526 U.S. 40 (1999) (workers'-compensation utilization review)."),
    SEC("Doctrinal Significance", frm=r"\item \textbf{\href{https://www.law.cornell.edu/supremecourt/text/17-1702}", to=r"\item \textbf{\href{https://www.law.cornell.edu/supremecourt/text/22-611}"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (No State Action): A Medicaid-Funded Nursing Home Transfers a Resident.} A privately owned nursing home, licensed and closely regulated by the State and receiving most of its revenue from Medicaid, decides through its own physicians that a resident needs only a lower level of care and transfers her to another facility without a hearing. The State then reduces her Medicaid benefits to match the new placement. Under \textit{Jackson}, licensing, heavy regulation, and public funding do not make the home's decision the State's; the question is whether the State compelled or put its own weight behind the specific transfer, and here private medical judgment made it. \textit{Blum v. Yaretsky}, 457 U.S. 991 (1982), applied \textit{Jackson} to these facts and found no state action, so the resident has no Fourteenth Amendment due process claim against the home."),
    N(r"\item \textbf{Same-Side (No State Action): A Franchised Internet Provider Cancels Service.} A privately owned broadband company holds an exclusive municipal franchise, strings its fiber along public rights-of-way, and is regulated by the state utility commission. It terminates a subscriber's service for disputed late payments without notice, under a termination clause in its filed terms of service that the commission never reviewed. Each of the subscriber's arguments fails as it did in \textit{Jackson}: regulation and a franchise do not supply a nexus to the specific termination; supplying internet service, like supplying electricity, has never been a power traditionally and exclusively reserved to the State; and the commission's passive acceptance of the filed terms does not put the State's weight behind the shutoff. Without state action, the subscriber's remedies lie in contract and state utility law."),
    N(r"\item \textbf{Opposite-Side (State Action): A Commission-Ordered Shutoff.}", glue=" "),
    S(r"A state utility commission issues an emergency order directing private electric utilities to remotely disconnect high-usage smart meters without a hearing.", glue=" "),
    S(r"Unlike \emph{Jackson}'s passive tariff filing, state compulsion establishes a close nexus (419 U.S. at 357; \href{https://supreme.justia.com/cases/federal/us/457/991/}{\emph{Blum}}), triggering \href{https://supreme.justia.com/cases/federal/us/436/1/}{\emph{Craft}} due-process scrutiny."),
    N(r"\item \textbf{Opposite-Side (Likely State Action): A Utility Condemns an Easement.} The same kind of private electric company, using a power of eminent domain that state law delegates to certificated utilities, files a condemnation proceeding and takes a permanent easement across a homeowner's backyard for a new transmission line. The homeowner sues, claiming the taking was not for public use and that the procedures denied her due process. \textit{Jackson} itself marks this as the contrasting case: the Court said that if Metropolitan were exercising ``some power delegated to it by the State which is traditionally associated with sovereignty, such as eminent domain,'' the case ``would be quite a different one.'' Condemnation is a sovereign power the State has lent to the utility, so the utility's use of it is fairly attributable to the State."),
    N(r"\item \textbf{Fence-Sitter (Charter School Unresolved): Charter School vs.\ Prison Clinic.}", glue=" "),
    S(r"A 100\% state-funded private charter school expels a student without a hearing; a private prison healthcare contractor withholds insulin.", glue=" "),
    S(r"The prison contractor is a state actor under \href{https://supreme.justia.com/cases/federal/us/487/42/}{\emph{West v. Atkins}}; the charter school sits on the unresolved \emph{Jackson}/\href{https://supreme.justia.com/cases/federal/us/457/830/}{\emph{Rendell-Baker}}/\href{https://www.law.cornell.edu/supct/cert/24-394}{\emph{Drummond}} boundary between non-exclusive education and statutory public-entity entwinement (\href{https://www.law.cornell.edu/supremecourt/text/531/288}{\emph{Brentwood}}).", glue=" "),
    N(r"The school is the hard case. On one side, education has never been an exclusive state prerogative, and \textit{Rendell-Baker} held that a privately run school funded almost entirely by public money was not a state actor when it fired employees. On the other, a State that labels charter schools as public schools makes them part of its public education system, and controls their charters looks more like the entwined State in \textit{Brentwood}. Because the Court divided evenly in \textit{Drummond}, the outcome is open."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [
    N(r"\textbf{Core Critiques:}", glue=" "),
    SEC("Pedagogical", frm="Critics emphasize three", to=r"\subsection{Exam Hypotheticals}"),
    N(r"\textbf{The Formalist Cliff (\textit{Memphis Light} Contrast):}", glue=" "),
    SEC("Pedagogical", frm="Four years after", to=r"\subsection{Core Critiques}"),
  ],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, court line, provisions list, comment lines, Chapter/Topic (Justia link kept in Memory Jogger and Judicial Votes).",
  "Concurring and Dissenting intro sentence ('No Justice filed a separate concurring opinion...') - replaced by Judicial Votes list; the original subsection headings with page ranges replaced by Group A headings.",
  "Legacy section: introductory paragraph (restates the two constraints); the 'Narrow exceptions survived' sentence (West v. Atkins, Edmonson, Brentwood); Lindke v. Freed / O'Connor-Ratcliff / Murthy item (public-official and jawboning cases, not applications of Jackson's holding); Drummond item (4-4 affirmance without opinion; still mentioned in the Fence-Sitter example). Kept: Consolidation sentence (Flagg Bros., Blum, Rendell-Baker, Lugar, Sullivan) and Halleck item.",
  "Exam Hypothetical 2 (Dominant Platform vs. Mayor's Page): mixes a Halleck/Murthy platform question with a Lindke official-account question not governed by Jackson; replaced by new examples.",
  "Exam Hypotheticals 1 and 3: the 'Analysis:' labels (text reused in Examples 3 and 5).",
 ],
 "notes": [],
}

emit(__file__, FILL)
