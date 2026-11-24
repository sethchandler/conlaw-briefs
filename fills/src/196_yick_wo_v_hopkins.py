"""Fill for 196_yick_wo_v_hopkins. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/118/356/"
def PIN(p): return S(r"\href{https://supreme.justia.com/cases/federal/us/118/356/}{118 U.S. at " + p + "}", glue="\n")

# NOTE: tools/manual_quotes.txt lists "<stem>.tex", so check_brief.py's MANUAL set never matches a
# stem and normalize_quotes.py always runs. Each quote block is built with its attribution after
# "---" inside the block; normalize_quotes.py then moves it to a Group A "\noindent ---" line.
def QB(quote, pin):
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue=" "), N("--- Justice Matthews,", glue=" "), PIN(pin), N(r"\end{quote}")]

QUOTES = (
  QB(r"``The Fourteenth Amendment to the Constitution is not confined to the protection of citizens. It says: `Nor shall any State deprive any person of life, liberty, or property without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws.' These provisions are universal in their application to all persons within the territorial jurisdiction, without regard to any differences of race, of color, or of nationality, and the equal protection of the laws is a pledge of the protection of equal laws.''", "369")
  + QB(r"``For the very idea that one man may be compelled to hold his life, or the means of living, or any material right essential to the enjoyment of life at the mere will of another seems to be intolerable in any country where freedom prevails, as being the essence of slavery itself.''", "370")
  + QB(r"``Though not regarded strictly as a natural right, but as a privilege merely conceded by society according to its will under certain conditions, nevertheless it is regarded as a fundamental political right, because preservative of all rights.''", "370")
  + QB(r"``Though the law itself be fair on its face and impartial in appearance, yet, if it is applied and administered by public authority with an evil eye and an unequal hand, so as practically to make unjust and illegal discriminations between persons in similar circumstances, material to their rights, the denial of equal justice is still within the prohibition of the Constitution.''", "373--374")
  + QB(r"``The fact of this discrimination is admitted. No reason for it is shown, and the conclusion cannot be resisted that no reason for it exists except hostility to the race and nationality to which the petitioners belong, and which, in the eye of the law, is not justified.''", "374")
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"San Francisco denied laundry permits to every Chinese applicant while granting nearly all non-Chinese applicants; a unanimous Court held that a facially neutral law administered ``with an evil eye and an unequal hand'' violates equal protection, and that the Fourteenth Amendment protects noncitizens as ``persons'' (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to=r"\subsection{Procedural History}")],
  "Procedural History": [SEC("Facts and Procedural History", frm=r"\subsection{Procedural History}", strip=r"\subsection{Procedural History}")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{reversed} both the Supreme Court of California (\textit{Yick Wo}) and the U.S.\ Circuit Court (\textit{Wo Lee}), 9--0, remanding with directions to discharge the petitioners. The cases were submitted April 14, 1886, and decided May 10, 1886 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/118/356}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Matthews delivered the opinion of a unanimous Court, joined by Chief Justice Waite and Justices Miller, Field, Bradley, Harlan, Woods, Gray, and Blatchford.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Matthews)}"),
    N(r"\subsubsection{Independent Federal Construction of the Ordinances}"),
    SEC("Reasoning", frm="Justice Matthews began by", to=r"\subsection{Distinguishing"),
    N(r"\subsubsection{Distinguishing \emph{Barbier v. Connolly} and \emph{Soon Hing v. Crowley}}"),
    SEC("Reasoning", frm="The Court dismantled", to=r"\subsection{Universal Textual"),
    N(r"\subsubsection{Universal Textual Scope of the Fourteenth Amendment (Noncitizens as ``Persons'')}"),
    SEC("Reasoning", frm="Turning to the petitioners", to=r"\subsection{Constitutional Antipathy"),
    N(r"\subsubsection{Constitutional Antipathy to Arbitrary Personal Power}"),
    SEC("Reasoning", frm="Before turning to the enforcement", to=r"\subsection{Unconstitutional Administration"),
    N(r"\subsubsection{Unconstitutional Administration: ``An Evil Eye and an Unequal Hand''}"),
    SEC("Reasoning", frm="Ultimately, the Court did not need"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Discriminatory Purpose Required (\textit{Washington v. Davis}):}", glue=" "),
    S(r"In \href{https://supreme.justia.com/cases/federal/us/426/229/}{\emph{Washington v. Davis}}, 426 U.S. 229 (1976), however, the Court squarely rejected a constitutional disparate-impact theory: holding that a facially neutral police entrance exam (Test 21) did not violate equal protection merely because Black applicants failed at four times the rate of white applicants, the Court ruled that challengers must prove a \emph{racially discriminatory purpose}. \emph{Davis} reframed \emph{Yick Wo} not as a disparate-impact precedent, but as an extreme case in which the statistical disparity was so stark and unexplained that discriminatory intent was inescapable."),
    N(r"\item \textbf{Proving Intent (\textit{Arlington Heights}):}", glue=" "),
    S(r"The following Term, in \href{https://supreme.justia.com/cases/federal/us/429/252/}{\emph{Village of Arlington Heights v. Metropolitan Housing Development Corp.}}, 429 U.S. 252 (1977), the Court codified the multi-factor evidentiary framework for proving discriminatory intent behind facially neutral official action: (1) stark disparate impact (noting that cases as clear as \emph{Yick Wo} and \emph{Gomillion} are ``rare''); (2) historical background; (3) the specific sequence of events leading to the decision; (4) procedural or substantive departures from normal practice; and (5) contemporary legislative or administrative statements."),
    N(r"\item \textbf{Selective Prosecution (\textit{Armstrong}):}", glue=" "),
    S(r"Nearly a century later, in \href{https://supreme.justia.com/cases/federal/us/517/456/}{\emph{United States v. Armstrong}}, 517 U.S. 456 (1996), the Court cited \emph{Yick Wo} while imposing a demanding threshold even to obtain \emph{discovery} on a selective-prosecution claim: a criminal defendant must produce ``some evidence'' of both discriminatory effect (that similarly situated individuals of a different race were \emph{not} prosecuted) and discriminatory intent, overcoming a strong presumption of prosecutorial regularity."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Discriminatory Administration): Pacifica's ``Fire Resilience Permits.''}", glue=" "),
    SEC("Pedagogical", frm="The City of Pacifica requires", to=r"\textbf{Analysis:} Under", glue=" "),
    SEC("Pedagogical", frm=r"Under \href{https://supreme.justia.com/cases/federal/us/118/356/}{\emph{Yick Wo}} (118 U.S. at 369", to=r"\subsection{Exam Hypothetical 2"),
    N(r"\item \textbf{Same-Side (Selective Enforcement of a Neutral Code): Sidewalk-Vending Citations.} A city ordinance bars sidewalk vending within 50 feet of a transit stop. Police records show that over three years officers issued 212 citations under the ordinance, 205 of them to vendors of Somali origin, although city inspectors' own photo surveys document dozens of other vendors at the same stops on the same days who were never cited. The police department offers no explanation for the pattern. As in \textit{Yick Wo}, the law is neutral on its face, but its administration draws a line between similarly situated persons by national origin, and the comparator evidence is concrete and unrebutted. That record is the kind of stark, unexplained pattern from which \textit{Davis} and \textit{Arlington Heights} allow a court to infer purposeful discrimination, so the citations violate equal protection."),
    N(r"\item \textbf{Opposite-Side (Disparate Impact Without Purpose): Pacifica's Uniform Safety Code.}", glue=" "),
    SEC("Pedagogical", frm=r"Pacifica instead repeals", to=r"\textbf{Analysis:} This regulation", glue=" "),
    SEC("Pedagogical", frm=r"This regulation tracks"),
    N(r"\item \textbf{Opposite-Side (No Comparator Proof): A Gambling Prosecution.} A defendant of Chinese descent is prosecuted under a facially neutral ordinance barring gambling rooms. He moves to dismiss on the ground that the ordinance is enforced only against Chinese-owned establishments, but he offers only general assertions and newspaper accounts of anti-Chinese sentiment; he identifies no non-Chinese gambling operators whom the police knew of and declined to charge. \textit{Yick Wo} does not help him. Its inference of hostility rested on an admitted record showing that similarly situated non-Chinese operators were treated differently. Without evidence that comparable violators of another race or nationality went unprosecuted, the claim fails, as it did in \href{https://supreme.justia.com/cases/federal/us/198/500/}{\emph{Ah Sin v. Wittman}}, 198 U.S. 500 (1905), and under \textit{Armstrong} he would not even obtain discovery."),
    N(r"\item \textbf{Fence-Sitter (Standardless Discretion, Moderate Disparity): Food-Truck Permits.} A city's permit board may grant or deny food-truck permits in the public interest, with no written criteria. Over two years it denies 45 percent of applications from noncitizen operators and 20 percent from citizen operators. The board points to some neutral reasons in its files (incomplete applications, parking conflicts), but the reasons are applied inconsistently, and one board member once remarked that the city had too many immigrant vendors. The standardless grant of power echoes the ordinances in \textit{Yick Wo}, and the remark and irregular reasons are \textit{Arlington Heights} evidence. But the disparity is far from \textit{Yick Wo}'s 200-to-0 record, the board has offered partial neutral explanations, and later cases such as \textit{Kotch} largely abandoned \textit{Yick Wo}'s arbitrary-power strand for economic regulation. Whether a court infers purposeful discrimination is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"    \item \textbf{Facial Arbitrariness", to=r"\end{itemize}")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "Case Metadata: parallel cites, lower-court dispositions (covered in Procedural History), Briefing Book chapter line.",
  "Concurring and Dissenting Opinions section ('There were no concurring or dissenting opinions ...'): restated in Judicial Votes.",
  "Key Quotations: lead-in sentence and the bold quotation labels; every quote and its pin cite kept.",
  "Legacy section: intro paragraph; Gomillion sentence; Feeney sentence (Feeney still cited in Example 3); Ah Sin sentence (Ah Sin used in Example 4); Nieves and Gonzalez v. Trevino paragraph; alienage-line paragraph (Truax, Graham, Plyler, Mathews v. Diaz, Ambach); 'Through 2026' items (SFFA, DHS v. Regents, Alexander, Skrmetti). Kept: Washington v. Davis, Arlington Heights, Armstrong.",
  "Exam hypothetical headings and 'Fact Pattern:'/'Analysis:' labels; their text is reused in Examples 1 and 3.",
 ],
 "notes": ["Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection."],
}

emit(__file__, FILL)
