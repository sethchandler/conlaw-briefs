"""Fill for 220_moore_v_united_states. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/602/22-800/"
C = "Concurring and Dissenting"
P = "Pedagogical"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Taxpayers who owned 13\% of an Indian company challenged the 2017 Mandatory Repatriation Tax as an unapportioned tax on unrealized income; the Court held 7--2 that Congress may attribute an entity's realized but undistributed income to its shareholders and tax them on it, while reserving whether the Constitution requires realization (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="They then sued for a refund")],
  "Procedural History": [SEC("Facts and Procedural History", frm="They then sued for a refund")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Ninth Circuit by a \textbf{7--2} vote. The case was argued December 5, 2023, and decided June 20, 2024 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/22-800_2024-06-20}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Kavanaugh delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Sotomayor, Kagan, and Jackson.
    \item \textbf{Concurring Opinions:} Justice Jackson filed a concurring opinion. Justice Barrett filed an opinion concurring in the judgment, joined by Justice Alito.
    \item \textbf{Dissenting Opinion:} Justice Thomas filed a dissenting opinion, joined by Justice Gorsuch.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kavanaugh)}"),
    N(r"\subsubsection{Constitutional Architecture of the Taxing Power}"),
    SEC("Reasoning", frm="Justice Kavanaugh began with", to=r"\subsection{Entity Realization"),
    N(r"\subsubsection{Entity Realization and Attribution Precedents}"),
    SEC("Reasoning", frm="Rather than resolving whether", to=r"\subsection{Longstanding Congressional"),
    N(r"\subsubsection{Longstanding Congressional Practice and Fiscal Consequences}"),
    SEC("Reasoning", frm="Reinforcing judicial precedent"),
    N(r"\subsection{Concurring Opinion (Justice Jackson)}"),
    SEC(C, frm="Joining the majority in full", to=r"\item \textbf{Justice Barrett"),
    N(r"\subsection{Opinion Concurring in the Judgment (Justice Barrett)}"),
    SEC(C, frm="Justice Barrett directly answered", to=r"\item \textbf{Justice Thomas"),
    N(r"\subsection{Dissenting Opinion (Justice Thomas)}"),
    SEC(C, frm="Justice Thomas argued", to=r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Attribution Valid): An Annual Tax on U.S. Shareholders of Foreign Subsidiaries.} Congress enacts a permanent annual tax requiring every U.S.\ person who owns at least 10\% of a controlled foreign corporation to report and pay tax on his pro rata share of the corporation's realized net business profits for that year, whether or not the profits are distributed. The corporation pays no U.S.\ tax on those profits. A 15\% shareholder argues that she has received nothing and so has no ``income.'' Under \textit{Moore}, the tax is valid without apportionment: the corporation has realized the income, and Congress may attribute that realized, undistributed income to its shareholders and tax them on their shares, just as the Mandatory Repatriation Tax and Subpart F do (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Attribution Valid): Partners Taxed on Profits a Partnership Retains.} A domestic real-estate partnership earns \$10 million in rental profits in a year and, as its agreement permits, distributes nothing to its partners. Congress requires each partner to pay income tax on his share of the partnership's profits, and a minority partner who cannot force a distribution objects that he is being taxed on money he never received. This is the paradigm case \textit{Moore} relied on. The partnership realized the income, the partners are taxed on their pro rata shares, and the entity itself is not taxed. The precedents the Court cited, especially \textit{Heiner v.\ Mellon}, 304 U.S.\ 271 (1938), upheld taxing partners on undistributed profits even when state law barred distribution, so the tax needs no apportionment."),
    N(r"\item \textbf{Opposite-Side (\textit{Moore} Does Not Apply): A Mark-to-Market Tax on Individual Holdings.}", glue=" "),
    S(r"Congress enacts an unapportioned annual 2\% ``Billionaire Appreciation Tax'' on the year-over-year increase in fair market value of unsold real estate, fine art, and publicly traded equities held by individuals worth over \$100 million.", glue=" "),
    S(r"Unlike \textit{Moore}, \textit{no entity has realized any income}---the tax targets pure unrealized appreciation of property held directly by individuals. Under \textit{Moore}'s explicit reservation, pass-through attribution cannot save this statute. Four Justices (Barrett, Alito, Thomas, Gorsuch) are already on record that unapportioned taxes on unrealized appreciation violate the Sixteenth Amendment and Direct Tax Clause; the Government would need all five remaining Justices (including Roberts and Kavanaugh, who stressed the Government's own concessions) either to reject a constitutional realization requirement (per Jackson) or to recharacterize the levy as an indirect excise."),
    N(r"\item \textbf{Opposite-Side (Arbitrary Attribution): Taxing a Corporation's Customers on Its Profits.} Congress provides that the undistributed profits of any foreign corporation shall be attributed to the U.S.\ persons who bought its products during the year, in proportion to their purchases, and taxed to them. A U.S.\ retailer that bought inventory from a foreign manufacturer, and owns none of its stock, is assessed tax on part of the manufacturer's earnings. \textit{Moore} permits Congress to attribute an entity's realized income to the entity's \emph{shareholders or partners}; it does not permit attribution to strangers to the entity. The Court also noted that Due Process bars arbitrary attribution, citing \textit{Burnet v.\ Wells}, 289 U.S.\ 670 (1933). Because the retailer has no ownership interest and no claim to the profits, the attribution is arbitrary and the tax cannot be sustained on \textit{Moore}'s reasoning."),
    N(r"\item \textbf{Fence-Sitter (How Far Attribution Reaches): A Pass-Through Tax on Shareholders of Public Companies.}", glue=" "),
    S(r"Congress repeals the corporate income tax (\S\ 11) for publicly traded U.S.\ corporations and enacts a pass-through tax attributing each corporation's realized annual net profits pro rata to every U.S.\ shareholder owning at least one share on December 31.", glue=" "),
    S(r"Under Kavanaugh's majority (see footnote 8 rejecting Barrett's domestic/widely held distinction), this satisfies pass-through attribution of entity-realized income, though challengers would press Due Process arbitrariness (lack of shareholder control or ability to compel dividends) and invoke Barrett's concurrence plus Thomas's dissent (4 Justices) to argue corporate form cannot be pierced for passive retail investors.", glue=" "),
    N(r"Because the majority decided only the controlled-foreign-corporation tax before it, and four Justices doubted that corporate form may be disregarded for passive investors, the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(P, frm=r"  \item \textbf{Doctrinal Minimalism", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: caption, docket number, Briefing Book placement, cert-grant date, SupremeCourt.gov page-proof link (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section in full (no Subsequent Developments subsection): the head-counting paragraph (commentary, not a later decision) and the 'Through 2026' tracks (2025 tax legislation, scholarship, S. 4490, state wealth-tax proposals, a state-court amicus brief). None is a later decision applying, narrowing, or extending Moore.",
  "Exam Hypotheticals labels and 'Analysis:' labels; their text is reused in Examples 3 and 5.",
 ],
 "notes": ["Example 5 adds one new closing sentence explaining why the moved Hypothetical 1 analysis is genuinely uncertain."],
}

emit(__file__, FILL)
