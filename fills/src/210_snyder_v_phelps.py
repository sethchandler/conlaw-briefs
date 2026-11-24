"""Fill for 210_snyder_v_phelps. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/562/443/"
SO = "Concurring and Dissenting"
PS = "Pedagogical Critiques"
JL = r"(\href{https://supreme.justia.com/cases/federal/us/562/443/}{Justia})"

def Q(text, attr):
    # Attribution is placed inside the quote block (Group B form) so that
    # tools/normalize_quotes.py converts it to Group A form; see notes.
    return [N(r"\begin{quote}", glue="\n"), S(text, glue="\n"), N(r"---", glue=" "),
            S(attr, glue="\n"), N(r"\end{quote}")]

QUOTES = (
  Q(r"``What Westboro said, in the whole context of how and where it chose to say it, is entitled to `special protection' under the First Amendment, and that protection cannot be overcome by a jury finding that the picketing was outrageous.''",
    r"Chief Justice Roberts, 562 U.S.\ at 458 " + JL)
  + Q(r"``Speech is powerful. It can stir people to action, move them to tears of both joy and sorrow, and---as it did here---inflict great pain. On the facts before us, we cannot react to that pain by punishing the speaker. As a Nation we have chosen a different course---to protect even hurtful speech on public issues to ensure that we do not stifle public debate.''",
    r"Chief Justice Roberts, 562 U.S.\ at 460--461 " + JL)
  + Q(r"``To uphold the application of state law in these circumstances would punish Westboro for seeking to communicate its views on matters of public concern without proportionately advancing the State's interest in protecting its citizens against severe emotional harm.''",
    r"Justice Breyer (concurring), 562 U.S.\ at 462--463 " + JL)
  + Q(r"``Our profound national commitment to free and open debate is not a license for the vicious verbal assault that occurred in this case. \dots\ In order to have a society in which public issues can be openly and vigorously debated, it is not necessary to allow the brutalization of innocent victims like petitioner.''",
    r"Justice Alito (dissenting), 562 U.S.\ at 463, 475 " + JL)
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Westboro Baptist Church picketed, on public land 1,000 feet away, the funeral of a Marine killed in Iraq; an 8--1 Court held that the First Amendment bars tort liability, including for intentional infliction of emotional distress, for peaceful speech on matters of public concern in a public forum, however hurtful (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Snyder sued Phelps")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Snyder sued Phelps")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Fourth Circuit by an \textbf{8--1} vote. The case was argued on October 6, 2010, and decided on March 2, 2011 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supct/html/09-751.ZO.html}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Roberts delivered the opinion of the Court, joined by Justices Scalia, Kennedy, Thomas, Ginsburg, Breyer, Sotomayor, and Kagan.
    \item \textbf{Concurring Opinion:} Justice Breyer filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Alito filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Breyer)}"),
    SEC(SO, frm="Joining the Court's opinion, Breyer", to=r"  \item \textbf{Justice Alito"),
    N(r"\subsection{Dissenting Opinion (Justice Alito)}"),
    SEC(SO, frm="Writing alone, Alito", to=r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Speech Protected): Protest Near a Police Officer's Funeral.} Activists protesting police violence stand on a public sidewalk several hundred feet from a church where a police officer killed on duty is being mourned. Following police instructions, they hold signs condemning the department's use-of-force record and declaring that police deaths are the price of brutal tactics. The officer's widow, who glimpses the signs from the procession, sues for intentional infliction of emotional distress. As in \textit{Snyder}, the signs' content addresses matters of public concern, the protesters chose a traditional public forum, they stayed at a distance and did not disrupt the service, and they had no prior private dispute with the family. A jury's finding that the protest was outrageous cannot overcome the First Amendment's protection (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Speech Protected): A Columnist's Vicious Attack on a Private Landlord.} During a city scandal over unsafe rental housing, a newspaper columnist writes a savage column calling a private landlord, who owns several of the cited buildings, a heartless slumlord who should be ashamed to show his face. The landlord, a private figure, sues for intentional infliction of emotional distress. \textit{Snyder} extended \textit{Hustler}'s protection to private-figure plaintiffs whenever the speech, judged by its content, form, and context, addresses a matter of public concern. Housing safety is a public issue, and the column was published to a broad audience as part of an ongoing public debate, so the landlord cannot recover for emotional distress on the ground that the commentary was outrageous."),
    N(r"\item \textbf{Opposite-Side (Liability Permitted): A Private Feud Dressed Up With Slogans.} After a dispute over a property line, a man repeatedly posts signs in his front yard, facing his neighbors' home, mocking their daughter's recent miscarriage, and adds one generic sign criticizing local taxes. The neighbors sue for intentional infliction of emotional distress. \textit{Snyder}'s protection depends on speech addressing a matter of public concern; the Court distinguished speech of purely private significance, which receives less protection under \textit{Dun \& Bradstreet}, and warned that a speaker cannot immunize a personal attack arising from a preexisting private relationship by sprinkling in public themes. Here the content, form, and context all reveal a private vendetta, so the tort claim may proceed."),
    N(r"\item \textbf{Opposite-Side (Regulation Likely Valid): A Content-Neutral Funeral Buffer Law.} A State makes it a misdemeanor to picket within 300 feet of a funeral from one hour before until one hour after the service, regardless of the message. A church group that pickets funerals is cited and challenges the law. \textit{Snyder} expressly distinguished such content-neutral time, place, and manner rules from tort liability that turns on the content of the speaker's message, noting that Maryland and many other States had adopted them. Because the law applies to all picketing regardless of viewpoint, it would be judged by the standard for time, place, and manner restrictions; a modest, time-limited buffer that leaves ample alternative channels is likely to survive, though \textit{McCullen v.\ Coakley} shows the tailoring must be real."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Residential Picketing and Doxxing by Anti-Drunk-Driving Activists.}", glue=" "),
    S(r"After a high-profile fatal car crash involving a drunk driver, an anti-drunk-driving activist group pickets outside the home of the deceased driver's grieving parents on a public sidewalk for three consecutive nights, carrying signs reading ``Drunk Drivers Are Murderers,'' ``Your Son Deserved to Die,'' and ``Weak DUI Laws Kill.'' The group also posts the parents' private home address and phone number on social media urging followers to ``make them feel the pain.'' The parents sue for IIED and intrusion upon seclusion.", glue=" "),
    S(r"\textbf{Activists' Best Argument (Applying \textit{Snyder}):} Under \textit{Snyder}, DUI enforcement and highway safety are classic matters of public concern, the picketing occurred on a traditional public sidewalk, the group had no prior private dispute with the parents, and a jury cannot impose IIED liability merely because the signs are cruel or ``outrageous.''"),
    S(r"\textbf{Parents' Best Argument (Opposite-Side Contrast):} Distinguish \textit{Snyder} on three decisive grounds. First, unlike a distant 1,000-foot church-adjacent plot, targeted picketing directly outside a private residence implicates the home's heightened privacy and the captive audience doctrine (\textit{Frisby v.\ Schultz}), supporting both intrusion upon seclusion and content-neutral residential picketing limits. Second, the online doxxing campaign---posting private contact details and urging followers to ``make them feel the pain''---resembles Westboro's unadjudicated online ``epic'' and goes beyond public debate into targeted private harassment (and potentially reckless ``true threats'' under \textit{Counterman v.\ Colorado}). Third, under Breyer's proportionality concurrence and Alito's dissent, the combination of residential targeting and doxxing directly invades private seclusion without advancing public debate.", glue=" "),
    N(r"Because \textit{Snyder} left both residential targeting and online campaigns unresolved, either side could prevail."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"  \item \textbf{The ``Pre-Existing", to=r"\end{itemize}")],
  "Key Quotations": [p for q in QUOTES for p in [q]],
 },
 "dropped": [
  "LaTeX comment lines naming the case and chapter; Case Metadata docket number and Chapter/Topic line.",
  "Legacy section in full (no Subsequent Developments subsection): introductory paragraphs; McCullen v. Coakley buffer-zone item (applies time/place/manner doctrine, not Snyder's holding; McCullen is mentioned in Example 4); 'Breathing Space' item (Alvarez, Mahanoy, Counterman, NRA v. Vullo, Chiles v. Salazar - general First Amendment cases, not applications of Snyder); 'Unresolved Digital Frontier' item (lower-court commentary).",
 ],
 "notes": [
  "tools/check_brief.py compares stems against tools/manual_quotes.txt, whose entries carry a .tex suffix, so listed briefs are still sent through normalize_quotes.py (which rejects hand-built Group A quotes). Each quote is therefore rebuilt with its attribution inside the quote block so the normalizer produces the Group A form.",
  "Neon's exam hypothetical, which argues both sides, is reused as the Fence-Sitter with one new closing sentence.",
 ],
}

emit(__file__, FILL)
