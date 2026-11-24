"""Fill for 189_crosby_v_nftc. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/530/363/"

def Q(quote, who, pin):
    # Attribution placed inside the quote block; tools/normalize_quotes.py then moves it to a
    # Group A "\noindent ---" line (check_brief.py does not match manual_quotes.txt's ".tex" names).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "),
            S(who, glue=""), N(",", glue=" "), S(pin, glue="\n"), N(r"\end{quote}")]

SOUTER = "Justice Souter, Majority Opinion"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"A unanimous Court held that Massachusetts's law barring state purchases from companies doing business with Burma was preempted under the Supremacy Clause because it obstructed the Federal Burma Act's grant of flexible presidential discretion, its calibrated sanctions, and its call for multilateral diplomacy (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to=r"\subsection{Litigation History}")],
  "Procedural History": [SEC("Facts and Procedural History", frm=r"\subsection{Litigation History}", strip=r"\subsection{Litigation History}")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{affirmed} the First Circuit, \textbf{9--0}, solely on statutory preemption grounds. The case was argued on March 22, 2000, and decided on June 19, 2000 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supct/html/99-474.ZO.html}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Souter delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices Stevens, O'Connor, Kennedy, Ginsburg, and Breyer.
    \item \textbf{Concurring Opinion:} Justice Scalia filed an opinion concurring in the judgment, joined by Justice Thomas.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Question Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Souter)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Judgment (Justice Scalia)}"),
    SEC("Concurring and Dissenting", frm="Justice Scalia agreed completely", to=r"\subsection{Dissenting Opinions}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"    \item \textbf{Subsequent Supreme Court Milestones:}", to=r"    \item \textbf{Congressional Overrides"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Preempted): A Broader, Unwaivable State Contracting Ban.}", glue=" "),
    S(r"Congress authorizes the President to ban new U.S.\ energy investment in Freedonia, subject to a national-security waiver. New York bars state agencies from contracting with \textit{any} domestic or foreign firm doing any business in Freedonia, without a waiver, sparking EU protests.", glue=" "),
    S(r"Preempted under \textit{Crosby}---the state spending defense fails, and the law blunts presidential waiver leverage, overrides Congress's calibrated scope, and impedes multilateral diplomacy."),
    N(r"\item \textbf{Same-Side (Preempted): A State Law Matching Federal Scope but Lacking the Waiver.} Congress bars U.S.\ persons from making new investments in a foreign country's mining sector and authorizes the President to waive the ban whenever he certifies that doing so serves national security. A State enacts a law imposing the same ban on the same class of persons and the same conduct, but with no waiver and no termination clause. The President later waives the federal ban as part of a negotiated agreement. Even though the state law tracks Congress's calibrated scope, it still conflicts with the first pillar of \textit{Crosby}: because it operates with no mechanism to yield to presidential waivers, it strips the President of control over the economic pressure Congress placed in his hands and reduces the value of his bargaining chips. The state law is preempted to the extent it outlasts the waiver."),
    N(r"\item \textbf{Opposite-Side (Survives): Congress Expressly Authorizes Matching State Divestment.}", glue=" "),
    S(r"Congress enacts a Freedonia Divestment Act expressly authorizing states to divest public pensions from firms on a Treasury defense list, provided state measures automatically sunset upon federal delisting or presidential waiver. Texas enacts a matching pension-divestment statute.", glue=" "),
    S(r"Upheld---express congressional authorization overcomes \textit{Crosby}, \textit{Zschernig}, and the dormant Foreign Commerce Clause, while automatic sunsetting and federal-list tracking preserve both presidential ``bargaining chips'' and congressional calibration."),
    N(r"\item \textbf{Opposite-Side (Crosby Inapplicable): A State Boycott With No Federal Statute in the Field.} A State bars its agencies from buying goods from companies that do business with a foreign country accused of human-rights abuses. Congress has enacted no sanctions statute concerning that country, and the President has issued no executive order or agreement addressing it. A trade association sues, relying on \textit{Crosby}. Obstacle preemption under \textit{Crosby} requires a federal statute whose purposes and objectives the state law frustrates; here there is no federal statute to obstruct, so \textit{Crosby}'s holding does not invalidate the law. The challengers must instead press the theories \textit{Crosby} expressly reserved, the dormant foreign affairs power under \textit{Zschernig v.\ Miller} and the dormant Foreign Commerce Clause, each of which raises open questions the Court did not decide."),
    N(r"\item \textbf{Fence-Sitter (Close Call): A State Pension Divestment Law That Tracks the Federal List Without Congressional Authorization.} Congress imposes sanctions on a foreign country's defense firms and lets the President add or remove firms from a Treasury list, but says nothing about state measures. A State requires its pension funds to divest from firms on the Treasury list and to reinvest automatically when a firm is delisted. For the State: unlike Massachusetts's law, its statute adds no new targets, follows every federal designation, and expires when federal sanctions do, preserving the President's bargaining chips and Congress's calibration. For the challengers: the State still adds economic pressure Congress did not impose, foreign governments may protest, and \textit{Crosby} held that congressional silence is ambiguous rather than permission. Whether a court treats close federal tracking as eliminating any obstacle is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"    \item \textbf{Market-Participant", to=r"\end{itemize}")],
  "Key Quotations":
    Q(r"``We find that the state law undermines the intended purpose and `natural effect' of at least three provisions of the federal Act, that is, its delegation of effective discretion to the President to control economic sanctions against Burma, its limitation of sanctions solely to United States persons and new investment, and its directive to the President to proceed diplomatically in developing a comprehensive, multilateral strategy towards Burma.''",
      SOUTER, r"530 U.S.\ at 373--374 (\href{https://caselaw.findlaw.com/court/us-supreme-court/530/363.html}{FindLaw} / \href{https://www.law.cornell.edu/supct/html/99-474.ZO.html}{Cornell LII}).")
    + Q(r"``Within the sphere defined by Congress, then, the statute has placed the President in a position with as much discretion to exercise economic leverage against Burma, with an eye toward national security, as our law will admit. And it is just this plenitude of Executive authority that we think controls the issue of preemption here. The President has been given this authority not merely to make a political statement but to achieve a political result, and the fullness of his authority shows the importance in the congressional mind of reaching that result. It is simply implausible that Congress would have gone to such lengths to empower the President if it had been willing to compromise his effectiveness by deference to every provision of state statute or local ordinance that might, if enforced, blunt the consequences of discretionary Presidential action. \dots\ Quite simply, if the Massachusetts law is enforceable the President has less to offer and less economic and diplomatic leverage as a consequence. In \textit{Dames \& Moore v.\ Regan}, 453 U.S.\ 654 (1981), we used the metaphor of the bargaining chip to describe the President's control of funds valuable to a hostile country, \textit{id.}, at 673; here, the state Act reduces the value of the chips created by the federal statute.''",
      SOUTER, r"530 U.S.\ at 375--377 (\href{https://caselaw.findlaw.com/court/us-supreme-court/530/363.html}{FindLaw} / \href{https://supreme.justia.com/cases/federal/us/530/363/}{Justia}).")
    + Q(r"``The fact of a common end hardly neutralizes conflicting means, see \textit{Gade v.\ National Solid Wastes Management Assn.}, 505 U.S.\ 88, 103 (1992), and the fact that some companies may be able to comply with both sets of sanctions does not mean that the state Act is not at odds with achievement of the federal decision about the right degree of pressure to employ. \dots\ Sanctions are drawn not only to bar what they prohibit but to allow what they permit, and the inconsistency of sanctions here undermines the congressional calibration of force.''",
      SOUTER, r"530 U.S.\ at 379--380 (\href{https://supreme.justia.com/cases/federal/us/530/363/}{Justia}).")
    + Q(r"``A failure to provide for preemption expressly may reflect nothing more than the settled character of implied preemption doctrine that courts will dependably apply, and in any event, the existence of conflict cognizable under the Supremacy Clause does not depend on express congressional recognition that federal and state law may conflict, \textit{Hines}, 312 U.S., at 67. The State's inference of congressional intent is unwarranted here, therefore, simply because the silence of Congress is ambiguous.''",
      SOUTER, r"530 U.S.\ at 387--388 (\href{https://www.law.cornell.edu/supct/html/99-474.ZO.html}{Cornell LII}).")
    + Q(r"``The only reliable indication of that intent---the only thing we know for sure can be attributed to all of them---is the words of the bill that they voted to make law. In a way, using unreliable legislative history to confirm what the statute plainly says anyway (or what the record plainly shows) is less objectionable since, after all, it has absolutely no effect upon the outcome. But in a way, this utter lack of necessity makes it even worse---calling to mind St.\ Augustine's enormous remorse at stealing pears when he was not even hungry, and just for the devil of it (`not seeking aught through the shame, but the shame itself!').''",
      "Justice Scalia, Concurring in the Judgment", r"530 U.S.\ at 390--391 (\href{https://www.law.cornell.edu/supct/html/99-474.ZC.html}{Cornell LII})."),
 },
 "dropped": [
  "Case Metadata: full case name, docket number, lower-court citations, caption-change note (lower-court history is in Procedural History), LaTeX comment header.",
  "Concurring and Dissenting Opinions: 'Dissenting Opinions -- None' subsection (stated in Judicial Votes).",
  "Legacy section: introductory paragraph; 'Congressional Overrides and Narrower State Laws' item (lower-court and statutory responses, not Supreme Court decisions on Crosby's holding); 'Textualist Pushback and 2025--2026 Frontiers' item (general obstacle-preemption cases, Shen v. Simpson, climate-tort commentary). Kept: Garamendi / Arizona / Zivotofsky item.",
  "Key Quotations: the bold topic labels on each list item (the Justice/opinion part of each label is kept as the attribution).",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all five quotations kept, none added. Attributions are emitted inside each quote block and converted by normalize_quotes.py because check_brief.py compares stems against manual_quotes.txt entries that end in .tex."],
}

emit(__file__, FILL)
