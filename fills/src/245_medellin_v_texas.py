"""Fill for 245_medellin_v_texas. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/552/491/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"The Court held 6--3 that neither the ICJ's \textit{Avena} judgment nor President Bush's memorandum directing state courts to give it effect was binding domestic law: a non-self-executing treaty obligation becomes enforceable in U.S. courts only through congressional implementing legislation (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Convicted of capital murder and sentenced")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Convicted of capital murder and sentenced")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Texas Court of Criminal Appeals by a \textbf{6--3} vote. The case was argued on October 10, 2007, and decided on March 25, 2008 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supct/html/06-984.ZS.html}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Roberts delivered the opinion of the Court, joined by Justices Scalia, Kennedy, Thomas, and Alito.
    \item \textbf{Concurring Opinion:} Justice Stevens filed an opinion concurring in the judgment.
    \item \textbf{Dissenting Opinion:} Justice Breyer filed a dissenting opinion, joined by Justices Souter and Ginsburg.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Judgment (Justice Stevens)}"),
    SEC("Concurring and Dissenting", frm="Stevens rejected any presumption", to=r"  \item \textbf{Justice Breyer"),
    N(r"\subsection{Dissenting Opinion (Justice Breyer)}"),
    SEC("Concurring and Dissenting", frm="Breyer faulted the majority", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Aftermath:}", glue=" "),
    S(r"(Following the decision, Congress declined to enact implementing legislation, and Texas executed Medell\'{i}n in August 2008.)"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Not Domestic Law): A Presidential Directive Enforcing an International Tribunal's Ruling.}", glue=" "),
    S(r"The United States ratifies a multilateral Environmental Disputes Treaty stating that signatory states ``undertake to give effect'' to binding rulings of an International Environmental Tribunal, with noncompliance referred to a diplomatic council. Congress enacts no implementing statute. After the Tribunal rules that a California coastal zoning law violates the treaty, the President issues a Presidential Directive ordering California courts to enjoin enforcement of the zoning law to honor U.S. treaty obligations.", glue=" "),
    S(r"Under \textit{Medell\'{i}n}, both the Tribunal's ruling and the Presidential Directive fail to preempt California law. The ``undertake to give effect'' text and diplomatic enforcement mechanism mark the treaty as non-self-executing, and under \textit{Youngstown} Category Three, the President cannot unilaterally transform a non-self-executing treaty into binding domestic law overriding state police-power regulations."),
    N(r"\item \textbf{Same-Side (Not Domestic Law): A Human-Rights Treaty Ratified With a Non-Self-Executing Declaration.} The Senate consents to a human-rights treaty guaranteeing fair criminal procedures, but attaches a declaration that the treaty's substantive provisions are not self-executing, and Congress passes no implementing statute. A state prisoner petitions a state court to vacate his conviction, arguing that a state evidentiary rule violates the treaty and is preempted under the Supremacy Clause. Under \textit{Medell\'{i}n}, a treaty is domestic law only if Congress implements it or the treaty itself conveys an intention that it be self-executing and is ratified on those terms. Here the ratifying Senate expressly said the opposite. The treaty binds the United States internationally, but it gives the prisoner no rule of decision that state courts must apply."),
    N(r"\item \textbf{Opposite-Side (Binding Domestic Law): Implementing Legislation or Explicit Self-Executing Text.} Return to the environmental-tribunal hypothetical, but change the legal backdrop.", glue=" "),
    S(r"First, if Congress enacts implementing legislation directing federal and state courts to enforce Tribunal judgments (as Congress did for ICSID arbitral awards in 22 U.S.C. \S~1650a), or if the Senate ratifies a treaty whose text explicitly directs that ``domestic courts of each Party shall enforce Tribunal orders as final judgments,'' the obligation becomes supreme federal law binding California courts under Article VI."),
    N(r"\item \textbf{Opposite-Side (Valid Executive Action): A Claims-Settlement Executive Agreement.} Alternatively,", glue=" "),
    S(r"if the President resolves a longstanding diplomatic crisis by entering an executive agreement settling commercial civil claims of U.S. citizens against a foreign sovereign within a 200-year tradition of congressional acquiescence, the agreement preempts contrary state civil remedies under \href{https://supreme.justia.com/cases/federal/us/453/654/}{\textit{Dames \& Moore v. Regan}} and \textit{Garamendi}."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): A Damages Suit for Failure to Give Consular Notice.} Police arrest a foreign national and never tell him of his right under Article 36 of the Vienna Convention to have his consulate notified. After his release, he sues the officers for damages under 42 U.S.C.\ \S~1983, claiming they violated rights secured by federal law. Unlike Medell\'{i}n's claim, this suit does not depend on an ICJ judgment or a presidential memorandum; it rests on the Convention itself, which Justices Stevens and Breyer viewed as self-executing. Whether Article 36 also confers individual rights enforceable in a private damages action is a separate question: the Court in \textit{Sanchez-Llamas v.\ Oregon}, 548 U.S.\ 331 (2006), assumed without deciding that it does, and \textit{Medell\'{i}n} did not resolve the point. The outcome therefore remains uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Federalism Versus", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Briefing Book placement line, lower-court line.",
  "Legacy section: opening framing sentence; New York Convention circuit-court paragraph (2025 lower-court arbitration decisions, sourced to a law-firm newsletter); Zivotofsky / Dames & Moore / Learning Resources v. Trump paragraph (tangential separation-of-powers commentary). Kept: the aftermath sentence (no implementing legislation; Medellin executed).",
  "Exam Hypothetical 'Analysis:' label and 'Opposite Side' Contrast lead-in sentence; the two modifications are reused as Examples 3 and 4.",
 ],
 "notes": ["Example 5 states that Sanchez-Llamas assumed without deciding that Article 36 grants individually enforceable rights; reviewer may wish to confirm."],
}

emit(__file__, FILL)
