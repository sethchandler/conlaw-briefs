"""Fill for 194_home_building_v_blaisdell. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/290/398/"
FS = "Facts and Procedural History"
RS = "Reasoning"
DS = "Doctrinal Significance"
PS = "Pedagogical Critiques"
EX = "Pedagogical Critiques"

def Q(text, who, src):
    # Attribution is placed inside the quote block (Group B form) so that
    # tools/normalize_quotes.py converts it to Group A form; see notes.
    return [N(r"\begin{quote}", glue="\n"), S(text, glue="\n"),
            N(r"---", glue=" "), who, src, N(r"\end{quote}")]

JC = r"(\href{https://supreme.justia.com/cases/federal/us/290/398/}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/290/398}{Cornell LII})"
CON = r"(\href{https://www.law.cornell.edu/constitution-conan/article-1/section-10/clause-1/blaisdell-case-and-state-modifications-to-private-contracts}{Cornell LII ConAn})"
QUOTES = (
  Q(r"``Emergency does not create power. Emergency does not increase granted power or remove or diminish the restrictions imposed upon power granted or reserved. The Constitution was adopted in a period of grave emergency. Its grants of power to the federal government and its limitations of the power of the States were determined in the light of emergency, and they are not altered by emergency. \ldots\ While emergency does not create power, emergency may furnish the occasion for the exercise of power.''",
    S(r"Chief Justice Hughes, 290 U.S.\ at 425--26", glue=" "), S(JC, glue="\n"))
  + Q(r"``is not an absolute one, and is not to be read with literal exactness, like a mathematical formula.''",
    S(r"Chief Justice Hughes, 290 U.S.\ at 428", glue=" "),
    [N(r"(describing the Contracts Clause's prohibition)", glue=" "),
     S(r"(\href{https://supreme.justia.com/cases/federal/us/290/398/}{Justia}; quoted in \emph{City of El Paso v. Simmons}, 379 U.S.\ 497, 508 (1965), \href{https://supreme.justia.com/cases/federal/us/379/497/}{Justia})", glue="\n")])
  + Q(r"``The reserved power cannot be construed so as to destroy the limitation, nor is the limitation to be construed to destroy the reserved power in its essential aspects.''",
    S(r"Chief Justice Hughes, 290 U.S.\ at 439", glue=" "), S(CON, glue="\n"))
  + Q(r"``If by the statement that what the Constitution meant at the time of its adoption it means to-day, it is intended to say that the great clauses of the Constitution must be confined to the interpretation which the framers, with the conditions and outlook of their time, would have placed upon them, the statement carries its own refutation. \ldots\ With a growing recognition of public needs and the relation of individual right to public security, the court has sought to prevent the perversion of the clause through its use as an instrument to throttle the capacity of the States to protect their fundamental interests.''",
    S(r"Chief Justice Hughes, 290 U.S.\ at 442--44", glue=" "), S(CON, glue="\n"))
  + Q(r"``The only legitimate inquiry we can make is whether it is constitutional. If it is not, its virtues, if it have any, cannot save it; if it is, its faults cannot be invoked to accomplish its destruction. If the provisions of the Constitution be not upheld when they pinch, as well as when they comfort, they may as well be abandoned.''",
    S(r"Justice Sutherland, Dissenting, 290 U.S.\ at 483", glue=" "), S(JC, glue="\n"))
)
# flatten the nested list used for quote 2
QUOTES = [p for x in QUOTES for p in (x if isinstance(x, list) else [x])]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"During the Great Depression, Minnesota let courts temporarily extend mortgage-redemption periods if the mortgagor paid a court-set rental value; a 5--4 Court upheld the law, holding that the Contracts Clause is not absolute and yields to a State's reasonable, temporary, conditioned exercise of its police power in an emergency (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="Following enactment of the Moratorium Law on April 18, 1933, the Blaisdells petitioned")],
  "Procedural History": [SEC(FS, frm="Following enactment of the Moratorium Law on April 18, 1933, the Blaisdells petitioned")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the judgment of the Supreme Court of Minnesota by a \textbf{5--4} vote. The case was argued on November 8--9, 1933, and decided on January 8, 1934 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/290/398}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Hughes delivered the opinion of the Court, joined by Justices Brandeis, Stone, Roberts, and Cardozo.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinion:} Justice Sutherland filed a dissenting opinion, joined by Justices Van Devanter, McReynolds, and Butler.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Hughes)}"),
    SEC(RS, to=r"\subsection{Emergency and"),
    N(r"\subsubsection{Emergency and Constitutional Power}"),
    SEC(RS, frm="Hughes began by rejecting", to=r"\subsection{Non-Literal"),
    N(r"\subsubsection{Non-Literal Construction and Implied Police-Power Reservation}"),
    SEC(RS, frm="Examining the historical origins", to=r"\subsection{Evolutionary"),
    N(r"\subsubsection{Evolutionary Constitutional Interpretation}"),
    SEC(RS, frm="Anticipating the dissent's", to=r"\subsection{The Five-Factor"),
    N(r"\subsubsection{The Five-Factor Balancing Test Applied to Minnesota's Act}"),
    SEC(RS, frm="Applying this framework", to=r"\subsection{Due Process and"),
    N(r"\subsubsection{Due Process and Equal Protection}"),
    SEC(RS, frm="Hughes disposed of"),
    N(r"\subsection{Dissenting Opinion (Justice Sutherland)}"),
    SEC("Concurring and Dissenting", frm="Writing for the four conservative"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Early Limits and Later Deference:}", glue=" "),
    SEC(DS, frm="Initially, the Court enforced", to="The Burger Court briefly"),
    N(r"\item \textbf{Burger Court Revival and the \textit{Energy Reserves} Test:}", glue=" "),
    SEC(DS, frm="The Burger Court briefly", to=r"\subsection{\emph{Sveen"),
    N(r"\item \textbf{\textit{Sveen v.\ Melin} (2018):}", glue=" "),
    SEC(DS, frm=r"In \href{https://www.law.cornell.edu/supremecourt/text/16-1432}", to="Through 2026, the Supreme Court"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Law Upheld): A Temporary, Compensated Pandemic Foreclosure Pause.} During a declared public-health emergency that causes mass layoffs, State W authorizes its courts, on a homeowner's showing of pandemic-related job loss, to postpone a foreclosure sale for up to twelve months, on condition that the homeowner pay the property's court-determined fair rental value toward taxes, insurance, and interest. The law expires when the emergency ends, and the debt, interest, and lender's lien remain intact. Every \textit{Blaisdell} factor favors the State: a genuine emergency, a public rather than private purpose, individualized judicial relief on reasonable conditions, protection of the lender's core investment, and temporary operation. Under the \textit{Energy Reserves} framework that grew out of \textit{Blaisdell}, the measure is a reasonable and appropriate means to a significant public purpose (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Law Upheld): A Notice Rule in a Regulated Industry.}", glue=" "),
    S(r"State Z requires solar lessors in a heavily regulated market to mail a one-page notice before automatic 10-year renewals take effect. \emph{Analysis:} Fails at \emph{Sveen} step one---heavy prior regulation lowers expectations (\emph{Energy Reserves}), and minimal paperwork preserves the core bargain."),
    N(r"\item \textbf{Opposite-Side (Law Struck Down): Permanent Commercial Rent Forgiveness.}", glue=" "),
    S(r"After a hurricane, State X permanently cancels 100\% of six months' commercial rent and personal guaranties without requiring tenant hardship or compensating landlords. \emph{Analysis:} Fails \emph{Sveen}/\emph{Blaisdell}---substantial impairment destroying core lease terms, and permanent, uncompensated relief mirrors \emph{Kavanaugh} and \emph{Melendez}."),
    N(r"\item \textbf{Opposite-Side (Law Struck Down): An Unconditional Five-Year Redemption Extension.} Facing falling farm prices but no acute crisis, State V extends the redemption period on every existing mortgage foreclosure by five years. Mortgagors need not show hardship or pay rent, no court supervises the extension, and the law has no expiration date. The law lacks each of the guardrails that saved Minnesota's statute: it is not tailored to an emergency, offers no individualized relief, leaves the mortgagee-purchaser uncompensated for lost possession, and is not temporary. That is the pattern struck down in \href{https://supreme.justia.com/cases/federal/us/295/56/}{\emph{W.\ B.\ Worthen Co.\ v.\ Kavanaugh}, 295 U.S.\ 56 (1935)}, and in the nineteenth-century cases \textit{Blaisdell} distinguished, such as \emph{Bronson v.\ Kinzie}."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): Repealing a Retirees' Cost-of-Living Adjustment.}", glue=" "),
    S(r"To close a budget deficit without raising taxes, State Y permanently repeals a statutory 3\% annual COLA for already-retired teachers. \emph{Analysis:} Public contract triggers \emph{U.S.\ Trust} heightened scrutiny; because less drastic fiscal alternatives exist, retroactive repeal is likely neither necessary nor reasonable.", glue=" "),
    N(r"The result is genuinely uncertain, however, because a court must first decide whether the COLA statute created a contract at all: statutes are presumed not to create contractual rights unless the legislature clearly intended to bind itself, \textit{National Railroad Passenger Corp.\ v.\ Atchison, Topeka \& Santa Fe Railway Co.}, 470 U.S.\ 451 (1985). If no contract exists, the Contracts Clause challenge fails at the threshold."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC(EX, frm=r"\emph{Blaisdell} pits", to=r"\textbf{``Opposite Side'' Contrast:}")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "LaTeX comment lines naming the case and chapter; Case Metadata (parallel citations, docket number, Minnesota citations, provisions, Library of Congress PDF link).",
  "'Concurring Opinions: No separate concurring opinions were filed' (restated in Judicial Votes).",
  "Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection.",
  "Legacy section: 'Through 2026' paragraph on COVID-19 moratoria circuit split (lower-court cases, Harvard Law Review). Kept: Worthen/Veix/El Paso paragraph, U.S. Trust/Spannaus/Energy Reserves paragraph, Sveen v. Melin.",
  "Critique: ''Opposite Side'' Contrast paragraph (Kavanaugh, Spannaus, U.S. Trust) - an exam tip, not a fact pattern; Example 4 covers the Kavanaugh pattern.",
  "Key Quotations: introductory 'All quotations below are verified verbatim' sentence and the five bold quotation labels; every quote and its attribution kept.",
 ],
 "notes": [
  "tools/check_brief.py compares stems against tools/manual_quotes.txt, whose entries carry a .tex suffix, so listed briefs are still sent through normalize_quotes.py (which rejects hand-built Group A quotes). Each quote is therefore rebuilt with its attribution inside the quote block so the normalizer produces the Group A form.",
  "Quote 2 in the original is a paraphrase lead-in plus a quoted fragment; only the quoted fragment is inside the quote block, and a new parenthetical '(describing the Contracts Clause's prohibition)' replaces the lead-in.",
 ],
}

emit(__file__, FILL)
