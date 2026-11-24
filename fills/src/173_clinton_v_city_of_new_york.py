"""Fill for 173_clinton_v_city_of_new_york. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/524/417/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"The Court held 6--3 that the Line Item Veto Act violates the Presentment Clause: when the President canceled a Medicaid spending provision and a targeted tax benefit after signing them into law, he in effect repealed parts of duly enacted statutes without bicameral passage and presentment (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Two sets of plaintiffs filed")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Two sets of plaintiffs filed")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the District Court by a \textbf{6--3} vote. The case was argued on April 27, 1998, and decided on June 25, 1998 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supct/html/97-1374.ZO.html}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Stevens delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices Kennedy, Souter, Thomas, and Ginsburg.
    \item \textbf{Concurring Opinion:} Justice Kennedy filed a concurring opinion (524 U.S. at 449).
    \item \textbf{Concurring in Part and Dissenting in Part:} Justice Scalia filed an opinion concurring in part and dissenting in part, joined by Justice O'Connor, and joined by Justice Breyer as to Part III (524 U.S. at 453).
    \item \textbf{Dissenting Opinion:} Justice Breyer filed a dissenting opinion, joined by Justices O'Connor and Scalia as to Part III (524 U.S. at 469).
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Stevens)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Kennedy)}"), N("Justice Kennedy", glue=" "),
    SEC("Concurring and Dissenting", frm="Replied directly", to=r"  \item \textbf{Justice Scalia", lc=True),
    N(r"\subsection{Opinion Concurring in Part and Dissenting in Part (Justice Scalia)}"), N("Justice Scalia", glue=" "),
    SEC("Concurring and Dissenting", frm="Disagreed on statutory", to=r"  \item \textbf{Justice Breyer", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Breyer)}"), N("Justice Breyer", glue=" "),
    SEC("Concurring and Dissenting", frm="Agreed appellees had standing", to=r"\end{itemize}", lc=True),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Cancellation Invalid): An Earmark-Cancellation Statute.} Congress authorizes the President, within ten days after signing any appropriations act, to cancel any congressionally directed spending item (an earmark) that he finds wasteful, with the canceled item having no legal force unless Congress passes a disapproval bill. A city whose earmarked grant for a water-treatment plant is canceled sues. The statute repeats the defect in the Line Item Veto Act: the President acts after the bill has become law, strikes only part of it, and relies on the same facts Congress had just weighed. Under \textit{Clinton}, that is a unilateral partial repeal outside Article I, \S~7, and the city's lost grant is the kind of concrete injury that gave New York standing (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Cancellation Invalid): Suspending Targeted Tax Credits.} A statute empowers the Secretary of the Treasury, within thirty days after any tax bill is enacted, to declare that any tax credit benefiting fewer than one hundred taxpayers shall not take effect if the Secretary concludes it is poor policy. A manufacturer that had negotiated a plant purchase in reliance on a newly enacted credit sues after the credit is voided. The power operates on enacted text, is discretionary, and rests on a policy disagreement with Congress rather than on any later-arising contingency, so it fails the three distinctions the majority drew from \textit{Field v. Clark}. Like the cancellation of \S~968 that injured Snake River, it is the functional equivalent of repealing part of a statute, and it must fall under \textit{Clinton}."),
    N(r"\item \textbf{Opposite-Side (Valid): Expedited Rescission Through Bicameralism and Presentment.} Congress adopts procedural rules under which the President may send a package of proposed spending rescissions within days of signing an appropriations act; each House must hold a prompt up-or-down vote without amendment, and a rescission takes effect only if both Houses pass the rescission bill and the President signs it. Nothing in \textit{Clinton} forbids this. The rescission becomes law exactly as Article I, \S~7 requires---passed by both Houses and presented to the President---so no statute is altered by the President alone. The fast-track rules simply change how Congress schedules its own votes, which each House may do in setting its rules of proceedings."),
    N(r"\item \textbf{Opposite-Side (Valid): Contingent Tariff Retaliation.} A trade statute sets duties on imported steel and directs the President to raise them by a fixed percentage on imports from any country that he finds, after enactment, has imposed discriminatory duties on American goods. A foreign exporter argues that the statute is a line-item veto in disguise. It is not. As in \href{https://supreme.justia.com/cases/federal/us/143/649/}{\textit{Field v. Clark}, 143 U.S. 649 (1892)}, the President's action depends on facts arising after enactment, he must act once he finds the contingency, and he carries out the policy Congress chose rather than rejecting it. \textit{Clinton} expressly distinguished this kind of contingent legislation, so the statute survives a Presentment Clause challenge."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Recasting Cancellation as Permissive Spending.}", glue=" "),
    SEC("Pedagogical", frm="To curb deficits without", to=r"\textit{Analysis:}", glue=" "),
    SEC("Pedagogical", frm="The Government will invoke", to=r"\textbf{``Opposite Side'' Contrast:}", glue=" "),
    N(r"The outcome is uncertain because the majority conceded (524 U.S. at 446--447) that Congress may appropriate discretionary ``sums not exceeding'' a stated amount, yet a directive that permanently blocks an earmarked item resembles the cancellation \textit{Clinton} struck down; the case may turn on whether a court treats the statute as a delegation of spending discretion or as a partial repeal under another label."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{Exam Hypothetical:}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, duplicate \\url{} printouts (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section in full: introductory paragraph (Chadha mirror-image framing); Impoundment Control Act item (2025 executive impoundment arguments) and Pocket Rescissions item (Department of State v. AIDS Vaccine Advocacy Coalition emergency stay; 2026 rescission and GAO determination; SCOTUSblog and HLR Blog commentary) - these concern the ICA and emergency-docket practice rather than a decision that overruled, narrowed, extended, or applied Clinton's holding.",
  "Exam Hypothetical: 'Opposite Side' Contrast (Clinton vs. Field v. Clark / J.W. Hampton) - an exam tip, not a fact pattern; its point is covered by Example 4.",
 ],
 "notes": ["Neon's exam hypothetical is reused as the Fence-Sitter with one new closing sentence explaining the uncertainty."],
}

emit(__file__, FILL)
