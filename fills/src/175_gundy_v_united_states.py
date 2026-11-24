"""Fill for 175_gundy_v_united_states. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/588/17-6086/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"An eight-Justice Court upheld SORNA's grant of authority to the Attorney General to specify the Act's applicability to pre-Act sex offenders: Justice Kagan's four-Justice plurality read the statute to require registration ``as soon as feasible'' and found an intelligible principle, Justice Alito concurred only in the judgment, and three Justices dissented (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="He was indicted and convicted")],
  "Procedural History": [SEC("Facts and Procedural History", frm="He was indicted and convicted")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} Gundy's conviction by a \textbf{5--3} vote, with no majority opinion. The case was argued on October 2, 2018, and decided on June 20, 2019 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Plurality Opinion:} Justice Kagan announced the judgment of the Court and delivered an opinion joined by Justices Ginsburg, Breyer, and Sotomayor.
    \item \textbf{Concurring Opinion:} Justice Alito concurred in the judgment.
    \item \textbf{Dissenting Opinion:} Justice Gorsuch filed a dissenting opinion, joined by Chief Justice Roberts and Justice Thomas.
    \item \textbf{Not Participating:} Justice Kavanaugh took no part in the consideration or decision of the case.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Plurality Opinion (Justice Kagan)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Alito)}"), N("Justice Alito", glue=" "),
    SEC("Concurring and Dissenting", frm="Issued a terse", to=r"  \item \textbf{Justice Gorsuch", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Gorsuch)}"), N("Justice Gorsuch", glue=" "),
    SEC("Concurring and Dissenting", frm="Delivered a sweeping", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Reaffirmation of the Intelligible", to=r"  \item \textbf{2026 Consolidation"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Delegation Upheld): A Transitional Rule for a New Drone Registry.} Congress creates a national registry for commercial drone operators, declares its purpose to establish a comprehensive national system, requires every operator to register before flying, and authorizes the FAA Administrator ``to specify the applicability'' of the requirement to operators who bought drones before the statute's enactment and to prescribe rules for operators unable to comply with the initial deadline. Read as the \textit{Gundy} plurality read SORNA, the clause concerns how and when existing operators come into the system, not whether they come in at all; the comprehensive-system purpose and the reference to operators ``unable to comply'' confine the Administrator to a feasibility judgment. That transitional, small-bore discretion easily supplies an intelligible principle, and Justice Alito's concurrence supports the result under existing precedent, although he did not join the plurality's statutory construction."),
    N(r"\item \textbf{Same-Side (Delegation Upheld): A Broad Health Standard for a New Pollutant.} Congress directs an agency to set air-quality standards for a newly identified airborne particle at the level ``requisite to protect the public health,'' after considering published scientific criteria. A regulated manufacturer argues that the phrase gives the agency unlimited discretion over a major industry. Under the intelligible-principle test the plurality applied in \textit{Gundy}, the challenge fails: the Court has repeatedly upheld standards of exactly this breadth, including this very phrase in \textit{Whitman v. American Trucking Assns., Inc.}, 531 U.S. 457 (2001), and the \textit{Gundy} plurality treated such precedents as proof that only a statute supplying no policy or standard at all fails the test. The challenger's real hope lies in persuading a majority to adopt Justice Gorsuch's dissent, which \textit{FCC v. Consumers' Research} declined to do."),
    N(r"\item \textbf{Opposite-Side (Delegation Likely Invalid): Unbounded Discretion Over Whether a Crime Applies.} Congress enacts a statute providing that the Attorney General may determine, in her sole discretion, whether and to what extent a new federal firearms felony applies to any category of persons, and may change those determinations at any time. The text, unlike SORNA's, expressly confers the whether-or-not discretion Gundy attributed to \S~20913(d), and nothing in the statute's purpose or structure narrows it. The \textit{Gundy} plurality conceded that ``[i]f that were so, we would face a nondelegation question,'' and its saving construction would be unavailable because the text forecloses it. The three \textit{Gundy} dissenters would treat the provision as letting the nation's chief prosecutor write his own criminal code, and the power fits none of Justice Gorsuch's three permissible categories. The statute would likely fall."),
    N(r"\item \textbf{Opposite-Side (Delegation Invalid): A Shipment Ban Left to the Secretary's Unguided Choice.} Congress authorizes the Secretary of Agriculture to prohibit the interstate shipment of any agricultural product whenever the Secretary chooses, makes violations a federal crime, and states no policy, finding, or standard to govern when a ban should issue. This is the pattern of \textit{Panama Refining Co. v. Ryan}, 293 U.S. 388 (1935), one of the two statutes the Court has struck down on nondelegation grounds, where Congress articulated no policy or standard whatsoever. Even the \textit{Gundy} plurality, which defended broad delegations, distinguished such statutes; nothing in the text gives the Secretary a principle to follow, so there is no saving construction to adopt. Every member of the \textit{Gundy} Court would likely find a violation of Article~I."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Criminal Rulemaking for Frontier AI.}", glue=" "),
    S(r"Responding to rapid developments in autonomous vehicles and artificial intelligence, Congress enacts the ``National AI Safety Act of 2026.'' Section 4 of the Act empowers the Secretary of Commerce ``to promulgate such rules, licensing conditions, and criminal prohibitions (punishable by up to five years' imprisonment) governing the training and deployment of frontier artificial intelligence models as the Secretary determines are necessary and appropriate to protect the public interest, promote American innovation, and safeguard national security.'' The statute contains no further definition of ``frontier'' models, no threshold metrics, and no list of prohibited practices. Relying on Section 4, the Secretary issues a rule making it a federal felony to release any open-weight AI model trained using more than $10^{25}$ floating-point operations without a federal license. A software developer indicted under the rule challenges Section 4 under the nondelegation doctrine.", glue=" "),
    N(r"\textbf{Challenger:}", glue=" "),
    S(r"Unlike SORNA's transitional ``as soon as feasible'' mandate in \textit{Gundy} or the bounded beneficiary and service criteria in \textit{FCC v. Consumers' Research}, Section 4 confers economy-wide criminal lawmaking power with zero determinate boundaries.", glue=" "),
    N(r"\textbf{Government:}", glue=" "),
    S(r"The government will invoke the Court's unbroken post-1935 practice of upholding ``public interest'' standards (\textit{NBC v. United States}; \textit{Yakus}) and argue that ``frontier'' AI and ``national security'' supply contextual boundaries---especially because, as Justice Kavanaugh emphasized in \textit{Consumers' Research} (and Justice Gorsuch acknowledged in his third \textit{Gundy} category), nondelegation and the major questions doctrine play a far more limited role when Congress delegates to the President or an accountable Cabinet Secretary in the \textit{national security} realm.", glue=" "),
    N(r"The outcome is uncertain because the case presses the question \textit{Gundy} left open: whether a delegation defining a serious crime demands more specificity than the ordinary intelligible-principle test requires."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{Exam Hypothetical")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: full case name, docket number, Chapter/Topic line (Justia link kept in Memory Jogger and Judicial Votes).",
  "Legacy section: introductory paragraphs (Paul v. United States statement); 'Indirect Policing via Statutory Canons' item (West Virginia, Biden v. Nebraska, Loper Bright, Allstates) - tangential; '2026 Consolidation' item (Learning Resources, Trump v. Slaughter) - not applications of Gundy's holding. Kept: FCC v. Consumers' Research item.",
  "Exam Hypothetical: remaining sentences of the Challenger's Argument (Whitman sliding scale, Schechter, major questions) and of the Government's defense (removal, narrowing construction), trimmed for length; the fact pattern and lead arguments are reused in the Fence-Sitter example.",
 ],
 "notes": [],
}

emit(__file__, FILL)
