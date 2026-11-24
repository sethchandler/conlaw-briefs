"""Fill for 209_virginia_v_black. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/538/343/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Reviewing Virginia's cross-burning statute, the Court held that a State may ban cross burning carried out with intent to intimidate, a form of true threat, without violating \textit{R.A.V.}; but a plurality struck down the provision treating any cross burning as prima facie evidence of that intent (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="After the Virginia Court of Appeals affirmed")],
  "Procedural History": [SEC("Facts and Procedural History", frm="After the Virginia Court of Appeals affirmed")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed in part, vacated in part, and remanded}. The case was argued on December 11, 2002, and decided on April 7, 2003 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/538/343}{Cornell LII}). Disposition:", glue=" "),
    S(r"7--2 to invalidate Black's conviction (plurality + Souter/Kennedy/Ginsburg; Scalia agreed the conviction could not stand due to the jury instruction but opposed dismissing the indictment); 5--4 to vacate and remand as to Elliott and O'Mara (plurality + Scalia)."),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion (Parts I--III):} Justice O'Connor delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices Stevens, Scalia, and Breyer.
    \item \textbf{Plurality Opinion (Parts IV--V):} Justice O'Connor, joined by Chief Justice Rehnquist and Justices Stevens and Breyer.
    \item \textbf{Concurring Opinion:} Justice Stevens filed a concurring opinion.
    \item \textbf{Opinions Concurring in Part and Dissenting in Part:} Justice Scalia filed an opinion concurring in part, concurring in the judgment in part, and dissenting in part, joined by Justice Thomas as to Parts I and II. Justice Souter filed an opinion concurring in the judgment in part and dissenting in part, joined by Justices Kennedy and Ginsburg.
    \item \textbf{Dissenting Opinion:} Justice Thomas filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Parts I--III) and Plurality Opinion (Parts IV--V) (Justice O'Connor)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Stevens)}"), N("Justice Stevens", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined O'Connor's opinion, reiterating", to=r"  \item \textbf{Justice Scalia", lc=True),
    N(r"\subsection{Opinion Concurring in Part, Concurring in the Judgment in Part, and Dissenting in Part (Justice Scalia)}"), N("Justice Scalia", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined Parts I--III but attacked", to=r"  \item \textbf{Justice Souter", lc=True),
    N(r"\subsection{Opinion Concurring in the Judgment in Part and Dissenting in Part (Justice Souter)}"), N("Justice Souter", glue=" "),
    SEC("Concurring and Dissenting", frm="Concluded the entire Virginia statute", to=r"  \item \textbf{Justice Thomas", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC("Concurring and Dissenting", frm="Argued that intimidating cross burning", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Subjective Mens Rea Required (\textit{Counterman v.\ Colorado}):}", glue=" "),
    S(r"In \textit{Counterman} (7--2, opinion by Justice Kagan), the Court held that to provide ``breathing space'' against self-censorship, the First Amendment requires the State in true-threats prosecutions to prove a subjective mens rea of at least \textbf{recklessness}---that the speaker ``consciously disregarded a substantial risk that his communications would be viewed as threatening violence.''", glue=" "),
    S(r"Crucially, the \textit{Counterman} majority clarified (n.~3) that \textit{Black}'s references to ``intent'' reflected Virginia's statutory element rather than a constitutional floor of purpose or knowledge.", glue=" "),
    N(r"(\href{https://supreme.justia.com/cases/federal/us/600/22-138/}{\textit{Counterman v.\ Colorado}, 600 U.S.\ 66 (2023)}.)"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Ban Valid): A Noose on an Election Clerk's Porch.}", glue=" "),
    S(r"Responding to a wave of threats against local election workers, a State enacts a statute making it a felony ``to hang a noose on the property of another or in a public place with the intent to intimidate any person,'' and adds: ``The display of a noose in public view shall be prima facie evidence of intent to intimidate.''", glue=" "),
    N(r"Defendant A hangs a noose on a Black election clerk's porch at night.", glue=" "),
    S(r"Under \textit{Black} Parts I--III, the core ban on hanging a noose with intent to intimidate is constitutional: like cross burning, a noose has a uniquely virulent history as a signal of impending racial and vigilante violence, and because the ban applies regardless of the victim's race or viewpoint, it fits \textit{R.A.V.}'s virulence exception.", glue=" "),
    N(r"If the jury finds intent from the context---a nighttime display at a targeted official's home---rather than from the prima facie clause, Defendant A's conviction stands."),
    N(r"\item \textbf{Same-Side (Ban Valid): An Effigy Burned in a Neighbor's Driveway.} A State makes it a crime to burn any object on another person's property with intent to place that person in fear of bodily harm. After a dispute, a man burns an effigy of his neighbor in the neighbor's driveway while shouting that the neighbor will be next. The statute does not single out any message or symbol; it targets intimidation, which \textit{Black} identifies as a type of true threat directed at a person with intent to place the victim in fear of bodily harm or death. Because the State must prove that intent from the facts, rather than presuming it from the act, the prosecution fits within the unprotected category and raises none of the \textit{R.A.V.} concerns that a content-selective ban would."),
    N(r"\item \textbf{Opposite-Side (Prima Facie Clause Invalid): A Noose in a Protest Sculpture.} Under the same noose statute, Defendant B, a political artist, hangs a noose on a public plaza sculpture to protest capital punishment, and the prosecution relies on the prima facie clause rather than proof of intent.", glue=" "),
    S(r"However, under \textit{Black} Parts IV--V, the prima facie evidence clause is facially unconstitutional because it strips away context and risks convicting Defendant B for core political protest."),
    N(r"\item \textbf{Opposite-Side (Statute or Prosecution Invalid): A Viewpoint-Selective Ban and an Objective Standard.}", glue=" "),
    S(r"Now remove the prima facie clause and alter the statute so it bans ``burning a cross or hanging a noose \textit{to intimidate any person on the basis of race, religion, or political party},'' or alternatively prosecutes Defendant B under a general threat statute using an \textit{objective reasonable-person standard} with no subjective mens rea. Under the first variation, adding the ``on the basis of'' list destroys the \textit{Black} distinction and triggers invalidation under \textit{R.A.V. v. St. Paul} as viewpoint/topic discrimination within a proscribable class. Under the second variation, prosecuting Defendant B without proving at least subjective \textit{recklessness} that others would view the display as threatening violence violates \textit{Counterman v. Colorado} (2023)."),
    N(r"\item \textbf{Fence-Sitter (Close Call): A Burning-Cross Image Posted Online.} During a local election, a man posts an image of a burning cross on social media and tags the account of a Black candidate, adding no words. He is prosecuted under a statute banning communications made with intent to intimidate. He says the post expressed his political views to his followers; the candidate says she understood it as a threat against her. Under \textit{Black}, a burning cross directed at a person can be a true threat, but the same symbol can also be political expression, and context decides which. Tagging the candidate points toward targeting her; the absence of any physical presence or explicit statement points the other way. Whether the State can prove intent to intimidate is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Tension with", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, metadata vote breakdown items (restated in Judicial Votes), duplicate links.",
  "Legacy section: first paragraph (framing; circuit split; Elonis); Counterman concurrence/dissent sentence; 'Through 2026' sentence (People v. Crawford, 2025 CO 22; Tenth Circuit certification of July 28, 2026). Kept: Counterman holding and footnote-3 sentences.",
  "Exam Hypothetical: 'Virginia v. Black Analysis' and 'Opposite Side Contrast' labels; the 'Two defendants are prosecuted' sentence (restated in Examples 1 and 3).",
 ],
 "notes": [],
}

emit(__file__, FILL)
