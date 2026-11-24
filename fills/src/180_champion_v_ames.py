"""Fill for 180_champion_v_ames. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/188/321/"
JL = r"(\href{https://supreme.justia.com/cases/federal/us/188/321/}{Justia})."

def Q(quote, attrib):
    # NOTE: tools/manual_quotes.txt lists "<stem>.tex", so check_brief.py's MANUAL set never
    # matches a stem and normalize_quotes.py always runs. Each quote is therefore moved with its
    # attribution inside the quote block (exactly as in the original list item), and
    # normalize_quotes.py moves the attribution to a Group A "\noindent ---" line.
    return [N(r"\begin{quote}", glue="\n"), S(quote + " --- " + attrib + " " + JL, glue="\n"),
            N(r"\end{quote}")]

QUOTES = (
  Q(r"``We are of opinion that lottery tickets are subjects of traffic, and therefore are subjects of commerce, and the regulation of the carriage of such tickets from state to state, at least by independent carriers, is a regulation of commerce among the several states.''", r"Justice Harlan, 188 U.S.\ at 354")
  + Q(r"``If a state, when considering legislation for the suppression of lotteries within its own limits, may properly take into view the evils that inhere in the raising of money in that mode, why may not Congress, invested with the power to regulate commerce among the several states, provide that such commerce shall not be polluted by the carrying of lottery tickets from one state to another?''", r"Justice Harlan, 188 U.S.\ at 356")
  + Q(r"``As a state may, for the purpose of guarding the morals of its own people, forbid all sales of lottery tickets within its limits, so Congress, for the purpose of guarding the people of the United States against the `widespread pestilence of lotteries' and to protect the commerce which concerns all the states, may prohibit the carrying of lottery tickets from one state to another.''", r"Justice Harlan, 188 U.S.\ at 357")
  + Q(r"``But, as often said, the possible abuse of a power is not an argument against its existence. There is probably no governmental power that may not be exerted to the injury of the public.''", r"Justice Harlan, 188 U.S.\ at 363")
  + Q(r"``An invitation to dine, or to take a drive, or a note of introduction, all become articles of commerce under the ruling in this case by being deposited with an express company for transportation. \dots\ It is a long step in the direction of wiping out all traces of state lines, and the creation of a centralized government.''", r"Chief Justice Fuller (dissenting), 188 U.S.\ at 371")
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"In the Lottery Case, the Court upheld 5--4 the federal ban on carrying lottery tickets across state lines, holding that lottery tickets are articles of commerce and that Congress's power to regulate interstate commerce includes the power to prohibit it---the root of the federal ``police power'' exercised through the channels of commerce (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Champion was arrested in Chicago")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Champion was arrested in Chicago")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Circuit Court's dismissal of the habeas petition by a \textbf{5--4} vote. The case was argued three times (February 1901, October 1901, and December 1902) and decided February 23, 1903 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/188/321}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Harlan delivered the opinion of the Court, joined by Justices Brown, White, McKenna, and Holmes.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinion:} Chief Justice Fuller filed a dissenting opinion, joined by Justices Brewer, Shiras, and Peckham.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Harlan)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Chief Justice Fuller)}"),
    SEC("Concurring and Dissenting", strip=r"\textbf{Chief Justice Fuller (dissenting, joined by Justices Brewer, Shiras, and Peckham):} "),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Extended to Other Harmful Articles:}", glue=" "),
    S(r"Immediately following \textit{Champion}, the Court relied on its commerce-prohibiting principle to uphold the Pure Food and Drug Act in \href{https://supreme.justia.com/cases/federal/us/220/45/}{\textit{Hipolite Egg Co.\ v.\ United States}}, 220 U.S.\ 45 (1911), the Mann Act (White-Slave Traffic Act) in \href{https://supreme.justia.com/cases/federal/us/227/308/}{\textit{Hoke v.\ United States}}, 227 U.S.\ 308 (1913), and the National Motor Vehicle Theft Act in \href{https://supreme.justia.com/cases/federal/us/267/432/}{\textit{Brooks v.\ United States}}, 267 U.S.\ 432 (1925)."),
    N(r"\item \textbf{Narrowed, Then Vindicated (\textit{Hammer} and \textit{Darby}):}", glue=" "),
    S(r"The Court briefly attempted to cabin \textit{Champion} during the \textit{Lochner} era in \href{https://supreme.justia.com/cases/federal/us/247/251/}{\textit{Hammer v.\ Dagenhart}}, 247 U.S.\ 251 (1918), striking down the federal Child Labor Act by distinguishing goods ``harmful in themselves'' (like lottery tickets or impure food) from ``harmless'' manufactured goods produced by child labor. That distinction proved unworkable---after eroding it in \href{https://supreme.justia.com/cases/federal/us/299/334/}{\textit{Kentucky Whip \& Collar Co.\ v.\ Illinois Central R.\ Co.}}, 299 U.S.\ 334 (1937) (prison-made goods), a unanimous Court overruled \textit{Hammer} in \href{https://supreme.justia.com/cases/federal/us/312/100/}{\textit{United States v.\ Darby}}, 312 U.S.\ 100 (1941), fully vindicating \textit{Champion} and Justice Holmes's \textit{Hammer} dissent by holding that Congress's motive in barring goods from interstate shipment is constitutionally irrelevant."),
    N(r"\item \textbf{The ``Channels'' Category Today:}", glue=" "),
    S(r"\textit{Champion} remains undisturbed bedrock law as the first pillar of the modern three-category Commerce Clause framework articulated in \href{https://supreme.justia.com/cases/federal/us/514/549/}{\textit{United States v.\ Lopez}}, 514 U.S.\ 549, 558 (1995): Congress's plenary authority to regulate ``the use of the channels of interstate commerce.''"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Channel-Closing Upheld): Banning Interstate Shipment of a Medication Lawful in Both States.}", glue=" "),
    S(r"Congress enacts the ``Interstate Reproductive Information and Materials Act,'' making it a federal felony to ship any over-the-counter abortifacient medication or printed instructional brochure across state lines via private courier. A distributor in State~A (where the medication is legal) ships a package via FedEx to a clinic in State~B (where it is also legal) and challenges the indictment under the Commerce Clause and Tenth Amendment.", glue=" "),
    N(r"As to the medication itself:", glue=" "),
    S(r"Under \textit{Champion} and \textit{Darby}, Congress's authority over the channels of interstate commerce is plenary and includes the power to prohibit interstate shipment of any article, regardless of whether the underlying motive is moral or regulatory, and even if both the origin and destination states permit the article locally."),
    N(r"\item \textbf{Same-Side (Channel-Closing Upheld): Unserialized Firearm Kits.} Congress makes it a federal crime to ship unserialized, build-it-yourself firearm kits across state lines. A seller in State~A mails a kit to a buyer in State~B and challenges the indictment solely on Commerce Clause and Tenth Amendment grounds, arguing that the kits are lawful where sold and that Congress is really regulating local gun ownership. Under \textit{Champion}, the kits are articles of traffic, and the power to regulate their interstate carriage includes the power to forbid it. Under \textit{Darby}, Congress's reason for closing the channel---crime control rather than commercial policy---is irrelevant, and there is no Tenth Amendment problem because the regulation rests on a delegated power. The indictment stands."),
    N(r"\item \textbf{Opposite-Side (External Limits): The Brochures.} Same statute, but the distributor challenges the ban on shipping the printed instructional brochures.", glue=" "),
    S(r"First, distinguish \textit{Champion} on external constitutional limits: Harlan expressly acknowledged that the commerce power ``may not be exercised so as to infringe rights secured or protected by that instrument'' (188 U.S.\ at 362--363); banning the interstate shipment of \textit{printed brochures} directly implicates the First Amendment (an issue Fuller flagged as absent in \textit{Champion}). Second, unlike \textit{Champion}, where Harlan stressed that Congress was ``supplement[ing] the action of those states---perhaps all of them'' that banned lotteries, here Congress is overriding the permissive policies of both State~A and State~B, reviving Fuller's structural objection that Congress is using channel-closing as a pretextual national police power. (Under current doctrine, the First Amendment challenge to the brochures is far stronger than the Tenth Amendment/Commerce Clause challenge to the physical pills.)"),
    N(r"\item \textbf{Opposite-Side (No Channel at All): A Federal Ban on Public Intoxication.} Citing the moral concerns that sustained \textit{Champion}, Congress makes it a federal crime for any adult to be publicly intoxicated anywhere in the United States. The statute has no jurisdictional element tying the offense to interstate travel or shipment. \textit{Champion} does not help the government: it upheld a regulation of the interstate \emph{movement} of articles, not a general federal power to punish local immorality. Because no channel of interstate commerce is being used, the statute must instead be justified as regulating activity that substantially affects interstate commerce, and under \href{https://supreme.justia.com/cases/federal/us/514/549/}{\textit{United States v.\ Lopez}}, 514 U.S. 549 (1995), and \textit{United States v.\ Morrison}, 529 U.S. 598 (2000), noneconomic local conduct of this kind cannot be aggregated to meet that test. The statute is invalid."),
    N(r"\item \textbf{Fence-Sitter (Has the Article Left the Channel?): Possession of Goods That Once Crossed State Lines.} Congress makes it a crime to possess any vaping device that has at any time traveled in interstate commerce. A buyer is prosecuted for possessing a device he purchased at a local shop three years after it was shipped into his State. The government argues that this is \textit{Champion}'s channels power plus a jurisdictional element; the Court read a similar felon-in-possession statute to require only such a minimal nexus in \textit{Scarborough v.\ United States}, 431 U.S. 563 (1977). The defendant answers that \textit{Champion} rested on stopping articles \emph{in transit}, as Harlan emphasized by saying Congress left purely internal lottery sales to the States, and that a once-in-commerce hook lets Congress reach any local possession, the general police power Fuller feared. The Court has not squarely resolved how far this kind of hook can reach, so the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{The ``Pollution''", to=r"\end{itemize}")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "Case Metadata: S. Ct./L. Ed. parallel cites, Chapter/Topic line (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: Heart of Atlanta sentence (relies on substantial-effects reasoning, not squarely Champion); 'Through 2026' framing and the Lopez/Morrison/NFIB/Bond/Raich survey of modern limits (tangential). Kept: Hipolite Egg/Hoke/Brooks extensions, Hammer/Darby, and the Lopez 'channels' sentence.",
  "Exam Hypothetical labels ('Government's Best Argument', 'Challenger's Best Argument (Opposite-Side Contrast)'); their text is reused in Examples 1 and 3.",
 ],
 "notes": [
  "Facts/Procedural split placed at Champion's arrest so that the indictment's description of the lottery-ticket shipment stays with the facts.",
  "Key Quotations rebuilt in Group A style (manual_quotes list); all five quotes and pin cites kept.",
 ],
}

emit(__file__, FILL)
