"""Fill for 190_marsh_v_alabama. See tools/fillkit.py."""
import os
from fillkit import *

ORIG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "originals", "briefs",
                         "190_marsh_v_alabama.tex"), encoding="utf-8").read()

def X(a, b, glue=None):
    """Verbatim span of the original from anchor a (inclusive) to anchor b (exclusive), stripped."""
    i = ORIG.index(a); j = ORIG.index(b, i)
    return S(ORIG[i:j].strip(), glue=glue)

J = "https://supreme.justia.com/cases/federal/us/326/501/"
JH = r"\href{https://supreme.justia.com/cases/federal/us/326/501/}"

def Q(quote, attrib):
    # Attribution inside the quote block; normalize_quotes.py moves it to a Group A "\noindent ---" line.
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "), S(attrib, glue="\n"),
            N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"When a private corporation owns and runs an entire company town open to the public, it performs a public function and is bound by the First and Fourteenth Amendments; Alabama therefore could not convict a Jehovah's Witness of trespass for leafletting on the town's business-block sidewalk (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The company-paid deputy sheriff arrested Marsh")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The company-paid deputy sheriff arrested Marsh")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{5--3} vote. The case was argued on December 6, 1945, and decided on January 7, 1946 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Opinion of the Court:} Justice Black delivered the opinion of the Court, joined by Justices Douglas, Murphy, and Rutledge; Justice Frankfurter joined except as to its Commerce Clause analogy.
    \item \textbf{Concurring Opinion:} Justice Frankfurter filed a concurring opinion (326 U.S. at 510--11).
    \item \textbf{Dissenting Opinion:} Justice Reed filed a dissenting opinion, joined by Chief Justice Stone and Justice Burton (326 U.S. at 511--17).
    \item \textbf{Not Participating:} Justice Jackson took no part in the consideration or decision of the case.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Opinion of the Court (Justice Black)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Frankfurter)}"),
    SEC("Concurring and Dissenting", frm="Justice Frankfurter joined", to=r"\subsection{Dissenting"),
    N(r"\subsection{Dissenting Opinion (Justice Reed)}"),
    SEC("Concurring and Dissenting", frm="Justice Reed condemned"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Shopping Centers: Expansion and Overruling (1968--1980):}", glue=" "),
    SEC("Doctrinal Significance", frm="For two decades", to=r"\subsection{The ``Traditionally"),
    N(r"\item \textbf{The ``Traditionally Exclusively'' Requirement (1974--2001):}", glue=" "),
    SEC("Doctrinal Significance", frm="Simultaneously, the Court narrowed", to=r"\subsection{Modern Digital-Era"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{\href{https://supreme.justia.com/cases/federal/us/587/", to=r"  \item \textbf{\href{https://supreme.justia.com/cases/federal/us/601/"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (State Action Found): The Corporate ``Tech Town.''}", glue=" "),
    X("Apex Robotics constructs", r"\begin{itemize}", glue=" "),
    X("This is the closest modern analogue to", r"\end{itemize}"),
    N(r"\item \textbf{Same-Side (State Action Found): A Private Company That Runs the County's Elections.} A county contracts with a private corporation to conduct its municipal elections from start to finish: the company qualifies candidates for the ballot, staffs the polls, counts the votes, and certifies the winners. The company refuses to place on the ballot any candidate who has criticized its parent firm. A disqualified candidate sues under the First and Fourteenth Amendments. Running public elections is one of the very few functions the post-\textit{Marsh} cases treat as traditionally and exclusively reserved to the State, as the white-primary decision in \href{https://supreme.justia.com/cases/federal/us/345/461/}{\textit{Terry v.\ Adams}, 345 U.S.\ 461 (1953)}, illustrates. As in \textit{Marsh}, a State cannot hand a governmental function to a private entity and thereby free it from constitutional limits, so the company is a state actor."),
    N(r"\item \textbf{Opposite-Side (No State Action): The Dominant Social-Media Platform.}", glue=" "),
    X("OmniStream, a privately owned", r"\begin{itemize}", glue=" "),
    X(r"\textbf{No state action.} Under \href{https://supreme.justia.com/cases/federal/us/587/17-1702/}{\textit{Halleck}} (587 U.S. 802), hosting", r"\end{itemize}"),
    N(r"\item \textbf{Opposite-Side (No Federal State Action): The Open-Air Lifestyle Shopping Center.}", glue=" "),
    X("Galleria Commons is a massive", r"\begin{itemize}", glue=" "),
    X(r"\textbf{No federal state action.}", r"\end{itemize}"),
    N(r"\item \textbf{Fence-Sitter (Uncertain): The Developer-Owned New Town.} A developer builds and continues to own an unincorporated, ungated community of 20,000 residents in which it holds title to every street, sidewalk, park, and the central shopping district, and it employs private security officers who enforce its rules; but the county supplies police, fire protection, water, and public schools. The developer bars petition circulators from its town-center sidewalks. The streets are open to the public and the town looks like the Chickasaw business block, which favors applying \textit{Marsh}. Yet \textit{Hudgens} confined \textit{Marsh} to private property with all the attributes of a town, and here the core municipal services remain public. Because the Court has never said how many municipal attributes are enough, a court could reasonably go either way."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Ambiguous", to=r"\end{itemize}")],
  "Key Quotations": (
    Q(r"``Ownership does not always mean absolute dominion. The more an owner, for his advantage, opens up his property for use by the public in general, the more do his rights become circumscribed by the statutory and constitutional rights of those who use it.''", JH + r"{Black, J., 326 U.S. at 506}")
    + Q(r"``Whether a corporation or a municipality owns or possesses the town, the public in either case has an identical interest in the functioning of the community in such manner that the channels of communication remain free.''", JH + r"{Black, J., 326 U.S. at 507}")
    + Q(r"``Many people in the United States live in company-owned towns. These people, just as residents of municipalities, are free citizens of their State and country. Just as all other citizens, they must make decisions which affect the welfare of community and nation. To act as good citizens, they must be informed. In order to enable them to be properly informed, their information must be uncensored.''", JH + r"{Black, J., 326 U.S. at 508}")
    + Q(r"``When we balance the Constitutional rights of owners of property against those of the people to enjoy freedom of press and religion, as we must here, we remain mindful of the fact that the latter occupy a preferred position.''", JH + r"{Black, J., 326 U.S. at 509}")
    + Q(r"``A company-owned town gives rise to a network of property relations. As to these, the judicial organ of a State has the final say. But a company-owned town is a town. In its community aspects, it does not differ from other towns.''", JH + r"{Frankfurter, J., concurring, 326 U.S. at 510--11}")
    + Q(r"``The rights of the owner, which the Constitution protects as well as the right of free speech, are not outweighed by the interests of the trespasser, even though he trespasses in behalf of religion or free speech.''", JH + r"{Reed, J., dissenting, 326 U.S. at 516}")
  ),
 },
 "dropped": [
  "Case Metadata: procedural posture line, constitutional provisions line, Chapter/Topic and duplicate URL lines (Justia link kept in Judicial Votes).",
  "Legacy section: introductory paragraph; subsection headings (replaced by short item labels); digital-era intro paragraph; Lindke v. Freed item (state action by government officials, not an application of Marsh's public-function holding); Moody v. NetChoice item and 'As of 2026' closing (Moody decided editorial rights, not state action; still cited in Example 3). Kept: Logan Valley/Lloyd/Hudgens/PruneYard arc, Jackson/Flagg Bros./Rendell-Baker/Blum tightening, Halleck.",
  "Key Quotations: lead-in sentence claiming verification; bold topical labels; the '(Frankfurter, J., concurring)' / '(Reed, J., dissenting)' trailing tags in item 5 (the paired quotes now carry their own attribution lines).",
  "Exam Hypotheticals: headings, the 'Contrast Apexville with two scenarios' lead-in, and 'Analysis:' / 'Opposite-Side Result:' labels (fact patterns and analyses reused in Examples 1, 3, 4).",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all six quotations kept (item 5's two quotes split into two blocks), none added."],
}

emit(__file__, FILL)
