"""Fill for 260_naacp_v_alabama. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/357/449/"
P = "Pedagogical"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Alabama tried to oust the NAACP and held it in contempt for refusing to hand over its rank-and-file membership lists; a unanimous Court held that compelled disclosure of members' identities, exposing them to reprisal without a compelling, closely related state interest, violates the freedom of association protected by the Fourteenth Amendment (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="In 1956, Alabama Attorney General")],
  "Procedural History": [SEC("Facts and Procedural History", frm="In 1956, Alabama Attorney General")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{reversed and remanded}, 9--0. The case was argued January 15--16, 1958, and decided June 30, 1958 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Harlan delivered the opinion of a unanimous Court, joined by Chief Justice Warren and Justices Black, Frankfurter, Douglas, Burton, Clark, Brennan, and Whittaker.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issues Presented"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Harlan)}"), SEC("Reasoning"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Civil Rights Progeny", to=r"  \item \textbf{\textit{First Choice"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{\textit{First Choice", to=r"\end{itemize}"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Disclosure Invalid): A Legislative Demand for an Advocacy Group's Members.} A state legislative committee investigating whether a small LGBTQ advocacy group in a rural county has lobbied without registering subpoenas the group's complete membership list. The group has already registered, produced its officers' names and its budget, and offered sworn testimony about its lobbying. It submits affidavits showing that members whose affiliation became known locally lost jobs and received threats. As in \textit{NAACP v.\ Alabama}, compelled disclosure would expose members to private reprisal made possible by state compulsion, and the rank-and-file names have no substantial bearing on the committee's stated purpose, which the group's other disclosures already serve. The subpoena cannot be enforced (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Disclosure Invalid): Teachers Required to List Every Association.} A State requires every public-school teacher, as a condition of employment, to file an affidavit listing every organization to which the teacher has belonged or contributed in the past five years. The State says it needs the information to evaluate teachers' fitness. Applying \textit{NAACP v.\ Alabama}, the Court struck down a nearly identical Arkansas law in \textit{Shelton v.\ Tucker}, 364 U.S.\ 479 (1960). The State may inquire into teachers' competence, but a demand for every association, with no limit to those relevant to fitness, reaches far beyond that interest and deters teachers from joining unpopular groups. Because disclosure is not closely tailored to the State's legitimate need, the requirement violates the freedom of association."),
    N(r"\item \textbf{Opposite-Side (Disclosure Valid): Contributions to a Federal Candidate.} A federal statute requires every candidate's campaign committee to report the name and address of anyone who contributes more than \$200, and the reports are made public. A donors' group challenges the law on its face, invoking \textit{NAACP v.\ Alabama}, but offers no evidence that its supporters have faced threats or harassment. Under \textit{Buckley v.\ Valeo}, 424 U.S.\ 1 (1976), disclosure of contributions to candidates survives exacting scrutiny because it informs voters, deters corruption, and supports enforcement of contribution limits. \textit{NAACP v.\ Alabama} still matters at the margin: a minor party or group that shows a reasonable probability that disclosure will bring threats or reprisals can seek an as-applied exemption."),
    N(r"\item \textbf{Opposite-Side (Disclosure Valid): Signers of a Referendum Petition.} Voters sign a petition to put a contested ballot measure before the electorate, and state law makes the signed petitions available to the public on request. Sponsors of the petition sue to block release of the signers' names, arguing that disclosure will chill participation. Under \textit{Doe v.\ Reed}, 561 U.S.\ 186 (2010), a facial challenge fails: signing a referendum petition is a public act in the lawmaking process, and disclosure serves the State's interest in detecting fraud and preserving the integrity of the election. Unlike the NAACP's members, the signers have not shown that disclosure will expose them to reprisal; if a particular group can make that showing, an as-applied challenge remains available."),
    N(r"\item \textbf{Fence-Sitter (Confidential Donor Lists and Foreign Influence): The Civic Transparency Act.}", glue=" "),
    S(r"To combat foreign disinformation in state policy debates, a State enacts the ``Civic Transparency Act,'' requiring any nonprofit that spends over \$5,000 annually on public-issue ads to file with the Secretary of State a confidential list of all donors contributing over \$250, subject to a \$50,000 daily contempt fine for noncompliance. The Attorney General serves a subpoena on a controversial environmental-advocacy group demanding its full donor roster to audit compliance. The group sues immediately in federal court.", glue=" "),
    N(r"For the group:", glue=" "),
    S(r"Under \textit{NAACP v. Alabama} and \textit{First Choice Women's Resource Centers v. Davenport} (2026), the group has immediate associational standing because the subpoena itself chills donors and forces it to vindicate their anonymity before exposure nullifies the right. On the merits, under \textit{NAACP v. Alabama} and \textit{Americans for Prosperity Foundation v. Bonta} (2021), the law fails exacting scrutiny: even confidential government collection chills dissident association, and a blanket \$250 donor dragnet is not narrowly tailored to detecting foreign interference when the State could use targeted, cause-based subpoenas or require foreign-funding certifications without sweeping up domestic rank-and-file donors.", glue=" "),
    N(r"For the State:", glue=" "),
    S(r"Invoke \textit{Buckley v. Valeo} and \textit{Doe v. Reed} to argue that combating foreign influence in public policy debates is a compelling governmental interest and that statutory confidentiality shields donors from the private physical and economic reprisals documented in \textit{NAACP v. Alabama}. Distinguish \textit{Bonta} by arguing the statute targets only organizations actively spending on public-issue campaigns rather than every registered charity, making the \$250 threshold substantially related to enforcing foreign-funding bans.", glue=" "),
    N(r"Because the law is aimed at a weighty interest but sweeps in every small domestic donor, its fate turns on how strictly a court applies \textit{Bonta}'s tailoring requirement."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC(P, frm=r"\begin{itemize}", to=r"\textbf{``Opposite Side'' Contrast")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, Cornell CONAN link.",
  "Concurring and Dissenting Opinions section ('None. ...'): restated in Judicial Votes; its commentary sentence on institutional solidarity dropped.",
  "Legacy section: introductory sentence (including the NAACP v. Alabama ex rel. Flowers parenthetical). Kept: Civil Rights Progeny item, Bonta item, First Choice Women's Resource Centers v. Davenport item.",
  "'Opposite Side' Contrast (Bryant v. Zimmerman and Doe v. Reed): an exam tip comparing real cases rather than a fact pattern; Bryant is covered in the Reasoning and Doe v. Reed in Example 4.",
  "Exam Hypothetical labels ('Organization's Best Arguments', 'State's Best Arguments'); their text is reused in Example 5.",
 ],
 "notes": ["Kept First Choice Women's Resource Centers, Inc. v. Davenport (2026) item (608 U.S. 174, unanimous, Gorsuch, J., April 29, 2026) is from Neon's original and should be verified against the official report."],
}

emit(__file__, FILL)
