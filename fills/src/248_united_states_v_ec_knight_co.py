"""Fill for 248_united_states_v_ec_knight_co. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/156/1/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"The Sugar Trust's purchase of four Philadelphia refineries gave it control of about 98\% of American sugar refining, yet the Court held 8--1 that the Sherman Act could not reach it because manufacturing is not commerce and affects interstate commerce only indirectly; Justice Harlan dissented alone, and the manufacture/commerce line was later repudiated (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The United States filed a bill")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The United States filed a bill")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the dismissal of the government's bill by an \textbf{8--1} vote. The case was argued on October 24, 1894, and decided on January 21, 1895 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/156/1}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Fuller delivered the opinion of the Court, joined by Justices Field, Gray, Brewer, Brown, Shiras, Jackson, and White.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinion:} Justice Harlan dissented alone.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Fuller)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Harlan)}"),
    SEC("Concurring and Dissenting", strip=r"\textbf{Justice John Marshall Harlan (dissenting):} "),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"\item \textbf{Early Erosion", to=r"\item \textbf{Enduring Federalism"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Beyond the Commerce Power): Local Possession of a Homemade Tool.}", glue=" "),
    S(r"Suppose instead that Congress enacts a federal statute criminalizing purely local, noncommercial possession of a homemade tool within 500 feet of a community park, with no jurisdictional nexus to interstate commerce and no broader regulation of an interstate commercial market, arguing that local violence indirectly reduces interstate tourism.", glue=" "),
    S(r"Here, the federalism principle animating \textit{E.C. Knight} prevails in modern dress: under \textit{Lopez} and \textit{Morrison}, Congress cannot aggregate attenuated, indirect effects of \textit{noneconomic} intrastate conduct without converting the Commerce Clause into a general police power reserved to the states."),
    N(r"\item \textbf{Same-Side (Beyond the Commerce Power): Compelling Purchases of Domestic Products.} To revive domestic manufacturing, Congress requires every adult who does not already own one to buy an American-made electric bicycle by a set date, reasoning that the combined decisions of millions of nonbuyers substantially affect the interstate market. \textit{E.C. Knight}'s manufacture/commerce line is long gone, so the challenge cannot rest on the fact that the bicycles are manufactured. But the Court's modern effort to define enforceable outer limits supplies one: in \href{https://supreme.justia.com/cases/federal/us/567/519/}{\textit{NFIB v. Sebelius}, 567 U.S. 519 (2012)}, a majority of Justices concluded that the Commerce Clause lets Congress regulate existing commercial activity but not compel individuals to enter commerce. The mandate would likely exceed the commerce power, though Congress might pursue the same goal through its taxing or spending powers."),
    N(r"\item \textbf{Opposite-Side (Federal Power Reaches It): A Chip-Fabrication Monopoly.}", glue=" "),
    S(r"A Delaware holding company acquires four intrastate semiconductor fabrication plants in Ohio, giving it 95\% of U.S. production of a chip shipped to automakers nationwide. The Department of Justice sues under the Sherman Act to unwind the merger.", glue=" "),
    S(r"Under \textit{E.C. Knight}'s 1895 framework, the defendants would argue that chip fabrication is ``manufacture,'' not ``commerce,'' and affects interstate trade only indirectly. Under modern doctrine (\textit{Jones \& Laughlin}, \textit{Wickard}, \textit{Raich}), the government easily prevails: chip manufacturing is quintessential economic activity whose monopolization substantially affects interstate commerce."),
    N(r"\item \textbf{Opposite-Side (Federal Power Reaches It): Price-Fixing at a Local Grain Elevator.} Grain-elevator operators in a single Kansas county agree on the prices they will pay farmers for wheat, nearly all of which the elevators then ship by rail to mills in other States. The operators argue that their agreement concerns only local purchases completed before any interstate shipment, the same kind of point that defeated the government in \textit{E.C. Knight}. The argument fails. Even before the New Deal, \href{https://supreme.justia.com/cases/federal/us/196/375/}{\textit{Swift \& Co. v. United States}, 196 U.S. 375 (1905)}, upheld a Sherman Act injunction against meatpackers' price-fixing at local stockyards because the livestock moved in a current of interstate commerce. Under modern doctrine the case is easier still: price-fixing is economic activity whose effect on the interstate wheat market is substantial, so Congress may reach it."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Homemade Firearms Within a National Market Scheme.} Congress enacts a comprehensive statute regulating the interstate market in firearm parts and kits, and, to keep that market closed to untraceable weapons, also bans the possession of any homemade firearm lacking a serial number, even one built entirely from materials found within a single State and never sold. A hobbyist charged with possessing such a gun argues that, as in \textit{Lopez}, mere possession is noneconomic. The government relies on \textit{Gonzales v. Raich}, 545 U.S. 1 (2005), which upheld a ban on home-grown marijuana as an essential part of a comprehensive scheme regulating an interstate market. Because the possession is noneconomic yet the statute is part of a broad market regulation, the case falls between \textit{Lopez} and \textit{Raich}, and the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\textbf{Pedagogical Critique:}", to=r"\textbf{Exam Hypothetical")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, chapter line, lower-court line, provisions list (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory paragraph (high-water-mark characterization; Hammer and Carter Coal mention); 'Enduring Federalism Echoes Through 2026' item (Lopez, Morrison, Raich, NFIB as later federalism cases, not applications of E.C. Knight's holding; Lopez, Morrison, Raich, and NFIB are used in the examples). Kept: 'Early Erosion and Complete Repudiation' item (Swift, Standard Oil, Jones & Laughlin, Wickard).",
  "Exam Hypothetical: its heading, 'Analysis:' and 'Contrast:' labels; both fact patterns reused verbatim (Examples 3 and 1).",
 ],
 "notes": [],
}

emit(__file__, FILL)
