"""Fill for 182_united_states_v_butler. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/297/1/"

def Q(label_attrib, quote):
    # Attribution inside the quote block; tools/normalize_quotes.py moves it to a Group A
    # "\noindent ---" line (check_brief.py runs it on every brief, so a pre-built Group A line would be rejected).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "), S(label_attrib, glue="\n"),
            N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Striking down the Agricultural Adjustment Act's processing tax 6--3, the Court adopted Hamilton's view that the Spending Clause confers an independent power to tax and spend for the general welfare, yet held that Congress may not use that power to coerce or purchase compliance with regulation of local agricultural production reserved to the states (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The United States subsequently presented")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The United States subsequently presented")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the First Circuit by a \textbf{6--3} vote. The case was argued on December 9--10, 1935, and decided on January 6, 1936 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/297/1}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Roberts delivered the opinion of the Court, joined by Chief Justice Hughes and Justices Van Devanter, McReynolds, Sutherland, and Butler.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinion:} Justice Stone filed a dissenting opinion, joined by Justices Brandeis and Cardozo.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Stone)}"),
    SEC("Concurring and Dissenting", frm="Justice Stone authored"),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Contract-Analogy"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Condition Invalid): Clawing Back Existing Funds to Force a Runoff Cap.}", glue=" "),
    S(r"Suppose Congress enacts the ``National Soil Conservation and Carbon Reduction Act,'' imposing a 2\% federal excise tax on all commercial fertilizer sales (deposited into the general Treasury) and simultaneously establishing a \$15 billion annual grant program offering states federal agricultural-extension grants conditioned on each state enacting a statutory cap on nitrogen runoff from local farms. If a state declines to enact the cap, it forfeits 100\% of its existing federal Medicaid and highway funding (totaling 18\% of the state's annual budget).", glue=" "),
    S(r"Under \textit{Butler}'s Hamiltonian holding and \textit{Helvering}, Congress may spend for national environmental and agricultural welfare even if local farming practices were beyond another enumerated power (and depositing the excise tax into the general Treasury avoids \textit{Butler}'s earmarking/standing pitfall). However, the funding condition fails both \textit{Dole} and \textit{NFIB}: (a) tying a fertilizer/nitrogen-runoff cap to \textit{Medicaid} funding fails \textit{Dole}'s relatedness requirement; and (b) threatening 18\% of a state's entire budget by clawing back massive, pre-existing programs is ``economic dragooning'' and ``a gun to the head'' under \textit{NFIB} (echoing \textit{Butler}'s coercion rationale)."),
    N(r"\item \textbf{Same-Side (Standing to Challenge the Whole Scheme): An Earmarked Fee That Funds Production Payments.} Congress imposes a per-ton fee on dairy processors, deposits the proceeds in a special fund, and directs the Secretary of Agriculture to use the fund only to pay dairy farmers who agree to cut milk output. A processor refuses to pay and argues that the payment program is unconstitutional. The Government responds that, under \textit{Massachusetts v.\ Mellon}, a payer has no standing to object to how federal money is spent. Under \textit{Butler}'s standing holding, that defense fails: the fee is earmarked, rises and falls with the payment program, and is an integral part of a single regulatory plan, so the processor may challenge the validity of the entire scheme. (The merits would now be judged under modern Commerce and Spending Clause doctrine rather than \textit{Butler}'s reserved-powers bar.)"),
    N(r"\item \textbf{Opposite-Side (Condition Valid): A New, Optional, Germane Grant.}", glue=" "),
    S(r"Now modify Hypothetical 1 on the \textbf{opposite side} of the doctrinal line: Congress instead offers states a brand-new \$2 billion federal ``Clean Waterways Grant'' specifically to fund state agricultural-extension monitoring of nitrogen runoff. Participation is entirely optional; states that decline lose only the new \$2 billion grant (less than 0.3\% of any state's budget), while states that accept receive unambiguous statutory notice of the monitoring rules.", glue=" "),
    S(r"On the \textit{programmatic condition} itself, Congress wins cleanly under \textit{Butler}'s Hamiltonian holding, Stone's dissent, \textit{Dole}, and \textit{NFIB}: the condition is unambiguous, directly germane to the new grant's purpose, and involves no threat to existing funds (pure ``hope of gain,'' not ``threat of loss'')."),
    N(r"\item \textbf{Opposite-Side (Spending Upheld): Direct Payments for a National Purpose Outside Other Enumerated Powers.} Congress appropriates money from the general Treasury to pay monthly stipends to individuals who complete apprenticeship training, finding that a national shortage of skilled workers depresses the economy as a whole. A taxpayer objects that job training is not within any enumerated power. \textit{Butler} itself defeats the objection: the Court adopted the Hamiltonian view that the power to spend for the general welfare is not limited by the other direct grants of legislative power. Because the payments impose no regulation on states and the revenue is not earmarked from a particular group, the program falls within the line of \href{https://supreme.justia.com/cases/federal/us/301/619/}{\textit{Helvering v.\ Davis}, 301 U.S.\ 619 (1937)}, which defers to Congress's judgment of the general welfare unless it is plainly arbitrary."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Withholding a Larger Share of Existing Highway Funds.} Congress provides that any state that does not adopt a federally specified distracted-driving law will lose 25 percent of its existing federal highway funds, an amount equal to about 2 percent of a typical state's budget. The condition is unambiguous and related to the purpose of highway spending, so it satisfies \textit{Dole}'s notice and relatedness requirements. The hard question is coercion, the principle \textit{Butler} first announced. The penalty is far larger than the 5 percent of highway funds upheld in \href{https://supreme.justia.com/cases/federal/us/483/203/}{\textit{South Dakota v.\ Dole}, 483 U.S.\ 203 (1987)}, but far smaller than the loss of all Medicaid funds held coercive in \href{https://supreme.justia.com/cases/federal/us/567/519/}{\textit{NFIB v.\ Sebelius}, 567 U.S.\ 519 (2012)}. Because \textit{NFIB} declined to fix where pressure turns into compulsion, the result is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{``Slot-Machine", to=r"\end{enumerate}")],
  "Key Quotations": (
    Q(r"Roberts, J., 297 U.S.\ at 62", r"``When an act of Congress is appropriately challenged in the courts as not conforming to the constitutional mandate, the judicial branch of the Government has only one duty---to lay the article of the Constitution which is invoked beside the statute which is challenged and to decide whether the latter squares with the former.''")
    + Q(r"Roberts, J., 297 U.S.\ at 66", r"``While, therefore, the power to tax is not unlimited, its confines are set in the clause which confers it, and not in those of \S\ 8 which bestow and define the legislative powers of the Congress. It results that the power of Congress to authorize expenditure of public moneys for public purposes is not limited by the direct grants of legislative power found in the Constitution.''")
    + Q(r"Roberts, J., 297 U.S.\ at 71, 73", r"``The power to confer or withhold unlimited benefits is the power to coerce or destroy. \dots\ This is coercion by economic pressure. The asserted power of choice is illusory. \dots\ The Congress cannot invade state jurisdiction to compel individual action; no more can it purchase such action.''")
    + Q(r"Stone, J., dissenting, 297 U.S.\ at 78--79", r"``The power of courts to declare a statute unconstitutional is subject to two guiding principles of decision which ought never to be absent from judicial consciousness. One is that courts are concerned only with the power to enact statutes, not with their wisdom. The other is that, while unconstitutional exercise of power by the executive and legislative branches of the government is subject to judicial restraint, the only check upon our own exercise of power is our own sense of self-restraint. For the removal of unwise laws from the statute books appeal lies not to the courts, but to the ballot and to the processes of democratic government.''")
    + Q(r"Stone, J., dissenting, 297 U.S.\ at 81, 85", r"``Threat of loss, not hope of gain, is the essence of economic coercion. \dots\ It is a contradiction in terms to say that there is power to spend for the national welfare while rejecting any power to impose conditions reasonably adapted to the attainment of the end which alone would justify the expenditure.''")
  ),
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, duplicate source-link line (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory paragraph ('through 2026' framing); 'Contract-Analogy Tightening Through 2025--2026' item (Medina v. Planned Parenthood, Landor v. Louisiana, CRS report) - concerns Spending Clause remedies rather than Butler's holding. Kept: 1937 Revolution (Steward Machine / Helvering), South Dakota v. Dole, NFIB v. Sebelius.",
  "Key Quotations: the bold topical labels before each quotation (only the attribution part of each label is moved).",
  "Exam Hypothetical 2: its personal-capacity damages twist and the Landor-based analysis of it (depends on a 2026 decision that could not be verified); the fact pattern's optional-grant portion and the programmatic-condition analysis are reused in Example 3. Hypothetical headings dropped.",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all five kept, none added. Attributions are emitted inside each quote block so normalize_quotes.py converts them (check_brief.py runs it on every brief)."],
}

emit(__file__, FILL)
