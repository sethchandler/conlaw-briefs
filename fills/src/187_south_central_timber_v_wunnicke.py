"""Fill for 187_south_central_timber_v_wunnicke. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/467/82/"
FS = "Facts and Procedural History"
RS = "Reasoning"
SO = "Concurring and Dissenting"
LG = "Doctrinal Significance"
PS = "Pedagogical Critiques"
CORN = r"(\href{https://www.law.cornell.edu/supremecourt/text/467/82}{Cornell LII})"

def Q(text, attrib):
    # Attribution placed inside the quote block (Group B form) so that
    # tools/normalize_quotes.py converts it to Group A form (see notes).
    return [N(r"\begin{quote}", glue="\n"), S(text, glue="\n"),
            N("---", glue=" "), S(attrib, glue="\n"), N(r"\end{quote}")]

QUOTES = (
  Q(r"``There is no talismanic significance to the phrase `expressly stated,' however; it merely states one way of meeting the requirement that, for a state regulation to be removed from the reach of the dormant Commerce Clause, congressional intent must be unmistakably clear. The requirement that Congress affirmatively contemplate otherwise invalid state legislation is mandated by the policies underlying dormant Commerce Clause doctrine.''",
    r"Justice White, \href{https://supreme.justia.com/cases/federal/us/467/82/}{467 U.S.\ at 91--92} " + CORN)
  + Q(r"``The fact that the state policy in this case appears to be consistent with federal policy---or even that state policy furthers the goals we might believe that Congress had in mind---is an insufficient indicium of congressional intent. Congress acted only with respect to federal lands; we cannot infer from that fact that it intended to authorize a similar policy with respect to state lands.''",
    r"Justice White, \href{https://supreme.justia.com/cases/federal/us/467/82/}{467 U.S.\ at 92--93} " + CORN)
  + Q(r"``The limit of the market participant doctrine must be that it allows a State to impose burdens on commerce within the market in which it is a participant, but allows it to go no further. The State may not impose conditions, whether by statute, regulation, or contract, that have a substantial regulatory effect outside of that particular market. Unless the `market' is relatively narrowly defined, the doctrine has the potential of swallowing up the rule that States may not impose substantial burdens on interstate commerce even if they act with the permissible state purpose of fostering local industry.''",
    r"Justice White (plurality opinion), \href{https://supreme.justia.com/cases/federal/us/467/82/}{467 U.S.\ at 97--98} " + CORN)
  + Q(r"``Alaska is merely paying the buyer of the timber indirectly, by means of a reduced price, to hire Alaska residents to process the timber. Under existing precedent, the State could accomplish that same result in any number of ways. \dots\ It seems to me unduly formalistic to conclude that the one path chosen by the State as best suited to promote its concerns is the path forbidden it by the Commerce Clause.''",
    r"Justice Rehnquist (dissenting), \href{https://supreme.justia.com/cases/federal/us/467/82/}{467 U.S.\ at 103} " + CORN)
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Alaska sold state timber on condition that buyers process it in Alaska before export; the Court held that a parallel federal-lands policy was not ``unmistakably clear'' congressional authorization, and a plurality held that the market-participant exception does not let a State impose conditions that regulate a downstream market it does not participate in (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to=r"\subsection{Procedural History}", strip=r"\subsection{Factual Background}")],
  "Procedural History": [SEC(FS, frm=r"\subsection{Procedural History}", strip=r"\subsection{Procedural History}")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} the Ninth Circuit by a \textbf{6--2} vote, with one Justice not participating. The case was argued on February 29, 1984, and decided on May 22, 1984 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/467/82}{Cornell LII}):"),
    SEC("Case Metadata", frm=r"    \begin{itemize}", to=r"\end{itemize}"),
    N(r"\end{itemize}"),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Opinion of the Court and Plurality Opinion (Justice White)}"),
    N(r"\subsubsection{Part II (Opinion of the Court): ``Unmistakably Clear'' Congressional Authorization}"),
    SEC(RS, frm="While Congress may redefine", to=r"\subsection{Part III"),
    N(r"\subsubsection{Part III (Plurality Opinion): The Downstream Market-Participant Boundary}"),
    SEC(RS, frm="The plurality distinguished", to=r"\subsection{Part IV"),
    N(r"\subsubsection{Part IV (Plurality Opinion): Per Se Invalidity and Foreign Commerce}"),
    SEC(RS, frm="As a naked local-processing"),
    N(r"\subsection{Concurring Opinion (Justice Brennan)}"), N("Justice Brennan", glue=" "),
    SEC(SO, frm="Joined Justice White in full", to=r"    \item \textbf{Concurrence in Part", lc=True),
    N(r"\subsection{Opinion Concurring in Part and in the Judgment (Justice Powell)}"), N("Justice Powell, joined by Chief Justice Burger,", glue=" "),
    SEC(SO, frm="Joined Parts~I and II but", to=r"    \item \textbf{Dissent", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Rehnquist)}"), N("Justice Rehnquist, joined by Justice O'Connor,", glue=" "),
    SEC(SO, frm="Criticized the plurality", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{The ``Unmistakably Clear'' Canon Applied:}", glue=" "),
    S(r"First, Part~II's six-Justice majority cemented the ``unmistakably clear'' canon for congressional authorization of state trade barriers, relied upon in \href{https://supreme.justia.com/cases/federal/us/477/131/}{\textit{Maine v.\ Taylor}}, 477 U.S.\ 131, 138--139 (1986) (rejecting implied consent under the Lacey Act), and contrasted with express statutory authorization in \href{https://supreme.justia.com/cases/federal/us/472/159/}{\textit{Northeast Bancorp, Inc.\ v.\ Board of Governors}}, 472 U.S.\ 159 (1985)."),
    N(r"\item \textbf{The Downstream Limit in Later Market-Participant Cases:}", glue=" "),
    SEC(LG, frm="Second, although Part~III", to="Through 2026"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Invalid Downstream Mandate): In-State Refining of State-Land Lithium.}", glue=" "),
    S(r"Nevada auctions state-land lithium leases requiring winning bidders to refine all extracted lithium at in-state facilities before export, invoking a federal statute requiring domestic processing of \emph{federal}-land minerals. Under \textit{Wunnicke} Part~II, parallel federal-land policy is not ``unmistakably clear'' authorization. Under Part~III, Nevada participates in raw-lithium leasing, not downstream refining; imposing post-extraction processing strings on a natural resource entering foreign trade fails market-participant immunity and is virtually \textit{per se} invalid under \href{https://supreme.justia.com/cases/federal/us/397/137/}{\textit{Pike v.\ Bruce Church, Inc.}}, 397 U.S.\ 137 (1970)."),
    N(r"\item \textbf{Same-Side (Invalid Downstream Mandate): Resale Restrictions on State-Made Cement.} A State that operates its own cement plant sells cement to private distributors on condition that they resell it only to customers within the State, even after title and payment have passed. Out-of-state builders who would buy from the distributors challenge the condition. The State may choose its own customers, as \textit{Reeves} allowed, but here it reaches past its sale to control the buyers' later dealings in a resale market where the State is not a participant. The plurality identified exactly this kind of post-sale restriction as one of the features absent from \textit{Reeves}, and a resale ban that walls off the State's market for local benefit is the kind of downstream regulation \textit{Wunnicke} forbids."),
    N(r"\item \textbf{Opposite-Side (Valid Market Participation): A State-Owned Refinery Choosing Its Customers.} Return to the lithium hypothetical, but suppose Nevada instead", glue=" "),
    S(r"operates a state-owned refinery and sells refined lithium exclusively to Nevada battery makers during shortages", glue=""),
    N(r". Nevada is now acting as a seller in the very market it has entered and is simply choosing its customers, the conduct \textit{Reeves} protected when South Dakota sold cement from its own plant to residents first. No condition follows the lithium after sale into a market Nevada does not participate in, so the market-participant exception applies and the Dormant Commerce Clause does not bar the preference."),
    N(r"\item \textbf{Opposite-Side (Valid Market Participation): Cash Subsidies Instead of Export Conditions.} Alternatively, suppose Nevada", glue=" "),
    S(r"auctions raw leases without export conditions while paying direct general-fund cash subsidies to in-state refiners", glue=""),
    N(r". Lessees remain free to ship raw ore anywhere, so the State has not stripped buyers of their choice, the feature that distinguished \textit{Alexandria Scrap} from Alaska's contract clause. The subsidy may favor local refiners, but a direct payment from the State's own funds is not a regulation of the downstream market, and the plurality noted that such alternatives remain open to a State."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Requiring Resident Logging Crews on State Land.} Alaska sells standing timber on state land and requires that the buyer use crews made up of Alaska residents to cut and haul the timber off state land; once the logs leave state land, the buyer may process and ship them anywhere. Alaska argues that, as in \textit{White}, the workers are effectively working on a state project before the sale is complete. The challenger replies that the condition regulates the separate labor market for logging services. Because the plurality defined the market by intuition without an objective test, and because Part~III never commanded a majority, it is unclear whether harvesting on state land falls inside the timber-sales market or downstream of it."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"\begin{itemize}", to=r"\subsection{Exam Hypothetical")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "Case Metadata: case-name, citation, court, dates, Chapter/Doctrinal Topic and disposition items (disposition and dates restated in Judicial Votes; vote-alignment list moved verbatim).",
  "Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the Justice White subsection.",
  "Legacy section: opening framing sentence and the 'Through 2026' paragraph (Ross, green-energy and procurement disputes, Crosby) - tangential. Kept: Maine v. Taylor / Northeast Bancorp sentence and the downstream-limit paragraph (New Energy, Camps Newfound, United Haulers, Davis).",
  "Exam 'Opposite Side' Contrast: analysis sentences dropped; its two fact variants (a) and (b) were moved verbatim into Examples 3 and 4 with new analysis.",
  "Key Quotations: the four bold quotation labels (e.g. 'Unmistakably Clear Congressional Authorization (Majority, Part II)') dropped; every quote and its attribution kept.",
 ],
 "notes": ["tools/manual_quotes.txt entries carry a .tex suffix, so check_brief.py still runs normalize_quotes.py on this brief; each quote is rebuilt with its attribution inside the quote block (Group B form) so the normalizer produces the Group A form, as in 186_pike_v_bruce_church."],
}

emit(__file__, FILL)
