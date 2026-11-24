"""Fill for 199_wisconsin_v_yoder. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/406/205/"
JH = r"\href{https://supreme.justia.com/cases/federal/us/406/205/}"
CL = r"; \href{https://www.law.cornell.edu/supremecourt/text/406/205}{Cornell LII}"

def Q(quote, attrib):
    # Attribution placed inside the quote block; tools/normalize_quotes.py moves it to a
    # Group A "\noindent ---" line (check_brief.py does not match manual_quotes.txt's ".tex" names).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "), S(attrib, glue="\n"),
            N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"Applying strict scrutiny under the Free Exercise Clause, the Court held that Wisconsin could not criminally punish Amish parents for refusing to send their children to formal high school after the eighth grade, because the State's interest in one or two more years of schooling did not outweigh the grave threat to the Amish religious way of life (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", frm="Respondents Jonas Yoder", to=r"\subsection{Procedural History}")],
  "Procedural History": [SEC("Facts and Procedural History", frm="On complaint of the public school")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Wisconsin Supreme Court (reversing respondents' convictions) by a \textbf{6--1} vote, with seven Justices participating. The case was argued on December 8, 1971, and decided on May 15, 1972 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/406/205}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Burger delivered the opinion of the Court, joined by Justices Brennan, Stewart, White, Marshall, and Blackmun.
    \item \textbf{Concurring Opinions:} Justice Stewart filed a concurring opinion, joined by Justice Brennan. Justice White filed a concurring opinion, joined by Justices Brennan and Stewart.
    \item \textbf{Dissenting Opinion:} Justice Douglas filed an opinion dissenting in part (concurring in the judgment as to Jonas Yoder and dissenting as to Adin Yutzy and Wallace Miller).
    \item \textbf{Not Participating:} Justices Powell and Rehnquist took no part in the consideration or decision of the case.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Burger)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Stewart)}"),
    SEC("Concurring and Dissenting", frm="Justice Stewart wrote briefly", to=r"\subsection{Justice White"),
    N(r"\subsection{Concurring Opinion (Justice White)}"),
    SEC("Concurring and Dissenting", frm="Justice White described", to=r"\subsection{Justice Douglas"),
    N(r"\subsection{Opinion Dissenting in Part (Justice Douglas)}"),
    SEC("Concurring and Dissenting", frm="Justice Douglas joined the judgment"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Early Narrowing:}", glue=" "),
    S(r"Over the next two decades, however, the Court narrowed its reach: \href{https://supreme.justia.com/cases/federal/us/455/252/}{\emph{United States v. Lee}}, 455 U.S. 252, 258--61 (1982), denied an Amish employer a Social Security tax exemption, and \href{https://supreme.justia.com/cases/federal/us/485/439/}{\emph{Lyng v. Northwest Indian Cemetery Protective Ass'n}}, 485 U.S. 439, 456--57 (1988), confined \emph{Yoder} to direct governmental coercion rather than internal government operations."),
    N(r"\item \textbf{\emph{Smith} and the ``Hybrid Situation'':}", glue=" "),
    S(r"In \href{https://supreme.justia.com/cases/federal/us/494/872/}{\emph{Employment Division v. Smith}}, 494 U.S. 872, 878--85 (1990), the Court largely repudiated \emph{Sherbert}--\emph{Yoder} strict scrutiny for neutral, generally applicable laws, but preserved \emph{Yoder} as a ``hybrid situation'' combining Free Exercise with the parental right to direct education recognized in \href{https://supreme.justia.com/cases/federal/us/268/510/}{\emph{Pierce v. Society of Sisters}}, 268 U.S. 510 (1925) (494 U.S. at 881--82 \& n.1)."),
    N(r"\item \textbf{Revitalization in \emph{Mahmoud v. Taylor}:}", glue=" "),
    S(r"In \href{https://www.law.cornell.edu/supremecourt/text/24-297}{\emph{Mahmoud v. Taylor}}, 606 U.S. 522 (2025) (6--3, Alito, J.), the Court decisively revitalized \emph{Yoder}, rejecting lower-court views that it was ``\emph{sui generis}'' and holding instead that it ``embodies a robust principle of general applicability.'' Granting a preliminary injunction to Muslim, Catholic, and Ukrainian Orthodox parents seeking advance notice and opt-outs from K--5 ``LGBTQ+-inclusive'' storybooks, the Court held that normative instruction posing ``a very real threat of undermining'' parental religious formation imposes a burden ``of the exact same character as that in \emph{Yoder},'' triggering strict scrutiny \emph{regardless} of \emph{Smith} neutrality and without deciding ``hybrid rights'' (606 U.S. 522, n.14). Justice Thomas concurred on \emph{Yoder}'s historical-pedigree inquiry, while Justice Sotomayor dissented (joined by Justices Kagan and Jackson), warning that treating ``mere exposure'' as coercion contradicts \emph{Lyng} and risks administrative chaos."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Exemption Required): Raising the Attendance Age to 18.} A State raises its compulsory-attendance age from 16 to 18 and prosecutes Old Order Amish parents whose 16- and 17-year-olds are learning farming and carpentry at home under parental supervision. The burden is the one the Court found in \textit{Yoder}: formal high school removes adolescents from the community during the formative years before adult baptism. The State's interests in citizenship and self-sufficiency are already served by eight years of schooling plus the Amish vocational system, and it cannot show with particularity how two more years of classroom attendance for this small group would harm those interests. Under \textit{Yoder}'s ``interests of the highest order'' standard, the prosecutions fail (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Strict Scrutiny Triggered): Normative Classroom Instruction.} Devout parents seek advance notice and the chance to excuse their children from", glue=" "),
    S(r"a mandatory fourth-grade unit with teacher scripts correcting traditional gender-role views", glue=""),
    N(r". The parents are not challenging what the school teaches other children; they seek to keep their own children out of instruction designed to change the religious views the parents are trying to instill. After \textit{Mahmoud v. Taylor} read \textit{Yoder} as a general principle rather than an Amish-specific exception, instruction of this kind is treated as a burden on parents' right to direct their children's religious upbringing that triggers strict scrutiny even though the curriculum applies to everyone. The school district must show a compelling reason for refusing an opt-out."),
    N(r"\item \textbf{Opposite-Side (No Exemption): Secular Communitarians.}", glue=" "),
    S(r"Parents in a self-sufficient, law-abiding, non-theistic agrarian commune inspired by Thoreau withdraw their 15-year-olds after eighth grade for structured farm-vocational training. Under \emph{Yoder}, their claim \emph{fails} strict scrutiny because ``purely secular considerations'' do not trigger the Religion Clauses (\href{https://supreme.justia.com/cases/federal/us/406/205/}{406 U.S. at 215--16}), leaving only rational-basis review under \emph{Pierce}---though Douglas's dissent (\href{https://supreme.justia.com/cases/federal/us/398/333/}{\emph{Welsh}}) and Establishment Clause parity provide sharp counterarguments."),
    N(r"\item \textbf{Opposite-Side (No Exemption): A Faith That Forbids All Schooling.} Members of a small religious community refuse to send their children to any school, or to provide any home instruction, because their faith forbids formal learning of any kind; their children reach adolescence unable to read. The State prosecutes the parents under its compulsory-attendance law. \textit{Yoder} rested heavily on the Amish acceptance of eight years of elementary schooling and on the ``relatively slight'' deviation at issue, and Justice White's concurrence, joined by two members of the majority, stressed that it would be ``a very different case'' if a religion forbade all formal schooling. The State's interest in basic literacy and the child's future is of the highest order and cannot be served by a less restrictive means, so the prosecutions likely succeed."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): A Vaccine Requirement With Medical Exemptions.} Devout parents seek a religious exemption from", glue=" "),
    S(r"a mandatory measles-vaccine rule permitting medical exemptions", glue=""),
    N(r" as a condition of school attendance. The State can rely on \textit{Prince v. Massachusetts}, which \textit{Yoder} distinguished as involving a threat to public health and safety, and argue that a communicable-disease rule does not interfere with religious formation the way high school did for the Amish. But the parents can argue that allowing medical exemptions while refusing religious ones means the rule is not generally applicable under \textit{Fulton v. City of Philadelphia}, 593 U.S. 522 (2021), which would trigger strict scrutiny regardless of \textit{Yoder}. Whether the State's interest in preventing outbreaks survives that scrutiny is genuinely contested."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{``Good Citizen''", to=r"\end{itemize}")],
  "Key Quotations":
    Q(r"``The essence of all that has been said and written on the subject is that only those interests of the highest order and those not otherwise served can overbalance legitimate claims to the free exercise of religion.''", r"Burger, C.J., " + JH + r"{406 U.S. at 215}" + CL)
    + Q(r"``A way of life, however virtuous and admirable, may not be interposed as a barrier to reasonable state regulation of education if it is based on purely secular considerations; to have the protection of the Religion Clauses, the claims must be rooted in religious belief.''", r"Burger, C.J., " + JH + r"{406 U.S. at 215}" + CL)
    + Q(r"``As the record shows, compulsory school attendance to age 16 for Amish children carries with it a very real threat of undermining the Amish community and religious practice as they exist today; they must either abandon belief and be assimilated into society at large or be forced to migrate to some other and more tolerant region.''", r"Burger, C.J., " + JH + r"{406 U.S. at 218}" + CL)
    + Q(r"``A regulation neutral on its face may, in its application, nonetheless offend the constitutional requirement for governmental neutrality if it unduly burdens the free exercise of religion.''", r"Burger, C.J., " + JH + r"{406 U.S. at 220}" + CL)
    + Q(r"``It is the future of the student, not the future of the parents, that is imperiled by today's decision. If a parent keeps his child out of school beyond the grade school, then the child will be forever barred from entry into the new and amazing world of diversity that we have today.''", r"Douglas, J., dissenting in part, " + JH + r"{406 U.S. at 245}" + CL),
 },
 "dropped": [
  "Case Metadata: docket number, posture, provisions/statute lines, file comments (Justia and Cornell links kept in Judicial Votes).",
  "Facts: the '\\subsection{Factual Background}' heading (the Group A section heading replaces it).",
  "Legacy section: opening 'high-water mark' sentence; RFRA / City of Boerne / Fulton sentence (not applications of Yoder); Mahmoud remand sentence (Feb. 19, 2026 permanent injunction - unverified); Miller v. McDonald paragraph (lower-court litigation). Kept: Lee/Lyng narrowing, Smith 'hybrid' treatment, Mahmoud v. Taylor.",
  "Key Quotations: bold topic labels before each quote (attributions kept).",
  "Exam Hypothetical 2: its Mahmoud/Prince/Miller analysis sentence (replaced by new analysis in Examples 2 and 5; Miller is a 2026 lower-court ruling the new text does not rely on).",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all five kept, none added. Attributions are emitted inside each quote block and converted by normalize_quotes.py, as in 181_missouri_v_holland.",
           "Example 5 cites Fulton v. City of Philadelphia, 593 U.S. 522 (2021), which the brief already discusses."],
}

emit(__file__, FILL)
