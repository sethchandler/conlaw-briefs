"""Fill for 221_craig_v_missouri. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/29/410/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"For a 4--3 Court, Chief Justice Marshall held that Missouri's interest-bearing loan-office certificates, issued on the faith of the state and designed to circulate as money, were unconstitutional ``bills of credit'' under Article I, Section 10, even though they were not legal tender, so a note given for them was void (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="After they defaulted, Missouri sued")],
  "Procedural History": [SEC("Facts and Procedural History", frm="After they defaulted, Missouri sued")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the Supreme Court of Missouri by a \textbf{4--3} vote. The case was argued on March 2--3, 1830, and decided on March 12, 1830 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Marshall delivered the opinion of the Court, joined by Justices Duvall, Story, and Baldwin.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justices Johnson, Thompson, and McLean each filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Marshall)}"), SEC("Reasoning"),
    N(r"\subsection{Justice Baldwin's Later Explanation of His Vote}"),
    SEC("Concurring and Dissenting", frm="No separate concurring", to="All three dissenters"),
    N(r"\subsection{Dissenting Opinion (Justice Johnson)}"), N("Justice Johnson", glue=" "),
    SEC("Concurring and Dissenting", frm="Offered two functional", to=r"  \item \textbf{Justice Smith Thompson", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Thompson)}"), N("Justice Thompson", glue=" "),
    SEC("Concurring and Dissenting", frm="Defined a constitutional bill", to=r"  \item \textbf{Justice John McLean", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice McLean)}"), N("Justice McLean", glue=" "),
    SEC("Concurring and Dissenting", frm="Argued that a bill of credit must", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Narrowed by \textit{Briscoe}:}", glue=" "),
    SEC("Doctrinal Significance", frm="After Marshall's death", to="Later nineteenth-century decisions"),
    N(r"\item \textbf{Later Narrowing Decisions:}", glue=" "),
    SEC("Doctrinal Significance", frm=r"In \href{https://www.law.cornell.edu/supremecourt/text/114/270}", to="Although the Civil War"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Unconstitutional): Faith-Backed Fiscal Liquidity Certificates.}", glue=" "),
    S(r"Facing a severe budget impasse, the State of Ozark enacts a statute directing its State Treasurer to print \$500 million in ``Fiscal Liquidity Certificates'' in \$5, \$20, and \$100 bearer denominations. The certificates are not legal tender for private debts, but they are receivable at face value for all state taxes and public-university tuition, and the statute pledges ``the full faith and credit of the State of Ozark'' for redemption in five years.", glue=" "),
    S(r"Unconstitutional under \textit{Craig}. Even without private legal-tender status or the label ``bills of credit,'' the certificates are issued directly by state officers, backed by the state's faith, and structured in small bearer denominations to circulate as a common medium of exchange."),
    N(r"\item \textbf{Same-Side (Unconstitutional): Interest-Bearing Scrip Backed by a Dedicated Fund.} During a cash shortage, a State's comptroller pays state employees and contractors with interest-bearing scrip in \$1, \$5, and \$10 denominations, payable to bearer and receivable for all state taxes and fees. The statute pledges the revenue of the state lottery to redeem the scrip within three years. The State argues that interest makes the scrip's value fluctuate and that a dedicated fund, not bare state credit, stands behind it. Those were the arguments of Justices Johnson and Thompson in dissent, and the \textit{Craig} majority rejected them: Missouri's certificates also bore interest and rested on a pledged fund. Because the scrip is issued directly by state officers in small denominations designed to circulate as money, it is a prohibited bill of credit."),
    N(r"\item \textbf{Opposite-Side (Constitutional): Ordinary State Bonds Sold to Investors.} To finance highway construction, a State sells \$800 million in twenty-year general-obligation bonds in \$5,000 denominations to banks, pension funds, and other investors, pledging its full faith and credit to repay them with interest. A taxpayer argues that paper issued on the faith of the State is a bill of credit under \textit{Craig}. The argument fails. Marshall explained that the Bills of Credit Clause does not bar ordinary state borrowing or contracts to pay for goods and services; it forbids paper intended to circulate through the community for its ordinary purposes as money. Large-denomination investment bonds are a loan to the State, not a medium of exchange, so they are not bills of credit even though they rest on the State's credit."),
    N(r"\item \textbf{Opposite-Side (Constitutional Under \textit{Briscoe}): Notes of a State-Owned Corporate Bank.} A State charters a bank, owned entirely by the State and governed by directors chosen by the legislature, that can sue and be sued in its own name. The bank lends its own small-denomination notes to borrowers, and the notes circulate as currency; they are redeemable from the bank's own capital and are not issued on the faith of the State. Under \textit{Briscoe v.\ Bank of Commonwealth of Kentucky}, 36 U.S.\ (11 Pet.) 257 (1837), the notes are not bills of credit because a separately incorporated, suable entity issues them on its own corporate funds. Justice Story's \textit{Briscoe} dissent, invoking \textit{Craig}'s rule that the Constitution prohibits things rather than names, would treat them as an indirect emission, but \textit{Briscoe} remains the governing rule."),
    N(r"\item \textbf{Fence-Sitter (Unsettled): A Reserve-Backed State Digital Token.}", glue=" "),
    S(r"By contrast, suppose the State of Frontier charters an independent, suable public corporation to issue ``Frontier Digital Dollars''---blockchain tokens redeemable on demand for \$1.00 U.S., backed 102\% by segregated U.S. dollars and short-term Treasury bills held in trust, with an explicit statutory disclaimer that neither the state's general faith nor its taxing power backs the tokens.", glue=" "),
    S(r"Under \textit{Briscoe} and \textit{Houston \& Texas Central}, the tokens likely survive Article I, Section 10 scrutiny because they are issued by a separately suable corporate instrumentality, backed by a dedicated, fully liquid reserve fund rather than sovereign credit, and redeemable on demand. Conversely, a functionalist challenger invoking Marshall's ``names, and not things'' principle in \textit{Craig} and Story's \textit{Briscoe} dissent would argue that a state-created, state-governed entity minting a circulating digital medium designed for everyday commerce and taxes is an impermissible indirect emission of bills of credit.", glue=" "),
    N(r"The Court has never applied \textit{Craig} or \textit{Briscoe} to a digital instrument, so which line controls is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Formalism", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: full caption, Chapter line, provisions line (Justia link kept).",
  "Separate opinions: lead-in sentence 'All three dissenters in Craig wrote separately...' (each dissent has its own subsection).",
  "Legacy section: opening framing sentence; closing paragraph on precious-metal tender statutes and Wyoming's 2026 Frontier Stable Token (commentary and non-judicial developments; its question survives in the Fence-Sitter). Kept: Briscoe paragraph; Poindexter v. Greenhow and Houston & Texas Central sentences.",
  "Exam Hypothetical 1 and 2: 'Analysis:' labels (their text is reused in Examples 1 and 5).",
 ],
}

emit(__file__, FILL)
