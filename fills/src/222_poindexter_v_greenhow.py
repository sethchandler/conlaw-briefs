"""Fill for 222_poindexter_v_greenhow. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/114/270/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"In the lead \textit{Virginia Coupon Case}, a 5--4 Court held that Virginia's tax-receivable bond coupons were valid contracts, not forbidden bills of credit; that the 1882 law refusing them impaired the obligation of contracts; and that a taxpayer could sue the collector who seized his desk because an officer enforcing a void statute is not the State (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="On April 26, 1883, Poindexter brought")],
  "Procedural History": [SEC("Facts and Procedural History", frm="On April 26, 1883, Poindexter brought")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{5--4} vote. The case was argued on March 20 and 23--25, 1885, and decided on April 20, 1885 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/114/270}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Matthews delivered the opinion of the Court, joined by Justices Field, Harlan, Woods, and Blatchford.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinion:} Justice Bradley filed a dissenting opinion, joined by Chief Justice Waite and Justices Miller and Gray, reported at \href{https://supreme.justia.com/cases/federal/us/114/325/}{114 U.S. 330} following \textit{Marye v.\ Parsons}.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Matthews)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Bradley)}"),
    SEC("Concurring and Dissenting", frm="Justice Bradley dissented"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Bills of Credit:}", glue=" "),
    S(r"First, its Bills of Credit holding---later reinforced in \href{https://www.law.cornell.edu/supremecourt/text/177/66}{\textit{Houston \& Texas Central Railroad Co. v. Texas}}, 177 U.S. 66 (1900)---cemented a narrow, intent-based definition of Article I, \S~10's monetary bar, ensuring states could freely issue municipal and state bonds, tax-anticipation warrants, and coupons without triggering federal invalidation."),
    N(r"\item \textbf{The Officer-Suit Exception:}", glue=" "),
    S(r"Its ``stripping'' theory---that an officer enforcing an unconstitutional state statute loses sovereign immunity---was refined in \href{https://www.law.cornell.edu/supremecourt/text/123/443}{\textit{In re Ayers}}, 123 U.S. 443 (1887) (barring suits that merely seek to compel state contract performance), and culminated in \href{https://supreme.justia.com/cases/federal/us/209/123/}{\textit{Ex parte Young}}, 209 U.S. 123 (1908), which directly cited \textit{Poindexter} to authorize prospective federal injunctions against state officials enforcing unconstitutional laws."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Officer Suit Allowed): Refusing Bond Coupons and Levying on a Company's Property.} A State issues twenty-year bonds whose interest coupons, by statute, are receivable for all state taxes at maturity. A later legislature forbids revenue officers to accept the coupons. A manufacturer tenders matured coupons for its franchise tax; the state revenue officer rejects them and seizes the company's delivery truck for nonpayment. The company sues the officer personally to recover the truck. Under \textit{Poindexter}, the receivability promise is a contract the later statute unconstitutionally impairs, the tender is equivalent to payment, and the void statute gives the officer no authority. He is therefore answerable as an individual wrongdoer, and the Eleventh Amendment does not bar the suit (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Not a Bill of Credit): Tax-Anticipation Warrants Receivable at Maturity.} To cover a seasonal cash shortfall, a State issues interest-bearing warrants in \$5{,}000 denominations, payable in one year and receivable for state taxes only once they mature. When the State later tries to disown the warrants by arguing that they were unconstitutional bills of credit, a holder sues. The argument fails under \textit{Poindexter}. The warrants are evidence of debt designed to be paid at maturity, not paper designed to circulate from hand to hand as money; their large denomination and maturity-only receivability confirm that the State did not intend them as currency. They are therefore valid obligations the State must honor."),
    N(r"\item \textbf{Opposite-Side (Likely Bills of Credit): Small-Denomination Tax Credit Notes.}", glue=" "),
    SEC("Pedagogical", frm="Facing a severe budget shortfall, State X", to=r"\textit{Analysis:}", glue=" "),
    SEC("Pedagogical", frm=r"Under \textit{Craig} and \textit{Poindexter}, the threshold issue"),
    N(r"\item \textbf{Opposite-Side (Suit Barred): Ordering the Treasurer to Pay Overdue Coupons.} After a State defaults on its bonds, a bondholder sues the state treasurer in federal court for an order directing him to pay the overdue interest coupons out of the state treasury. Unlike Poindexter, the bondholder does not complain that an officer has committed an affirmative wrong against his property; he seeks to compel the State itself to perform its contract with public funds. \textit{Poindexter} expressly distinguished such suits, which \textit{Louisiana v.\ Jumel}, 107 U.S.\ 711 (1883), held barred, and \textit{In re Ayers} confirmed that a suit seeking only to compel performance of a state contract is a suit against the State. The Eleventh Amendment bars it."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): An Injunction Ordering Collectors to Accept Coupons.} Instead of waiting for a seizure, a taxpayer holding matured coupons sues the state tax commissioner in federal court for an injunction requiring all collectors to accept the coupons for taxes in the future. \textit{Poindexter} supports the claim on the merits, and \textit{Ex parte Young}, which built on \textit{Poindexter}, permits prospective injunctions against officials enforcing unconstitutional laws. But the order would require officials to take affirmative action that compels the State to honor its contract, which looks like the specific performance \textit{Poindexter} and \textit{In re Ayers} treated as a suit against the State. Whether a court characterizes the relief as stopping enforcement of a void law or as enforcing the State's contract would likely decide the case."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\textbf{Pedagogical Critique:}", to=r"\textbf{``Opposite Side'' Contrast", strip=r"\textbf{Pedagogical Critique:} ")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: parallel citations, court/posture line, Briefing Book placement, constitutional-provisions line (Justia and Cornell links kept in Judicial Votes).",
  "Separate-opinions sentence 'No separate concurring opinions were filed.' (stated in Judicial Votes).",
  "Legacy section: framing sentences ('crossroads of three enduring federalism doctrines', 'Second, Poindexter is a foundational pillar...'); the 'Through 2026' sentence listing Treasure Salvors, Pennhurst, Coeur d'Alene, Seminole Tribe, Alden, and Whole Woman's Health (general Ex parte Young limits, not developments of Poindexter's holding); the Contracts Clause paragraph (Sveen v. Melin - general modern Contracts Clause test). Kept: Houston & Texas Central sentence and In re Ayers / Ex parte Young sentence.",
  "Exam Hypotheticals: 'Opposite Side' Contrast with Craig v. Missouri - a description of a decided case, not a hypothetical; its content is reflected in Example 3.",
 ],
}

emit(__file__, FILL)
