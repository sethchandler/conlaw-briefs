"""Fill for 256_cedar_point_nursery_v_hassid. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/594/20-107/"
LII = r"(\href{https://www.law.cornell.edu/supremecourt/text/20-107}{Cornell LII})"

def Q(quote, who):
    # Attribution placed inside the quote block; tools/normalize_quotes.py moves it to a
    # Group A "\noindent ---" line (check_brief.py runs it for every brief).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "), S(who, glue=" "),
            S(LII, glue="\n"), N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"A California rule letting union organizers enter farms for up to three hours a day, 120 days a year, was held 6--3 to be a \emph{per se} physical taking: a regulation that appropriates the owner's right to exclude for third parties requires just compensation, however intermittent the access, subject to limited exceptions (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Cedar Point and Fowler sued ALRB")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Cedar Point and Fowler sued ALRB")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} the Ninth Circuit's decision (923 F.3d 524) by a \textbf{6--3} vote. The case was argued on March 22, 2021, and decided on June 23, 2021 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/20-107}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Roberts delivered the opinion of the Court, joined by Justices Thomas, Alito, Gorsuch, Kavanaugh, and Barrett.
    \item \textbf{Concurring Opinion:} Justice Kavanaugh filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Breyer filed a dissenting opinion, joined by Justices Sotomayor and Kagan.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Kavanaugh)}"), N("Justice Kavanaugh", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined the majority in full", to=r"\item \textbf{Justice Breyer", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Breyer)}"), N("Justice Breyer", glue=" "),
    SEC("Concurring and Dissenting", frm="Argued that California", to=r"\end{itemize}", lc=True),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Per Se Taking): Wildlife Surveys on Fenced Timberland.}", glue=" "),
    S(r"A State enacts a statute granting certified environmental nonprofits a right to enter private, fenced timberlands (closed to the public) for four hours per week during spring migration to conduct wildlife-habitat surveys, imposing civil penalties on landowners who refuse entry.", glue=" "),
    S(r"Under \textit{Cedar Point}, the statute does not merely restrict how owners harvest timber; it appropriates a formal right of physical invasion for third parties. Intermittent duration (four hours weekly) affects only compensation, not liability. Because no background common-law privilege authorizes third-party wildlife surveys and the mandate is untethered to any government permit or benefit, it effects a \emph{per se} physical taking requiring just compensation."),
    N(r"\item \textbf{Same-Side (Per Se Taking): Canvassers in a Gated Community.} A city ordinance requires the owners' association of every private, gated residential community to admit registered political canvassers two weekends a month during election season so they can go door to door, and fines associations that refuse. The streets are private and closed to the public. Under \textit{Cedar Point}, the ordinance does not regulate how owners use their land; it grants third parties a right to physically enter it, appropriating the owners' right to exclude. That the access is limited to a few weekends affects only the amount of compensation. \textit{PruneYard} does not help the city, because \textit{Cedar Point} confined it to property generally open to the public, and no exception applies: canvassing is not a background common-law privilege, and the access is not a condition on a government benefit."),
    N(r"\item \textbf{Opposite-Side (No Per Se Taking): Licensing Inspections and a Zoning Setback.}", glue=" "),
    S(r"Now suppose a State requires commercial meatpacking plants, as a condition of obtaining a state food-processing license, to permit state agriculture inspectors to enter processing floors at reasonable business hours to test for bacterial contamination, and separately enacts a zoning ordinance barring new processing plants within 500 feet of residential schools.", glue=" "),
    S(r"Here, the outcome flips completely: (1) the inspection requirement falls squarely within \textit{Cedar Point}'s third exception because physical access is conditioned on a regulatory license and bears an essential nexus and rough proportionality to preventing foodborne public-health risks (\textit{Nollan}/\textit{Dolan}); and (2) the 500-foot zoning setback appropriates no right of physical entry at all---it merely restricts the owner's \emph{use} of her own land, triggering deferential \textit{Penn Central} balancing rather than \textit{Cedar Point}'s \emph{per se} rule."),
    N(r"\item \textbf{Opposite-Side (No Per Se Taking): A Highway Crew's One-Time Intrusion.} While repaving a state highway, a state road crew mistakenly parks its trucks and stores gravel on an adjoining farmer's field for two days, damaging part of a crop, and then leaves. No statute or regulation gives the State any right of access to the field. The farmer claims a \emph{per se} physical taking under \textit{Cedar Point}. The claim fails under the Court's first limiting boundary: an isolated physical invasion not undertaken under a granted right of access is ordinarily a trespass, remedied in tort, not an appropriation of the right to exclude. If the intrusion recurred or became part of a deliberate government program, the farmer could argue for a taking, and courts would weigh factors like those in \textit{Arkansas Game and Fish Comm'n v. United States}, 568 U.S. 23 (2012)."),
    N(r"\item \textbf{Fence-Sitter (Unsettled): Union Organizers at a Supermarket.} A state statute gives union organizers a right to stand on the private sidewalk and parking lot of any large supermarket, for limited hours, to speak with employees and customers. The store is open to the shopping public every day, but its owner bars all solicitation. The owner argues that \textit{Cedar Point} makes the statute a \emph{per se} taking because it grants third parties a right of access the owner never consented to. The State responds that \textit{Cedar Point} itself distinguished \textit{PruneYard}, which allowed access to a shopping center generally open to the public. Yet organizers are not customers using the property as invited, and the \textit{Cedar Point} majority treated the right to exclude as a fundamental element of property that cannot be balanced away. How far \textit{PruneYard} survives is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Unanswered Remedial", to=r"\end{itemize}")],
  "Key Quotations":
    Q(r"``The essential question is not, as the Ninth Circuit seemed to think, whether the government action at issue comes garbed as a regulation (or statute, or ordinance, or miscellaneous decree). It is whether the government has physically taken property for itself or someone else---by whatever means---or has instead restricted a property owner's ability to use his own property.''", "Roberts, C.J.")
    + Q(r"``The access regulation appropriates a right to invade the growers' property and therefore constitutes a per se physical taking. \ldots{} There is no reason the law should analyze an abrogation of the right to exclude in one manner if it extends for 365 days, but in an entirely different manner if it lasts for 364.''", "Roberts, C.J.")
    + Q(r"``We cannot agree that the right to exclude is an empty formality, subject to modification at the government's pleasure. On the contrary, it is a `fundamental element of the property right,' \textit{Kaiser Aetna}, 444 U.S., at 179--180, that cannot be balanced away.''", "Roberts, C.J.")
    + Q(r"``The regulation does not appropriate anything. \ldots{} It gives union organizers the right temporarily to invade a portion of the property owners' land. It thereby limits the landowners' right to exclude certain others. The regulation regulates (but does not appropriate) the owners' right to exclude.''", "Breyer, J., dissenting"),
 },
 "dropped": [
  "Case Metadata: full case name, docket number, court line, certiorari date, SupremeCourt.gov page-proof link (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section, entirely: introductory sentence; Tyler/Pung item (tax-foreclosure surplus cases, which build on but do not apply Cedar Point's holding); Sheetz item (exactions, tangential); DeVillier item (cause of action, tangential); eviction-moratoria circuit-split item (lower-court decisions and a 2025 certiorari denial, not a Supreme Court decision applying Cedar Point). No Supreme Court decision in the original squarely applies, narrows, or extends the holding, so the Subsequent Developments subsection is omitted.",
  "Key Quotations: the bold descriptive labels before each quotation; the attributions 'Roberts, C.J.' / 'Breyer, J., dissenting' and the Cornell LII link are kept.",
  "Exam Hypotheticals: their headings and 'Analysis:' / 'Opposite Side Contrast Analysis:' labels (both fact patterns reused verbatim as Examples 1 and 3).",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all four kept, none added. The original gives no pin cites, so none are supplied."],
}

emit(__file__, FILL)
