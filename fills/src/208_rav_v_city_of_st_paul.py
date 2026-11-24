"""Fill for 208_rav_v_city_of_st_paul. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/505/377/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"After a teenager burned a cross in a Black family's yard, the Court unanimously struck down St.~Paul's bias-motivated crime ordinance; Justice Scalia's five-Justice majority held that even within an unprotected category like fighting words, government may not single out disfavored topics or viewpoints for punishment (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="R.A.V. moved to dismiss")],
  "Procedural History": [SEC("Facts and Procedural History", frm="R.A.V. moved to dismiss")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} the Minnesota Supreme Court's judgment. The judgment was unanimous (9--0), but the Justices divided 5--4 on the rationale. The case was argued on December~4, 1991, and decided on June~22, 1992 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/90-7675}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Scalia delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices Kennedy, Souter, and Thomas.
    \item \textbf{Concurring Opinions:} Justice White concurred in the judgment, joined by Justices Blackmun and O'Connor, and by Justice Stevens except as to Part~I-A. Justice Blackmun concurred in the judgment. Justice Stevens concurred in the judgment, joined by Justices White and Blackmun as to Part~I.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Scalia)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Judgment (Justice White)}"), N("Justice White", glue=" "),
    SEC("Concurring and Dissenting", frm="Argued that the Court should", to=r"\item \textbf{Justice Blackmun", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Blackmun)}"), N("Justice Blackmun", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined White's overbreadth", to=r"\item \textbf{Justice Stevens", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Stevens)}"), N("Justice Stevens", glue=" "),
    SEC("Concurring and Dissenting", frm="Rejected both Scalia's", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"\item \textbf{Hate-Crime Penalty", to=r"\item \textbf{Viewpoint Discrimination and"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Law Invalid): Fighting Words That Disparage the Police.} After tense street protests, a city makes it a crime to direct at a police officer any fighting words that disparage law enforcement, while leaving fighting words praising the police, or insulting the officer on other grounds, unregulated. A protester convicted for a face-to-face epithet challenges the ordinance. Under \textit{R.A.V.}, the city may ban fighting words because of their abusive mode, but it may not pick out only those that carry a disfavored message. This ordinance is worse than St.~Paul's: it discriminates by viewpoint on its face, licensing one side of the debate over policing to fight freestyle. The city's interest in protecting officers could be served by a neutral ban on all fighting words directed at anyone, so the law fails strict scrutiny."),
    N(r"\item \textbf{Same-Side (Law Invalid): Obscenity Banned Only When It Mocks Officials.} A state already bars the sale of obscene material under the governing test for obscenity, then adds a felony enhancement that applies only to obscene videos that ridicule elected officials. A distributor of such a video challenges the enhancement. Obscenity is a proscribable category, but \textit{R.A.V.} holds that categories of unprotected speech are not ``entirely invisible to the Constitution.'' The enhancement does not target what makes obscenity unprotected, such as especially graphic prurient content; it targets political criticism, a message the State could never suppress directly. Like Justice Scalia's example of banning only libel critical of the government, the distinction suggests that official suppression of ideas is afoot, and none of the three exceptions saves it."),
    N(r"\item \textbf{Opposite-Side (Law Likely Valid): Threats Against Election Workers.} A state law imposes heavier penalties for true threats of violence made against election officials and poll workers than for other true threats. A defendant convicted of threatening a county clerk argues that, under \textit{R.A.V.}, the law singles out threats on a particular subject. The State answers with \textit{R.A.V.}'s first exception. Justice Scalia explained that Congress may criminalize only threats against the President because the reasons threats are proscribable---fear, disruption, and the risk of violence---have special force there. The same reasoning applies to the officials who run elections: the law selects the subset of threats in which the very harms that make threats unprotected are most acute, and it does not favor any viewpoint on the election itself. The law is likely valid."),
    N(r"\item \textbf{Opposite-Side (Prosecution Valid): Bias Enhancement for Conduct.} Suppose St.~Paul had charged R.A.V. under Minnesota's content-neutral laws against terroristic threats and criminal damage to property, and the State then sought a longer sentence under a statute that enhances penalties when the defendant intentionally selected the victim because of race. That prosecution would raise no \textit{R.A.V.} problem. The underlying crimes punish conduct without regard to any message, and the enhancement punishes the discriminatory selection of a victim, not the expression of an idea. As the Court later held in \href{https://supreme.justia.com/cases/federal/us/508/476/}{\textit{Wisconsin v. Mitchell}, 508~U.S.~476 (1993)}, bias-motivated conduct may be punished more severely, which is why Justice Scalia observed that St.~Paul had sufficient means to punish cross burning without the ordinance."),
    N(r"\item \textbf{Fence-Sitter (Contested): A Campus Harassment Act.}", glue=" "),
    S(r"Following a wave of campus confrontations, a state enacts the ``Campus Harassment Act,'' making it a misdemeanor to utter face-to-face fighting words on public university grounds ``that demean a person on the basis of nationality, religion, or political ideology.'' A student prosecuted for shouting a religious slur at a classmate challenges the statute on its face under the First Amendment.", glue=" "),
    N(r"\textbf{Challenger:}", glue=" "),
    S(r"Even if limited to \textit{Chaplinsky} fighting words, the statute selectively proscribes fighting words addressing three enumerated topics (nationality, religion, political ideology) while leaving unregulated equally provocative fighting words based on personal appearance, family, or athletics. Like St. Paul's ordinance, it fails strict scrutiny because a content-neutral ban on \textit{all} campus fighting words would equally protect campus order without singling out disfavored subjects.", glue=" "),
    N(r"\textbf{State:}", glue=" "),
    S(r"The State would argue that the statute fits \textit{R.A.V.}'s first exception (like \textit{Virginia v. Black}) if legislative findings show that nationality- and religion-based fighting words on campus carry a uniquely virulent risk of immediate violence, or that the law is evenhanded across all viewpoints (unlike St. Paul's ordinance, it covers ``political ideology'' on all sides).", glue=" "),
    N(r"The outcome turns on whether a court sees a demeaning-by-topic rule as a virulent subset of fighting words or as the same topic-based selection \textit{R.A.V.} condemned; the word ``demean'' itself may lead a court to find viewpoint discrimination."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\textbf{Critiques:}", to=r"\textbf{Exam Hypothetical:}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, comment lines (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory paragraph (characterization of R.A.V.'s significance); Matal v. Tam item (viewpoint discrimination generally); 'Recent Roberts Court Refinement' item (Counterman, Vidal v. Elster, Chiles v. Salazar) - tangential. Kept: Wisconsin v. Mitchell and Virginia v. Black items.",
  "Exam Hypothetical: final sentence of the State's 'Opposite Side Contrast' (Mitchell-style alternative), now developed in Example 4; 'Challenger's Argument' and 'Opposite Side Contrast' labels replaced by short labels in the Fence-Sitter example.",
 ],
 "notes": [],
}

emit(__file__, FILL)
