"""Fill for 219_smith_v_doe. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/538/84/"
FS = "Facts and Procedural History"
RS = "Reasoning"
SO = "Concurring and Dissenting"
LG = "Doctrinal Significance"
PS = "Pedagogical Critiques"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Alaska applied its sex offender registration and Internet notification law to offenders convicted before it was enacted; the Court held 6--3 that the law was a civil, nonpunitive regulation under the two-step intent--effects test, so its retroactive application did not violate the Ex Post Facto Clause (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="Along with John Doe I's wife")],
  "Procedural History": [SEC(FS, frm="Along with John Doe I's wife")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} the Ninth Circuit by a \textbf{6--3} vote. The case was argued on November 13, 2002, and decided on March 5, 2003 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Kennedy delivered the opinion of the Court, joined by Chief Justice Rehnquist and Justices O'Connor, Scalia, and Thomas.
    \item \textbf{Concurring Opinions:} Justice Thomas filed a concurring opinion. Justice Souter filed an opinion concurring in the judgment.
    \item \textbf{Dissenting Opinions:} Justice Stevens filed a dissenting opinion. Justice Ginsburg filed a dissenting opinion, joined by Justice Breyer.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kennedy)}"),
    SEC(RS, to=r"\subsection{Step One"),
    N(r"\subsubsection{Step One: Legislative Intent}"),
    SEC(RS, frm="Determining whether a statute", to=r"\subsection{Step Two"),
    N(r"\subsubsection{Step Two: Punitive Effects (\textit{Mendoza-Martinez} Guideposts)}"),
    SEC(RS, frm="The Court evaluated ASORA's effects"),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC(SO, frm="Joined the majority in full", to=r"  \item \textbf{Justice Souter", lc=True),
    N(r"\subsection{Opinion Concurring in the Judgment (Justice Souter)}"), N("Justice Souter", glue=" "),
    SEC(SO, frm="Rejected the ``clearest proof''", to=r"  \item \textbf{Justice Stevens", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Stevens)}"), N("Justice Stevens", glue=" "),
    SEC(SO, frm="Argued that ASORA", to=r"  \item \textbf{Justice Ginsburg", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Ginsburg)}"), N("Justice Ginsburg, joined by Justice Breyer,", glue=" "),
    SEC(SO, frm="Agreed with Souter", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC(LG, frm=r"  \item \textbf{2026 Supreme Court Application", to=r"  \item \textbf{Federal Circuit Divergence"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Civil Regulation; No Ex Post Facto Violation): A Retroactive Financial-Fraud Registry.}", glue=" "),
    S(r"Congress enacts the ``Investor Protection Act,'' codified in the civil securities title, requiring anyone convicted of securities fraud since 1995 to report all bank accounts quarterly for life and publishing their home address, photo, and employer on a searchable SEC ``Fraudster Watch'' website, with no off-ramp for rehabilitation.", glue=" "),
    S(r"Under \textit{Smith}, the government argues civil intent (express investor-protection purpose, civil codification, administrative enforcement) and nonpunitive effects (no physical restraint, passive online archive of public convictions, rational fit). Challengers argue under \textit{Snyder} and Justice Ginsburg's dissent that lifetime reporting of private financial accounts and home addresses without individualized risk assessment is excessive and stigmatizing, though \textit{Smith}'s ``clearest proof'' standard heavily favors the government unless geographic or occupational bans are added."),
    N(r"\item \textbf{Same-Side (Civil Regulation; No Ex Post Facto Violation): Civil Commitment of a Dangerous Offender.} As an inmate convicted of child sexual abuse nears release, the State petitions under a newly enacted statute to commit him to a secure treatment facility as a sexually violent predator, relying partly on conduct that predates the law. The statute is placed in the probate code, requires proof of a mental abnormality making the person dangerous, and provides for release once he is no longer dangerous. Under the intent--effects test that \textit{Smith} drew from \textit{Kansas v.\ Hendricks}, 521 U.S.\ 346 (1997), the legislature's civil purpose controls unless the clearest proof shows punitive effect, and \textit{Hendricks} upheld materially identical commitment against an Ex Post Facto challenge."),
    N(r"\item \textbf{Opposite-Side (Punishment): Residency Bans Enforced by the Sentencing Court.}", glue=" "),
    S(r"Suppose instead Congress amends federal criminal statutes to impose a retroactive ``Public Safety Surcharge'' and a 1,500-foot residential exclusion zone around schools and parks on all pre-enactment offenders, enforced by the sentencing court at a criminal modification hearing with immediate re-incarceration for any technical violation.", glue=" "),
    S(r"Unlike \textit{Smith}, this statute fails at \textit{both} steps. Under Step One and \href{https://www.law.cornell.edu/supremecourt/text/24-482}{\textit{Ellingburg v. United States}} (2026), codification in the criminal code, imposition by a sentencing court, and enforcement through criminal resentencing reveal punitive legislative intent, ending the inquiry. Even if Congress labeled it ``civil,'' under Step Two and \textit{Snyder} / \href{https://law.justia.com/cases/federal/appellate-courts/ca6/23-5248/23-5248-2024-05-15.html}{\textit{Doe v. Lee}} (6th Cir. 2024), retroactive residential banishment and revocation-style enforcement impose affirmative physical restraints historically regarded as punishment, supplying the ``clearest proof'' needed to invalidate the law under the Ex Post Facto Clause."),
    N(r"\item \textbf{Opposite-Side (Punishment): Applying Harsher Sentencing Guidelines to an Earlier Crime.} A defendant commits bank fraud in 2005 and is sentenced in 2010 under amended federal Sentencing Guidelines that raise his recommended range well above the range in effect when he acted. No one disputes that a prison sentence is punishment, so there is no civil label for \textit{Smith}'s intent--effects inquiry to test; the only question is whether the change increases the punishment attached to his crime. In \textit{Peugh v.\ United States}, 569 U.S.\ 530 (2013), the Court held that sentencing a defendant under Guidelines promulgated after the offense, when they yield a higher range, violates the Ex Post Facto Clause, even though the Guidelines are advisory."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Lifetime GPS Monitoring Run by the Corrections Department.} A State requires every registrant convicted of an aggravated sex offense, including those convicted before the law took effect, to wear a GPS ankle monitor for life, with the corrections department tracking his location around the clock. The statute declares a public-safety purpose and sits in the civil code, so Step One favors the State. At Step Two, however, the device is a continuous physical burden supervised by corrections officers, resembling the probation and supervised release that \textit{Smith} distinguished because Alaska's registrants could move and work without supervision. Whether that restraint supplies the clearest proof of punishment, or is a reasonable means of protecting the public, has divided courts and is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"  \item \textbf{The ``Clearest", to=r"\subsection{Exam")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: full caption, lower-court citations, Cornell LII links, constitutional-provision line.",
  "Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection.",
  "Legacy section: introductory paragraph (including United States v. Kebodeaux, which merely assumed SORNA's validity); 'Federal Circuit Divergence on Expanded Registries' item (lower-court decisions, including November 2026 Sixth Circuit rulings); 'State Constitutional Pushback' item (state-law decisions). Kept: Ellingburg v. United States (2026).",
  "Exam hypothetical labels 'Analysis:' / 'Contrast:' and the 'Opposite Side' heading (fact patterns and analysis moved verbatim into Examples 1 and 3).",
 ],
 "notes": [
  "Kept Ellingburg v. United States, 607 U.S. ___ (Jan. 20, 2026) item could not be independently verified by the drafter; verify in audit.",
  "Example 1's moved analysis presents both sides but concludes the Smith standard heavily favors the government; it is labeled Same-Side accordingly.",
 ],
}

emit(__file__, FILL)
