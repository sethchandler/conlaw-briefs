"""Fill for 235_united_states_v_vaello_madero. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/596/20-303/"
FS = "Facts and Procedural History"
SO = "Concurring and Dissenting"
PS = "Pedagogical Critiques"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"The SSA sued a disabled U.S. citizen to recover SSI payments made after he moved to Puerto Rico; the Court held 8--1 that the Fifth Amendment does not require Congress to extend SSI to Puerto Rico, because the territory's general exemption from federal income taxes supplies a rational basis under the Territory Clause (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="In June 2016, when Vaello Madero visited")],
  "Procedural History": [SEC(FS, frm="In June 2016, when Vaello Madero visited")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the First Circuit by an \textbf{8--1} vote. The case was argued on November 9, 2021, and decided on April 21, 2022 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/20-303}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Kavanaugh delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Thomas, Breyer, Alito, Kagan, Gorsuch, and Barrett.
    \item \textbf{Concurring Opinions:} Justice Thomas filed a concurring opinion. Justice Gorsuch filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Sotomayor filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kavanaugh)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC(SO, frm="Joined the majority in full, but", to=r"  \item \textbf{Justice Gorsuch", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Gorsuch)}"), N("Justice Gorsuch", glue=" "),
    SEC(SO, frm="Joined the majority because", to=r"  \item \textbf{Justice Sotomayor", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Sotomayor)}"), N("Justice Sotomayor", glue=" "),
    SEC(SO, frm="Argued that excluding", to=r"\end{itemize}", lc=True),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Territorial Exclusion Upheld): A Federal Heating and Cooling Credit.}", glue=" "),
    S(r"Congress enacts a new federal ``National Heating and Cooling Credit'' funded from general Treasury revenues and administered directly by the IRS, available to low-income households in the 50 States and D.C., but excluding residents of Guam and Puerto Rico while maintaining separate block grants for those territories. A disabled U.S. citizen living in Guam sues under the Fifth Amendment.", glue=" "),
    S(r"Congress wins under \emph{Vaello Madero}, \href{https://supreme.justia.com/cases/federal/us/435/1/}{\emph{Torres}}, and \href{https://supreme.justia.com/cases/federal/us/446/651/}{\emph{Rosario}}. Under the Territory Clause and deferential rational-basis review, Guam's distinct federal tax structure supplies a rational basis for territorial exclusion without any dollar-for-dollar accounting."),
    N(r"\item \textbf{Same-Side (Territorial Asymmetry Upheld): A Cap on Federal Medicaid Funds for the Territories.} Congress funds Medicaid in the States through an open-ended federal match but gives Puerto Rico and the other territories a fixed annual block of federal money, so that once the cap is reached the territory must pay the full cost. Low-income residents of Puerto Rico argue that the disparity denies them equal protection. Under \textit{Vaello Madero}, Congress may weigh the general balance of benefits to and burdens on territorial residents, including their exemption from most federal income taxes, the cost of greater reimbursement, and the risk of disrupting the territory's economy. \textit{Harris v.\ Rosario} upheld lower AFDC reimbursements to Puerto Rico on similar reasoning, and the cap survives rational-basis review."),
    N(r"\item \textbf{Opposite-Side (Exclusion Invalid): Excluding Residents of a State.} Now suppose Congress", glue=" "),
    S(r"excludes residents of West Virginia from the same federal credit because West Virginia residents pay less per capita in federal income taxes than residents of New York", glue=""),
    N(r". \textit{Vaello Madero}'s rationale does not carry over:", glue=" "),
    S(r"Congress cannot rely on the Territory Clause, and \emph{Vaello Madero} Footnote 1 expressly refuses to extend territorial fiscal-balance deference to exclusions of individual States---which would also collide with structural principles of equal state sovereignty and interstate travel."),
    N(r"\item \textbf{Opposite-Side (Strict Scrutiny): An Ancestry-Based Exclusion in Puerto Rico.} Alternatively, suppose Congress", glue=" "),
    S(r"excludes Puerto Rico residents from SSI only if they are of Hispanic ancestry while granting SSI to non-Hispanic residents of Puerto Rico", glue=""),
    N(r". Here", glue=" "),
    S(r"the classification ceases to be a geographic/territorial line and becomes an explicit racial or national-origin classification triggering strict scrutiny under Fifth Amendment equal protection (\href{https://supreme.justia.com/cases/federal/us/515/200/}{\emph{Adarand}}; or, on Justice Thomas's view, violating the Citizenship Clause), which the federal government cannot survive."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Excluding Puerto Rico From a Payroll-Tax-Funded Benefit.} Congress creates a federal paid family-leave benefit financed entirely by a new payroll tax that is collected from workers and employers in Puerto Rico just as in the States, but it pays benefits only to residents of the States. A worker in Puerto Rico who paid the tax is denied benefits. \textit{Vaello Madero} rested on Puerto Rico's exemption from federal income taxes, a rationale that is missing when residents pay the very tax that funds the program, much as Justice Sotomayor stressed that Puerto Ricans pay payroll taxes. Yet rational-basis review accepts any conceivable justification and the majority looked to the general balance of benefits and burdens rather than any one tax, so a court could uphold the exclusion. The outcome is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC(PS, to=r"\textbf{Exam Hypothetical", strip=r"\textbf{Pedagogical Critiques.} ")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, court line, Briefing Book placement, provisions list, duplicate links (Justia and Cornell links kept in Judicial Votes).",
  "Entire Legacy section (CBO baseline, SSI Equality Act reintroduction, Fitisemanu certiorari denial, Insular Cases and Bolling debates): none is a later decision overruling, narrowing, extending, or applying Vaello Madero's holding, so no Subsequent Developments subsection.",
  "Exam Scenario B was split into its two variants (Examples 3 and 4); its connecting words '(1)'/'(2)', 'Both measures fail', and 'In (1),'/'In (2),' were replaced by new connectors.",
 ],
 "notes": [],
}

emit(__file__, FILL)
