"""Fill for 170_ala_schechter_poultry_corp_v_united_states. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/295/495/"
FS = "Facts and Procedural History"
LG = "Doctrinal Significance"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"In the ``sick chicken case,'' a unanimous Court reversed a Brooklyn kosher slaughterhouse's convictions under a New Deal poultry code, holding that NIRA \S\,3 unconstitutionally delegated legislative power to the President and trade groups and that the code's reach to purely local slaughtering and sales exceeded the commerce power (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="A federal grand jury in the Eastern District")],
  "Procedural History": [SEC(FS, frm="A federal grand jury in the Eastern District")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{reversed} the remaining convictions (No.\ 854) and \textbf{affirmed} the Second Circuit's reversal of the wage-and-hour counts (No.\ 864), \textbf{9--0}. The case was argued May 2--3, 1935, and decided May 27, 1935 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/295/495}{Cornell LII}):"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Majority Opinion:} Chief Justice Hughes delivered the opinion of the Court", glue=" "),
    S(r"(joined by Justices Van Devanter, McReynolds, Brandeis, Sutherland, Butler, and Roberts; Justices Cardozo and Stone joined the judgment and concurred separately)."),
    N(r"""\item \textbf{Concurring Opinion:} Justice Cardozo filed a concurring opinion, joined by Justice Stone.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Hughes)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Cardozo)}"),
    SEC("Concurring and Dissenting", strip=r"\textbf{Justice Cardozo, concurring (joined by Justice Stone):} "),
    N(r"\subsection{Subsequent Developments}"),
    SEC(LG, frm=r"\begin{itemize}", to=r"  \item \textbf{\textit{Gundy v. United States}"),
    SEC(LG, frm=r"  \item \textbf{\textit{FCC v. Consumers' Research}", to=r"  \item \textbf{\textit{Learning Resources"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Delegation Invalid): Industry-Drafted AI Codes Backed by Criminal Penalties.}", glue=" "),
    S(r"Suppose Congress enacts the ``Artificial Intelligence Stabilization Act of 2026,'' authorizing the President to approve ``Codes of Safe AI Competition'' drafted by a consortium of major AI laboratories whenever the President finds a code ``tends to promote innovation, national competitiveness, and public safety.'' Violations carry criminal fines up to \$100,000 per day, and the President's approval is exempted from the Administrative Procedure Act and judicial review. A small open-source AI startup indicted for violating a code's compute-reporting rule challenges the statute.", glue=" "),
    S(r"Directly tracks \textit{Schechter Poultry} and \textit{Carter Coal}: (1) standardless, conflicting statutory aims (``innovation'' vs.\ ``public safety''); (2) private delegation to self-interested industry incumbents with no binding agency oversight (distinguishing \textit{Consumers' Research} and \textit{Sunshine Anthracite}); (3) elimination of APA procedural safeguards and judicial review; and (4) criminal penalties across a transformative economic sector (triggering both \textit{Schechter} and, if ambiguous, the major questions doctrine under \textit{West Virginia v. EPA} and \textit{Learning Resources})."),
    N(r"\item \textbf{Same-Side (Delegation Invalid): Letting a Majority of Producers Bind the Whole Industry.} Congress provides that producers responsible for two-thirds of a mineral's annual output, together with a majority of the industry's workers, may fix maximum hours and minimum wages that bind every producer in the country, including firms that opposed the terms. A small producer prosecuted for paying below the agreed scale challenges the law. As in \textit{Schechter}, coercive lawmaking power has been handed to private parties whose interests may be adverse to their competitors', with no public official reviewing the rules. The Court struck down a nearly identical scheme in \textit{Carter v. Carter Coal Co.}, 298 U.S.\ 238 (1936), building on \textit{Schechter}'s condemnation of delegation to trade associations."),
    N(r"\item \textbf{Opposite-Side (Delegation Valid): Health-Based Air Quality Standards.} Congress directs an environmental agency to set nationwide ambient air standards at the level needed to protect public health with an adequate margin of safety, after notice-and-comment rulemaking subject to judicial review. Industry groups argue the standard gives the agency open-ended discretion over the economy. Unlike NIRA \S\,3, the statute names a single objective, assigns the task to a public agency rather than private trade groups, and channels the agency through procedures and court review. Under the intelligible-principle test, the delegation is valid, as the Court held in \textit{Whitman v. American Trucking Ass'ns}, 531 U.S.\ 457 (2001)."),
    N(r"\item \textbf{Opposite-Side (Commerce Power Sustained): A Federal Minimum Wage for Local Slaughterhouse Workers.} Congress applies a federal minimum-wage and overtime law to slaughterhouse employees nationwide, including a firm that, like the Schechters, buys birds shipped from other states and sells only to local butchers. Under \textit{Schechter}'s direct/indirect line, the law could not reach such local labor. Modern doctrine has abandoned that line: \textit{United States v.\ Darby}, 312 U.S.\ 100 (1941), sustained federal wage-and-hour regulation, and \textit{Wickard v.\ Filburn}, 317 U.S.\ 111 (1942), allows Congress to regulate local economic activity whose aggregate effect on interstate commerce is substantial. Wages in the slaughtering industry readily meet that test, so the law is valid."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Criminal Penalties for Violating Broad Market Rules.} Congress authorizes the Secretary of Commerce to issue any rules the Secretary finds necessary to promote fair and orderly markets in emerging technologies, and makes willful violation a federal crime. A public agency, not an industry group, writes the rules after notice and comment. The government argues that fair and orderly markets is as intelligible as the public-interest standards the Court has long upheld, and \textit{Consumers' Research} reaffirmed the lenient test. The challenger answers that, as with NIRA's codes, the statute lets an executive official write criminal law for an entire sector under open-ended goals, the concern pressed by Justice Gorsuch's dissents in \textit{Gundy} and \textit{Consumers' Research}. Because the Court has upheld similarly general standards yet several Justices want stricter review of delegations backed by criminal sanctions, the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{``Opposite Side'' Contrast")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket numbers, consolidated caption, Chapter/Topic line, duplicate \\url{} printouts (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory 'Black Monday' paragraph; Gundy item (plurality; its dissent is referenced in Example 5); 'Sub-Constitutional Enforcement via Major Questions and Loper Bright' item (statutory doctrines, not applications of Schechter's holding); Learning Resources v. Trump item (IEEPA statutory holding; it is still named in the reused hypothetical). Kept: Commerce Clause repudiation, 'One Good Year' intelligible-principle item, FCC v. Consumers' Research.",
  "'Opposite Side' Contrast (Schechter vs. Curtiss-Wright and Consumers' Research): an exam tip, not a fact pattern.",
  "Exam Hypothetical: 'Government's Best Arguments' bullet (the analysis of the reused Example 1 keeps the challenger's arguments; the government's intelligible-principle response is reflected in Examples 3 and 5).",
 ],
 "notes": ["Example 1 reuses Neon's AI-codes hypothetical; its analysis begins with Neon's verbless fragment 'Directly tracks ...' moved verbatim."],
}

emit(__file__, FILL)
