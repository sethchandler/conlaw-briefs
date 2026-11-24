"""Fill for 233_tennessee_wine_and_spirits_retailers_assn_v_thomas. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/588/18-96/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Tennessee required retail liquor-store license applicants to have lived in the State for two years; the Court held 7--2 that the rule violated the dormant Commerce Clause and was not saved by \S~2 of the Twenty-first Amendment, which does not shield protectionist alcohol laws lacking evidence-backed health or safety justifications (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The TABC's executive director filed")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The TABC's executive director filed")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Sixth Circuit by a \textbf{7--2} vote. The case was argued on January 16, 2019, and decided on June 26, 2019 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/18-96}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Alito delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Ginsburg, Breyer, Sotomayor, Kagan, and Kavanaugh.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinion:} Justice Gorsuch filed a dissenting opinion, joined by Justice Thomas.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Alito)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Gorsuch)}"),
    SEC("Concurring and Dissenting", frm="Gorsuch argued that the Dormant"),
    N(r"\subsection{Subsequent Developments}"),
    S(r"Through 2026, however, Justice Gorsuch's dissent proved prescient: lower courts have deeply fractured over how \textit{Tennessee Wine} applies to state laws allowing \textit{in-state} wine retailers to ship directly to consumers while barring \textit{out-of-state} retailers unless they maintain an in-state physical storefront. Two rival methodologies emerged across the circuits:"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"On May 18, 2026"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Law Invalid): A Property-Ownership Requirement for Craft-Beer Licenses.}", glue=" "),
    S(r"State X enacts a statute allowing only individuals who have owned real property in State X for three years to hold a craft-beer wholesale or retail license, asserting that property owners are ``more invested in preventing underage drinking.'' Out-of-state applicant Z challenges the law.", glue=" "),
    S(r"Under \textit{Tennessee Wine}, the statute is \textbf{unconstitutional}. It facially discriminates against nonresidents, is not an essential feature of a three-tier system, and rests on ``mere speculation'' rather than concrete evidence, while nondiscriminatory alternatives (age-verification audits, clerk training, license revocation) readily advance public safety."),
    N(r"\item \textbf{Same-Side (Law Invalid): An All-Resident Ownership Rule for Corporate Retailers.} A State allows a corporation to hold a retail liquor license only if every one of its officers, directors, and shareholders is a state resident, which bars any publicly traded chain from opening a store. The State says local ownership keeps retailers accountable to the community. Applying \textit{Tennessee Wine}, the rule discriminates against nonresidents on its face, and the State must show with concrete evidence that its predominant effect is protecting health or safety rather than protecting in-state owners from competition. Accountability can be secured through registered agents, background checks, inspections, and license revocation, as the Court explained in rejecting Tennessee's rationales, so the ownership rule falls outside \S~2's protection."),
    N(r"\item \textbf{Opposite-Side (Law Likely Valid): Neutral Density Caps, Price Floors, and Storefront Rules.}", glue=" "),
    S(r"Now suppose State X eliminates all residency and property-ownership requirements and instead enacts a \textit{facially neutral} statute capping the total number of retail liquor licenses per county at one per 10,000 residents, imposing a uniform minimum retail price per ounce of alcohol, and requiring every licensed retailer (in-state or out-of-state owned) to operate a brick-and-mortar storefront in State X subject to unannounced state health-and-tax inspections, backed by empirical studies tying outlet density and price floors to reduced alcohol-related hospitalizations. Here, State X holds a far stronger defense: the density cap and uniform price floor are nondiscriminatory public-health measures squarely within \S~2's ``leeway'' (which Alito expressly endorsed, slip op. at 36), and under post-\textit{Tennessee Wine} circuit precedent such as \href{https://law.justia.com/cases/federal/appellate-courts/ca9/23-16148/23-16148-2025-03-04.html}{\textit{Day v. Henry} (9th Cir. 2025)}, an evenhanded physical-presence requirement tied to three-tier inspection and tax enforcement is far more likely to survive \S~2 scrutiny than a durational-residency bar."),
    N(r"\item \textbf{Opposite-Side (Law Likely Valid): A State-Run Retail Monopoly.} A State repeals its private retail licensing system and provides that all packaged liquor will be sold only in stores owned and staffed by a state agency. A national retail chain that hoped to enter the market challenges the law. Unlike Tennessee's residency rule, the monopoly does not favor residents over nonresidents: it excludes every private seller, in-state or out-of-state, equally. \textit{Tennessee Wine} condemns laws that discriminate against nonresidents and whose predominant effect is protectionism. Because the monopoly does not discriminate, that inquiry is never triggered, and the State's choice falls within the leeway \S~2 gives each State in choosing alcohol-related public health and safety measures."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Direct Shipping by Out-of-State Retailers.} A State lets its licensed wine retailers ship wine directly to consumers' homes but forbids out-of-state retailers to do so unless they open a licensed store in the State. An out-of-state retailer argues that the law discriminates against it just as Tennessee's residency rule did. The State answers that requiring an in-state premises is part of its three-tier system, which \textit{Granholm} called unquestionably legitimate, and that in-state stores can be inspected and audited. As the Subsequent Developments above show, lower courts have divided over whether courts may treat physical presence as an essential feature of the three-tier system or must demand concrete evidence under the predominant-effect test, and the Supreme Court has not resolved the question."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Doctrinal Indeterminacy", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, lower-court citations, provisions list, slip-opinion link (kept in Key Quotations).",
  "Legacy section: first paragraph (settled the circuit split - restates the holding; National Pork Producers v. Ross - narrowed other dormant Commerce Clause branches, tangential); final paragraph on May 18, 2026 cert denials in Day v. Henry and Chicago Wine Co. v. Braun. Kept: the retailer-shipping split paragraph lead-in and the two circuit-method items (Day v. Henry; Block v. Canepa).",
  "Exam Hypothetical: 'Analysis:' label and headings (texts reused in Examples 1 and 3).",
 ],
 "notes": [
  "Kept Subsequent Developments items cite Day v. Henry (9th Cir. 2025, amended Sept. 2025) and a June 2026 blog post; verify in audit.",
  "Subsequent Developments is lower-court material only (no later Supreme Court decision applies Tennessee Wine); kept because the open retailer-shipping question is what students need to state current law.",
 ],
}

emit(__file__, FILL)
