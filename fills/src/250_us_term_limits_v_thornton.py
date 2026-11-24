"""Fill for 250_us_term_limits_v_thornton. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/514/779/"
FS = "Facts and Procedural History"
SO = "Concurring and Dissenting"
DS = "Doctrinal Significance"
PS = "Pedagogical Critiques"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Arkansas barred three-term Representatives and two-term Senators from its general-election ballot; a 5--4 Court held that the Constitution's qualifications for Congress are fixed and exclusive, so neither Congress nor a State may add term limits, whether directly or disguised as ballot-access rules---only an Article V amendment can (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="Ten days later, on November 13, 1992")],
  "Procedural History": [SEC(FS, frm="Ten days later, on November 13, 1992")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Supreme Court of Arkansas by a \textbf{5--4} vote. The case was argued on November 29, 1994, and decided on May 22, 1995 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/514/779}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Stevens delivered the opinion of the Court, joined by Justices Kennedy, Souter, Ginsburg, and Breyer.
    \item \textbf{Concurring Opinion:} Justice Kennedy filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Thomas filed a dissenting opinion, joined by Chief Justice Rehnquist and Justices O'Connor and Scalia.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Stevens)}"),
    SEC("Reasoning", to=r"\subsection{Reaffirming"),
    N(r"\subsubsection{Reaffirming \textit{Powell} and Rejecting Reserved State Power}"),
    SEC("Reasoning", frm="First, Stevens reaffirmed", to=r"\subsection{Ballot-Access"),
    N(r"\subsubsection{Ballot-Access Disguise and the Elections Clause}"),
    SEC("Reasoning", frm="Second, Stevens rejected"),
    N(r"\subsection{Concurring Opinion (Justice Kennedy)}"),
    SEC(SO, frm="Providing the decisive fifth vote", to=r"\subsection{Dissenting Opinion"),
    N(r"\subsection{Dissenting Opinion (Justice Thomas)}"),
    SEC(SO, frm="In a sweeping 80-page dissent"),
    N(r"\subsection{Subsequent Developments}"),
    SEC(DS, frm=r"\begin{itemize}", to="Through 2026, \\textit{Thornton} remains"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Unconstitutional): District Residency and a Tax-Return Ballot Label.}", glue=" "),
    S(r"Seeking to combat corruption and promote local accountability, State X amends its state constitution to (1) require every U.S. House candidate to reside inside the specific congressional district for at least two years before the election, and (2) print ``REFUSED TAX-RETURN DISCLOSURE'' beside the name of any congressional candidate who declines to release five years of federal tax returns. \textit{Analysis:} Both provisions are \textbf{unconstitutional} under \textit{Thornton} and \href{https://supreme.justia.com/cases/federal/us/531/510/}{\textit{Cook v. Gralike}, 531 U.S. 510 (2001)}. Article I, \S~2, cl. 2 requires only that a Representative be an inhabitant of the \textit{State} ``when elected''; State X cannot add a durational district-residency qualification. Likewise, printing a pejorative ballot label to coerce tax disclosure is not a neutral ``Manner'' regulation under Article I, \S~4, cl. 1, but an unconstitutional effort to handicap a class of federal candidates and dictate electoral outcomes."),
    N(r"\item \textbf{Same-Side (Unconstitutional): Congress Limits Its Own Members' Terms by Statute.} Responding to public pressure, Congress passes a statute providing that no person who has served six terms in the House or two terms in the Senate is eligible for election to that chamber again. A long-serving Representative sues to stay on the ballot. \textit{Thornton} reaffirmed \textit{Powell v.\ McCormack}'s holding that the Qualifications Clauses are exclusive and that Congress itself cannot add to them, and Stevens's opinion explained that any change to those qualifications must come through Article V. A statutory term limit is an added qualification for congressional service, so it is unconstitutional no matter which body enacts it (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Constitutional): State Term Limits, Resign-to-Run, and Neutral Ballot Rules.}", glue=" "),
    S(r"Now suppose State X instead (1) imposes a two-term limit on \textit{State X's own Governor and state legislators}, (2) enforces a ``resign-to-run'' rule requiring sitting state judges to resign their state office upon declaring candidacy for Congress, and (3) enacts a uniform ballot-access rule requiring any independent congressional candidate to submit signatures from 2 percent of registered voters in the district by June 1 and prohibiting sore-loser candidates who lost a party primary from appearing on the general-election ballot. All three measures are \textbf{constitutional}. Term limits on \textit{state} officials rest squarely within State X's reserved Tenth Amendment sovereignty; ``resign-to-run'' laws permissibly regulate \textit{state officeholders} rather than imposing a qualification on federal office (which Stevens expressly distinguished in \textit{Thornton}, 514 U.S. at 835 n. 48, citing \textit{Clements v. Fashing}, 457 U.S. 957 (1982)); and neutral signature thresholds and sore-loser rules are valid Elections Clause ``Manner'' regulations designed to prevent voter confusion and ballot overcrowding rather than to exclude a substantive class of federal candidates."),
    N(r"\item \textbf{Opposite-Side (Constitutional): A State Applies for an Article V Convention.} Frustrated by \textit{Thornton}, a state legislature adopts a resolution applying to Congress, under Article V, to call a convention for proposing a constitutional amendment imposing congressional term limits, and urges its congressional delegation to support such an amendment. Opponents argue that the State is again trying to impose term limits it may not adopt. Unlike Arkansas's Amendment 73, the resolution adds no qualification, keeps no candidate off the ballot, and does not handicap any class of candidates. It pursues precisely the route \textit{Thornton} identified as the only legitimate path to congressional term limits: amendment of the Constitution under Article V, in which the Constitution gives state legislatures an express role."),
    N(r"\item \textbf{Fence-Sitter (Neutral Information or a Handicap?): A Ballot Notation of Terms Served.} A State requires its ballots to list, beside each congressional incumbent's name, the number of terms the incumbent has served (for example, noting that a Representative is completing a sixth term). The notation is accurate and applies to every incumbent, and the State says it simply informs voters. But the measure was adopted by an initiative whose sponsors openly sought to promote congressional term limits, and the label may be designed to disadvantage long-serving incumbents. Under \textit{Thornton} and \textit{Cook v.\ Gralike}, a ballot rule is invalid if it is meant to handicap a class of candidates and dictate electoral outcomes, but neutral, factual ballot information is a familiar Elections Clause regulation. Whether this notation is the former or the latter is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"    \item \textbf{Competing Founding", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: consolidated case and docket numbers, lower-court citation, provisions line.",
  "Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection; Concurring and Dissenting subsection headings replaced by the standard subsection headings.",
  "Legacy section: introductory sentence and 'Through 2026' closing paragraph. Kept: Cook v. Gralike, Chiafalo v. Washington, Trump v. Anderson items.",
 ],
 "notes": [
  "Neon's 'Opposite Side' Contrast is a genuine fact pattern (three State X measures) and is reused whole as Example 3.",
 ],
}

emit(__file__, FILL)
