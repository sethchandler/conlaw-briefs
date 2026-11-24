"""Fill for 184_haaland_v_brackeen. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/599/21-376/"
LII = r"(\href{https://www.law.cornell.edu/supremecourt/text/21-376}{Cornell LII})"

def Q(quote, who):
    # Attribution placed inside the quote block; tools/normalize_quotes.py moves it to a
    # Group A "\noindent ---" line (check_brief.py runs it for every brief).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "), S(who, glue=" "),
            S(LII, glue="\n"), N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Rejecting a multi-front attack on the Indian Child Welfare Act, the Court held 7--2 that ICWA falls within Congress's Article~I power over Indian affairs, that its custody rules do not commandeer the States, and that the individual challengers and Texas lacked standing to press equal protection claims against federal officials (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The individual petitioners joined Texas")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The individual petitioners joined Texas")],
  "Judicial Votes": [
    N(r"The Supreme Court decided the case by a \textbf{7--2} vote. It was argued on November 9, 2022, and decided on June 15, 2023 (\href{" + J + r"}{Justia}; " + LII[1:] + r". Disposition:", glue=" "),
    S(r"994 F.3d 249 affirmed in part (Article I legislative authority), reversed in part (Tenth Amendment anticommandeering), and vacated and remanded in part with instructions to dismiss for lack of jurisdiction (equal protection and nondelegation)", glue=""), N("."),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Barrett delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Sotomayor, Kagan, Gorsuch, Kavanaugh, and Jackson.
    \item \textbf{Concurring Opinions:} Justice Gorsuch filed a concurring opinion, joined by Justices Sotomayor and Jackson as to Parts I and III. Justice Kavanaugh filed a concurring opinion.
    \item \textbf{Dissenting Opinions:} Justice Thomas and Justice Alito each filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Barrett)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Gorsuch)}"), N("Justice Gorsuch", glue=" "),
    SEC("Concurring and Dissenting", frm="Chronicled the history", to=r"\item \textbf{Justice Kavanaugh", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Kavanaugh)}"), N("Justice Kavanaugh", glue=" "),
    SEC("Concurring and Dissenting", frm="Emphasized that the equal", to=r"\item \textbf{Justice Thomas", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC("Concurring and Dissenting", frm="Argued that the majority", to=r"\item \textbf{Justice Alito", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Alito)}"), N("Justice Alito", glue=" "),
    SEC("Concurring and Dissenting", frm="Criticized the majority", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"\item \textbf{Redressability and State Standing", to=r"\item \textbf{State ICWA Laws"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Statute Upheld): A Federal Rule for Tribal Members' Estates.}", glue=" "),
    S(r"Congress enacts a statute requiring ``any party'' petitioning a state probate court over an off-reservation tribal member's intestate estate to show ``active efforts'' to notify the tribe, apply a federal heirloom preference favoring tribal relatives, and have state probate clerks transmit inventories to the Interior Department. Under \textit{Brackeen}, there is no ``probate carveout'' to Article I Indian-affairs power; the ``any party'' rule is evenhanded; the preference validly preempts state law in state courts; clerk reporting is an ancillary judicial duty; and neither a State nor a surviving spouse suing federal officials in federal court has standing to raise an equal protection challenge."),
    N(r"\item \textbf{Same-Side (No Standing): An Adoption Agency Sues the Secretary.} A private adoption agency that places children with non-Indian foster families sues the Secretary of the Interior in federal district court, alleging that ICWA's foster-care preferences in \S~1915(b) disadvantage its families on the basis of race, and seeks a declaratory judgment and an injunction against the Secretary. Under \textit{Brackeen}, the suit must be dismissed for lack of redressability: state courts and state agencies, not the Secretary, apply the placement preferences, so a judgment against the Secretary would not bind the state judges who decide each placement. That a favorable federal opinion might persuade state courts does not count, because it is the judgment, not the opinion, that redresses an injury. The agency's families may raise the claim in an appropriate state-court custody proceeding in which the preferences are applied, as Justice Kavanaugh's concurrence noted."),
    N(r"\item \textbf{Opposite-Side (Statute Invalid): A Nationwide Child-Welfare Mandate Under the Interstate Commerce Clause.}", glue=" "),
    S(r"Now suppose Congress invokes the \emph{Interstate} Commerce Clause to enact a nationwide child-welfare law applying to \emph{all} children that directs ``every State's Department of Child Protective Services'' (and no private actors) to conduct 50-state extended-family searches and orders state legislatures to adopt federal foster-licensing codes. Here, the outcome flips on every axis: (1) under the Interstate Commerce Clause (\textit{Lopez}; \textit{Morrison}), non-economic family custody proceedings lack a commercial nexus, making ``children are not commodities'' dispositive; (2) singling out state agencies and state legislatures directly violates \textit{Printz}, \textit{New York}, and \textit{Murphy}; and (3) the State possesses direct sovereign standing to challenge the federal command."),
    N(r"\item \textbf{Opposite-Side (Provision Likely Invalid): A Search Duty Imposed Only on State Agencies.} Amending ICWA itself, Congress requires each State's child-welfare agency, and no other party, to complete a documented nationwide search for extended-family and tribal placements before any Indian child may enter foster care, and to file monthly search reports with the Secretary of the Interior. Congress's Article~I power over Indian affairs still covers the subject, so the challenge turns on the Tenth Amendment. \textit{Brackeen} upheld \S~1912 because it binds ``any party'' evenhandedly and upheld \S~1915 because, under \textit{Adoptive Couple v. Baby Girl}, it imposes no search duty on state agencies. A duty addressed only to state executive agencies, with reporting by agency officials rather than ancillary court recordkeeping, is the kind of direct command to state officers that \textit{Printz} and \textit{Murphy} forbid, so the State would likely prevail."),
    N(r"\item \textbf{Fence-Sitter (Undecided): An Equal Protection Challenge Raised in State Court.} Non-Indian foster parents seek to adopt a child who is eligible for membership in one tribe and has a biological parent who is a member of that tribe; a family belonging to a different tribe asks for the placement under \S~1915(a)'s ``other Indian families'' preference. In the state adoption proceeding, where the preference is actually applied, the foster parents argue that it is a racial classification barred by \textit{Palmore v. Sidoti}, 466 U.S. 429 (1984). An actual application of the preference would address the redressability problem identified in the federal suit, allowing the foster parents to raise the merits \textit{Brackeen} left open. The tribe answers that, under \textit{Morton v. Mancari}, 417 U.S. 535 (1974), classifications tied to tribal membership are political, not racial. The foster parents reply that a preference for families of any tribe looks less like a political tie to the child's own tribe and more like ancestry. Justice Kavanaugh called the issue ``serious,'' and the Court has not resolved it."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Unstated Outer", to=r"\end{itemize}")],
  "Key Quotations":
    Q(r"``To be clear, however, `plenary' does not mean `free-floating.' A power unmoored from the Constitution would lack both justification and limits. So like the rest of its legislative powers, Congress's authority to regulate Indians must derive from the Constitution, not the atmosphere.''", "Barrett, J.")
    + Q(r"``It could not be otherwise---Article I gives Congress a series of enumerated powers, not a series of blank checks. Thus, we reiterate that Congress's authority to legislate with respect to Indians is not unbounded. It is plenary within its sphere, but even a sizeable sphere has borders. \ldots{} But the Constitution does not erect a firewall around family law.''", "Barrett, J.")
    + Q(r"``It is a federal court's judgment, not its opinion, that remedies an injury; thus it is the judgment, not the opinion, that demonstrates redressability. The individual petitioners can hope for nothing more than an opinion, so they cannot satisfy Article III.''", "Barrett, J.")
    + Q(r"``Our Constitution reserves for the Tribes a place---an enduring place---in the structure of American life. It promises them sovereignty for as long as they wish to keep it. And it secures that promise by divesting States of authority over Indian affairs and by giving the federal government certain significant (but limited and enumerated) powers aimed at building a lasting peace.''", "Gorsuch, J., concurring"),
 },
 "dropped": [
  "Case Metadata: full consolidated case name, docket numbers, certiorari date, SupremeCourt.gov slip-opinion and page-proof links (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: 'Article I Authority and Anticommandeering' summary paragraph (restates the holding); 'State ICWA Laws and the Unresolved Equal Protection Issue' item (state legislation and a 2026 certiorari denial, not decisions applying Brackeen's holding). Kept: 'Redressability and State Standing' item (United States v. Texas, Murthy v. Missouri, Arizona v. Navajo Nation).",
  "Key Quotations: the bold descriptive labels before each quotation (e.g., 'Plenary Power Must Have Constitutional Borders'); the attribution 'Barrett, J.' / 'Gorsuch, J., concurring' and the Cornell LII link are kept.",
  "Exam Hypotheticals: headings 'Hypothetical 1 (Tracking Brackeen)' and 'Hypothetical 2 (Opposite Side Contrast)' replaced by Group A labels; both fact patterns reused verbatim (Examples 1 and 3).",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all four kept, none added. The original gives no pin cites, so none are supplied."],
}

emit(__file__, FILL)
