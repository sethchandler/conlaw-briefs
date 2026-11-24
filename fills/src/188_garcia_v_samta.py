"""Fill for 188_garcia_v_samta. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/469/528/"
FTC = r"Blackmun, J., for the Court"

# NOTE: tools/manual_quotes.txt lists "<stem>.tex", so check_brief.py's MANUAL set never matches a
# stem and normalize_quotes.py always runs on the output. Each quote block is therefore built with
# its attribution after "---" inside the block; normalize_quotes.py then moves the attribution to a
# Group A "\noindent ---" line. Quote text is moved verbatim with S().
def QB(quote, *attrib):
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue=" "), N("---", glue=" "), *attrib, N(r"\end{quote}")]

QUOTES = (
  QB(r"``We therefore now reject, as unsound in principle and unworkable in practice, a rule of state immunity from federal regulation that turns on a judicial appraisal of whether a particular governmental function is `integral' or `traditional.' Any such rule leads to inconsistent results at the same time that it disserves principles of democratic self-governance, and it breeds inconsistency precisely because it is divorced from those principles.''",
     S(FTC + r", \href{https://supreme.justia.com/cases/federal/us/469/528/}{469 U.S. at 546--547}", glue="\n"))
  + QB(r"``Apart from the limitation on federal authority inherent in the delegated nature of Congress' Article I powers, the principal means chosen by the Framers to ensure the role of the States in the federal system lies in the structure of the Federal Government itself.''",
     S(FTC, glue=""), N(r", 469 U.S.\ at 550", glue="\n"))
  + QB(r"``State sovereign interests, then, are more properly protected by procedural safeguards inherent in the structure of the federal system than by judicially created limitations on federal power.''",
     S(FTC, glue=""), N(r", 469 U.S.\ at 552", glue="\n"))
  + QB(r"``Nonetheless, against this background, we are convinced that the fundamental limitation that the constitutional scheme imposes on the Commerce Clause to protect the `States as States' is one of process, rather than one of result. Any substantive restraint on the exercise of Commerce Clause powers must find its justification in the procedural nature of this basic limitation, and it must be tailored to compensate for possible failings in the national political process, rather than to dictate a `sacred province of state autonomy.'\,''",
     S(FTC + r", \href{https://supreme.justia.com/cases/federal/us/469/528/}{469 U.S. at 554}", glue="\n"))
  + QB(r"``The States' role in our system of government is a matter of constitutional law, not of legislative grace.''",
     N(r"Powell, J., dissenting, 469 U.S.\ at 567", glue="\n"))
  + QB(r"``The Court today surveys the battle scene of federalism and sounds a retreat.''",
     N(r"O'Connor, J., dissenting, 469 U.S.\ at 580", glue="\n"))
  + QB(r"``I do not think it incumbent on those of us in dissent to spell out further the fine points of a principle that will, I am confident, in time again command the support of a majority of this Court.''",
     N(r"Rehnquist, J., dissenting, 469 U.S.\ at 580 (\href{" + J + r"}{Justia})", glue="\n"))
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Overruling \textit{National League of Cities v. Usery}, the Court held 5--4 that a city transit authority must obey the Fair Labor Standards Act's wage and overtime rules: ``traditional governmental functions'' immunity is unworkable, and the States are protected mainly by the political process, not by judicially defined enclaves of sovereignty (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to=r"\subsection{Procedural History}", strip=r"\subsection{Factual Background and Statutory Evolution}")],
  "Procedural History": [SEC("Facts and Procedural History", frm=r"\subsection{Procedural History}", strip=r"\subsection{Procedural History}")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{5--4} vote, expressly overruling \textit{National League of Cities v. Usery}. The case was argued March 19, 1984, reargued October 1, 1984, and decided February 19, 1985 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Blackmun delivered the opinion of the Court, joined by Justices Brennan, White, Marshall, and Stevens.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Powell filed a dissenting opinion, joined by Chief Justice Burger and Justices Rehnquist and O'Connor (469 U.S.\ at 557--579). Justice Rehnquist filed a dissenting opinion (469 U.S.\ at 579--580). Justice O'Connor filed a dissenting opinion, joined by Justices Powell and Rehnquist (469 U.S.\ at 580--589).
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Blackmun)}"),
    N(r"\subsubsection{Unworkability and Democratic Flaws of ``Traditional Governmental Functions''}"),
    SEC("Reasoning", frm="Because SAMTA conceded", to=r"\subsection{The Political Safeguards"),
    N(r"\subsubsection{The Political Safeguards of Federalism}"),
    SEC("Reasoning", frm="Rejecting ``freestanding"),
    N(r"\subsection{Dissenting Opinion (Justice Powell)}"),
    SEC("Concurring and Dissenting", frm="Powell condemned", to=r"\item \textbf{Justice Rehnquist"),
    N(r"\subsection{Dissenting Opinion (Justice Rehnquist)}"),
    SEC("Concurring and Dissenting", frm="Joining both Powell", to=r"\item \textbf{Justice O'Connor"),
    N(r"\subsection{Dissenting Opinion (Justice O'Connor)}"),
    SEC("Concurring and Dissenting", frm="Joining Powell, O'Connor grounded", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Reaffirmed for Generally Applicable Rules:}", glue=" "),
    S(r"The Court also reaffirmed \textit{Garcia}'s core in \href{https://supreme.justia.com/cases/federal/us/485/505/}{\textit{South Carolina v. Baker}}, 485 U.S. 505 (1988) (upholding tax rules pressuring States to issue registered bonds), and \href{https://supreme.justia.com/cases/federal/us/528/141/}{\textit{Reno v. Condon}}, 528 U.S. 141 (2000) (upholding the Driver's Privacy Protection Act because it regulated States as database suppliers rather than as sovereign lawmakers)."),
    SEC("Doctrinal Significance", frm=r"\item \textbf{Anti-Commandeering:}", to=r"\item \textbf{Sovereign Immunity"),
    N(r"\item \textbf{Limits on Enforcing the FLSA Against States:}", glue=" "),
    S(r"Under \href{https://supreme.justia.com/cases/federal/us/527/706/}{\textit{Alden v. Maine}}, 527 U.S. 706 (1999), Article~I cannot abrogate a nonconsenting State's sovereign immunity from private FLSA damages suits in state court, limiting enforcement to federal suits, injunctive relief, or municipal entities like SAMTA."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Generally Applicable Rule Valid): Bus-Fleet Electrification.}", glue=" "),
    S(r"Congress passes a Commerce Clause statute whose Section~1 requires all public and private operators of 25+ passenger buses to electrify half their fleets by 2030, and whose Section~2 orders state DMVs to audit private operators and revoke registrations for non-compliance.", glue=" "),
    N(r"As to Section~1:", glue=" "),
    S(r"Section~1 survives under \textit{Garcia} and \href{https://supreme.justia.com/cases/federal/us/528/141/}{\textit{Reno}} as a generally applicable regulation of market participants (subject to \href{https://supreme.justia.com/cases/federal/us/527/706/}{\textit{Alden}} on private damages suits against States)."),
    N(r"\item \textbf{Same-Side (Generally Applicable Rule Valid): Federal Shift Caps for Police and Firefighters.}", glue=" "),
    S(r"Suppose Congress caps maximum shift lengths for municipal police and firefighters.", glue=" "),
    S(r"If framed as a generally applicable safety rule covering both public and private emergency/security workers, it is valid; States must seek statutory relief through Congress (though if it targets public agencies exclusively, States may invoke the exclusivity question reserved in \textit{Reno}, 528 U.S. at 151).", glue=" "),
    N(r"Under the overruled \textit{National League of Cities} framework and the \textit{Garcia} dissents, by contrast:", glue=" "),
    S(r"The law would be struck down regardless of general applicability, because police and fire services were paradigmatic ``traditional governmental functions'' (426 U.S. at 851), and dictating shift structures directly displaces core local fiscal and operational choices."),
    N(r"\item \textbf{Opposite-Side (Commandeering): State DMVs as Federal Enforcers.} Same statute, but a State challenges Section~2.", glue=" "),
    S(r"Section~2 violates the anti-commandeering rule of \href{https://supreme.justia.com/cases/federal/us/505/144/}{\textit{New York}} and \href{https://supreme.justia.com/cases/federal/us/521/898/}{\textit{Printz}} by conscripting state executive agencies to enforce a federal regulatory scheme."),
    N(r"\item \textbf{Opposite-Side (Sovereign Immunity): Private Overtime Suits Against a State in Its Own Courts.} Congress amends the FLSA to authorize state employees to sue their nonconsenting State for back overtime and liquidated damages in the State's own courts. A group of state prison guards sues, and the State moves to dismiss. Under \textit{Garcia}, the guards are covered: the FLSA's wage and overtime rules validly bind the State as an employer. But \textit{Garcia} answers only whether Congress may impose the obligation, not how it may be enforced. Under \href{https://supreme.justia.com/cases/federal/us/527/706/}{\textit{Alden v. Maine}}, 527 U.S. 706 (1999), Congress's Article~I powers cannot subject a nonconsenting State to private damages suits in its own courts, so the suit must be dismissed. The guards must look to a suit by the Secretary of Labor, injunctive relief, or the State's consent."),
    N(r"\item \textbf{Fence-Sitter (Rules Aimed Only at States): Federal Pay and Hours Rules for State Judicial Staff.} Invoking the Commerce Clause, Congress sets minimum salaries and maximum weekly hours for state-court law clerks and legislative staff, positions that exist only in state government; no private employer is covered. \textit{Garcia} points toward validity: it rejected judicial enclaves of state immunity and left the States to protect themselves in Congress, and the statute regulates the States as employers rather than ordering them to legislate or enforce federal law, so it does not commandeer. But the statute is not generally applicable, which is the question \textit{Reno} expressly reserved, and it reaches the internal staffing of state courts and legislatures, the kind of core state structure for which \textit{Gregory v. Ashcroft}, 501 U.S. 452 (1991), demands an unmistakably clear statement. Whether a regulation aimed solely at States' own governing institutions survives is unsettled."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"    \item \textbf{Erosion", to=r"\end{itemize}")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "Case Metadata: consolidated Donovan caption, parallel cites, docket numbers, provisions line, Cornell CONAN link.",
  "Key Quotations: lead-in sentence ('All quotations below are verified verbatim ...') and the bold quotation labels; the two-part quote 2 and the three dissent quotes split into separate quote blocks with their pin cites.",
  "Legacy section: FLSA 1985 amendments/Moreau sentence; 'Rehnquist and Roberts Courts' framing paragraph; Gregory v. Ashcroft clear-statement item (Gregory still cited in Example 5); NFIB/Bond sentences. Kept: Baker/Reno reaffirmance, anti-commandeering item (New York, Printz, Murphy, Haaland), Alden sentence.",
  "Hypothetical 2's 'Opposite Side' analysis is reused inside Example 2 to show how the overruled test would have come out.",
 ],
 "notes": ["Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection."],
}

emit(__file__, FILL)
