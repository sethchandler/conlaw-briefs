"""Fill for 203_cohen_v_california. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/403/15/"
FS = "Facts and Procedural History"
LG = "Doctrinal Significance"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"A 19-year-old wore a jacket reading ``Fuck the Draft'' in a Los Angeles courthouse corridor; the Court held 5--4 that a State may not criminalize the public display of a single expletive conveying a political message, because it was not obscenity or fighting words and unwilling viewers could avert their eyes (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="He was convicted in Los Angeles Municipal Court")],
  "Procedural History": [SEC(FS, frm="He was convicted in Los Angeles Municipal Court")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the California Court of Appeal by a \textbf{5--4} vote. The case was argued on February 22, 1971, and decided on June 7, 1971 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/403/15}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Harlan delivered the opinion of the Court, joined by Justices Douglas, Brennan, Stewart, and Marshall.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinion:} Justice Blackmun filed a dissenting opinion, joined by Chief Justice Burger and Justice Black, and joined as to its second paragraph by Justice White.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Harlan)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Blackmun)}"),
    SEC("Concurring and Dissenting", frm="Blackmun offered two grounds", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    SEC(LG, frm=r"\begin{itemize}", to=r"  \item \textbf{Contemporary Digital"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Speech Protected): A Profane Protest Sign Outside City Hall.} During a rally on the plaza outside city hall, a resident holds a sign using the same four-letter word to condemn the mayor's housing policy. Families walking to a nearby park see it, and police arrest the resident under an ordinance banning offensive language in public places. As in \textit{Cohen}, the sign targets a policy and a public official rather than any individual present, so it is not fighting words, it is not erotic and so not obscene, and passersby in a public square can look away. The State may not punish the word merely because it offends, and the arrest violates the First Amendment."),
    N(r"\item \textbf{Same-Side (Speech Protected): A Ban on Profane Bumper Stickers.} A State makes it a misdemeanor to display on any vehicle a sticker containing profanity, and police cite a driver whose sticker uses an expletive to protest a war. Other motorists and pedestrians who see the sticker are outside the home and can avert their eyes, so they are not a captive audience. The law reaches emotive political expression that \textit{Cohen} protects, gives officials the boundless power over vocabulary Harlan rejected because one man's vulgarity is another's lyric, and is not tied to any setting that would justify special decorum rules. The citation cannot stand."),
    N(r"\item \textbf{Opposite-Side (Speech Punishable): A Face-to-Face Epithet Inviting a Fight.} During a heated argument on a sidewalk, a man steps within inches of a rival, uses the same expletive together with personal slurs aimed at him, and dares him to throw a punch. He is convicted under a statute narrowly construed to reach only words likely to provoke the average listener to immediate violence. Unlike Cohen's jacket, this speech is a personally abusive epithet directed to the person of the hearer, the core of \textit{Chaplinsky}'s fighting-words category that \textit{Cohen} preserved. The conviction is consistent with the First Amendment."),
    N(r"\item \textbf{Opposite-Side (Restriction Upheld): Profanity Broadcast Into the Home.} A radio station airs, in the early afternoon, a comedy routine that repeats several vulgar words, and a parent driving with a young child complains. The federal regulator sanctions the station under its indecency rules. Unlike the corridor in \textit{Cohen}, broadcast speech reaches listeners in the privacy of the home and is uniquely accessible to children, so a warning or averting one's eyes cannot fully protect them. In \textit{FCC v.\ Pacifica Foundation}, 438 U.S.\ 726 (1978), the Court upheld a sanction on just these facts, showing that \textit{Cohen}'s rule depends on the medium and setting."),
    N(r"\item \textbf{Fence-Sitter (Close Call): A Courtroom Ban on Profane Apparel.}", glue=" "),
    S(r"A city enacts a narrow ordinance prohibiting ``any person inside a municipal courtroom or jury-assembly room from wearing apparel displaying profanity.'' A protester wears a jacket reading ``Fuck the Police'' into the municipal courtroom while court is in session and refuses the bailiff's order to remove it.", glue=" "),
    S(r"Distinguish \textit{Cohen} on three fronts. First, unlike California's statewide breach-of-the-peace statute, this ordinance is location-specific and gives clear notice (addressing Harlan's notice objection at 403 U.S. at 19). Second, a courtroom in session is a nonpublic forum where the government may impose reasonable, viewpoint-neutral decorum rules (and jurors/litigants compelled to attend are far closer to a true captive audience than corridor passersby). Third, however, the challenger will invoke \textit{Cohen} and \textit{Brunetti} to argue that banning ``profanity'' still invites arbitrary, viewpoint-skewed enforcement unless strictly tied to courtroom disruption.", glue=" "),
    N(r"The case is close because \textit{Cohen} expressly left open location-specific decorum rules but condemned giving officials power to police offensive words."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\begin{itemize}", to=r"\subsection*{Exam Hypothetical}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Source comment lines and Case Metadata: Chapter/Topic line and Cornell/Justia list (links kept in Judicial Votes).",
  "Legacy section: introductory paragraph and 'Contemporary Digital and Public-Forum Disputes (Through 2026)' item (general commentary, no decision). Kept: Iancu v. Brunetti and Mahanoy items.",
  "Exam Hypothetical 'Opposite Side Contrast' (Pacifica) - an exam tip contrasting a real case; Pacifica now appears as new Example 4.",
 ],
 "notes": ["Example 5 reuses Neon's courtroom-apparel hypothetical with its three-part analysis and adds one sentence explaining the uncertainty."],
}

emit(__file__, FILL)
