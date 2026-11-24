"""Fill for 207_ward_v_rock_against_racism. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/491/781/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Upholding New York City's rule that Central Park bandshell performers use city sound equipment and a city technician, the Court held that a content-neutral time, place, and manner regulation is narrowly tailored if it serves a substantial interest that would be achieved less effectively without it; it need not be the least restrictive means (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="RAR sued in the U.S. District Court")],
  "Procedural History": [SEC("Facts and Procedural History", frm="RAR sued in the U.S. District Court")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the Second Circuit by a \textbf{6--3} vote. The case was argued on February 27, 1989, and decided on June 22, 1989 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Kennedy delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices White, O'Connor, and Scalia.
    \item \textbf{Concurring Opinion:} Justice Blackmun concurred in the result, without opinion.
    \item \textbf{Dissenting Opinion:} Justice Marshall filed a dissenting opinion, joined by Justices Brennan and Stevens.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kennedy)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Result (Justice Blackmun)}"), N("Justice Blackmun", glue=" "),
    SEC("Concurring and Dissenting", frm="Concurred in the judgment", to=r"  \item \textbf{Justice Marshall", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Marshall)}"), N("Justice Marshall", glue=" "),
    SEC("Concurring and Dissenting", frm="Agreed that the guideline", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Restoring Bite", to=r"  \item \textbf{2025--2026"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Regulation Valid): Volume Control at an Amphitheater Next to a Hospital.} A city requires every event at a public waterfront amphitheater beside a hospital to run its amplification through a city-owned sound-limiting system that keeps volume below a set level at the hospital's property line. Performers and speakers choose their own content and sound mix. The rule targets noise, not message, so it is content-neutral under \textit{Ward}'s purpose inquiry. It directly advances the city's substantial interest in protecting patients from unwelcome noise, that interest would be served less effectively without it, and speakers remain free to say anything at the amphitheater at a moderated volume, leaving ample alternative channels (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Regulation Valid): A Less Restrictive Alternative Does Not Defeat the Rule.} To prevent disruption of trials, a county bars amplified sound on the plaza in front of its courthouse during court hours on weekdays, while allowing unamplified demonstrations at any time and amplified rallies on evenings and weekends. Protesters show that a decibel limit enforced by sheriff's deputies would protect the courtrooms nearly as well. Under \textit{Ward}, that showing is not enough: a time, place, and manner rule ``need not be the least restrictive or least intrusive means'' of serving the government's interest. Because the ban is confined to the hours and place where the problem arises, it does not burden substantially more speech than necessary, and it is valid."),
    N(r"\item \textbf{Opposite-Side (Regulation Likely Invalid): Standardless Power to Mute Political Speech.}", glue=" "),
    S(r"Following loud late-night protests outside municipal buildings, City X enacts an ordinance governing its downtown Public Plaza (a traditional public forum). The ordinance bans all privately owned bullhorns, amplifiers, and speakers after 7:00 p.m., requiring any evening speaker seeking amplification to use a city-operated PA system capped at 70 decibels and staffed by a municipal technician who may mute the microphone if sound ``unreasonably disturbs nearby commerce or residential tranquility.'' A grassroots labor group challenging the ordinance argues it violates the First Amendment.", glue=" "),
    S(r"Unlike \textit{Ward}---where the city's system met all performers' technical needs, covered a fixed bandshell, and carried an established narrowing construction requiring deference to speakers---City X's ordinance grants a technician standardless authority to ``mute'' live political speech based on subjective ``disturbance'' with no narrowing construction or consultation protocol, inviting a strong facial unbridled-discretion/prior-restraint attack. Moreover, under \textit{McCullen v. Coakley}, if City X never tried enforcing its general noise ordinance or issuing citations to actual violators before banning all private bullhorns across an entire public plaza, the ordinance burdens substantially more peaceful speech than necessary and fails \textit{Ward}'s narrow-tailoring prong."),
    N(r"\item \textbf{Opposite-Side (Strict Scrutiny Applies): A Volume Rule Keyed to Content.} A city's park guideline lets the city's sound technician lower the volume of any performance that contains ``offensive or hateful lyrics,'' while leaving other performances at full volume. The rule fails at \textit{Ward}'s first step. \textit{Ward} upheld New York's guideline because it was adopted to control noise and not ``because of disagreement with the message'' conveyed, and because the city's technician deferred to sponsors on everything but volume. A rule that turns the knob based on what the lyrics say is content-based, so it falls outside \textit{Ward}'s intermediate scrutiny and must survive strict scrutiny, which it almost certainly cannot."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): A Total Ban on Amplification on a Park's Main Lawn.} Citing noise complaints from new apartment towers, a city bans all amplified sound on the main lawn of its largest park, the traditional site of mass rallies, and permits amplification only at a small stage in a remote corner. The rule is content-neutral, and under \textit{Ward} the city need not prove that a decibel limit would fail. But \textit{Ward} upheld a rule that merely moderated volume and banned no type of expression; here, a rally of thousands on the lawn cannot be heard without amplification, so the alternative channels may be inadequate, and \textit{McCullen} suggests the city must show it seriously tried less intrusive tools. Whether the ban burdens substantially more speech than necessary is a close question."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{Exam Hypothetical")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: full case name, docket number, Chapter/Topic line, duplicate source link (Justia link kept in Judicial Votes).",
  "Legacy section: introductory paragraph (Turner Broadcasting framing); '2025--2026 Applications' item (TikTok v. Garland citation and West Virginia v. B.P.J. (June 30, 2026) - passing citations, and the latter cannot be verified here). Kept: McCullen and Reed / City of Austin items.",
  "Exam Hypothetical: the 'City's Defense' bullet (restates Ward's test) and 'Opposite Side Contrast' label; the fact pattern and challenger analysis are reused in Example 3.",
 ],
 "notes": [],
}

emit(__file__, FILL)
