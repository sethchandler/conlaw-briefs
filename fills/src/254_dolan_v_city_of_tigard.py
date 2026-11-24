"""Fill for 254_dolan_v_city_of_tigard. See tools/fillkit.py."""
import os
from fillkit import *

ORIG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "originals", "briefs",
                         "254_dolan_v_city_of_tigard.tex"), encoding="utf-8").read()

def X(a, b, glue=None):
    i = ORIG.index(a); j = ORIG.index(b, i)
    return S(ORIG[i:j].strip(), glue=glue)

J = "https://supreme.justia.com/cases/federal/us/512/374/"
JH = r"\href{https://supreme.justia.com/cases/federal/us/512/374/}"
CD = "Concurring and Dissenting"
P = "Pedagogical"

def Q(first, speaker, pin):
    # Speaker and pin cite moved verbatim from the original's label; attribution inside the block so
    # normalize_quotes.py converts it to a Group A "\noindent ---" line.
    i = ORIG.index(first); j = ORIG.index(r"\end{quote}", i)
    return [N(r"\begin{quote}", glue="\n"), S(ORIG[i:j].strip(), glue="\n"), N(r"---", glue=" "),
            S(speaker, glue=", "), S(JH + "{" + pin + "}", glue="\n"), N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"When Tigard conditioned Florence Dolan's store-expansion permit on dedicating a public floodplain greenway and a bike path, the Court held 5--4 that, beyond \textit{Nollan}'s essential nexus, the city must make an individualized determination of rough proportionality between the dedication and the development's impact, and it had not (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="After the Tigard City Council approved the order")],
  "Procedural History": [SEC("Facts and Procedural History", frm="After the Tigard City Council approved the order")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{5--4} vote. The case was argued on March 23, 1994, and decided on June 24, 1994 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Rehnquist delivered the opinion of the Court, joined by Justices O'Connor, Scalia, Kennedy, and Thomas.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Stevens filed a dissenting opinion, joined by Justices Blackmun and Ginsburg. Justice Souter filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Rehnquist)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Stevens)}"), N("Justice Stevens", glue=" "),
    SEC(CD, frm="Argued that state-court precedents", to=r"  \item \textbf{Justice Souter", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Souter)}"), N("Justice Souter", glue=" "),
    SEC(CD, frm="Contended that the majority", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Physical Access"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Extension to Legislative", to="On June 15, 2026"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Conditions Invalid): A Boardwalk Easement and an Arts Fee for a Warehouse.}", glue=" "),
    X("A coastal city enacts an ordinance requiring", r"\textbf{Analysis:}", glue=" "),
    X(r"Under \href{https://supreme.justia.com/cases/federal/us/601/22-1074/}{\emph{Sheetz}} and", r"\textbf{``Opposite Side'' Contrast:}"),
    N(r"\item \textbf{Same-Side (Fee Invalid): A Traffic Fee Far Exceeding the Project's Impact.} A county requires every applicant for a permit to build a backyard cottage to pay a \$60{,}000 traffic-mitigation fee, although the county's own engineering study estimates that a cottage adds about \$3{,}000 worth of traffic burden to county roads. An owner pays under protest and sues. After \textit{Koontz}, a demand for money is an exaction subject to \textit{Nollan} and \textit{Dolan}, and after \textit{Sheetz}, the fee is not exempt because the legislature set it. Traffic mitigation has an essential nexus to new housing, but a fee twenty times the projected impact is not roughly proportional in extent, and the county cannot carry its burden of justifying it (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Conditions Valid): Denial, or a Private Buffer and a Calibrated Fee.}", glue=" "),
    X("Now alter the conditions:", r"\end{document}"),
    N(r"\item \textbf{Opposite-Side (Dedication Valid): A Turn Lane Supported by a Traffic Study.} A developer seeks approval for a 300-home subdivision whose only entrance will be on a two-lane county road. A traffic study commissioned by the county shows that the subdivision will generate most of the peak-hour traffic at the entrance, and the county conditions approval on dedicating a 12-foot strip along the frontage for a turn lane. The condition serves the legitimate goal of traffic safety (\textit{Nollan}'s nexus), and the county has made the individualized, quantified determination \textit{Dolan} requires: the strip is related in nature and extent to the traffic the project will create. No precise calculation is required, so the dedication stands."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): A Citywide School-Impact Fee Schedule.} A city adopts an ordinance charging every new home a school-impact fee of \$4 per square foot, based on a study of the average number of students generated by new housing citywide. A builder of a retirement community restricted to residents aged 55 and older argues that its homes will add almost no students. After \textit{Sheetz}, the legislative fee is subject to \textit{Nollan/Dolan}, but the Court left open whether a fee schedule based on averages for a class of developments must be tailored as specifically as a parcel-by-parcel exaction. The city will rely on its study and the impracticality of individualized fees; the builder will invoke \textit{Dolan}'s demand for an individualized determination. The outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(P, frm=r"  \item \textbf{Burden Inversion", to=r"\end{itemize}")],
  "Key Quotations":
    Q("``We think a term such as", "Chief Justice Rehnquist", "512 U.S. at 391")
    + Q("``Under the well-settled doctrine", "Chief Justice Rehnquist", "512 U.S. at 385")
    + Q("``We see no reason why the Takings Clause", "Chief Justice Rehnquist", "512 U.S. at 392")
    + Q("``The Court has made a serious error", "Justice Stevens (Dissenting)", "512 U.S. at 405"),
 },
 "dropped": [
  "Case Metadata: court line, provisions and chapter lines (Justia link kept in Judicial Votes).",
  "Separate-opinions intro ('No separate concurring opinions were filed. Two dissents challenged...') - stated in Judicial Votes.",
  "Legacy section: introductory paragraph (Nollan/Dolan exactions framing, Cornell LII); Cedar Point Nursery item (per se access-regulation taking, not an application of Dolan); final Sheetz sentence on a June 15, 2026 certiorari denial (unverifiable). Kept: Lingle, Koontz, and Sheetz items.",
  "Key Quotations: the bold topical labels (only the speaker and pin cite are moved).",
  "Exam Hypothetical: subsection heading and 'Hypothetical:' / 'Analysis:' / 'Opposite Side Contrast' labels (fact patterns and analyses reused in Examples 1 and 3).",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all four kept, none added."],
}

emit(__file__, FILL)
