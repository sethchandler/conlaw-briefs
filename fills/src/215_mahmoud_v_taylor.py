"""Fill for 215_mahmoud_v_taylor. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/606/24-297/"
CL = r"\href{https://www.law.cornell.edu/supremecourt/text/24-297}"
JS = r"\href{https://supreme.justia.com/cases/federal/us/606/24-297/}{Justia}"
SC = r"\href{https://www.supremecourt.gov/opinions/24pdf/24-297_4f14.pdf}{SupremeCourt.gov}"

def Q(quote, attrib):
    # Attribution placed inside the quote block; tools/normalize_quotes.py moves it to a
    # Group A "\noindent ---" line (check_brief.py does not match manual_quotes.txt's ".tex" names).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "), S(attrib, glue="\n"),
            N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Holding 6--3 that a Maryland school board burdened parents' free exercise by requiring young children to receive normative LGBTQ+-inclusive storybook instruction without notice or opt-outs, the Court applied \textit{Wisconsin v. Yoder} to trigger strict scrutiny without asking whether the policy was neutral and generally applicable (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Three sets of religiously diverse parents")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Three sets of religiously diverse parents")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{6--3} vote. The case was argued on April 22, 2025, and decided on June 27, 2025 (\href{" + J + r"}{Justia}; " + CL + r"{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Alito delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Thomas, Gorsuch, Kavanaugh, and Barrett.
    \item \textbf{Concurring Opinion:} Justice Thomas filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Sotomayor filed a dissenting opinion, joined by Justices Kagan and Jackson.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Question Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Alito)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"),
    SEC("Concurring and Dissenting", frm="Joining in full", to=r"  \item \textbf{Justice Sotomayor"),
    N(r"\subsection{Dissenting Opinion (Justice Sotomayor)}"),
    SEC("Concurring and Dissenting", frm="Justice Sotomayor argued", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Extension to Parental Notification of Gender Transition:}", glue=" "),
    S(r"On March 2, 2026, in \href{https://www.law.cornell.edu/supremecourt/text/25A810}{\textit{Mirabelli v. Bonta}, 607 U.S. 492 (2026) (per curiam)} (\href{https://www.supremecourt.gov/opinions/25pdf/607us2r17_bqmc.pdf}{SupremeCourt.gov}), the Court vacated a Ninth Circuit stay and reinstated an injunction blocking California school policies that barred staff from disclosing a student's social gender transition to parents without student consent. Relying squarely on \textit{Mahmoud}, the Court held that concealing a child's gender transition imposes an even ``greater'' intrusion on parents' Free Exercise and Fourteenth Amendment substantive due process rights and likely fails \textit{Mahmoud}'s strict scrutiny."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Parents Prevail): A Workbook Hostile to Religion.}", glue=" "),
    S(r"A public school district introduces a mandatory second-grade civics workbook titled \textit{No Gods Needed} that portrays religious belief as outdated superstition and directs teachers to respond to students who cite Scripture by saying, ``Those stories are just myths.'' No notice or opt-out is allowed, though the district allows opt-outs for health class. Under \textit{Mahmoud}, normative instruction hostile to parents' faith aimed at impressionable seven-year-olds triggers automatic strict scrutiny under \textit{Yoder} and fails narrow tailoring given existing opt-out mechanisms."),
    N(r"\item \textbf{Same-Side (Parents Prevail): Lessons Designed to Change Children's Religious Practices.} A district adopts a mandatory kindergarten-through-second-grade ``fairness'' unit in which teachers read stories portraying religious dietary and modesty rules as unfair to others and follow scripts telling children who mention such rules that they should rethink them. The district refuses notice or opt-outs, although it excuses students from other units for medical and language reasons. As in \textit{Mahmoud}, the instruction is aimed at very young children, is normative rather than informational, and pressures children to abandon practices their parents are trying to instill---a burden ``of the same character as that in \textit{Yoder}.'' Strict scrutiny applies, and the district's existing opt-out mechanisms undercut any claim that excusing these students is unworkable (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (School District Prevails): Neutral High-School Science.}", glue=" "),
    S(r"A public high school requires eleventh-grade biology students to study evolutionary theory from a standard, neutral science textbook that neither disparages religion nor instructs teachers to rebuke religious students, and explicitly permits students to hold personal religious views. A parent sues for a religious opt-out under \textit{Mahmoud}.", glue=" "),
    S(r"The district has strong grounds to prevail. Unlike \textit{Mahmoud}'s five-to-eleven-year-olds, high school juniors are far less impressionable (\href{https://www.law.cornell.edu/supremecourt/text/24-297}{slip op. at 21--22}); the instruction is neutrally presented academic science rather than normative moral advocacy with teacher-led ``disruption'' of religious views; and core high-school science standards advance a compelling educational interest where piecemeal opt-outs are far harder to administer without undermining graduation requirements."),
    N(r"\item \textbf{Opposite-Side (No Right to the Relief Sought): Removing Books for Every Student.} Parents who object to an elementary reading unit do not ask for notice or an opt-out for their own children; instead they sue to require the district to remove the books from the curriculum for all students. \textit{Mahmoud} protects parents' right to direct the religious upbringing of \textit{their own} children, and the relief it ordered was advance notice and the opportunity to excuse those children. It does not give parents a veto over what a public school teaches other families' children. The parents' claim fails, although they may still seek notice and an opt-out under \textit{Mahmoud}."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): A Middle-School Health Lesson on Gender Identity.} A district's mandatory seventh-grade health unit explains, in factual terms, that some people identify with a gender different from their sex at birth, and teachers are told to require students to treat classmates respectfully but not to correct students' religious views. Religious parents demand notice and an opt-out, which the district refuses. The parents can argue that the lesson conveys a message contrary to their faith during formative years. The district can respond that twelve-year-olds are less impressionable than \textit{Mahmoud}'s five-to-eleven-year-olds and that the unit is informational ``exposure'' rather than the ``unmistakably normative'' instruction the Court condemned. Where the line falls is unsettled."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Erosion", to=r"\end{enumerate}")],
  "Key Quotations":
    Q(r"``A government burdens the religious exercise of parents when it requires them to submit their children to instruction that poses `a very real threat of undermining' the religious beliefs and practices that the parents wish to instill. \textit{Wisconsin v. Yoder}, 406 U. S. 205, 218 (1972). And a government cannot condition the benefit of free public education on parents' acceptance of such instruction.''", CL + r"{606 U.S. 522 (2025)}, slip op. at 1--2; " + JS)
    + Q(r"``When the burden imposed is of the same character as that imposed in \textit{Yoder}, we need not ask whether the law at issue is neutral or generally applicable before proceeding to strict scrutiny. That much is clear from our decisions in \textit{Yoder} and \textit{Smith}.''", CL + r"{slip op. at 36}; " + SC)
    + Q(r"``When it comes to instruction that would burden the religious exercise of parents, the Board cannot escape its obligations under the Free Exercise Clause by crafting a curriculum that is so burdensome that a substantial number of parents elect to opt out. There is no de maximis exception to the Free Exercise Clause.''", CL + r"{slip op. at 39}; " + SC)
    + Q(r"``Casting aside longstanding precedent, the Court invents a constitutional right to avoid exposure to `subtle' themes `contrary to the religious principles' that parents wish to instill in their children. [Internal citation omitted.] Exposing students to the `message' that LGBTQ people exist, and that their loved ones may celebrate their marriages and life events, the majority says, is enough to trigger the most demanding form of judicial scrutiny.''", CL + r"{Sotomayor, J., dissenting, slip op. at 1--2}; " + JS),
 },
 "dropped": [
  "Case Metadata: full case name, docket number, lower-court citations, provision/Chapter lines, duplicate source links (Justia, Cornell kept in Judicial Votes).",
  "Legacy section: introductory paragraph (framing; Mozert); final sentence on districts revising policies (K-12 Dive). Kept: Mirabelli v. Bonta (2026).",
  "Key Quotations: bold topic labels before each quote (attributions kept).",
  "Exam Hypotheticals: headings and 'Analysis' label.",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all four kept, none added. Attributions are emitted inside each quote block and converted by normalize_quotes.py, as in 181_missouri_v_holland.",
           "Kept Mirabelli v. Bonta (March 2, 2026) item is beyond this drafter's ability to verify; it must be checked in the audit."],
}

emit(__file__, FILL)
