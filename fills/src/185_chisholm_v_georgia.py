"""Fill for 185_chisholm_v_georgia. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/2/419/"
JL = r"\href{https://supreme.justia.com/cases/federal/us/2/419/}"

def quote(text, who, pin, extra=None):
    parts = [N(r"\begin{quote}", glue="\n"), S(text, glue="\n"), N(r"\end{quote}", glue="\n"),
             N(r"\noindent ---", glue=" "), S(who, glue="")]
    parts.append(N(extra if extra else ",", glue=" "))
    parts += [S(JL + "{" + pin + "}", glue=""), N(".")]
    return parts

FILL = {
 "sections": {
  "Memory Jogger": [N(r"In the Court's first major constitutional decision, a South Carolina executor sued Georgia on a Revolutionary War debt; the Justices held 4--1, in seriatim opinions, that Article III lets a citizen of one State sue another State without its consent---a ruling the Eleventh Amendment promptly overturned (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Chisholm first sued Georgia")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Chisholm first sued Georgia")],
  "Judicial Votes": [
    N(r"The Supreme Court, exercising original jurisdiction, ruled for the plaintiff by a \textbf{4--1} vote and ordered that default judgment be entered unless Georgia appeared or showed cause. The case was argued on February 5, 1793, and decided on February 18, 1793 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority (Seriatim Opinions):} Chief Justice Jay and Justices Cushing, Wilson, and Blair each delivered a separate opinion; there was no single opinion of the Court.
    \item \textbf{Concurring Opinions:} None apart from the seriatim majority opinions.
    \item \textbf{Dissenting Opinion:} Justice Iredell dissented alone.
\end{itemize}"""),
    N(r"Five Justices participated, and the seriatim opinions were delivered in reverse order of seniority."),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Seriatim Majority Opinions (Chief Justice Jay and Justices Cushing, Wilson, and Blair)}"), SEC("Reasoning"),
    N(r"\subsection{Distinctions Among the Seriatim Majority Opinions}"),
    SEC("Concurring and Dissenting", frm=r"\begin{itemize}", to=r"\subsection{Dissenting Opinion"),
    N(r"\subsection{Dissenting Opinion (Justice Iredell)}"),
    SEC("Concurring and Dissenting", frm="Justice Iredell dissented alone"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{The Eleventh Amendment:}", glue=" "),
    S(r"Congress proposed the \href{https://www.law.cornell.edu/constitution-conan/amendment-11/historical-background-on-eleventh-amendment}{Eleventh Amendment} on March 4, 1794, and States ratified it on February 7, 1795: ``The Judicial power of the United States shall not be construed to extend to any suit in law or equity, commenced or prosecuted against one of the United States by Citizens of another State, or by Citizens or Subjects of any Foreign State.''", glue=" "),
    S(r"Although the Court entered default judgment for Chisholm in 1794, no writ of inquiry was executed; in \href{https://supreme.justia.com/cases/federal/us/3/378/}{\emph{Hollingsworth v. Virginia}, 3 U.S. (3 Dall.) 378 (1798)}, the Court unanimously dismissed all pending suits against States."),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{In-State and State-Court Immunity:}", to=r"  \item \textbf{2021--2026 Refinements:}"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (No Immunity Bar): The State as Plaintiff.} A Texas supplier sells generators to Louisiana and then refuses to honor its warranty. Flip the posture of a typical immunity case:", glue=" "),
    S(r"if \emph{Louisiana} sues the Texas supplier in federal court, immunity does not apply---creating the one-way asymmetry Chief Justice Jay criticized (\href{https://supreme.justia.com/cases/federal/us/2/419/}{2 U.S. at 473})", glue=""),
    N(r". The Eleventh Amendment reaches only suits ``commenced or prosecuted against'' a State, so Article III's grant over controversies between a State and citizens of another State still operates when the State is the one suing, just as Georgia was suing South Carolina citizens in \emph{Georgia v.\ Brailsford} while claiming immunity in \emph{Chisholm}."),
    N(r"\item \textbf{Same-Side (Relief Available): Prospective Relief Against a State Officer.} After Louisiana's legislature passes a statute cancelling its outstanding contracts with out-of-state suppliers, a Texas supplier sues the state treasurer in federal court, seeking an injunction against enforcement of the statute as a violation of the Contracts Clause. The suit may proceed: under \href{https://supreme.justia.com/cases/federal/us/209/123/}{\emph{Ex parte Young}, 209 U.S.\ 123 (1908)}, a federal court may order a state officer to stop violating federal law prospectively, and the officer cannot shelter behind the State's immunity. This preserves part of the \emph{Chisholm} majority's concern that a State not escape its contracts without judicial accountability. The supplier cannot, however, obtain an order requiring payment of the past debt from the state treasury."),
    N(r"\item \textbf{Opposite-Side (Suit Barred): An Unpaid Contract Debt in Federal Court.}", glue=" "),
    S(r"A Texas supplier sues the State of Louisiana in federal court for \$15 million on an unpaid generator contract, alleging breach of contract and a Contracts Clause violation. Under \emph{Chisholm}, the suit proceeds (\href{https://supreme.justia.com/cases/federal/us/2/419/}{2 U.S. at 456}); today, it is barred by the \href{https://www.law.cornell.edu/constitution-conan/amendment-11/historical-background-on-eleventh-amendment}{Eleventh Amendment} and \href{https://supreme.justia.com/cases/federal/us/134/1/}{\emph{Hans}}, and \href{https://supreme.justia.com/cases/federal/us/209/123/}{\emph{Ex parte Young}} does not permit retroactive treasury damages."),
    N(r"\item \textbf{Opposite-Side (Suit Barred): Federal Wage Claims in the State's Own Courts.} State probation officers in Maine sue the State in a Maine state court, seeking back overtime pay owed under the federal Fair Labor Standards Act. They argue that the Eleventh Amendment, which speaks only to ``the Judicial power of the United States,'' says nothing about state courts. Under \href{https://supreme.justia.com/cases/federal/us/527/706/}{\emph{Alden v.\ Maine}, 527 U.S.\ 706 (1999)}, the suit is barred: Congress may not use its Article I powers to subject a nonconsenting State to private damages suits in its own courts. The result rests on the structural view of state sovereignty traced to Justice Iredell's dissent, not on the Amendment's text that the \emph{Chisholm} majority's textualism would have emphasized."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Is a State-Created Hospital Authority an ``Arm of the State''?} A State creates a public hospital authority as a separate corporation. The Governor appoints its board, and most of its budget comes from annual state appropriations, but state law says the State is not legally liable for the authority's debts. An out-of-state vendor sues the authority in federal court for unpaid invoices. If the authority is an arm of the State, the Eleventh Amendment bars the suit; if it is more like a city or county, it is not immune. State control and funding point toward immunity, but the State treasury's freedom from legal liability for its judgments---the factor the Court stressed in \emph{Hess v.\ Port Authority Trans-Hudson Corp.}, 513 U.S.\ 30 (1994)---points the other way, so the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Textualism Inverted", to=r"\end{itemize}")],
  "Key Quotations": (
    quote(r"``To the Constitution of the United States, the term SOVEREIGN, is totally unknown. There is but one place where it could have been used with propriety. But even in that place, it would not, perhaps, have comported with the delicacy of those who ordained and established that Constitution. They might have announced themselves `SOVEREIGN' people of the United States. But serenely conscious of the fact, they avoided the ostentatious declaration.''", "Justice James Wilson", "2 U.S. at 454")
    + quote(r"``A state, like a merchant, makes a contract. A dishonest state, like a dishonest merchant, wilfully refuses to discharge it. The latter is amenable to a court of justice. Upon general principles of right, shall the former, when summoned to answer the fair demands of its creditor, be permitted, Proteus-like, to assume a new appearance, and to insult him and justice by declaring `I am a Sovereign state?' Surely not.''", "Justice James Wilson", "2 U.S. at 456")
    + quote(r"``No such ideas obtain here; at the Revolution, the sovereignty devolved on the people, and they are truly the sovereigns of the country, but they are sovereigns without subjects (unless the African slaves among us may be so called), and have none to govern but themselves; the citizens of America are equal as fellow citizens, and as joint tenants in the sovereignty.''", "Chief Justice John Jay", "2 U.S. at 471--472")
    + quote(r"``Every State in the Union, in every instance where its sovereignty has not been delegated to the United States, I consider to be as completely sovereign as the United States are in respect to the powers surrendered. The United States are sovereign as to all the powers of Government actually surrendered: each State in the Union is sovereign as to all the powers reserved.''", "Justice James Iredell", "2 U.S. at 435", extra=", dissenting,")
  ),
 },
 "dropped": [
  "Case Metadata: case name/caption, counsel, provisions at issue, Chapter Placement, duplicate links (Justia link kept in Memory Jogger and Judicial Votes).",
  "Legacy section: introductory FJC sentence on alarm among States; 'Vindication of Iredell' lead-in sentence; '2021--2026 Refinements' item (PennEast, Torres, Galette) - refinements of later immunity doctrine, not Chisholm's holding. Kept: Eleventh Amendment/Hollingsworth sentences, Hans/Alden/Hyatt item, Ex parte Young/Seminole Tribe/Fitzpatrick/Allen item.",
  "Exam 'Opposite Side' Contrast item (2): separate public corporation under Galette (2026) - relies on a 2026 decision not verifiable here; the arm-of-the-State question is treated as the Fence-Sitter instead.",
  "Key Quotations: the descriptive topic labels ('on the Term Sovereign', etc.); speaker names and pin cites moved into Group A attribution lines.",
 ],
 "notes": [
  "Key Quotations built manually in Group A style (stem is listed in tools/manual_quotes.txt).",
 ],
}

emit(__file__, FILL)
