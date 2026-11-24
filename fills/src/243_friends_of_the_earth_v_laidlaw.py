"""Fill for 243_friends_of_the_earth_v_laidlaw. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/528/167/"
FS = "Facts and Procedural History"
SO = "Concurring and Dissenting"
LG = "Doctrinal Significance"
PS = "Pedagogical Critiques"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Environmental groups sued a polluter under the Clean Water Act for civil penalties; the Court held 7--2 that members who curtailed use of a river had standing even without proof of environmental harm, that penalties deterring ongoing violations provide redress, and that voluntary cessation moots a case only if the defendant shows it is absolutely clear the violations cannot reasonably be expected to recur (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="On April 10, 1992, petitioners")],
  "Procedural History": [SEC(FS, frm="On April 10, 1992, petitioners")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} the Fourth Circuit by a \textbf{7--2} vote. The case was argued on October 12, 1999, and decided on January 12, 2000 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/528/167}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Ginsburg delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices Stevens, O'Connor, Kennedy, Souter, and Breyer.
    \item \textbf{Concurring Opinions:} Justice Stevens filed a concurring opinion. Justice Kennedy filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Scalia filed a dissenting opinion, joined by Justice Thomas.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Ginsburg)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Stevens)}"),
    SEC(SO, frm="Justice Stevens wrote separately", to=r"\textbf{Justice Kennedy"),
    N(r"\subsection{Concurring Opinion (Justice Kennedy)}"),
    SEC(SO, frm="Joining the Court's Article III", to=r"\textbf{Justice Scalia"),
    N(r"\subsection{Dissenting Opinion (Justice Scalia)}"),
    SEC(SO, frm="Justice Scalia attacked"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC(LG, frm=r"  \item \textbf{Enduring Authority", to=r"  \item \textbf{Tightening Concrete"),
    N(r"\item \textbf{Tension With \textit{TransUnion} on Concrete Injury:}", glue=" "),
    S(r"By contrast, \textit{Laidlaw}'s expansive view of injury and citizen-suit redressability stands in growing tension with \href{https://www.law.cornell.edu/supremecourt/text/20-297}{\textit{TransUnion LLC v. Ramirez}, 594 U.S. 413 (2021)} (\href{https://supreme.justia.com/cases/federal/us/594/20-297/}{Justia}).", glue=" "),
    S(r"Echoing Justice Scalia's \textit{Laidlaw} dissent, \textit{TransUnion} held that Congress cannot create Article III injury merely by enacting a statutory cause of action; plaintiffs must show concrete harm bearing a ``close historical or common-law analogue,'' and unmaterialized risk of future harm cannot support retrospective damages."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Live Case; Not Moot): Post-Filing Compliance by a Chemical Plant.}", glue=" "),
    S(r"A state environmental group whose members regularly kayak on Buffalo Bayou sues a chemical plant under CWA \S~505 while the plant is actively exceeding its benzene permit limits, seeking civil penalties payable to the Treasury. Six months into discovery, the plant installs new scrubbers, achieves full compliance, and moves to dismiss as moot.", glue=" "),
    S(r"Under \textit{Laidlaw} and \textit{FBI v. Fikre}, the group had standing at filing (curtailed recreational use plus ongoing violations redressable by deterrent civil penalties), and the plant's post-filing compliance does not moot the case unless the plant proves it is ``absolutely clear'' that benzene violations cannot reasonably be expected to recur."),
    N(r"\item \textbf{Same-Side (Standing Exists): Birdwatchers Who Stay Away From a Marsh.} A paper mill upstream of a coastal marsh repeatedly exceeds the dioxin limits in its discharge permit. Members of a birding club submit affidavits that they used to visit the marsh monthly but have stopped because they fear the illegal discharges, and one says her lakeside cabin has become harder to rent. The mill shows that scientists have found no measurable harm to the marsh's wildlife. Under \textit{Laidlaw}, the relevant injury is to the plaintiffs, not the environment: a reasonable concern about ongoing unlawful pollution that leads members to give up specific, regular uses of an identified place is concrete injury in fact, unlike the vague some-day intentions in \textit{Lujan}."),
    N(r"\item \textbf{Opposite-Side (No Standing): Violations Ended Before Suit.} Suppose", glue=" "),
    S(r"the same chemical plant cured all benzene violations and permanently surrendered its discharge permit \textit{before} the environmental group filed suit", glue=""),
    N(r". Standing is measured when the complaint is filed, and at that moment nothing remained to deter. Civil penalties payable to the Treasury for wholly past violations cannot redress the members' injury, which is why \textit{Steel Co.\ v.\ Citizens for a Better Environment} found no standing. The voluntary-cessation doctrine never comes into play, because it applies only to a case that was live when filed and is later claimed to be moot."),
    N(r"\item \textbf{Opposite-Side (No Standing): An Undisclosed Credit-File Error.} Alternatively, suppose", glue=" "),
    S(r"a consumer sues a credit bureau for statutory damages over an internal file error that was never disclosed to any third party", glue=""),
    N(r". The consumer has a statutory cause of action, but under \textit{TransUnion} a bare statutory violation is not enough: the inaccurate file, never sent to anyone, causes no concrete harm with a close historical analogue such as defamation. Unlike the \textit{Laidlaw} members, who changed how they used a real place because of ongoing pollution, the consumer has suffered nothing Article III recognizes, so the suit must be dismissed."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Closing the Plant but Keeping the Permit.} After a citizen suit is filed over ongoing permit violations, the defendant shuts down its facility, lays off its workers, and lists the property for sale, but keeps its discharge permit in force and says it has no present plans to reopen. That is essentially Laidlaw's own posture, which the Court remanded without deciding. The defendant argues that closure makes recurrence impossible; the plaintiffs answer that a retained permit leaves the defendant free to resume discharges at will, and \textit{Fikre} held that a bare assurance of no present intent does not carry the formidable burden. Whether the closure is truly permanent is a factual question that could go either way."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"  \item \textbf{Reasonable Fear", to=r"\subsection{Exam")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: parallel S. Ct. citation, docket number, provisions line, duplicate Cornell links.",
  "Legacy section: introductory paragraph; second half of the TransUnion item (National Park Service v. National Trust for Historic Preservation 2026 stay - an emergency order, tangential). Kept: Already / FBI v. Fikre item and TransUnion sentences.",
  "Exam Hypothetical 2 ('Opposite Side' Contrast): its framing sentence and combined analysis dropped; its two fact variants moved verbatim into Examples 3 and 4 with new analysis.",
 ],
 "notes": [],
}

emit(__file__, FILL)
