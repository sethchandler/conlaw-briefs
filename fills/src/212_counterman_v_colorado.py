"""Fill for 212_counterman_v_colorado. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/600/22-138/"
C = "Concurring and Dissenting"
P = "Pedagogical"

# NOTE: tools/manual_quotes.txt lists "<stem>.tex", so check_brief.py's MANUAL set never matches a
# stem and normalize_quotes.py always runs. Each quote block is built with its attribution after
# "---" inside the block; normalize_quotes.py then moves it to a Group A "\noindent ---" line.
def QB(quote, attrib):
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue=" "), N("---", glue=" "), S(attrib, glue="\n"), N(r"\end{quote}")]

QUOTES = (
  QB(r"``We hold that it does, but that a mental state of recklessness is sufficient. The State must show that the defendant consciously disregarded a substantial risk that his communications would be viewed as threatening violence. The State need not prove any more demanding form of subjective intent to threaten another.''",
     r"Kagan, J., \href{https://www.supremecourt.gov/opinions/22pdf/600us1r51_g3bi.pdf}{600 U.S. at 69}")
  + QB(r"``Yet the First Amendment may still demand a subjective mental-state requirement shielding some true threats from liability. The reason relates to what is often called a chilling effect. Prohibitions on speech have the potential to chill, or deter, speech outside their boundaries.''",
     r"Kagan, J., \href{https://www.supremecourt.gov/opinions/22pdf/600us1r51_g3bi.pdf}{600 U.S. at 75}")
  + QB(r"``There is simply no need to reach out in this stalking case to determine whether anything more than recklessness is needed for punishing true threats generally.''",
     r"Sotomayor, J., concurring in part and in the judgment, \href{https://supreme.justia.com/cases/federal/us/600/22-138/}{600 U.S. at 85}")
  + QB(r"``The reality is that recklessness is not grounded in law, but in a Goldilocks judgment: Recklessness is not too much, not too little, but instead `just right.'''",
     r"Barrett, J., dissenting, \href{https://supreme.justia.com/cases/federal/us/600/22-138/}{600 U.S. at 119}")
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"A man convicted of stalking a singer through hundreds of Facebook messages won a new trial: the Court held 7--2 that a true-threats prosecution requires proof that the speaker was at least reckless---that he consciously disregarded a substantial risk his words would be viewed as threatening violence---not merely that a reasonable person would see a threat (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Colorado charged Counterman under")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Colorado charged Counterman under")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{vacated and remanded} by a \textbf{7--2} vote. The case was argued April 19, 2023, and decided June 27, 2023 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Kagan delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Alito, Kavanaugh, and Jackson.
    \item \textbf{Concurring Opinion:} Justice Sotomayor filed an opinion concurring in part and concurring in the judgment, joined by Justice Gorsuch as to Parts I, II, III-A, and III-B.
    \item \textbf{Dissenting Opinions:} Justice Thomas filed a dissenting opinion. Justice Barrett filed a dissenting opinion, joined by Justice Thomas.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kagan)}"),
    N(r"\subsubsection{Why a Subjective Mental State Is Required: ``Strategic Protection'' Against Chill}"),
    SEC("Reasoning", frm="Justice Kagan began from", to=r"\subsection{Why Recklessness"),
    N(r"\subsubsection{Why Recklessness---Not Purpose or Knowledge---Strikes the Right Balance}"),
    SEC("Reasoning", frm="Descending the"),
    N(r"\subsection{Concurring Opinion (Justice Sotomayor)}"),
    SEC(C, frm="Sotomayor agreed", to=r"\item \textbf{Justice Thomas"),
    N(r"\subsection{Dissenting Opinion (Justice Thomas)}"),
    SEC(C, frm="Joining Justice Barrett's dissent in full", to=r"\item \textbf{Justice Barrett"),
    N(r"\subsection{Dissenting Opinion (Justice Barrett)}"),
    SEC(C, frm="Barrett argued", to=r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Objective Instruction Invalid): A Heated Zoning Comment.}", glue=" "),
    SEC(P, frm="During a heated livestreamed debate", to=r"\textbf{Analysis:} The conviction", glue=" "),
    SEC(P, frm="The conviction violates", to=r"\subsubsection{Hypothetical 2"),
    N(r"\item \textbf{Same-Side (No Subjective Recklessness): A Delusional Reader's Single Email.}", glue=" "),
    S(r"After a single encounter at a book signing, an author receives one rambling email from a reader experiencing paranoid delusions: ``The universe requires your silence; your final chapter ends Friday.'' Medical experts establish the reader genuinely believed he was transmitting a harmless spiritual prophecy and never perceived any risk of causing fear. Under \textit{Counterman}, a criminal true-threats conviction fails for lack of subjective recklessness."),
    N(r"\item \textbf{Opposite-Side (Recklessness Provable): Persistent Messages After Explicit Notice.}", glue=" "),
    S(r"Same reader sends 150 messages over six months despite the author blocking ten accounts and sending a cease-and-desist letter warning, ``Your messages terrify me; stop contacting me.'' Even if the reader claims he meant no harm, continuing to send ominous messages after explicit notice easily supports a jury finding of \textbf{recklessness} under \textit{Counterman}---and if prosecuted purely for repeated, unwanted post-notice contact rather than message content, \href{https://law.justia.com/cases/colorado/supreme-court/2025/24sa226.html}{\textit{Crawford}} indicates \textit{Counterman}'s true-threats test may not even be triggered."),
    N(r"\item \textbf{Opposite-Side (Higher Mental State Satisfies the Floor): A Threat Statute Requiring Intent.} After a dispute with his former business partner, a man texts her a photo of her house with the message that she will not live to see the lawsuit through. He is prosecuted under a statute requiring proof that he sent the message with the purpose of placing the recipient in fear of death, and the jury, so instructed, convicts. He argues on appeal that the message was a joke. \textit{Counterman} does not help him. It sets recklessness as the constitutional \emph{minimum}; a State may require more, and a jury finding of purpose necessarily includes conscious disregard of the risk that the message would be seen as threatening. Whether the message was a jest or a true threat was a question for the jury, decided in context under \textit{Watts} and \textit{Virginia v. Black}, and the conviction stands."),
    N(r"\item \textbf{Fence-Sitter (Civil Protective Orders): An Objective Standard Outside Criminal Law.} A woman seeks a civil protective order against a former coworker who has sent her a series of hostile messages, including one saying she would regret reporting him. The state statute authorizes an order on a finding that a reasonable person would regard the messages as threatening; it requires no proof of the respondent's state of mind. The coworker argues that, after \textit{Counterman}, the order punishes his speech without proof of recklessness. \textit{Counterman}'s rationale---that an objective standard chills protected speech---applies to any state-imposed sanction for speech. But the Court decided a criminal case, the order carries no criminal penalty and only restricts future contact, and Justice Barrett's dissent flagged exactly this civil setting as unresolved. Whether the recklessness floor applies to civil protective orders remains open."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(P, frm=r"  \item \textbf{The Delusional", to=r"\end{itemize}")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "LaTeX comment lines (case/chapter/'Prepared for' comments) after \\maketitle.",
  "Case Metadata: party caption, cert-grant date, court-below line, provisions line (Justia link kept in Judicial Votes).",
  "Legacy section in full (no Subsequent Developments subsection): intro paragraph and four 2023--2026 items (People v. Crawford (Colo. 2025), Mckesson v. Doe cert denial, State v. Calloway / United States v. Woollacott, civil protective-order scholarship). None is a Supreme Court decision overruling, narrowing, extending, or squarely applying Counterman, and several are post-2023 lower-court or scholarly developments.",
  "Key Quotations: bold quotation labels; every quote and its pin cite kept.",
  "Exam hypothetical headings, 'Analysis:' label, and 'Scenario A/B' labels; their text is reused in Examples 1--3.",
 ],
 "notes": [
  "Example 3 (moved verbatim from Neon's Scenario B) still cites People v. Crawford (Colo. 2025), whose legacy item was dropped; the citation should be verified.",
  "Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection.",
 ],
}

emit(__file__, FILL)
