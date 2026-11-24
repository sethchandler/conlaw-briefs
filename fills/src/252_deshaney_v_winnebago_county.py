"""Fill for 252_deshaney_v_winnebago_county. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/489/189/"
C = "Concurring and Dissenting"
P = "Pedagogical"
CORNELL = r"; \href{https://www.law.cornell.edu/supremecourt/text/489/189}{Cornell LII}"

# NOTE: tools/manual_quotes.txt lists "<stem>.tex", so check_brief.py's MANUAL set never matches a
# stem and normalize_quotes.py always runs. Each quote block is built with its attribution after
# "---" inside the block; normalize_quotes.py then moves it to a Group A "\noindent ---" line.
def QB(quote, who, pin):
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue=" "), N("--- " + who, glue=" "),
            S(r"\href{https://supreme.justia.com/cases/federal/us/489/189/}{489 U.S. at " + pin + "}" + CORNELL, glue="\n"),
            N(r"\end{quote}")]

R = "Chief Justice Rehnquist, for the Court,"
QUOTES = (
  QB(r"``The Clause is phrased as a limitation on the State's power to act, not as a guarantee of certain minimal levels of safety and security. It forbids the State itself to deprive individuals of life, liberty, or property without `due process of law,' but its language cannot fairly be extended to impose an affirmative obligation on the State to ensure that those interests do not come to harm through other means. . . . Its purpose was to protect the people from the State, not to ensure that the State protected them from each other.''", R, "195--196")
  + QB(r"``The affirmative duty to protect arises not from the State's knowledge of the individual's predicament or from its expressions of intent to help him, but from the limitation which it has imposed on his freedom to act on his own behalf.''", R, "200")
  + QB(r"``While the State may have been aware of the dangers that Joshua faced in the free world, it played no part in their creation, nor did it do anything to render him any more vulnerable to them.''", R, "201")
  + QB(r"``Poor Joshua! Victim of repeated attacks by an irresponsible, bullying, cowardly, and intemperate father, and abandoned by respondents, who placed him in a dangerous predicament and who knew or learned what was going on, and yet did essentially nothing except, as the Court revealingly observes, \textit{ante} at 193, `dutifully recorded these incidents in [their] files.'''", "Justice Blackmun, dissenting,", "213")
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"A Wisconsin county social-services agency repeatedly documented signs that four-year-old Joshua DeShaney was being abused by his father but never removed him; the Court held 6--3 that the Due Process Clause imposes no duty to protect against private violence unless the State has taken the person into custody or created the danger (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Joshua and his mother sued")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Joshua and his mother sued")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Seventh Circuit by a \textbf{6--3} vote. The case was argued November 2, 1988, and decided February 22, 1989 (\href{" + J + r"}{Justia}" + CORNELL + r"):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Rehnquist delivered the opinion of the Court, joined by Justices White, Stevens, O'Connor, Scalia, and Kennedy.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Brennan filed a dissenting opinion, joined by Justices Marshall and Blackmun. Justice Blackmun filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Question Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Rehnquist)}"),
    N(r"\subsubsection{Text, History, and the Negative-Liberties Baseline}"),
    SEC("Reasoning", frm="Chief Justice Rehnquist began", to=r"\subsection{Narrowing the Custodial"),
    N(r"\subsubsection{Narrowing the Custodial ``Special Relationship'' Exception}"),
    SEC("Reasoning", frm="Petitioners argued that DSS", to=r"\subsection{State Tort Law"),
    N(r"\subsubsection{State Tort Law and the Social-Worker Dilemma}"),
    SEC("Reasoning", frm="Rehnquist emphasized that"),
    N(r"\subsection{Dissenting Opinion (Justice Brennan)}"),
    SEC(C, frm="Justice Brennan criticized", to=r"\item \textbf{Justice Blackmun"),
    N(r"\subsection{Dissenting Opinion (Justice Blackmun)}"),
    SEC(C, frm="Writing separately, Justice Blackmun", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Reinforced and Extended (\textit{Collins}; \textit{Castle Rock}):}", glue=" "),
    S(r"The Supreme Court reinforced this boundary in \href{https://www.law.cornell.edu/supremecourt/text/503/115}{\textit{Collins v. City of Harker Heights}, 503 U.S. 115 (1992)} (no substantive due process duty to provide municipal employees a safe workplace), and closed the procedural-entitlement loophole left open in \textit{DeShaney}'s footnote 2 in \href{https://supreme.justia.com/cases/federal/us/545/748/}{\textit{Town of Castle Rock v. Gonzales}, 545 U.S. 748 (2005)}, holding that even a seemingly mandatory state domestic-violence restraining-order statute confers no constitutionally protected ``property'' interest in police enforcement."),
    N(r"\item \textbf{State-Created Danger in the Circuits:}", glue=" "),
    S(r"Meanwhile, Chief Justice Rehnquist's observation that Wisconsin ``played no part in [the dangers'] creation, nor did it do anything to render him any more vulnerable to them'' (\href{https://supreme.justia.com/cases/federal/us/489/189/}{489 U.S. at 201}) spawned the federal circuits' \textbf{state-created danger} doctrine. Most federal courts of appeals recognize substantive due process liability when a state actor affirmatively creates or enhances a foreseeable risk of private harm with conscience-shocking culpability, though the Supreme Court has never formally endorsed the doctrine and circuit tests diverge sharply (\href{https://lawreview.uchicago.edu/online-archive/exploring-statutory-remedies-state-created-dangers-after-fisher-v-moore}{U. Chi. L. Rev. Online})."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (State Prevails): Slow Response to Protective-Order Violations.}", glue=" "),
    S(r"City police receive three 911 calls reporting that a local resident is threatening his estranged spouse outside her apartment in violation of a state protective order. Dispatch logs the calls as low priority, no patrol car arrives for two hours, and the resident assaults the spouse. Under \textit{DeShaney} and \href{https://supreme.justia.com/cases/federal/us/545/748/}{\textit{Castle Rock}}, a \S~1983 Due Process suit fails: the victim was not in state custody, police did not affirmatively create the danger, and state protective-order statutes confer no federal procedural property interest in arrest (remedies lie, if at all, in state tort law or Equal Protection if non-enforcement was discriminatory)."),
    N(r"\item \textbf{Same-Side (State Prevails): Broken Promises of Extra Patrols.} A woman tells her local police department that a former boyfriend has threatened to kill her. An officer promises that patrol cars will drive past her house every hour that week, but none do, and on the third night the former boyfriend breaks in and injures her. She sues the officer and the city under \S~1983, arguing that the promise created a special relationship. Under \textit{DeShaney}, the claim fails. The State did not restrain her liberty, and the danger came from a private actor. The Court made clear that an affirmative duty arises not from the State's knowledge of a person's predicament or its ``expressions of intent to help him,'' but only from limits it has imposed on the person's freedom to act on her own behalf. Any remedy lies in state tort law (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Plaintiff Prevails): A Child Stranded on the Highway.}", glue=" "),
    S(r"After arresting an intoxicated driver at 1:00 a.m. in sub-freezing weather on an unlit rural interstate, a state trooper confiscates the car keys and orders the driver's sober seven-year-old passenger out of the car to ``walk home'' along the highway shoulder rather than waiting for a guardian. The child is struck by a passing motorist.", glue=" "),
    S(r"Unlike \textit{DeShaney}, the officer did not merely stand by while a preexisting private danger unfolded. By affirmatively removing the child from a safe vehicle and stranding her in an exposed, lethal environment she could not escape, the state actor affirmatively created the peril and rendered the child far more vulnerable to harm (\href{https://supreme.justia.com/cases/federal/us/489/189/}{489 U.S. at 201}; cf. \textit{White v. Rochford}, 592 F.2d 381 (7th Cir. 1979)). In circuits recognizing state-created danger (and arguably as a brief custodial deprivation of liberty), the plaintiff states a viable substantive due process claim."),
    N(r"\item \textbf{Opposite-Side (Custody Triggers a Duty): A Prisoner Beaten by a Cellmate.} A state prisoner tells prison officers that his cellmate has threatened to kill him and asks to be moved. The officers laugh off the request, and that night the cellmate beats him severely. Unlike Joshua, the prisoner is in state custody: the State has locked him in a cell with his attacker and taken away his ability to protect himself or seek help. \textit{DeShaney} itself explained that when the State so restrains a person's liberty, as in \textit{Estelle v.\ Gamble} and \textit{Youngberg v.\ Romeo}, it assumes a duty to provide for his basic needs, including reasonable safety. The prisoner can state a constitutional claim if he shows the officers knew of and disregarded a substantial risk to his safety, the Eighth Amendment standard the Court applied to prisoners attacked by other inmates in \textit{Farmer v.\ Brennan}, 511 U.S.\ 825 (1994)."),
    N(r"\item \textbf{Fence-Sitter (Foster Care): Abuse in a State-Selected Foster Home.} A county child-welfare agency removes a six-year-old from her parents and places her with foster parents it has licensed and supervises. Caseworkers receive two reports that the foster father is hitting her but do not investigate, and she is seriously injured. The agency relies on \textit{DeShaney}: the abuser was a private person, not a state employee. The child answers that the State took her from her family and chose where she would live, a restraint on her liberty much closer to institutionalization than Joshua's situation. \textit{DeShaney} expressly left open whether a child in state-arranged foster care stands in a custodial relationship with the State (489 U.S.\ at 201 n.9), and the Supreme Court has not resolved the question, so the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(P, frm=r"  \item \textbf{Action vs. Inaction", to=r"\end{enumerate}")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "Case Metadata: full caption, parallel cites, docket number, provisions and chapter lines.",
  "Key Quotations: bold quotation labels; every quote and its pin cite kept.",
  "Legacy section: opening framing sentence; 'Through 2026' paragraph on Fisher v. Moore and Sterling v. City of Jackson (Fifth Circuit, 2025--2026) - lower-court developments. Kept: Collins / Castle Rock sentence and the state-created-danger paragraph.",
  "Exam hypothetical headings and 'Analysis:' label; their text is reused in Examples 1 and 3.",
 ],
 "notes": ["Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection."],
}

emit(__file__, FILL)
