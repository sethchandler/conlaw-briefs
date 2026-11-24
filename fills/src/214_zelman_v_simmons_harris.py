"""Fill for 214_zelman_v_simmons_harris. See tools/fillkit.py."""
import os
from fillkit import *

ORIG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "originals", "briefs",
                         "214_zelman_v_simmons_harris.tex"), encoding="utf-8").read()

def X(a, b, glue=None):
    i = ORIG.index(a); j = ORIG.index(b, i)
    return S(ORIG[i:j].strip(), glue=glue)

J = "https://supreme.justia.com/cases/federal/us/536/639/"
JH = r"\href{https://supreme.justia.com/cases/federal/us/536/639/}"
CD = "Concurring and Dissenting"

def Q(first, speaker, pin):
    # Speaker and pin cite are both moved verbatim from the original's label; the attribution sits
    # inside the block so normalize_quotes.py converts it to a Group A "\noindent ---" line.
    i = ORIG.index(first); j = ORIG.index(r"\end{quote}", i)
    return [N(r"\begin{quote}", glue="\n"), S(ORIG[i:j].strip(), glue="\n"), N(r"---", glue=" "),
            S(speaker, glue=", "), S(JH + "{" + pin + "}", glue="\n"), N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Upholding Cleveland's school-voucher program 5--4, the Court held that a religion-neutral aid program that gives assistance to a broad class of families, who then direct it to religious schools through their own genuine and independent private choice, does not violate the Establishment Clause (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="After the Ohio Supreme Court rejected")],
  "Procedural History": [SEC("Facts and Procedural History", frm="After the Ohio Supreme Court rejected")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the Sixth Circuit by a \textbf{5--4} vote. The case was argued on February 20, 2002, and decided on June 27, 2002 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Rehnquist delivered the opinion of the Court, joined by Justices O'Connor, Scalia, Kennedy, and Thomas.
    \item \textbf{Concurring Opinions:} Justice O'Connor and Justice Thomas each filed a concurring opinion.
    \item \textbf{Dissenting Opinions:} Justice Stevens filed a dissenting opinion. Justice Souter filed a dissenting opinion, joined by Justices Stevens, Ginsburg, and Breyer. Justice Breyer filed a dissenting opinion, joined by Justices Stevens and Souter.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Rehnquist)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice O'Connor)}"), N("Justice O'Connor", glue=" "),
    SEC(CD, frm="Emphasized that the decision", to=r"  \item \textbf{Justice Thomas", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC(CD, frm="Questioned whether the Establishment", to=r"  \item \textbf{Justice Stevens", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Stevens)}"), N("Justice Stevens", glue=" "),
    SEC(CD, frm="Argued that Cleveland's", to=r"  \item \textbf{Justice Souter", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Souter)}"), N("Justice Souter", glue=" "),
    SEC(CD, frm="Charged the majority", to=r"  \item \textbf{Justice Breyer", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Breyer)}"), N("Justice Breyer", glue=" "),
    SEC(CD, frm="Focused on the Establishment", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"That same Term,"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Aid Upheld): An Education Savings Account in a County With Only Religious Schools.}", glue=" "),
    X("A State establishes an ``Education Savings Account''", r"\textbf{Analysis:}", glue=" "),
    X(r"Under \href{https://supreme.justia.com/cases/federal/us/536/639/}{\emph{Zelman}}, the ESA program survives.", r"\textbf{``Opposite Side'' Contrast:}"),
    N(r"\item \textbf{Same-Side (No Establishment Clause Excuse): Excluding Religious Schools From the ESA.}", glue=" "),
    X("Now flip the challenge:", r"\end{document}"),
    N(r"\item \textbf{Opposite-Side (Aid Invalid): Vouchers Redeemable Only at One Denomination's Schools.} A State offers tuition vouchers to low-income families but allows them to be redeemed only at schools affiliated with a single named church, on the theory that its schools have the best record in the district. Parents still choose whether to use the voucher, but the program is not neutral with respect to religion: the State itself, not independent private choice, has selected which religion's schools may receive the money. \textit{Zelman} protected Ohio's program because it was neutral and open to religious and secular schools alike; a program that prefers one faith fails that threshold requirement and violates the Establishment Clause (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (No Private Choice): Direct Grants Earmarked for Religious Instruction.} A State appropriates funds paid directly to religious schools, in amounts set by the State, to pay for daily religion classes and chapel services, without any family deciding where the money goes. \textit{Zelman} drew a sharp line between such direct aid and programs of true private choice. Here the circuit between government and religion is never broken: the State itself sends tax money to finance religious teaching and worship, so the advancement of religion is attributable to the government rather than to parents, and the program cannot claim \textit{Zelman}'s protection."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): A Choice of Rehabilitation Programs With a Long Secular Waitlist.} A State lets nonviolent offenders avoid jail by completing a funded residential rehabilitation program of their choice. Most participating providers are faith-based programs that include worship, while the only secular provider has a six-month waitlist. The program is neutral on its face and the money follows each participant's choice, which points toward \textit{Zelman}. But \textit{Zelman} stressed that the choice must be genuine and that adequate secular options must be available, and an offender facing jail in the meantime may have what Justice Souter called a Hobson's choice. Whether a court counts the waitlisted secular option as a real alternative, and whether the coercive criminal setting matters, could decide the case."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{The Denominator", to=r"\end{itemize}")],
  "Key Quotations":
    Q("``[W]here a government aid program is neutral", "Chief Justice Rehnquist", "536 U.S. at 652")
    + Q("``The constitutionality of a neutral educational aid", "Chief Justice Rehnquist", "536 U.S. at 658")
    + Q("``There would be a tragic irony", "Justice Thomas (Concurring)", "536 U.S. at 680")
    + Q("``The criterion is one of genuinely free choice", "Justice Souter (Dissenting)", "536 U.S. at 707"),
 },
 "dropped": [
  "Case Metadata: consolidated-case names, court line, provisions and chapter lines (Justia link kept in Judicial Votes).",
  "Legacy section: introductory sentence; Kennedy v. Bremerton sentence at the end of the Carson item (abandoning Lemon is not a development of Zelman's holding); 'Public-Charter Frontier (2025--2026)' item (Drummond 4--4 affirmance without precedential opinion). Kept: Locke v. Davey and Trinity Lutheran/Espinoza/Carson items.",
  "Key Quotations: the bold topical labels (only the speaker name and pin cite are moved).",
  "Exam Hypothetical: subsection headings and 'Hypothetical:' / 'Analysis:' / 'Opposite Side Contrast' labels (fact patterns and analyses reused in Examples 1 and 2).",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all four kept, none added. The speaker is moved from each label (e.g., 'Justice Souter (Dissenting)') and the pin cite from its parenthetical; they are joined with a comma."],
}

emit(__file__, FILL)
