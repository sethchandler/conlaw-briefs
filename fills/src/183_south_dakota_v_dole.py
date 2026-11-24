"""Fill for 183_south_dakota_v_dole. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/483/203/"
JH = r"\href{https://supreme.justia.com/cases/federal/us/483/203/}"

def Q(quote, attrib):
    # Attribution placed inside the quote block; tools/normalize_quotes.py moves it to a
    # Group A "\noindent ---" line (check_brief.py does not match manual_quotes.txt's ".tex" names).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "), S(attrib, glue="\n"),
            N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Upholding 7--2 a federal law withholding 5\% of highway funds from States with a drinking age under 21, the Court set the test for conditional spending: conditions must serve the general welfare, be unambiguous, relate to the federal interest, violate no independent constitutional bar, and not coerce (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Facing the loss of 5\\%")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Facing the loss of 5\\%")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Eighth Circuit by a \textbf{7--2} vote. The case was argued on April 28, 1987, and decided on June 23, 1987 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Rehnquist delivered the opinion of the Court, joined by Justices White, Marshall, Blackmun, Powell, Stevens, and Scalia.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Brennan filed a dissenting opinion (483 U.S. at 212). Justice O'Connor filed a dissenting opinion (483 U.S. at 212--218).
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Rehnquist)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Brennan)}"),
    SEC("Concurring and Dissenting", frm="In a concise", to=r"\subsection{Justice O'Connor"),
    N(r"\subsection{Dissenting Opinion (Justice O'Connor)}"),
    SEC("Concurring and Dissenting", frm="Justice O'Connor accepted"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Anti-Coercion Given", to=r"  \item \textbf{The ``Contract Analogy"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Condition Valid): New EV-Corridor Grants with a Building-Code Condition.}", glue=" "),
    S(r"Congress creates a new \$10 billion Federal EV Corridor Grant Program. Participating states must (1) spend the funds exclusively on public fast-charging stations along interstate highways and (2) require EV-ready wiring in newly constructed commercial parking garages. Nonparticipating states forgo only the new grant and lose zero existing highway funds.", glue=" "),
    S(r"It pursues the general welfare, gives clear prospective notice, relates directly to interstate EV transportation (valid under \textit{Dole}'s majority even though requirement (2) regulates building codes), induces no unconstitutional conduct, and avoids coercion by risking no pre-existing funds."),
    N(r"\item \textbf{Same-Side (Condition Valid): A Blood-Alcohol Limit Tied to Highway Funds.} Suppose Congress directs the Secretary of Transportation to withhold 5\% of specified federal highway funds from any State that does not adopt a 0.08 blood-alcohol limit for drunk-driving offenses. The statute states the condition plainly, and it is even more tightly related to the federal interest in safe interstate travel than the drinking-age condition in \textit{Dole}, because it regulates driving itself. A State may constitutionally adopt such a limit, so there is no independent constitutional bar, and the amount at stake is the same ``relatively mild encouragement'' the Court approved. Under \textit{Dole}'s test the condition is valid even if Congress could not impose the limit directly (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Condition Invalid): Threatening All Existing Education Funds.}", glue=" "),
    S(r"Congress enacts the \textit{Safe Campuses Act}, directing the Secretary of Education to withhold 100\% of a state's existing federal K--12 Title I funding (8\% of the average state's total operating budget) unless the state enacts a criminal ban on all firearm possession within 1,000 feet of any public university campus and directs state police to enforce it.", glue=" "),
    S(r"Unconstitutional under \href{https://supreme.justia.com/cases/federal/us/567/519/}{\textit{NFIB v. Sebelius}, 567 U.S. 519 (2012)}. Threatening 100\% of an existing funding stream totaling 8\% of a state's budget is a ``gun to the head,'' far beyond \textit{Dole}'s 5\% highway cut (less than 0.5\% of South Dakota's budget).", glue=" "),
    N(r"Relatedness is also doubtful:", glue=" "),
    S(r"Arguably satisfied under Chief Justice Rehnquist's deferential standard (campus safety relates to education funding), but vulnerable under Justice O'Connor's dissent because it regulates criminal law around \textit{universities} using \textit{K--12} funding rather than specifying how Title I funds are spent."),
    N(r"\item \textbf{Opposite-Side (Condition Invalid): Inducing Racial Discrimination.} Congress offers a modest new grant to state university systems on the condition that each participating university reserve a fixed number of admission seats for applicants of a single race. The grant is small and optional, so there is no coercion problem, and the condition is related to the federal interest in higher education. It fails anyway under \textit{Dole}'s fourth prong: the independent-constitutional-bar limit forbids Congress from using federal funds ``to induce the States to engage in activities that would themselves be unconstitutional,'' and the Court named invidious racial discrimination as its example. Because a State could not itself adopt a racial quota consistent with the Equal Protection Clause, Congress cannot pay it to do so."),
    N(r"\item \textbf{Fence-Sitter (Close Call): A 25\% Education-Fund Condition.} Congress amends an existing federal K--12 grant program to withhold 25\% of each State's existing funds unless the State bans student cell phones during the school day in all public schools. The condition is clear, plausibly serves the general welfare, and relates to the program's educational purpose, and a phone ban violates no one's constitutional rights. The difficulty is coercion. The threatened amount is far larger than the 5\% highway cut in \textit{Dole} but smaller than the loss of all Medicaid funds in \textit{NFIB}, and it attaches to pre-existing funds rather than a new program. Neither decision supplies a metric for the space between them, so whether this is ``relatively mild encouragement'' or ``a gun to the head'' is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{The ``Trojan Horse''", to=r"\end{enumerate}")],
  "Key Quotations":
    Q(r"``Thus, objectives not thought to be within Article I's `enumerated legislative fields,' \textit{id.} at 297 U. S. 65, may nevertheless be attained through the use of the spending power and the conditional grant of federal funds.''", r"Rehnquist, C.J., " + JH + r"{483 U.S. at 207}")
    + Q(r"``These cases establish that the `independent constitutional bar' limitation on the spending power is not, as petitioner suggests, a prohibition on the indirect achievement of objectives which Congress is not empowered to achieve directly. Instead, we think that the language in our earlier opinions stands for the unexceptionable proposition that the power may not be used to induce the States to engage in activities that would themselves be unconstitutional.''", r"Rehnquist, C.J., " + JH + r"{483 U.S. at 210}")
    + Q(r"``Our decisions have recognized that, in some circumstances, the financial inducement offered by Congress might be so coercive as to pass the point at which `pressure turns into compulsion.' . . . Here Congress has offered relatively mild encouragement to the States to enact higher minimum drinking ages than they would otherwise choose. But the enactment of such laws remains the prerogative of the States not merely in theory, but in fact.''", r"Rehnquist, C.J., " + JH + r"{483 U.S. at 211--212}")
    + Q(r"``When Congress appropriates money to build a highway, it is entitled to insist that the highway be a safe one. But it is not entitled to insist as a condition of the use of highway funds that the State impose or change regulations in other areas of the State's social and economic life because of an attenuated or tangential relationship to highway use or safety. . . . Rather than a condition determining how federal highway money shall be expended, it is a regulation determining who shall be able to drink liquor. As such, it is not justified by the spending power.''", r"O'Connor, J., dissenting, " + JH + r"{483 U.S. at 215, 218}")
    + Q(r"``Since States possess this constitutional power, Congress cannot condition a federal grant in a manner that abridges this right. The Amendment, itself, strikes the proper balance between federal and state authority.''", r"Brennan, J., dissenting, " + JH + r"{483 U.S. at 212}"),
 },
 "dropped": [
  "Case Metadata: docket number, LOC PDF link, court-below link, provisions/statutes/topic lines, file comments (Justia link kept in Judicial Votes).",
  "Legacy section: introductory paragraph; 'Contract Analogy' item (Cummings, Talevski, Medina, Landor - remedies and Section 1983 enforceability under Spending Clause statutes, not applications of Dole's holding); 'Executive-Imposed Grant Conditions' item (pending lower-court litigation). Kept: NFIB v. Sebelius and American Library Ass'n / Sabri items.",
  "Key Quotations: the bold topic labels before each quote (attributions kept).",
  "Exam Hypothetical 1: General Welfare & Clear Notice and Independent Constitutional Bar roadmap bullets (Second Amendment point is speculative); Exam Hypothetical 2: Statute B (relies on Landor (2026) and repeats the coercion point of Example 3) and headings.",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all five kept, none added. Attributions are emitted inside each quote block and converted by normalize_quotes.py, as in 181_missouri_v_holland, because check_brief.py never matches manual_quotes.txt's '.tex' entries.",
           "Examples 2, 4, and 5 are new hypotheticals; Example 2 is framed as a hypothetical rather than a description of any actual federal statute."],
}

emit(__file__, FILL)
