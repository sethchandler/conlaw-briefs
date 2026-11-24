"""Fill for 200_abrams_v_united_states. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/250/616/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Affirming the Espionage Act convictions of five Russian-born radicals who scattered leaflets urging a munitions strike, the Court held 7--2 that intent to hinder the war could be inferred from the likely effects of their speech; Justice Holmes's dissent, demanding a clear and imminent danger, became a foundation of modern free-speech law (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="A federal grand jury indicted")],
  "Procedural History": [SEC("Facts and Procedural History", frm="A federal grand jury indicted")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the convictions by a \textbf{7--2} vote. The case was argued on October 21--22, 1919, and decided on November 10, 1919 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/250/616}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Clarke delivered the opinion of the Court, joined by Chief Justice White and Justices McKenna, Day, Van Devanter, Pitney, and McReynolds.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinion:} Justice Holmes filed a dissenting opinion, joined by Justice Brandeis.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Clarke)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Holmes)}"),
    SEC("Concurring and Dissenting", strip=r"\textbf{Dissent (Holmes, J., joined by Brandeis, J.):} "),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Holmes Vindicated (\textit{Brandenburg}):}", glue=" "),
    S(r"Half a century later, \href{https://supreme.justia.com/cases/federal/us/395/444/}{\emph{Brandenburg v. Ohio}}, 395 U.S. 444, 447 (1969), overruled \emph{Whitney} and vindicated Holmes's imminence principle: government may punish advocacy of force or law violation only where it is ``directed to inciting or producing imminent lawless action and is likely to incite or produce such action'' (see also \href{https://supreme.justia.com/cases/federal/us/414/105/}{\emph{Hess v. Indiana}}, 414 U.S. 105 (1973))."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Conviction Upheld): Speech Coordinated With a Foreign Terrorist Organization.} During an overseas conflict, members of a U.S. advocacy group, working at the request of and in coordination with a group the Secretary of State has designated a foreign terrorist organization, produce recruiting videos and train its members to petition international bodies. They are prosecuted under the federal ban on providing material support to such organizations. Like the \textit{Abrams} majority, the Court in \href{https://supreme.justia.com/cases/federal/us/561/1/}{\textit{Holder v. Humanitarian Law Project}}, 561 U.S. 1 (2010), deferred to the political branches' judgment about speech that could aid an enemy in wartime, upholding the ban as applied to speech coordinated with such groups. Because the speech is directed by the foreign organization rather than independent advocacy, the defendants cannot rely on Holmes's imminence requirement, and the conviction likely stands."),
    N(r"\item \textbf{Same-Side (Conviction Upheld Even Under Holmes's Test): A Call to Storm a Recruiting Station.} At an antiwar rally outside a military recruiting office, a speaker points to the building and tells an angry crowd to break in now and burn the draft files before the police arrive; several listeners immediately smash the windows. The speaker is convicted of incitement. Here even Justice Holmes would affirm. Unlike the ``silly leaflet'' in \textit{Abrams}, the speech was intended to produce an immediate evil and created a present danger of it. It also satisfies \textit{Brandenburg}'s test, since it was directed to inciting imminent lawless action and was likely to produce it. The case shows that the dissent's rule protects advocacy, not a speaker who directs an immediate crime."),
    N(r"\item \textbf{Opposite-Side (Speech Protected): Urging a Strike Next Month.}", glue=" "),
    S(r"During a U.S.\ military deployment abroad, an activist group posts videos in English and Spanish urging port dockworkers to launch a ``nationwide solidarity strike next month'' to protest U.S.\ arms shipments to an allied nation, while explicitly stating they oppose hostile foreign powers. Congress prosecutes them under a federal statute barring advocacy intended to hinder military logistics.", glue=" "),
    S(r"Under the \emph{Abrams} majority, foreseeable disruption of military supply chains satisfies intent and warrants conviction. Under Holmes's dissent and \href{https://supreme.justia.com/cases/federal/us/395/444/}{\emph{Brandenburg}}, the prosecution fails on both \emph{mens rea} (collateral effect vs.\ specific intent to aid an enemy) and \emph{imminence} (a vague call for a strike ``next month'' lacks immediate lawless incitement)."),
    N(r"\item \textbf{Opposite-Side (Speech Protected): Calling the President a Coward.} During a war, a pamphleteer distributes leaflets calling the President a coward and the government a fraud, and is prosecuted under a modern statute that, like Count One in \textit{Abrams}, punishes ``disloyal, scurrilous and abusive language'' about the government. The pamphlet urges no action at all. Holmes rejected the claim that the First Amendment left the common law of seditious libel in force, and the Court later adopted that view, explaining in \href{https://supreme.justia.com/cases/federal/us/376/254/}{\textit{New York Times Co. v. Sullivan}}, 376 U.S. 254 (1964), that the Sedition Act of 1798 had been condemned in the court of history. Criticism of officials, however harsh, is core political speech; because it threatens no imminent lawless action, the conviction cannot stand under \textit{Brandenburg}."),
    N(r"\item \textbf{Fence-Sitter (Borderline Imminence): A Viral Call to Shut Down a Plant.}", glue=" "),
    S(r"A viral social-media post generated by an anonymous user urges followers to ``shut down the local defense-contractor plant right now,'' and 200 armed protesters gather outside the gates within twenty minutes, blocking deliveries.", glue=" "),
    S(r"Unlike the ``silly leaflet'' tossed from a New York window in \emph{Abrams}, instant algorithmic mobilization combined with explicit, contemporaneous direction (``right now'') and high likelihood of immediate unlawful obstruction presents a textbook borderline case where even Holmes's ``immediate evil'' standard and \emph{Brandenburg}'s imminence/likelihood prongs could be satisfied.", glue=" "),
    N(r"The case is close because the government must also prove that the anonymous poster intended imminent lawless action, and ``shut down'' could mean a lawful protest or picket; whether the words and the crowd's rapid response establish that intent is a question on which reasonable judges could differ."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Holmes's Unacknowledged", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: comment lines, court and posture lines, key provisions (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: Gitlow/Whitney framing sentence and 'Through 2026' lead-in; Counterman v. Colorado item (true-threats mens rea, tangential); Moody v. NetChoice item and 2024-2026 scholarship (tangential); Holder v. HLP / TikTok v. Garland item (national-security deference generally; HLP reused in Example 1). Kept: Brandenburg/Hess sentence.",
  "Pedagogical section: 'Opposite Side' Contrast subsection (pro-government and pro-speaker lenses) - argument summaries, not fact patterns.",
  "Exam Hypotheticals: their bold headings and 'Analysis:' labels (both fact patterns reused in Examples 3 and 5).",
 ],
 "notes": [],
}

emit(__file__, FILL)
