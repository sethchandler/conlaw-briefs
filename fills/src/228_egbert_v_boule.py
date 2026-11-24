"""Fill for 228_egbert_v_boule. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/596/21-147/"
C = "Concurring and Dissenting"
P = "Pedagogical"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"An innkeeper roughed up by a Border Patrol agent in his own driveway could not sue under \textit{Bivens}: the Court held 6--3 (Fourth Amendment) and 9--0 (First Amendment retaliation) that no implied damages remedy exists whenever there is any reason to think Congress is better equipped to create one (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="In January 2017, Boule sued")],
  "Procedural History": [SEC("Facts and Procedural History", frm="In January 2017, Boule sued")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the Ninth Circuit, by a \textbf{6--3} vote on the Fourth Amendment excessive-force claim and \textbf{9--0} on the First Amendment retaliation claim. The case was argued March 2, 2022, and decided June 8, 2022 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/21-147}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Thomas delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Alito, Kavanaugh, and Barrett.
    \item \textbf{Concurring Opinions:} Justice Gorsuch filed an opinion concurring in the judgment. Justice Sotomayor, joined by Justices Breyer and Kagan, concurred in the judgment as to the First Amendment claim.
    \item \textbf{Dissenting Opinion:} Justice Sotomayor, joined by Justices Breyer and Kagan, dissented as to the Fourth Amendment claim.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Thomas)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Judgment (Justice Gorsuch)}"),
    SEC(C, to=r"\textbf{Justice Sotomayor", strip=r"\textbf{Justice Gorsuch (Concurring in the Judgment):} "),
    N(r"\subsection{Concurring in the Judgment in Part and Dissenting in Part (Justice Sotomayor)}"),
    SEC(C, frm=r"\textbf{Justice Sotomayor", strip=r"\textbf{Justice Sotomayor (Concurring in the Judgment in Part and Dissenting in Part, joined by Justices Breyer and Kagan):} "),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{\textit{Goldey v. Fields}", to=r"  \item \textbf{Ongoing Erosion"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (No \textit{Bivens} Remedy): An FBI Raid Far From the Border.}", glue=" "),
    S(r"Suppose FBI agents execute a warrantless raid on a U.S. citizen's apartment in Houston, Texas (more than 100 miles from an international land border), handcuff the homeowner in front of his family, and break his arm without probable cause. He sues under \textit{Bivens}.", glue=" "),
    S(r"The plaintiff will argue his claim falls squarely within \textit{Bivens}'s core domestic Fourth Amendment facts and involves no border-security factor. Under \textit{Egbert} and \textit{Goldey}, however, the agents will argue that FBI agents are a ``new category of defendants,'' that DOJ's Office of the Inspector General provides an ``alternative remedial structure,'' and that there is at least ``a single reason'' Congress is better equipped to authorize damages---likely defeating the claim unless the court treats it as factually identical to \textit{Bivens}."),
    N(r"\item \textbf{Same-Side (No \textit{Bivens} Remedy): Retaliation by a Federal Inspector.} A restaurant owner publicly criticizes a federal food-safety agency. Days later, an agency inspector conducts an unannounced inspection and issues a string of citations that are later dismissed. The owner sues the inspector for damages under \textit{Bivens}, alleging First Amendment retaliation. \textit{Egbert} squarely forecloses the claim: all nine Justices agreed that no \textit{Bivens} action exists for First Amendment retaliation, because a plaintiff can easily allege a retaliatory motive for almost any adverse federal action, and permitting such suits would chill legitimate official conduct across the federal workforce. Whether to provide a damages remedy for retaliation by federal officers is for Congress (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Express Statutory Cause of Action): The Same Force by a State Trooper.} A state highway patrol trooper stops a driver, drags him from the car without provocation, and throws him to the pavement, breaking his collarbone. The driver sues the trooper for damages under 42 U.S.C.\ \S~1983. \textit{Egbert} poses no obstacle. Its reasoning rests on separation of powers: courts should not \emph{imply} a damages action that Congress has not created. Here Congress has expressly supplied the cause of action against persons acting under color of state law, so there is no question whether Congress or the courts should decide. The driver may proceed on his Fourth Amendment excessive-force claim, subject to ordinary defenses such as qualified immunity."),
    N(r"\item \textbf{Opposite-Side (Prospective Relief): Enjoining an Ongoing Federal Practice.} Residents of a border town show that Border Patrol agents, under a written sector policy, routinely enter fenced private backyards without warrants or consent to look for migrants. The residents sue the agency head in her official capacity, seeking a declaratory judgment and an injunction against the practice; they seek no damages. \textit{Egbert} limits only implied retrospective money damages against individual officers. It does not withdraw the federal courts' power to grant prospective equitable relief against ongoing unconstitutional federal conduct, whether through traditional equity jurisdiction or under the Administrative Procedure Act's waiver of sovereign immunity for nonmonetary relief (5 U.S.C.\ \S~702). The suit may proceed to the merits."),
    N(r"\item \textbf{Fence-Sitter (A Near-Replica of \textit{Bivens}): Narcotics Agents Search a Home.} Federal drug agents enter a New York apartment without a warrant, manacle the tenant in front of his family, threaten them, search the apartment, and strip-search the tenant at a federal facility. The tenant sues the agents for damages under the Fourth Amendment. The facts track \textit{Bivens} itself, which \textit{Egbert} declined to overrule, so a court could hold the claim arises in no new context. But \textit{Egbert} warned that ``parallel circumstances'' with \textit{Bivens} are not enough unless the claim also survives the Court's restrictive modern framework, and the agency's internal complaint process might count as an alternative remedial structure. Justice Gorsuch saw no principled way to distinguish such cases. Whether even a \textit{Bivens} replica survives is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(P, frm=r"  \item \textbf{Remedial Asymmetry", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: parallel cite, docket number, provisions line, SupremeCourt.gov page-proof link (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: two framing paragraphs; 'Ongoing Erosion of Core Bivens Precedents (2025--2026)' item (circuit-court trends, Nielsen v. Watanabe merits briefing, legislative proposals) - not a decision applying or narrowing Egbert. Kept: Goldey v. Fields item.",
  "Hypothetical 2 ('Opposite Side' Contrast): an exam tip rather than a fact pattern; its two points are turned into Examples 3 and 4.",
  "Hypothetical 1 'Analysis:' label.",
 ],
 "notes": ["Kept Goldey v. Fields (2025) item (per curiam, 606 U.S. ___) is from Neon's original and should be verified against the official report."],
}

emit(__file__, FILL)
