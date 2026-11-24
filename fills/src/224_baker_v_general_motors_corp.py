"""Fill for 224_baker_v_general_motors_corp. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/522/222/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"A Michigan consent injunction barring a former GM engineer from testifying against GM could not stop him from testifying, under subpoena, in a Missouri wrongful-death suit brought by strangers to the Michigan case: sister-state judgments get exacting full faith and credit with no public-policy exception, but enforcement measures do not travel and a decree cannot control other courts' litigation (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Her sons, Kenneth Lee Baker")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Her sons, Kenneth Lee Baker")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{reversed and remanded} (9--0 in the judgment), though the Justices split 5--4 on the rationale. The case was argued on October 15, 1997, and decided on January 13, 1998 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/96-653}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Ginsburg delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices Stevens, Souter, and Breyer.
    \item \textbf{Concurring Opinions:} Justice Scalia concurred in the judgment. Justice Kennedy concurred in the judgment, joined by Justices O'Connor and Thomas.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Ginsburg)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Judgment (Justice Scalia)}"),
    SEC("Concurring and Dissenting", frm=r"Writing alone, \href", to=r"\item \textbf{Justice Kennedy"),
    N(r"\subsection{Concurring in the Judgment (Justice Kennedy)}"),
    SEC("Concurring and Dissenting", frm=r"\href{https://www.law.cornell.edu/supct/html/96-653.ZC1.html}{Justice Kennedy} warned", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"\item \textbf{Post-\textit{Baker} Supreme Court", to=r"\item \textbf{Records, Executive"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Testimony Allowed): A Gagged Pharmaceutical Scientist.}", glue=" "),
    S(r"State~A enters a stipulated permanent injunction barring a former pharmaceutical scientist from testifying nationwide about a drug's side effects, with a side letter waiving contempt if subpoenaed. Nonparty plaintiffs injured in State~B sue the manufacturer in State~B and subpoena the scientist.", glue=" "),
    S(r"Under \textit{Baker}, State~B's court may compel testimony without violating Article~IV, Section~1; State~A lacks authority to control evidentiary subpoenas in nonparty litigation outside its borders."),
    N(r"\item \textbf{Same-Side (Forum Law Controls Enforcement): Garnishment Under the Forum's Rules.} A creditor wins a valid money judgment in State~A, whose law allows garnishment of up to half of a debtor's wages, and registers it in State~B, where the debtor now lives and works. State~B caps wage garnishment at a much lower percentage and exempts the debtor's homestead. The creditor argues that full faith and credit requires State~B to apply State~A's garnishment rules. Under \textit{Baker}, State~B must recognize the judgment and treat the debt as conclusively established; it may not relitigate liability. But the Clause does not require a State to adopt another State's time, manner, and mechanisms for enforcing judgments. Enforcement measures do not travel with the judgment, so State~B's evenhanded garnishment limits and exemptions govern collection."),
    N(r"\item \textbf{Opposite-Side (Full Faith and Credit Binds): A Money Judgment on a Confidentiality Settlement.} Suppose", glue=" "),
    S(r"a State~A court with personal and subject-matter jurisdiction enters a final \textit{money judgment} for breach of a non-disclosure settlement against Elwell, and GM seeks to domesticate that money judgment in State~B, whose legislature has declared such confidentiality clauses contrary to State~B's public policy.", glue=" "),
    N(r"State~B must enforce the judgment. Unlike the injunction in \textit{Baker}, the judgment does not try to control State~B's courts or witnesses; it simply fixes a debt between parties over whom State~A had jurisdiction. \textit{Baker} reaffirmed that there is no roving public-policy exception for judgments, and \textit{Fauntleroy v. Lum}, 210 U.S. 230 (1908), required enforcement of a judgment on a claim the forum State itself would not have enforced."),
    N(r"\item \textbf{Opposite-Side (Preclusion Binds the Bakers): The Bakers Litigate and Lose in Michigan.}", glue=" "),
    S(r"Suppose instead that the Bakers had intervened in the Michigan proceeding, fully litigated whether Elwell's testimony was protected by attorney--client privilege, and lost in a final Michigan judgment.", glue=" "),
    N(r"The Bakers would then be parties bound by the Michigan judgment, and the Michigan court would have had adjudicatory authority over them. \textit{Baker}'s rule that a judgment rendered by a court with jurisdiction over the persons it governs qualifies for recognition throughout the land would require the Missouri federal court to give the privilege ruling the same issue-preclusive effect it has in Michigan, whatever Missouri's policy favoring disclosure."),
    N(r"\item \textbf{Fence-Sitter (Unsettled): An Out-of-State Judgment Against a Shield-Law Physician.} A court in State~A, where abortion is banned, enters a civil money judgment against a physician licensed in State~B for prescribing abortion medication by telehealth to a State~A resident. State~B has enacted a shield law forbidding its officials to enforce such judgments, and a State~B court clerk refuses to file it. Under \textit{Baker}'s exacting rule, State~B's contrary policy cannot justify refusal, which suggests the judgment must be enforced. But the physician may argue that the judgment is penal and so falls outside full faith and credit under \textit{Huntington v. Attrill}, 146 U.S. 657 (1892), or that State~A lacked personal jurisdiction over a physician who never entered State~A. How those doctrines apply to telehealth remains unsettled."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\textbf{Pedagogical Critique:}", to=r"\textbf{Exam Hypothetical")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, chapter line, lower-court line, provisions list (Justia and Cornell links kept in Judicial Votes).",
  "Concurring and Dissenting intro sentence (covered by Judicial Votes); the bold item labels.",
  "Legacy section: introductory paragraph (restates the two rules); 'Records, Executive Officials, and Congress's Effects Power' item (Adar v. Smith, a lower-court decision; Respect for Marriage Act, legislation not applying Baker); 'Interstate Shield-Law Litigation (2025--2026)' item (ongoing lower-court litigation and commentary; its issue is reframed as the Fence-Sitter hypothetical without the post-2023 specifics). Kept: 'Post-Baker Supreme Court Reaffirmations' item (Hyatt I/III, Lance v. Dennis, V.L. v. E.L.).",
  "Exam Hypotheticals: 'Analysis:' label; the 'Opposite Side' Contrast's 'Contrast:' paragraph (its points are restated in Examples 3 and 4, which split the two scenarios).",
 ],
 "notes": [],
}

emit(__file__, FILL)
