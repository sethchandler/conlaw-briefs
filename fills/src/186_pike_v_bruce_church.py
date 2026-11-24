"""Fill for 186_pike_v_bruce_church. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/397/137/"
FS = "Facts and Procedural History"
RS = "Reasoning"
PS = "Pedagogical Critiques"
CITE = r"(\href{https://supreme.justia.com/cases/federal/us/397/137/}{397 U.S. at %s}; \href{https://www.law.cornell.edu/supremecourt/text/397/137}{Cornell LII})"

def Q(text, pin):
    # Attribution is placed inside the quote block (Group B form) so that
    # tools/normalize_quotes.py converts it to Group A form; see notes.
    return [N(r"\begin{quote}", glue="\n"), S(text, glue="\n"),
            N(r"--- Justice Stewart", glue=" "), S(CITE % pin, glue=""), N(".", glue="\n"),
            N(r"\end{quote}")]

QUOTES = (
  Q(r"``Although the criteria for determining the validity of state statutes affecting interstate commerce have been variously stated, the general rule that emerges can be phrased as follows: where the statute regulates evenhandedly to effectuate a legitimate local public interest, and its effects on interstate commerce are only incidental, it will be upheld unless the burden imposed on such commerce is clearly excessive in relation to the putative local benefits. \textit{Huron Cement Co. v. Detroit}, 362 U. S. 440, 362 U. S. 443. If a legitimate local purpose is found, then the question becomes one of degree. And the extent of the burden that will be tolerated will, of course, depend on the nature of the local interest involved, and on whether it could be promoted as well with a lesser impact on interstate activities.''", "142")
  + Q(r"``The appellant's order would forbid the company to pack its cantaloupes outside Arizona not for the purpose of keeping the reputation of its growers unsullied, but to enhance their reputation through the reflected good will of the company's superior produce. The appellant, in other words, is not complaining because the company is putting the good name of Arizona on an inferior or deceptively packaged product, but because it is not putting that name on a product that is superior and well packaged.''", "144")
  + Q(r"``The nature of that burden is, constitutionally, more significant than its extent. For the Court has viewed with particular suspicion state statutes requiring business operations to be performed in the home State that could more efficiently be performed elsewhere. Even where the State is pursuing a clearly legitimate local interest, this particular burden on commerce has been declared to be virtually per se illegal.''", "145")
  + Q(r"``While the order issued under the Arizona statute does not impose such rigidity on an entire industry, it does impose just such a straitjacket on the appellee company with respect to the allocation of its interstate resources. Such an incidental consequence of a regulatory scheme could perhaps be tolerated if a more compelling state interest were involved. But here, the State's interest is minimal, at best -- certainly less substantial than a State's interest in securing employment for its people. If the Commerce Clause forbids a State to require work to be done within its jurisdiction to promote local employment, then surely it cannot permit a State to require a person to go into a local packing business solely for the sake of enhancing the reputation of other producers within its borders.''", "146")
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Arizona ordered a grower to pack its premium Parker cantaloupes in Arizona rather than in its California sheds 31 miles away, so the melons would carry Arizona's name; a unanimous Court struck the order under the \textit{Pike} balancing test, which invalidates evenhanded laws whose burden on interstate commerce is clearly excessive in relation to their putative local benefits (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to=r"\subsection{Procedural History}", strip=r"\subsection{Factual Background}")],
  "Procedural History": [SEC(FS, frm=r"\subsection{Procedural History}", strip=r"\subsection{Procedural History}")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{affirmed} the three-judge District Court's permanent injunction, \textbf{8--0}, on direct appeal. The case was argued on January 13, 1970, and decided on March 2, 1970 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/397/137}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Stewart delivered the opinion of the Court, joined by Chief Justice Burger and Justices Black, Douglas, Harlan, Brennan, White, and Marshall.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
    S(r"8--0 (unanimous; one vacancy existed between Justice Abe Fortas's resignation and Justice Harry Blackmun's appointment)"),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Stewart)}"),
    N(r"\subsubsection{Threshold Rejection of the ``Intrastate Preparation'' Defense}"),
    SEC(RS, frm="Justice Stewart rejected", to=r"\subsection{The \textit{Pike} Balancing"),
    N(r"\subsubsection{The \textit{Pike} Balancing Framework}"),
    SEC(RS, frm="Synthesizing", to=r"\subsection{Minimal Local"),
    N(r"\subsubsection{Minimal Local Interest vs. Forced In-State Operations}"),
    SEC(RS, frm="While Arizona's 1929 Act"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"), N(r"\item \textbf{\textit{National Pork Producers Council v.\ Ross} (2023):}", glue=" "),
    SEC("Doctrinal Significance", frm=r"In \href{https://www.law.cornell.edu/supremecourt/text/21-468}", to="Through 2026, lower courts"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Pike Violated): Forced In-State Data Servers.}", glue=" "),
    S(r"State A requires all locally grown spinach to be logged on physical servers inside State A before interstate shipment to aid health inspections, forcing a border grower to build a redundant \$450,000 in-state data center despite instantaneous remote access from its State B facility. Even post-\href{https://www.law.cornell.edu/supremecourt/text/21-468}{\textit{Ross}}, mandating local operations when remote access achieves the same goal fails \textit{Pike}."),
    N(r"\item \textbf{Same-Side (Pike Violated): Requiring Shrimp to Be Processed In-State.} A coastal State requires that shrimp caught in its waters be peeled and the heads and hulls removed at in-state plants before the shrimp may be shipped out of state, asserting an interest in conserving the shell waste as fertilizer. A packing company with efficient processing plants just across the border challenges the law. Like Arizona's order, the law requires an operation that could be performed more efficiently elsewhere to be performed at home---the burden \textit{Pike} called virtually per se illegal. \textit{Pike} relied on \textit{Foster-Fountain Packing Co.\ v.\ Haydel}, 278 U.S.\ 1 (1928), which held the challenge to a materially identical Louisiana shrimp law sufficient and reversed the denial of an interlocutory injunction, and the State's interest could be served with far less impact on interstate activity."),
    N(r"\item \textbf{Opposite-Side (State Prevails): A Neutral Packaging Ban.}", glue=" "),
    S(r"State C bans retail sale of produce in single-use polystyrene clamshells to curb landfill waste, applying identically to in-state and out-of-state growers with no local-packing mandate. An out-of-state grower faces \$1.2 million in retooling costs. Under \href{https://supreme.justia.com/cases/federal/us/449/456/}{\textit{Clover Leaf Creamery}}, \href{https://supreme.justia.com/cases/federal/us/437/117/}{\textit{Exxon}}, and \href{https://www.law.cornell.edu/supremecourt/text/21-468}{\textit{Ross}}, State C wins: there is no forced in-state processing, firm-level retooling is merely a shift in ``methods of operation,'' and the environmental benefit is substantial."),
    N(r"\item \textbf{Opposite-Side (State Prevails): A City Smoke-Abatement Ordinance Applied to Ships.} A port city's air-pollution ordinance limits the density of smoke that any furnace or boiler within city limits may emit, and the city applies it to the boilers of a cargo vessel docked there while loading goods for interstate voyages. The shipowner must refit its boilers and argues that the ordinance burdens interstate commerce. The ordinance regulates evenhandedly, serves a legitimate local health interest, and has only incidental effects on commerce; it requires no operation to be relocated in-state. That is the pattern \textit{Pike} cited from \href{https://supreme.justia.com/cases/federal/us/362/440/}{\textit{Huron Portland Cement Co.\ v.\ Detroit}, 362 U.S.\ 440 (1960)}, which upheld exactly such an ordinance, and the burden is not clearly excessive in relation to the benefit."),
    N(r"\item \textbf{Fence-Sitter (Close Call After \textit{Ross}): A Sales Ban on Milk From Hormone-Treated Cows.} State D bans the in-state sale of milk from cows treated with a federally approved growth hormone, citing contested health concerns and consumer preference. The rule applies equally to in-state dairies, but because most of the State's milk comes from out-of-state cooperatives, they must build segregated supply chains at a cost of hundreds of millions of dollars. No forced in-state processing is involved, so the case turns on balancing. Under \textit{Ross}, three Justices declined to balance economic costs against the particular moral interest in animal welfare asserted there, four found that comparable compliance costs did not plausibly allege a substantial burden on the interstate market, and others would apply \textit{Pike} balancing to an industry-wide burden. With the Court so divided, the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"  \item \textbf{Hidden", to=r"\end{enumerate}")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "Case Metadata: full caption, parallel S. Ct. citation, docket number, jurisdictional statute line, Chapter line, provision line.",
  "Concurring and Dissenting Opinions section ('None ...'): restated in Judicial Votes.",
  "Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection.",
  "Legacy section: 'Two-Tier Framework and Pre-2023 Evolution' survey (Philadelphia, Exxon, Clover Leaf, Kassel, Edgar, Bendix, Davis) and the 'Through 2026' lower-court paragraph (Triumph Foods, Feldon). Kept: National Pork Producers Council v. Ross.",
  "Key Quotations: the four bold quotation labels (e.g. 'The Canonical Pike Balancing Test') dropped; every quote and its pin cite kept.",
 ],
 "notes": ["tools/check_brief.py compares stems against tools/manual_quotes.txt, whose entries carry a .tex suffix, so listed briefs are still sent through normalize_quotes.py (which rejects hand-built Group A quotes as 'already Group A style'). Each quote is therefore rebuilt with its attribution inside the quote block so the normalizer produces the Group A form; the final output is the same."],
}

emit(__file__, FILL)
