"""Fill for 240_trump_v_hawaii. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/585/17-965/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Upholding Proclamation No.~9645, President Trump's third entry-restriction order, the Court held 5--4 that \S~1182(f) gives the President broad power to suspend entry and that, under deferential rational-basis review, the facially neutral proclamation survived an Establishment Clause challenge; it also repudiated \textit{Korematsu} (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The State of Hawaii, three U.S. citizens")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The State of Hawaii, three U.S. citizens")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{5--4} vote. The case was argued on April 25, 2018, and decided on June 26, 2018 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/17-965}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Roberts delivered the opinion of the Court, joined by Justices Kennedy, Thomas, Alito, and Gorsuch.
    \item \textbf{Concurring Opinions:} Justice Kennedy and Justice Thomas each filed a concurring opinion.
    \item \textbf{Dissenting Opinions:} Justice Breyer filed a dissenting opinion, joined by Justice Kagan. Justice Sotomayor filed a dissenting opinion, joined by Justice Ginsburg.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Kennedy)}"), N("Justice Kennedy", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined the majority in full", to=r"\item \textbf{Justice Thomas", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC("Concurring and Dissenting", frm="Argued that the President", to=r"\item \textbf{Justice Breyer", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Breyer)}"), N("Justice Breyer", glue=" "),
    SEC("Concurring and Dissenting", frm="Focused on whether", to=r"\item \textbf{Justice Sotomayor", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Sotomayor)}"), N("Justice Sotomayor", glue=" "),
    SEC("Concurring and Dissenting", frm="Charged that a", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Applied (\textit{Department of State v. Mu\~noz}):}", glue=" "),
    S(r"In \href{https://supreme.justia.com/cases/federal/us/602/23-334/}{\textit{Department of State v. Mu\~noz}, 602 U.S. 899 (2024)}, the Court reinforced \textit{Hawaii} and \textit{Mandel} in holding that a U.S. citizen has no fundamental liberty interest in a noncitizen spouse's visa admission."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Proclamation Upheld): Suspending Tourist Visas After a Vetting Review.}", glue=" "),
    S(r"Following a six-month interagency review finding that four foreign nations---three of which are predominantly Buddhist---lack biometric passport controls and fail to share criminal-record databases, the President issues a proclamation under 8 U.S.C. \S~1182(f) suspending nonimmigrant tourist visas from those four nations, with case-by-case hardship waivers. During the campaign, the President repeatedly vowed to ``halt Buddhist immigration.'' A U.S. university challenges the proclamation under the INA and Establishment Clause.", glue=" "),
    S(r"Valid under \textit{Trump v. Hawaii}. Section 1182(f) confers broad discretion upon a presidential finding of detriment, and under \textit{Mandel}/rational-basis review, the facially neutral text, interagency vetting record, and waiver provisions supply an independent national-security justification sufficient to survive Establishment Clause scrutiny."),
    N(r"\item \textbf{Same-Side (Proclamation Upheld): An Open-Ended Suspension to Pressure a Foreign Government.} The President finds that a foreign government's refusal to accept the return of its nationals ordered removed from the United States harms U.S. interests, and under \S~1182(f) suspends the entry of that country's nationals as immigrants until the government begins cooperating. Plaintiffs argue that \S~1182(f) authorizes only temporary emergency measures and that the suspension discriminates by nationality in immigrant-visa issuance, contrary to \S~1152(a)(1)(A). Both arguments failed in \textit{Trump v. Hawaii}. The Court read \S~1182(f) to leave to the President whether, whose, for how long, and on what conditions entry is suspended, noting past nationality-based suspensions without fixed end dates, and held that \S~1152 governs visa issuance, not the threshold question of admissibility. The suspension is lawful."),
    N(r"\item \textbf{Opposite-Side (Order Invalid): A Domestic Policy Targeting Buddhist-Studies Programs.}", glue=" "),
    S(r"By contrast, suppose the same President issues an executive order directing the Department of Education to revoke federal accreditation eligibility from all \textit{domestic} private colleges located in the United States that offer Buddhist-studies degree programs, citing a vague ``national cultural security'' concern after making identical campaign statements denigrating Buddhism.", glue=" "),
    S(r"Unconstitutional. Unlike \textit{Trump v. Hawaii}, this policy regulates domestic institutions and U.S. citizens within the United States rather than foreign-national entry at the border, and it lacks any statutory delegation akin to \S~1182(f). Without \textit{Mandel}'s border-entry deference, domestic Establishment Clause and Free Exercise scrutiny (\textit{Masterpiece Cakeshop}; \textit{Church of the Lukumi Babalu Aye}) applies in full force, and the overt religious targeting and extrinsic evidence of animus render the order invalid."),
    N(r"\item \textbf{Opposite-Side (Likely Invalid): An Entry Ban Defined by Religion on Its Face.} The President issues a proclamation under \S~1182(f) suspending the entry of all foreign nationals who adhere to a named religion, citing general terrorism concerns but no country-specific vetting review. U.S. citizens separated from relatives abroad sue. \textit{Trump v. Hawaii} does not save the proclamation, because the Court's analysis depended on what the policy did not do: Proclamation No.~9645 was neutral on its face, rested on a multi-agency review of foreign governments' practices, and excluded most of the world's Muslims. A proclamation that classifies by religion on its face announces the very ground the Establishment Clause forbids, so it cannot reasonably be understood to rest on a justification independent of unconstitutional grounds, even under rational-basis review."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): Waivers That Exist Only on Paper.} A facially neutral \S~1182(f) proclamation restricts entry from several Muslim-majority countries and promises case-by-case waivers. In litigation, plaintiffs produce evidence that consular officers were told not to grant waivers, that almost none were granted, and that the agency review the proclamation cites had recommended lifting restrictions on two of the countries. Under the majority's approach, a court asks only whether the policy can reasonably be understood to rest on a legitimate national-security justification, and a neutral text plus an agency process ordinarily suffices. But Justice Breyer's dissent argued that waivers operating as window dressing would show the policy's real basis was religious animus. How much evidence of pretext can overcome the deference \textit{Trump v. Hawaii} prescribes remains unsettled."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Double Standard", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: Chapter line, provisions list, SupremeCourt.gov official-proof link (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory sentence; 'Executive Immigration Authority' item (revocation and 2025-2026 policy, not decisions); Trump v. United States sentence (quotes Hawaii on presidential speech, tangential); 'End of Universal Injunctions' item (Trump v. CASA concerns Justice Thomas's concurrence, not Hawaii's holding); 'Anti-Canon and Rational-Basis Deference' item (SFFA remark and 'through 2026' commentary). Kept: Department of State v. Munoz sentence.",
  "Exam Hypotheticals: their headings and 'Analysis:' labels (both fact patterns reused verbatim as Examples 1 and 3).",
 ],
 "notes": [],
}

emit(__file__, FILL)
