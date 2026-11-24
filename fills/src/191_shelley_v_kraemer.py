"""Fill for 191_shelley_v_kraemer. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/334/1/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Private racially restrictive covenants do not themselves violate the Fourteenth Amendment, but a state court's enforcement of them is state action that denies equal protection; a unanimous six-Justice Court reversed Missouri and Michigan decrees ousting Black families from homes they had bought from willing sellers (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [
    SEC("Facts and Procedural History", to="On October 9, 1945"),
    S(r"\subsection{The Michigan Litigation (\textit{McGhee v. Sipes}, No.~87)}"),
    SEC("Facts and Procedural History", frm="In June 1934", to="On January 30, 1945"),
  ],
  "Procedural History": [
    N(r"\textbf{Missouri (\textit{Shelley v. Kraemer}):}", glue=" "),
    SEC("Facts and Procedural History", frm="On October 9, 1945", to=r"\subsection{The Michigan"),
    N(r"\textbf{Michigan (\textit{McGhee v. Sipes}):}", glue=" "),
    SEC("Facts and Procedural History", frm="On January 30, 1945"),
  ],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the judgments of the Supreme Courts of Missouri and Michigan by a \textbf{6--0} vote. The cases were argued on January 15--16, 1948, and decided on May 3, 1948 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Vinson delivered the opinion of the Court, joined by Justices Black, Frankfurter, Douglas, Murphy, and Burton.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} None.
    \item \textbf{Not Participating:} Justices Reed, Jackson, and Rutledge took no part in the consideration or decision of the cases."""),
    S(r"Although the Justices issued no public explanation in the \textit{United States Reports}, historical scholarship and contemporary accounts attribute their recusals to their ownership of residential properties subject to racially restrictive covenants."),
    N(r"\end{itemize}"),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Vinson)}"), SEC("Reasoning"),
    N(r"\subsection{Companion Case: \textit{Hurd v. Hodge}}"),
    SEC("Concurring and Dissenting", frm="In the companion District of Columbia case", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Extension to Damages Actions:}", glue=" "),
    SEC("Doctrinal Significance", frm="Five years after", to="In 1968, federal statutory law"),
    SEC("Doctrinal Significance", frm=r"    \item \textbf{Limits Even in Racial Disputes:}", to=r"    \item \textbf{Selective Vitality"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Enforcement Barred): A Religious Covenant Used to Divest Title.}", glue=" "),
    S(r"A homeowners' association sues in state court to enforce a recorded neighborhood covenant barring sales to non-Christian buyers, seeking to divest title after a willing owner sells her home to a Muslim family.", glue=" "),
    S(r"Scenario~A falls squarely under \textit{Shelley} (and violates the Fair Housing Act): third parties are enlisting judicial coercion to override a voluntary transaction and enforce neighborhood-wide exclusion."),
    N(r"\item \textbf{Same-Side (Enforcement Barred): Damages Against the Selling Owner.} A recorded subdivision covenant bars sale to persons of a particular national origin. An owner sells to a willing buyer of that origin, and the neighbors, rather than seeking to evict the buyer, sue the seller in state court for breach of the covenant and ask for money damages. Under \textit{Shelley}, a state court that lends its coercive power to a discriminatory private agreement is itself acting for the State, and \textit{Barrows v. Jackson}, 346 U.S. 249 (1953), applied that reasoning to damages actions because the threat of liability would pressure owners to refuse willing buyers. The court must deny relief; the Equal Protection Clause reaches national-origin classifications as well as race (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (No Constitutional Violation): Excluding a Guest From One's Own Home.}", glue=" "),
    S(r"A private homeowner bars a neighbor from a home dinner party because of the neighbor's religion and calls police to prosecute the neighbor for criminal trespass.", glue=" "),
    N(r"Unlike in \textit{Shelley}, no willing owner is being overridden: the State's trespass law enforces the owner's own choice about her own home, and", glue=" "),
    S(r"an \textit{unwilling} owner's personal trespass exclusion reflects private associational autonomy rather than third-party coercion", glue=""),
    N(r". Reading \textit{Shelley} to reach this case would turn every invocation of neutral property law into constitutional state action."),
    N(r"\item \textbf{Opposite-Side (No State Action): Enforcing a Non-Disparagement Clause.}", glue=" "),
    S(r"A private contractor petitions a state court to enjoin a former employee from publishing a critical op-ed in breach of a voluntary settlement's non-disparagement clause. The employee cites \textit{Shelley}, claiming judicial enforcement triggers First Amendment strict scrutiny.", glue=" "),
    S(r"Although \textit{Shelley}'s broad language invites the argument, modern courts reject extending its attribution rationale to private speech contracts (\textit{United Egg Producers}), preserving private ordering under \href{https://supreme.justia.com/cases/federal/us/587/17-1702/}{\textit{Manhattan Community Access Corp. v. Halleck}, 587 U.S. 802 (2019)}, while confining judicial state action to racial discrimination or core courtroom processes such as peremptory strikes (\href{https://supreme.justia.com/cases/federal/us/500/614/}{\textit{Edmonson v. Leesville Concrete Co.}, 500 U.S. 614 (1991)})."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): A Testamentary Condition Based on a Beneficiary's Spouse.} A will leaves a large bequest to the testator's grandson on the condition that he marry a person of the testator's own faith within seven years; otherwise the money passes to a charity. The grandson marries outside the faith and asks the state probate court to strike the condition, arguing that judicial enforcement is state action under \textit{Shelley}. He can point out that the court's decree would give legal force to a private religious exclusion. But no willing seller and willing buyer are being overridden: the court would simply carry out the testator's own disposition of his own property under neutral probate rules, the posture that \textit{Evans v. Abney} treated as permissible. Because \textit{Shelley}'s reach beyond restrictive covenants has never been defined, the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"    \item \textbf{Collapse", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket numbers, Oyez link, lower-court citations, Chapter line, companion-case line, file comments (Justia link kept in Judicial Votes).",
  "Concurring and Dissenting: 'no concurring or dissenting opinions' sentence and the lead-in (restated in Judicial Votes).",
  "Legacy section: 1968 statutory displacement paragraph (Fair Housing Act, Jones v. Alfred H. Mayer - statutory, not an application of Shelley's holding); 'Doctrinal Containment' intro paragraph; Palmore / Lugar / Edmonson item; Halleck / Lindke item (general state-action doctrine); UURLRA land-records subsection. Kept: Barrows v. Jackson and Evans v. Abney.",
  "Exam Hypothetical 1: Scenario B(2) (neutral trust reversion) - restates Evans v. Abney, which is kept under Subsequent Developments; headings and 'Opposite Side' labels.",
 ],
 "notes": ["Example 2 cites Barrows v. Jackson, 346 U.S. 249 (1953), which the brief already discusses.",
           "Example 4 reuses Neon's non-disparagement hypothetical, which cites United Egg Producers (11th Cir.) and Halleck as the brief does."],
}

emit(__file__, FILL)
