"""Fill for 258_shaw_v_reno. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/509/630/"
FS = "Facts and Procedural History"
SO = "Concurring and Dissenting"
DS = "Doctrinal Significance"
PS = "Pedagogical Critiques"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Voters challenged North Carolina's snake-like, majority-Black District 12, drawn after a Justice Department objection; a 5--4 Court held that a redistricting plan so bizarre that it is unexplainable on grounds other than race states an Equal Protection claim triggering strict scrutiny, even without any dilution of a group's voting strength (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="Five white residents of Durham County")],
  "Procedural History": [SEC(FS, frm="Five white residents of Durham County")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{5--4} vote. The case was argued on April 20, 1993, and decided on June 28, 1993 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice O'Connor delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices Scalia, Kennedy, and Thomas.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice White filed a dissenting opinion, joined by Justices Blackmun and Stevens. Justices Blackmun, Stevens, and Souter each filed a separate dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice O'Connor)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice White)}"), N("Justice White", glue=" "),
    SEC(SO, frm="Argued appellants alleged no", to=r"  \item \textbf{Justice Blackmun", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Blackmun)}"), N("Justice Blackmun", glue=" "),
    SEC(SO, frm="Joined Justice White and underscored", to=r"  \item \textbf{Justice Stevens", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Stevens)}"), N("Justice Stevens", glue=" "),
    SEC(SO, frm="Maintained that bizarre shapes", to=r"  \item \textbf{Justice Souter", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Souter)}"), N("Justice Souter", glue=" "),
    SEC(SO, frm="Emphasized two differences", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    SEC(DS, frm=r"\begin{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Strict Scrutiny; District Invalid): A Barbell-Shaped Hispanic-Majority District.}", glue=" "),
    S(r"After the 2030 census, a State with a 28\% Hispanic voting-age population enacts a congressional map containing a 210-mile, barbell-shaped District 4 that splits nine counties to connect two distant urban Hispanic enclaves, achieving a 52\% Hispanic voting-age population. Legislative emails show mapmakers set a ``50\%+ HVAP floor'' to preempt a threatened VRA \S~2 lawsuit, though no court had found intentional discrimination and no illustrative map could create the district while preserving the State's partisan-advantage goals. A white voter residing in District 4 sues under the Equal Protection Clause.", glue=" "),
    S(r"The plaintiff has standing as a District 4 resident (\textit{Shaw II}) and states a strong \textit{Shaw} claim. Both the bizarre, county-splitting geometry and the direct email evidence of a 50\%+ racial target show that race predominated over traditional districting principles, triggering strict scrutiny. Under \textit{Louisiana v. Callais} (2026), the State cannot establish a compelling interest in VRA \S~2 compliance because \S~2 requires a strong inference of intentional racial discrimination and an illustrative map that satisfies the State's legitimate political goals without using race; District 4 is therefore an unconstitutional racial gerrymander."),
    N(r"\item \textbf{Same-Side (Strict Scrutiny Triggered): A Mechanical Racial Target in a Regular-Looking District.} A legislature redraws a congressional district that had elected the minority community's preferred candidates by comfortable margins for twenty years. Mapmakers testify that they were instructed to raise the district's Black voting-age population above 50 percent, and to do so they move tens of thousands of Black voters in and out of the district, splitting several precincts, although the district's outline is not especially strange. \textit{Shaw}'s logic does not depend on a bizarre shape alone: once race predominates over traditional principles, strict scrutiny applies. In \textit{Cooper v.\ Harris}, 581 U.S.\ 285 (2017), the Court struck down a North Carolina district drawn to a 50-percent racial target where the State lacked a strong basis in evidence that the VRA required it (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (\textit{Shaw} Claim Fails): Partisan Line-Drawing.}", glue=" "),
    S(r"Now alter the facts: suppose the legislature draws a compact, county-respecting District 4 that moves 20,000 heavily Democratic Hispanic voters \textit{out} of District 4 into neighboring District 5 to lock in a safe Republican incumbent in District 4, without any racial target in the legislative record, and challengers fail to produce an alternative map that achieves the same Republican partisan margin while keeping those voters in District 4. Under \textit{Alexander v. South Carolina State Conference of the NAACP} (2024) and \textit{Rucho}, the presumption of legislative good faith and the adverse inference from the missing alternative map defeat the \textit{Shaw} racial-gerrymandering claim because the challengers failed to disentangle race from permissible partisan politics."),
    N(r"\item \textbf{Opposite-Side (No Strict Scrutiny): Awareness of Race in a Compact District.} A State's redistricting commission draws a compact, contiguous district that follows county and city lines and keeps a recognized metropolitan area together. The district happens to be 55 percent Black, and the commission's records show that members knew its racial makeup and discussed it, but every boundary choice is explained by population equality, compactness, and respect for political subdivisions. A voter alleges a racial gerrymander. \textit{Shaw} acknowledged that legislatures are always aware of race when they redistrict; what triggers strict scrutiny is a plan that subordinates traditional districting principles to race. Because traditional criteria, not race, explain these lines, the district is reviewed deferentially and stands."),
    N(r"\item \textbf{Fence-Sitter (Compelling Interest Uncertain): A Remedial District Ordered After a VRA Finding.} After a federal court finds that a State's map violates \S~2 of the Voting Rights Act by diluting Black votes, the legislature draws a new, somewhat irregular majority-Black district, consciously using race to meet the court's remedy. White and Black voters inside the district bring a \textit{Shaw} challenge. Race plainly predominated, so strict scrutiny applies. \textit{Shaw} left open whether VRA compliance can be a compelling interest; later cases assumed it could when the State has a strong basis in evidence, and a prior judicial finding of a violation is strong evidence. But \textit{Callais}, as described above, narrowed that interest to \S~2 applied to intentional discrimination. Whether this remedial district survives depends on whether the earlier \S~2 finding rested on proof that meets that narrower standard and on whether the district is narrowly tailored---a genuinely open question."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"  \item \textbf{Standing and Expressive", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, Justia PDF link, Cornell ConAn link.",
  "Legacy section: introductory sentence only. Kept all three items (Miller/Shaw II; Cooper/Rucho/Alexander; Allen v. Milligan/Louisiana v. Callais).",
  "Exam hypothetical labels ('Shaw / Miller / Callais Analysis', ''Opposite Side'' Contrast); their text is reused in Examples 1 and 3.",
 ],
 "notes": [
  "Kept legacy item on Louisiana v. Callais (2026) and Examples 1 and 5 rely on Callais as described by Neon; it post-dates the drafter's reliable knowledge and must be verified.",
 ],
}

emit(__file__, FILL)
