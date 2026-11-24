"""Fill for 205_virginia_state_board_of_pharmacy_v_vccc. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/425/748/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Striking down Virginia's ban on advertising prescription-drug prices, the Court held 7--1 that purely commercial speech is protected by the First Amendment and that consumers have a reciprocal right to receive truthful information about lawful products (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="A three-judge U.S. District Court")],
  "Procedural History": [SEC("Facts and Procedural History", frm="A three-judge U.S. District Court")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the District Court by a \textbf{7--1} vote; Justice Stevens took no part in the consideration or decision of the case. The case was argued on November 11, 1975, and decided on May 24, 1976 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Blackmun delivered the opinion of the Court, joined by Chief Justice Burger and Justices Brennan, Stewart, White, Marshall, and Powell.
    \item \textbf{Concurring Opinions:} Chief Justice Burger and Justice Stewart each filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Rehnquist filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Blackmun)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Chief Justice Burger)}"), N("Chief Justice Burger", glue=" "),
    SEC("Concurring and Dissenting", frm="Emphasized that 95", to=r"  \item \textbf{Justice Stewart", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Stewart)}"), N("Justice Stewart", glue=" "),
    SEC("Concurring and Dissenting", frm="Wrote separately to reassure", to=r"  \item \textbf{Justice Rehnquist", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Rehnquist)}"), N("Justice Rehnquist", glue=" "),
    SEC("Concurring and Dissenting", frm="Mounted a prescient", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Immediate Expansion", to=r"  \item \textbf{Modern Debates"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Ban Invalid): Optometrists Barred From Advertising Eyeglass Prices.} A State's optometry board disciplines any licensed optometrist who advertises the price of eye examinations or eyeglasses, explaining that price competition will lead consumers to choose cheap, careless providers. A consumer group and an optometrist who wants to advertise sue. Under \textit{Virginia Pharmacy}, the consumers have standing to assert their reciprocal right to receive the information, and the advertisements are truthful statements about a lawful transaction. The State's rationale is the same paternalistic one the Court rejected: it seeks to protect professional standards by keeping the public in ignorance rather than by regulating the quality of care directly. The ban is unconstitutional, even though \textit{Williamson v.\ Lee Optical Co.} once upheld a similar rule as economic regulation."),
    N(r"\item \textbf{Same-Side (Ban Invalid): Lawyers Barred From Advertising Fees for Routine Services.} A state bar rule forbids attorneys from advertising in newspapers that they will handle uncontested divorces, simple wills, or name changes for stated flat fees. Two lawyers who run a low-cost legal clinic publish such an advertisement and are disciplined. Footnote~25 of \textit{Virginia Pharmacy} reserved the question of lawyer advertising, but the Court answered it a year later in \textit{Bates v.\ State Bar of Arizona}, 433 U.S.\ 350 (1977), applying \textit{Virginia Pharmacy}'s reasoning. Truthful price information about routine services helps consumers find affordable counsel, and the bar's fears that advertising will undermine professionalism are the kind of paternalism the First Amendment forbids. The State may still prohibit false or misleading claims."),
    N(r"\item \textbf{Opposite-Side (Regulation Valid): In-Person Solicitation of Accident Victims.} A lawyer visits a hospitalized accident victim and her family, urging them to sign a contingent-fee agreement on the spot, and is disciplined under a rule banning in-person solicitation for profit. \textit{Virginia Pharmacy} protected impersonal, truthful price information that consumers can evaluate at their own pace. Face-to-face solicitation is different: it pressures a vulnerable listener for an immediate decision, invites overreaching, and occurs outside public view, where false or misleading statements are hard to detect. Under \textit{Ohralik v.\ Ohio State Bar Ass'n}, 436 U.S.\ 447 (1978), the State may ban it as a prophylactic measure, consistent with \textit{Virginia Pharmacy}'s own statement that commercial speech remains subject to regulation."),
    N(r"\item \textbf{Opposite-Side (Regulation Valid): Advertising Prescription Drugs for Sale Without a Prescription.} An online seller advertises that it will ship prescription-only medications to Virginia customers without requiring a prescription, listing prices for each drug. The State fines the seller under a law prohibiting such advertisements. The seller invokes \textit{Virginia Pharmacy}, which protected price advertising for prescription drugs. The claim fails. \textit{Virginia Pharmacy} protected truthful information about entirely lawful commercial activity, and the Court expressly preserved the State's power to bar advertisements proposing unlawful transactions. Because selling prescription drugs without a prescription is itself illegal, the advertisement proposes an unlawful transaction and receives no First Amendment protection, so the State may prohibit it outright."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Restricting Sportsbook Promotions.}", glue=" "),
    S(r"To combat rising rates of online sports-gambling addiction, a State where sports betting is legal enacts a statute prohibiting licensed sportsbooks from advertising ``promotional odds, signup bonuses, or payout percentages'' in any print or digital medium, while allowing sportsbooks to display those terms inside their mobile apps once a user creates an account. A consumer advocacy group representing recreational bettors and a licensed sportsbook sue under the First Amendment.", glue=" "),
    N(r"\textit{For the challengers:}", glue=" "),
    S(r"Under \textit{Virginia Pharmacy}, the consumer group has standing via the reciprocal right to receive truthful commercial information. Because sports betting is lawful and the banned ads are truthful, the statute fails \textit{Central Hudson} and \textit{Sorrell}: it is a content- and speaker-based ban resting on forbidden paternalism (keeping bettors ignorant to dampen demand) rather than directly regulating betting limits or mandating addiction warnings.", glue=" "),
    N(r"\textit{For the State:}", glue=" "),
    S(r"Distinguish \textit{Virginia Pharmacy} because the State is not banning \textit{all} access (terms remain available in-app, resembling a channel limit) and is targeting a vice activity with severe externalities rather than essential medicine. Under \textit{Central Hudson}, reducing gambling addiction is a substantial interest, promotional bonuses uniquely induce impulsive wagering (echoing \textit{Ohralik}'s concern with overreaching), and the restriction is tailored to promotional inducements rather than all speech about sportsbooks.", glue=" "),
    N(r"The case is close because the law partly suppresses truthful information to reduce demand, which \textit{Virginia Pharmacy} and \textit{44 Liquormart} condemn, yet leaves the information available to account holders and targets inducements to a harmful activity."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{``Opposite Side'' Contrast")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line (Justia link kept in Judicial Votes).",
  "Legacy section: introductory sentence; 'Modern Debates Through 2026' item (First Amendment Lochnerism commentary, Janus, 2025--2026 disclosure litigation). Kept: Bates/Carey, Central Hudson, 44 Liquormart/Lorillard, and Sorrell items.",
  "'Opposite Side' Contrast (Lee Optical and Ohralik): an exam tip, not a fact pattern; its two cases are used in new Examples 1 and 3.",
  "Exam Hypothetical: the 'Challengers' Best Arguments' and 'State's Best Arguments' labels (their text is reused in the Fence-Sitter).",
 ],
 "notes": ["Four legacy items kept (each a Supreme Court decision extending or applying the holding)."],
}

emit(__file__, FILL)
