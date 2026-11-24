"""Fill for 257_usda_v_moreno. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/413/528/"
JL = r"\href{https://supreme.justia.com/cases/federal/us/413/528/}"

def quote(text, attrib):
    return [N(r"\begin{quote}", glue="\n"), S(text, glue="\n"), N(r"\end{quote}", glue="\n"),
            N(r"\noindent ---", glue=" "), S(attrib, glue=""), N(".")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Congress cut off food stamps to any household containing an unrelated member, aiming at ``hippie communes''; the Court held 7--2 that the classification failed even rational-basis review, because a bare congressional desire to harm a politically unpopular group is not a legitimate governmental interest (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Moreno and other plaintiffs filed")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Moreno and other plaintiffs filed")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the three-judge District Court by a \textbf{7--2} vote. The case was argued on April 23, 1973, and decided on June 25, 1973 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/413/528}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Brennan delivered the opinion of the Court, joined by Justices Douglas, Stewart, White, Marshall, Blackmun, and Powell.
    \item \textbf{Concurring Opinion:} Justice Douglas filed a concurring opinion (413 U.S.\ at 538--545).
    \item \textbf{Dissenting Opinion:} Justice Rehnquist filed a dissenting opinion, joined by Chief Justice Burger (413 U.S.\ at 545--547).
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Brennan)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Douglas)}"),
    SEC("Concurring and Dissenting", frm="Douglas candidly conceded", to=r"  \item \textbf{Justice Rehnquist"),
    N(r"\subsection{Dissenting Opinion (Justice Rehnquist)}"),
    SEC("Concurring and Dissenting", frm="Rehnquist accused the majority", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{The Animus Quadrilogy:}", to=r"  \item \textbf{Retrenchment"),
    N(r"\item \textbf{Retrenchment (\textit{Trump v.\ Hawaii}):}", glue=" "),
    S(r"In \href{https://supreme.justia.com/cases/federal/us/585/17-965/}{\textit{Trump v. Hawaii}, 585 U.S. 667 (2018)}, the Court upheld the President's travel proclamation despite challenged statements, stressing that a policy survives rational-basis review unless it is ``inexplicable by anything but animus.''"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Invalid Animus): Excluding Protest Misdemeanants From Housing Vouchers.}", glue=" "),
    S(r"Facing complaints from homeowners about noise and parking near a university, a city amends its municipal housing-voucher program to disqualify any household containing ``an individual with a prior misdemeanor conviction for participating in an unpermitted street protest.'' During floor debate, the ordinance's sponsor declares, ``Taxpayers shouldn't subsidize radical campus agitators.'' When sued, the city argues the rule rationally conserves limited housing funds and promotes neighborhood stability.", glue=" "),
    S(r"Because protest misdemeanants are not a suspect class, rational-basis review applies (alongside First Amendment retaliation concerns). Under \href{https://supreme.justia.com/cases/federal/us/413/528/}{\textit{Moreno}}, the sponsor's statement flags a ``bare desire to harm a politically unpopular group.'' Like the fraud rationale in \textit{Moreno}, the city's post hoc justifications fail ``rational basis with bite'': violent felons and noisy tenants remain eligible while peaceful misdemeanor protesters are singled out, rendering the means-ends fit grossly under- and over-inclusive and inexplicable by anything other than animus."),
    N(r"\item \textbf{Same-Side (Invalid Animus): Excluding Households With Tattoo Artists From Utility Relief.}", glue=" "),
    S(r"A state excludes from emergency utility-bill relief any otherwise eligible household that includes an unrelated adult who works as a tattoo artist or body piercer, following legislative remarks denouncing ``counterculture freeloaders.'' Even if the state argues cash-based trades underreport income, existing income-verification rules address fraud, and targeting one stigmatized occupation fails \textit{Moreno}."),
    N(r"\item \textbf{Opposite-Side (Valid Under Deferential Review): A Neutral Unrelated-Occupant Zoning Limit.}", glue=" "),
    S(r"A town enacts a neutral residential zoning ordinance limiting single-family zones to related persons or no more than two unrelated persons living together, citing traffic congestion, noise, and neighborhood quiet (modeled on \href{https://supreme.justia.com/cases/federal/us/416/1/}{\textit{Village of Belle Terre v. Boraas}, 416 U.S. 1 (1974)}).", glue=" "),
    N(r"Unlike \textit{Moreno}, the ordinance", glue=" "),
    S(r"lacks record evidence of bare animus toward an unpopular group, does not strip subsistence aid from destitute households, and bears a plausible, non-pretextual connection to legitimate land-use goals---surviving traditional rational-basis review."),
    N(r"\item \textbf{Opposite-Side (Valid Under Deferential Review): A Work Requirement for Food Assistance.} Congress provides that able-bodied adults without dependents may receive food assistance for only three months in any three-year period unless they work or join a training program at least twenty hours a week. Challengers argue that the rule harms poor, unemployed adults. Unlike the 1971 amendment in \textit{Moreno}, the rule is tied directly to the program's purposes of helping those in need while encouraging self-sufficiency, the record shows no aim of harming an unpopular group, and the line it draws---between those who can work and those who cannot---bears a plausible relation to that goal. Under the deferential review of \textit{Dandridge v.\ Williams}, the rule survives even if it is a blunt instrument."),
    N(r"\item \textbf{Fence-Sitter (Mixed Motives): A Ban on Living in Vehicles.} A city bans sleeping in parked vehicles on public streets overnight, citing sanitation complaints and traffic safety. During debate, several council members describe the people affected in disparaging terms and say the city should make them leave. Under \textit{Moreno}, a bare desire to harm a politically unpopular group is not a legitimate interest, and the remarks resemble the anti-hippie statements in the Food Stamp Act's history. But sanitation and street safety are plausible, independent justifications, and \textit{Trump v.\ Hawaii} suggests that a policy survives unless it is inexplicable by anything but animus. Whether a court treats the hostile remarks as revealing the law's real purpose or as stray comments is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Doctrinal Candor", to=r"\end{itemize}")],
  "Key Quotations": (
    quote(r"``For if the constitutional conception of `equal protection of the laws' means anything, it must, at the very least, mean that a bare congressional desire to harm a politically unpopular group cannot constitute a legitimate governmental interest.''", r"Brennan, J., " + JL + "{413 U.S. at 534}")
    + quote(r"``Thus, in practical operation, the 1971 amendment excludes from participation in the food stamp program, not those persons who are `likely to abuse the program' but, rather, only those persons who are so desperately in need of aid that they cannot even afford to alter their living arrangements so as to retain their eligibility.''", r"Brennan, J., " + JL + "{413 U.S. at 538}")
    + quote(r"``The right of association, the right to invite the stranger into one's home is too basic in our constitutional regime to deal with roughshod.''", r"Douglas, J., concurring, " + JL + "{413 U.S. at 543}")
    + quote(r"``The Court's opinion would make a very persuasive congressional committee report arguing against the adoption of the limitation in question. Undoubtedly, Congress attacked the problem with a rather blunt instrument . . . . But questions such as this are for Congress, rather than for this Court . . . .''", r"Rehnquist, J., dissenting, " + JL + "{413 U.S. at 545--546}")
  ),
 },
 "dropped": [
  "Case Metadata: docket number, LOC PDF link, court-below line (in Procedural History), provisions list.",
  "Legacy section: lead-in paragraph; Retrenchment item's Skrmetti sentence (no animus holding; tangential) with 2025-2026 lower-court/law-review commentary, and the 'Thus, through 2026' summary. Kept: animus quadrilogy item (Cleburne, Romer, Windsor, Lawrence concurrence); Trump v. Hawaii sentence.",
  "Exam Hypotheticals: 'Analysis:' label, subsubsection headings, and Law A/Law B labels (texts reused in Examples 1-3).",
  "Key Quotations: descriptive topic labels (speaker and pin cite moved into Group A attribution lines).",
 ],
 "notes": [
  "Key Quotations built manually in Group A style (stem listed in tools/manual_quotes.txt).",
 ],
}

emit(__file__, FILL)
