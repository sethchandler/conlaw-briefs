"""Fill for 261_tinker_v_des_moines. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/393/503/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Holding 7--2 that students do not ``shed their constitutional rights to freedom of speech or expression at the schoolhouse gate,'' the Court ruled that a school may not punish passive political expression, such as black armbands protesting the Vietnam War, unless it reasonably forecasts material and substantial disruption (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Petitioners sued through their fathers")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Petitioners sued through their fathers")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{7--2} vote. The case was argued on November 12, 1968, and decided on February 24, 1969 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Fortas delivered the opinion of the Court, joined by Chief Justice Warren and Justices Douglas, Brennan, White, and Marshall.
    \item \textbf{Concurring Opinions:} Justice Stewart and Justice White each filed a concurring opinion.
    \item \textbf{Dissenting Opinions:} Justice Black and Justice Harlan each filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Question Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Fortas)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Stewart)}"), N("Justice Stewart", glue=" "),
    SEC("Concurring and Dissenting", frm="Agreed with the judgment and much", to=r"  \item \textbf{Justice White", lc=True),
    N(r"\subsection{Concurring Opinion (Justice White)}"), N("Justice White", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined the Court's opinion while", to=r"  \item \textbf{Justice Black", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Black)}"), N("Justice Black", glue=" "),
    SEC("Concurring and Dissenting", frm="Issued a fierce dissent", to=r"  \item \textbf{Justice Harlan", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Harlan)}"), N("Justice Harlan", glue=" "),
    SEC("Concurring and Dissenting", frm="Agreed that public schools", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Three Categorical Carve-Outs", to=r"  \item \textbf{2025--2026 Frontier"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Student Wins): A ``Green Tyranny'' T-Shirt.}", glue=" "),
    S(r"Following a polarizing local school-board vote on district climate policy, a 16-year-old public high school student wears a plain T-shirt to school reading ``Board Policy = Green Tyranny.'' She attends classes quietly, though two classmates argue loudly with her in the cafeteria during lunch, requiring a monitor to tell them to sit down. The principal orders her to turn the shirt inside out under a newly announced rule barring ``apparel criticizing school board policies,'' explaining that heated community protests over the vote might spill into the hallways. Meanwhile, students wearing ``Save Our Planet'' shirts are not disciplined.", glue=" "),
    S(r"The T-shirt is passive, non-vulgar, non-school-sponsored political speech squarely governed by \textit{Tinker} (not \textit{Fraser}, \textit{Hazelwood}, or \textit{Morse}). A brief lunchtime argument resolved by a monitor falls far short of ``material and substantial interference,'' and the principal's generalized worry about community protests is precisely the ``undifferentiated fear or apprehension of disturbance'' \textit{Tinker} rejects. Moreover, permitting ``Save Our Planet'' shirts while banning anti-policy shirts mirrors Des Moines's unconstitutional viewpoint singling-out."),
    N(r"\item \textbf{Same-Side (Student Wins): Lunchtime Leaflets About a City Council Meeting.} During the lunch period, a high school student hands classmates leaflets urging them to attend a city council meeting on local police policy. The leaflets are not vulgar, are not school-sponsored, and promote no illegal activity. A few students toss them aside; no class is interrupted. The principal suspends the student under a rule forbidding distribution of political material on campus, explaining that police policy is a divisive topic that could upset some families. Under \textit{Tinker}, the school must point to facts reasonably forecasting material and substantial interference with schoolwork or discipline, and a wish to avoid the discomfort of an unpopular viewpoint is not enough. Peaceful communication among students during lunch is the kind of intercommunication \textit{Tinker} treated as part of education, so the suspension violates the First Amendment."),
    N(r"\item \textbf{Opposite-Side (School Prevails): Documented Disruption and a Viewpoint-Neutral Ban.} Change two facts in the T-shirt example:", glue=" "),
    S(r"suppose (1) prior weeks at the same school saw physical altercations, walked-out classes, and repeated hallway confrontations specifically triggered by competing climate-policy apparel, and (2) the school enforces a viewpoint-neutral ban on \textit{all} apparel referencing the climate dispute (barring both ``Green Tyranny'' and ``Save Our Planet'' shirts) while allowing students to debate the issue in social-studies class and after-school clubs. Under those facts, the school has concrete, documented evidence reasonably forecasting ``material and substantial disruption'' rather than mere undifferentiated fear, and has eliminated viewpoint discrimination---bringing the restriction squarely within \textit{Tinker}'s permissible exception (and paralleling \textit{Blackwell v. Issaquena County Bd. of Ed.}, 363 F.2d 749 (5th Cir. 1966), distinguished by Justice Fortas in \textit{Tinker})."),
    N(r"\item \textbf{Opposite-Side (School Prevails): Editing the Journalism Class Newspaper.} Students in a high school journalism class write an article for the class's newspaper, which is produced with school funds under a teacher's supervision, describing named classmates' experiences with family divorce. The principal removes the article before publication, concerned that the families were not given a chance to respond and that the material is inappropriate for younger readers. \textit{Tinker}'s disruption test does not govern. Under \textit{Hazelwood School District v.\ Kuhlmeier}, 484 U.S.\ 260 (1988), a school may control the content of school-sponsored expressive activities, such as a curricular newspaper, when its actions are reasonably related to legitimate pedagogical concerns. Because readers would attribute the newspaper to the school, the principal may edit it without proving any forecast of disruption."),
    N(r"\item \textbf{Fence-Sitter (Unsettled): A Weekend Post Mocking a Teacher.} On a Saturday, from home, a student posts on social media an edited photo of a teacher with a crude, demeaning caption, which spreads quickly among classmates. On Monday, students giggle and pass the image around during the teacher's class, and the teacher reports feeling humiliated. The school suspends the student. Under \textit{Mahanoy}, off-campus speech receives strong protection because the school's \textit{in loco parentis} role is diminished there, yet the Court left room for schools to address serious bullying or harassment of particular people. The school can point to some in-class distraction and to \textit{Tinker}'s undefined concern for the rights of others; the student can answer that the post was off-campus mockery that caused discomfort rather than material and substantial disruption. How courts strike that balance remains uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{Exam Hypothetical")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: full case name, docket number, Chapter/Topic line.",
  "Legacy section: introductory sentence; '2025--2026 Frontier Disputes' item (pending litigation and commentary). Kept: Fraser/Hazelwood/Morse carve-outs and Mahanoy items.",
  "Exam Hypothetical: 'Hypothetical:' and 'Analysis & Opposite Side Contrast' labels, 'Student's Winning Case' and 'Opposite Side Contrast' item labels, and the lead-in 'Change two facts:' (text reused in Examples 1 and 3).",
 ],
}

emit(__file__, FILL)
