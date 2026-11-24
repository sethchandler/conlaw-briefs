"""Fill for 255_kelo_v_city_of_new_london. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/545/469/"
JL = r" (\href{https://supreme.justia.com/cases/federal/us/545/469/}{Justia})"

def Q(quote, attrib):
    # Attribution placed inside the quote block; tools/normalize_quotes.py moves it to a
    # Group A "\noindent ---" line (check_brief.py does not match manual_quotes.txt's ".tex" names).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "), S(attrib, glue="\n"),
            N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Upholding 5--4 New London's condemnation of unblighted homes for a comprehensive economic-development plan, the Court held that promoting economic development is a ``public purpose'' satisfying the Takings Clause's public-use requirement under deferential review, while leaving States free to impose stricter limits (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="In December 2000, the homeowners sued")],
  "Procedural History": [SEC("Facts and Procedural History", frm="In December 2000, the homeowners sued")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Connecticut Supreme Court by a \textbf{5--4} vote. The case was argued on February 22, 2005, and decided on June 23, 2005 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Stevens delivered the opinion of the Court, joined by Justices Kennedy, Souter, Ginsburg, and Breyer.
    \item \textbf{Concurring Opinion:} Justice Kennedy filed a concurring opinion.
    \item \textbf{Dissenting Opinions:} Justice O'Connor filed a dissenting opinion, joined by Chief Justice Rehnquist and Justices Scalia and Thomas. Justice Thomas filed a separate dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Question Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Stevens)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Kennedy)}"),
    SEC("Concurring and Dissenting", frm="Joining the majority in full", to=r"  \item \textbf{Justice O'Connor"),
    N(r"\subsection{Dissenting Opinion (Justice O'Connor)}"),
    SEC("Concurring and Dissenting", frm="O'Connor warned", to=r"  \item \textbf{Justice Thomas"),
    N(r"\subsection{Dissenting Opinion (Justice Thomas)}"),
    SEC("Concurring and Dissenting", frm="Joining O'Connor's dissent", to=r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Taking Valid): A Regional Industrial-Park Plan.} After its largest factory closes, a county adopts, following two years of studies and public hearings, a comprehensive plan to redevelop 200 acres into an industrial park. Developers and tenants will be chosen later through competitive bidding. Most owners sell, but several owners of well-kept, unblighted farmhouses refuse, and the county condemns their land. Under \textit{Kelo}, job creation and an expanded tax base are a legitimate public purpose, the plan is judged as a whole rather than lot by lot, and no particular private beneficiary was identified in advance. Courts will not second-guess whether the projected benefits will materialize, so the takings satisfy the Public Use Clause (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Taking Valid): Land for a Common-Carrier Rail Line.} A State authorizes a privately owned railroad, regulated as a common carrier that must serve all shippers on equal terms, to condemn a strip of farmland for a new freight line. The landowner objects that the property is being transferred to a private company. \textit{Kelo} confirms this is an easy case: even before reaching the broader ``public purpose'' test, the Court treated transfers to a private common carrier whose services are open to the public as a settled example of public use. With just compensation paid, the taking is valid."),
    N(r"\item \textbf{Opposite-Side (Taking Likely Invalid): A One-Parcel Transfer to a Disappointed Buyer.}", glue=" "),
    S(r"Without any prior city-wide redevelopment study, a prosperous suburb receives a proposal from MegaTech Corp.\ to build a corporate campus if the city acquires an adjacent, profitable family-owned nursery whose owner refused MegaTech's private purchase offer. Two weeks later, the city council passes a one-parcel ``economic revitalization'' resolution condemning the nursery for immediate transfer to MegaTech, citing projected property-tax increases. The nursery owner sues under the Fifth Amendment's Public Use Clause (assume no stricter state-law bar).", glue=" "),
    S(r"Unlike New London's multi-year, 90-acre integrated plan in a distressed city where most private tenants were initially unknown, this is an isolated, one-to-one transfer ($A$ to $B$) initiated \textit{after} a specific private beneficiary failed to buy the land on the open market, with no comprehensive plan and rushed procedures. Under Stevens's ``mere pretext'' prohibition (545 U.S.\ at 478, 487) and Kennedy's meaningful rational-basis concurrence (545 U.S.\ at 491--493), a court should invalidate the taking as an unconstitutional private-benefit transfer---and preserve an alternative argument to overrule \textit{Kelo} under Justice Thomas's originalist ``actual public use'' standard."),
    N(r"\item \textbf{Opposite-Side (Taking Barred by State Law): A State Constitutional Amendment.} A city adopts a plan just like New London's and condemns unblighted homes for private office and retail development. The State's constitution, however, has been amended to forbid takings for transfer to private entities for the primary purpose of economic development or increased tax revenue. The owners sue in state court under the state constitution. The taking would satisfy the federal Public Use Clause under \textit{Kelo}, but \textit{Kelo} sets only a floor: the Court stressed that ``nothing in our opinion precludes any State from placing further restrictions on its exercise of the takings power.'' The state-law bar controls, and the condemnation fails."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): A Downtown Arena for a Named Team.} A city negotiates with a professional sports team that wants a new arena, then adopts a 20-acre downtown redevelopment plan, after public hearings, that includes the arena, a public plaza, and housing, and condemns several unblighted businesses on the site. The city can invoke \textit{Kelo}: a formal plan, public deliberation, and genuine economic-development goals. But the plan was prompted by, and is built around, a single identified private beneficiary, which is the scenario Justice Kennedy flagged as possibly warranting ``a more stringent standard of review.'' Whether a court finds a public purpose or a pretextual private transfer depends on how it weighs the planning process against the team's central role."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Just Compensation", to=r"\end{itemize}")],
  "Key Quotations":
    Q(r"``Promoting economic development is a traditional and long accepted function of government. There is, moreover, no principled way of distinguishing economic development from the other public purposes that we have recognized. \dots\ We emphasize that nothing in our opinion precludes any State from placing further restrictions on its exercise of the takings power.''", r"Justice Stevens, 545 U.S.\ at 484, 489" + JL)
    + Q(r"``A court applying rational-basis review under the Public Use Clause should strike down a taking that, by a clear showing, is intended to favor a particular private party, with only incidental or pretextual public benefits.''", r"Justice Kennedy (concurring), 545 U.S.\ at 491" + JL)
    + Q(r"``The specter of condemnation hangs over all property. Nothing is to prevent the State from replacing any Motel 6 with a Ritz-Carlton, any home with a shopping mall, or any farm with a factory. \dots\ The beneficiaries are likely to be those citizens with disproportionate influence and power in the political process, including large corporations and development firms.''", r"Justice O'Connor (dissenting), 545 U.S.\ at 503, 505" + JL)
    + Q(r"``The most natural reading of the Clause is that it allows the government to take property only if the government owns, or the public has a legal right to use, the property. \dots\ Though citizens are safe from the government in their homes, the homes themselves are not.''", r"Justice Thomas (dissenting), 545 U.S.\ at 508, 518" + JL),
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, duplicate source links (Justia link kept in Judicial Votes).",
  "Legacy section (entire subsection omitted): Fort Trumbull aftermath paragraph (history); post-Kelo state reforms item (state legislation, not a decision applying Kelo; the point is covered by Example 4); 'Continuing Calls to Reconsider Kelo' item (dissent from denial of certiorari and cert denials - not decisions).",
  "Exam Hypothetical: 'City's Best Argument' bullet (restates Kelo's holding) and the 'Owner's Best Argument' label and its opening sentence; the fact pattern and owner's analysis are reused in Example 3.",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all four kept, none added. Attributions are emitted inside each quote block and converted by normalize_quotes.py, as in 181_missouri_v_holland.",
           "No Subsequent Developments subsection: no later Supreme Court decision in the legacy section overruled, narrowed, or applied Kelo's holding."],
}

emit(__file__, FILL)
