"""Fill for 198_everson_v_board_of_education. See tools/fillkit.py."""
import os
from fillkit import *

ORIG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "originals", "briefs",
                         "198_everson_v_board_of_education.tex"), encoding="utf-8").read()

def X(a, b, glue=None):
    """Verbatim span of the original from anchor a (inclusive) to anchor b (exclusive), stripped."""
    i = ORIG.index(a); j = ORIG.index(b, i)
    return S(ORIG[i:j].strip(), glue=glue)

J = "https://supreme.justia.com/cases/federal/us/330/1/"
JH = r"\href{https://supreme.justia.com/cases/federal/us/330/1/}"

def Q(first, attrib, closer="''", opener="``"):
    # The original prints these as unmarked block quotes; Group A style (and normalize_quotes.py)
    # needs ``...''. Only the opening/closing marks are new; the quote text is moved verbatim from the
    # quote environment, and the attribution inside the block is converted to a "\noindent ---" line.
    i = ORIG.index(first); j = ORIG.index(r"\end{quote}", i)
    body = ORIG[i:j].strip()
    return [N(r"\begin{quote}", glue="\n"), N(opener, glue=""), S(body, glue=""), N(closer, glue="\n"),
            N(r"---", glue=" "), S(attrib, glue="\n"), N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Incorporating the Establishment Clause against the states and invoking Jefferson's ``wall of separation between church and State,'' the Court nonetheless upheld 5--4 New Jersey's reimbursement of bus fares for children attending parochial schools as a neutral public-welfare benefit, like police and fire protection (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Arch R. Everson, a taxpayer")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Arch R. Everson, a taxpayer")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the New Jersey Court of Errors and Appeals by a \textbf{5--4} vote. The case was argued on November 20, 1946, and decided on February 10, 1947 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/330/1}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Black delivered the opinion of the Court, joined by Chief Justice Vinson and Justices Reed, Douglas, and Murphy.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Jackson filed a dissenting opinion, joined by Justice Frankfurter. Justice Rutledge filed a dissenting opinion, joined by Justices Frankfurter, Jackson, and Burton.
\end{itemize}"""),
    S(r"Notably, all four dissenting Justices agreed with Justice Black's two foundational constitutional premises---that the Establishment Clause is incorporated against the states via the Fourteenth Amendment and that it mandates a strict separation of church and state---but forcefully argued that the majority betrayed its own principles in upholding the Ewing Township reimbursement scheme."),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Black)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Jackson)}"),
    SEC("Concurring and Dissenting", frm="Justice Jackson opened", to=r"\subsection{Dissenting Opinion of Justice Rutledge"),
    N(r"\subsection{Dissenting Opinion (Justice Rutledge)}"),
    SEC("Concurring and Dissenting", frm="Justice Rutledge authored"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Early Applications of the Wall and the Child-Benefit Theory (1948--1971):}", glue=" "),
    X("Early decisions enforced Justice Black's", "Since 2002, however"),
    N(r"\item \textbf{Neutrality Becomes a Mandate (2002--2022):}", glue=" "),
    X("Since 2002, however", "Days later,"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Aid Upheld): Free Transit Passes for All Students.} A city gives every enrolled K--12 student a free pass for its public buses and subways, whether the student attends a public, private secular, or religious school. A taxpayer sues, arguing that passes used to reach Catholic and Jewish day schools are tax support for religious institutions. Under \textit{Everson}, the program is a general public-welfare benefit paid to students and their families, not to the schools, and it is indistinguishable from the bus-fare reimbursements the Court upheld. Excluding religious-school students would make the city an adversary of religion rather than a neutral, so the passes survive the Establishment Clause challenge (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Aid Upheld): Loaning Secular Textbooks to All Students.} A state lends approved secular textbooks in mathematics, science, and history to every student in grades 7--12, including students at parochial schools; the books remain state property and the school never receives money. Taxpayers object that the books free up parochial-school budgets for religious instruction. Extending \textit{Everson}'s child-benefit reasoning, \href{https://supreme.justia.com/cases/federal/us/392/236/}{\textit{Board of Education v.\ Allen}, 392 U.S.\ 236 (1968)}, upheld exactly this kind of program: the benefit runs to students and parents, the materials are secular, and the State contributes nothing to the schools' religious mission. Rutledge's fungibility objection did not carry the day in \textit{Everson}, and it does not here."),
    N(r"\item \textbf{Opposite-Side (Aid Invalid): Tax Grants to Pay Clergy Salaries.} To help congregations hit hard by an economic downturn, a county appropriates tax revenue for grants to churches, synagogues, and mosques to pay the salaries of their clergy, distributing the money equally among all faiths that apply. Equal treatment of all religions does not save the program. \textit{Everson} declared that government may not pass laws that aid all religions and that no tax in any amount may be levied to support religious activities or institutions, and the grants pay for the core religious function itself rather than a service ``separate'' from it like police or fire protection. Madison's objection to the nondiscriminatory Virginia assessment, which both the majority and Rutledge embraced, applies directly."),
    N(r"\item \textbf{Opposite-Side (Practice Invalid): Religious Classes Inside Public Schools.} A public school district lets clergy of several faiths come into its classrooms for an hour each week during the school day to teach religion to students whose parents consent, while other students move to another room for secular study. The program uses the public school building and the State's compulsory-attendance machinery to help religious groups spread their faith. Applying \textit{Everson}'s incorporated Establishment Clause, \href{https://supreme.justia.com/cases/federal/us/333/203/}{\textit{McCollum v.\ Board of Education}, 333 U.S.\ 203 (1948)}, held such a program unconstitutional; unlike \textit{Everson}'s bus fares, the aid here goes to religious instruction itself."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Private Aid Versus Charter Status.}", glue=" "),
    X("The State of Franklin reimburses", r"\textbf{``Opposite Side'' Contrast:}"),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Federalism", to=r"\end{itemize}")],
  "Key Quotations":
    Q(r"The ``establishment of religion'' clause of the First Amendment means at least this", r"Black, J., for the Court, \href{https://supreme.justia.com/cases/federal/us/330/1/}{330 U.S. at 15--16}", closer=r"\,''", opener=r"``\,")
    + Q(r"That Amendment requires the state to be a neutral", r"Black, J., for the Court, \href{https://supreme.justia.com/cases/federal/us/330/1/}{330 U.S. at 18}")
    + Q(r"In fact, the undertones of the opinion", r"Jackson, J., dissenting, \href{https://supreme.justia.com/cases/federal/us/330/1/}{330 U.S. at 19}", closer=r"\,''")
    + Q(r"But we cannot have it both ways.", r"Jackson, J., dissenting, \href{https://www.law.cornell.edu/supremecourt/text/330/1}{330 U.S. at 27--28}")
    + Q(r"Neither so high nor so impregnable today", r"Rutledge, J., dissenting, \href{https://supreme.justia.com/cases/federal/us/330/1/}{330 U.S. at 29}"),
 },
 "dropped": [
  "Case Metadata: parallel citations, court line, lower-court disposition line, constitutional-provisions line (Justia and Cornell links kept in Judicial Votes).",
  "Separate-opinions intro sentence 'No concurring opinions were filed.' (stated in Judicial Votes); the remaining intro sentence was moved into Judicial Votes.",
  "Legacy section: opening framing sentence; Kennedy v. Bremerton sentence (abandoning Lemon is not a development of Everson's holding); 'Through 2026' paragraph (Drummond 4--4 affirmance, Catholic Charities, Mahmoud v. Taylor, St. Mary Catholic Parish v. Roy argument) - tangential or unverifiable recent events. Kept: early applications (McCollum, Engel, Zorach, Allen, Lemon) and the Zelman/Locke/Trinity Lutheran/Espinoza/Carson line.",
  "Key Quotations: bold topical labels before each quotation (only the attribution part is moved).",
  "Exam Hypothetical: 'Opposite Side' Contrast (St. Mary Catholic Parish v. Roy nondiscrimination-condition scenario) - an exam-discussion prompt resting on a pending 2026 case that cannot be verified; the hypothetical itself is reused as the Fence-Sitter.",
 ],
 "notes": [
  "Key Quotations rebuilt from verbatim pieces (manual_quotes list); all five kept, none added. The original sets them as unmarked block quotes, so new opening/closing quotation marks (``...'') were added around each verbatim quote to match Group A style and let normalize_quotes.py convert the attributions; where a quote already ends in '' a thin space separates the marks.",
  "The Reasoning section's own \\subsection headings remain inside the Majority Opinion subsection (moved verbatim).",
 ],
}

emit(__file__, FILL)
