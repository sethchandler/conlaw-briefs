"""Fill for 204_new_york_times_co_v_united_states. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/403/713/"
C = "Concurring and Dissenting"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"In the Pentagon Papers Case, the Nixon Administration sought to stop the \textit{New York Times} and \textit{Washington Post} from publishing a classified Vietnam War study; a 6--3 \textit{per curiam} held that the Government had not carried the ``heavy burden'' required to justify a prior restraint, with nine Justices writing separately (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The Nixon Administration sought")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The Nixon Administration sought")],
  "Judicial Votes": [
    N(r"By a \textbf{6--3} vote, the Supreme Court \textbf{reversed} the Second Circuit (\textit{New York Times}) with directions to affirm the District Court, \textbf{affirmed} the D.C.\ Circuit (\textit{Washington Post}), and vacated all stays. The cases were argued June 26, 1971, and decided June 30, 1971 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Per Curiam:} A brief unsigned opinion announced the judgment; no rationale commanded a majority beyond it.
    \item \textbf{Concurring Opinions:} Justice Black (joined by Justice Douglas); Justice Douglas (joined by Justice Black); Justice Brennan; Justice Stewart (joined by Justice White); Justice White (joined by Justice Stewart); and Justice Marshall.
    \item \textbf{Dissenting Opinions:} Chief Justice Burger; Justice Harlan (joined by Chief Justice Burger and Justice Blackmun); and Justice Blackmun.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Question Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Per Curiam Opinion}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Black)}"),
    SEC(C, frm="Emphasizing Madison's", to=r"\item \textbf{Justice Douglas"),
    N(r"\subsection{Concurring Opinion (Justice Douglas)}"),
    SEC(C, frm="Douglas echoed", to=r"\item \textbf{Justice Brennan"),
    N(r"\subsection{Concurring Opinion (Justice Brennan)}"),
    SEC(C, frm="Brennan faulted", to=r"\item \textbf{Justice Stewart"),
    N(r"\subsection{Concurring Opinion (Justice Stewart)}"),
    SEC(C, frm="Recognizing that the Executive", to=r"\item \textbf{Justice White"),
    N(r"\subsection{Concurring Opinion (Justice White)}"),
    SEC(C, frm="White conceded", to=r"\item \textbf{Justice Marshall"),
    N(r"\subsection{Concurring Opinion (Justice Marshall)}"),
    SEC(C, frm="Framing the dispute", to=r"\item \textbf{Chief Justice Burger"),
    N(r"\subsection{Dissenting Opinion (Chief Justice Burger)}"),
    SEC(C, frm="Burger declined", to=r"\item \textbf{Justice Harlan"),
    N(r"\subsection{Dissenting Opinion (Justice Harlan)}"),
    SEC(C, frm="Calling the Court's", to=r"\item \textbf{Justice Blackmun"),
    N(r"\subsection{Dissenting Opinion (Justice Blackmun)}"),
    SEC(C, frm="Joining Harlan and endorsing", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Gag Orders on Trial Coverage:} The Court applied the same high barrier when", glue=" "),
    S(r"invalidating gag orders on media reporting of criminal trials in \textit{Nebraska Press Ass'n v.\ Stuart}, 427 U.S.\ 539 (1976)", glue=""),
    N("."),
    N(r"\item \textbf{Fiduciary Prepublication Review:}", glue=" "),
    S(r"In \textit{Snepp v.\ United States}, 444 U.S.\ 507 (1980), the Court enforced a former CIA agent's contractual prepublication review agreement and imposed a constructive trust on book royalties, distinguishing government employees with fiduciary access to secrets from outside newspapers."),
    N(r"\item \textbf{Protective Orders on Discovery:}", glue=" "),
    S(r"Similarly, in \textit{Seattle Times Co.\ v.\ Rhinehart}, 467 U.S.\ 20 (1984), a unanimous Court held that a protective order barring a newspaper-litigant from publishing information obtained solely through compelled civil pretrial discovery is not a ``classic prior restraint'' triggering \textit{New York Times}'s heavy presumption."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Injunction Barred): Leaked Memo Exposing Official Deception.}", glue=" "),
    S(r"An anonymous Defense Department contractor leaks two classified documents to the \textit{National Ledger}: (1) a 2022 internal policy memo revealing that senior officials knowingly exaggerated intelligence estimates to justify a foreign cyber-operation; and (2) live cryptographic keys and exact GPS coordinates for an active U.S.\ naval convoy currently transiting a hostile strait. The Attorney General seeks an emergency federal court injunction barring publication of both documents, relying solely on the President's Article II Commander-in-Chief authority without pointing to any statute authorizing civil injunctions.", glue=" "),
    S(r"Under \textit{New York Times}, an injunction against \textbf{Document 1} is plainly unconstitutional under all six concurrences: it is historical policy criticism exposing official deception, posing no direct, immediate, and irreparable catastrophe."),
    N(r"\item \textbf{Same-Side (Injunction Barred): A State's Leaked Emergency Plan.} A newspaper obtains a leaked copy of a State's confidential hurricane-evacuation plan, which shows that officials knew the plan's shelter capacity was badly inadequate. The Governor asks a federal court to enjoin publication, arguing that disclosure could cause public panic and help criminals predict where police will be deployed during a storm. Those predicted harms are speculative and depend on the reactions of third parties. Under the \textit{per curiam}, the restraint comes to court with a ``heavy presumption against its constitutional validity,'' and the Governor's ``surmise or conjecture'' (in Justice Brennan's phrase) about possible harm falls far short of Justice Stewart's showing of direct, immediate, and irreparable damage. The injunction must be denied (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Narrow Injunction Likely Upheld): Live Convoy Coordinates and Cryptographic Keys.} Same facts, as to Document 2.", glue=" "),
    S(r"\textbf{Document 2} squarely tests the \textit{Near}/\textit{New York Times} fault lines: under Justices Black and Douglas (absolutism) and Justice Marshall (lack of statutory authorization under \textit{Youngstown}), an injunction still fails; however, under Justice Brennan's ``transport already at sea'' exception and Justice Stewart's ``direct, immediate, and irreparable damage'' standard (joined by the three dissenters' deference framework), a majority of the Court's doctrinal spectrum would likely uphold a narrow injunction as to the live convoy coordinates and active cryptographic keys---and under Justice White's concurrence, publishing the cryptographic keys would also expose the paper to post-publication criminal prosecution under 18 U.S.C.\ \S~798."),
    N(r"\item \textbf{Opposite-Side (Restraint Permitted): A Former Analyst's Memoir.} A former intelligence analyst signed an employment agreement promising to submit any writing about her work for prepublication review. She completes a memoir describing classified operations and announces that she will publish it without review. The Government sues to enjoin publication of the unreviewed manuscript and to impose a constructive trust on any profits. \textit{New York Times} does not control, because the analyst is not an outside newspaper publishing what it received; she voluntarily assumed a duty of confidentiality as a condition of access to secrets. Under \textit{Snepp v.\ United States}, 444 U.S. 507 (1980), the agreement is enforceable, and the Government may require review before publication and recover her profits if she breaches it."),
    N(r"\item \textbf{Fence-Sitter (Statutory Authorization): A Narrow Congressional Injunction Statute.} Congress enacts a statute authorizing federal courts, after an \textit{in camera} hearing, to enjoin publication of the names of covert intelligence officers currently serving abroad when publication would create a substantial risk of physical harm to them. A news site announces that it will publish a list of such names it has obtained. The statute answers the objection pressed by Justices White and Marshall, who stressed the absence of congressional authorization, and naming a deployed officer may resemble Brennan's troop-ship example. But Justices Black and Douglas would bar any prior restraint, and Stewart's standard demands that harm be direct, immediate, and irreparable, not merely a risk. Because \textit{New York Times} produced no majority rationale, whether such a statute could be applied to a publisher is unresolved."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"    \item \textbf{Fractured", to=r"\end{enumerate}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket numbers, Chapter/Topic line, Cornell CONAN link.",
  "Legacy section: framing paragraphs; Daily Mail and Bartnicki (subsequent-publication cases, not prior restraints); Progressive and CNN v. Noriega (lower-court/stay rulings); 'Through 2026' Espionage Act/WikiLeaks commentary. Kept: Nebraska Press clause, and the Snepp and Rhinehart sentences moved from the 'Opposite Side' Contrast.",
  "'Opposite Side' Contrast heading and lead-in sentence (exam tip); its Snepp and Rhinehart sentences moved to Subsequent Developments, and Snepp is applied in Example 4.",
  "Exam Hypothetical 'Analysis:' label; its text is split between Examples 1 and 3.",
 ],
 "notes": ["Critique section is moved with ITEMS from an enumerate list; enumerate wrappers are not stripped by ITEMS, so the slice stops before \\end{enumerate} and the labels become paragraphs."],
}

emit(__file__, FILL)
