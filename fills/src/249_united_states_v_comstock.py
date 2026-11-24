"""Fill for 249_united_states_v_comstock. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/560/126/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Federal prisoners nearing release challenged a statute allowing their indefinite civil commitment as sexually dangerous; the Court held 7--2 that the Necessary and Proper Clause authorized it as a rational, narrow incident of Congress's power to run federal prisons and act as a responsible custodian (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to=r"Acting under \S~4248, the federal government")],
  "Procedural History": [SEC("Facts and Procedural History", frm=r"Acting under \S~4248, the federal government")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{7--2} vote. The case was argued on January 12, 2010, and decided on May 17, 2010 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/08-1224}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Breyer delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Stevens, Ginsburg, and Sotomayor.
    \item \textbf{Concurring Opinions:} Justice Kennedy filed an opinion concurring in the judgment. Justice Alito filed an opinion concurring in the judgment.
    \item \textbf{Dissenting Opinion:} Justice Thomas filed a dissenting opinion, joined by Justice Scalia in all but Part III--A--1--b.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Breyer)}"), SEC("Reasoning"),
    N(r"\subsection{Opinion Concurring in the Judgment (Justice Kennedy)}"),
    SEC("Concurring and Dissenting", frm="Justice Kennedy agreed that", to=r"\textbf{Concurrence in the Judgment (Justice Alito):}"),
    N(r"\subsection{Opinion Concurring in the Judgment (Justice Alito)}"),
    SEC("Concurring and Dissenting", frm="Echoing Kennedy's unease", to=r"\textbf{Dissent (Justice Thomas"),
    N(r"\subsection{Dissenting Opinion (Justice Thomas)}"),
    SEC("Concurring and Dissenting", frm="Justice Thomas argued that"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{\textit{Comstock} Distinguished (\textit{NFIB v.\ Sebelius}):}", glue=" "),
    S(r"Two years later, in \href{https://supreme.justia.com/cases/federal/us/567/519/}{\textit{National Federation of Independent Business v. Sebelius}}, 567 U.S. 519 (2012), Chief Justice Roberts---who had joined Breyer's majority in \textit{Comstock}---joined by the four joint dissenters on this point, rejected the federal government's attempt to sustain the Affordable Care Act's individual health-insurance mandate under the Necessary and Proper Clause. Roberts sharply distinguished \textit{Comstock} as an exercise of authority ``derivative of, and in service to, a granted power,'' holding that even if the mandate was ``necessary,'' compelling inactive individuals to enter commerce to create the predicate for regulation was not ``proper.''"),
    N(r"\item \textbf{\textit{Comstock} Applied (\textit{United States v.\ Kebodeaux}):}", glue=" "),
    S(r"One year later, however, the Court reaffirmed \textit{Comstock}'s core framework in \href{https://supreme.justia.com/cases/federal/us/570/387/}{\textit{United States v. Kebodeaux}}, 570 U.S. 387 (2013), holding 7--2 (again via Justice Breyer) that the Military Regulation Clause combined with the Necessary and Proper Clause empowered Congress to apply federal sex-offender registration requirements (SORNA) to a former Air Force serviceman who had already completed his court-martial sentence, because he remained subject to a preexisting federal registration obligation. Chief Justice Roberts and Justice Alito concurred in the judgment to stress that Congress lacks a general federal police power."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Within Congress's Power): Commitment of Violently Dangerous Federal Prisoners.} Congress amends federal law to allow civil commitment, at the end of a federal sentence, of any prisoner in Bureau of Prisons custody who suffers from a serious mental illness and, as a result, would pose a serious danger of violent conduct if released. As in \S~4248, the government must prove dangerousness by clear and convincing evidence, and the Attorney General must transfer custody to any willing State. Every \textit{Comstock} consideration points toward validity: the statute rationally serves the federal power to imprison and care for federal prisoners, extends a long tradition of federal commitment of dangerous mentally ill prisoners, reflects the government's role as a responsible custodian, accommodates state interests, and is confined to people already in federal custody."),
    N(r"\item \textbf{Same-Side (Within Congress's Power): Holding a Contagious Prisoner Past the Release Date.} A federal inmate due for release next week develops a highly contagious, dangerous infectious disease. A federal statute allows the Bureau of Prisons, after a hearing, to keep such an inmate in medical isolation beyond the end of his sentence until he is no longer contagious, unless the health authorities of his home State agree to take custody. Under \textit{Comstock}, Congress may act as a responsible custodian of those it lawfully holds, protecting the communities into which a prisoner would be released. The measure is narrow, limited to people already in federal custody, temporary, and deferential to state health authorities, so it is a necessary and proper incident of running federal prisons rather than a general police power."),
    N(r"\item \textbf{Opposite-Side (Beyond Congress's Power): Commitment of State Felons via a Firearm Nexus.}", glue=" "),
    S(r"Congress enacts a statute authorizing federal courts to impose lifetime federal civil commitment on any person who has ever been convicted of a \emph{state} violent felony if the person once purchased a firearm that traveled in interstate commerce, even if the person was never in federal custody and the state declines to commit him. A challenger attacks the statute as exceeding Article I.", glue=" "),
    S(r"Under \textit{Comstock}, \textit{Kebodeaux}, and \textit{NFIB}, the statute is unconstitutional. Unlike \S~4248 in \textit{Comstock}, the law is not tied to existing federal custody or responsible management of federal prisons, lacks any historical pedigree of federal supervision over state-only offenders, intrudes directly into the states' traditional police power, and uses an attenuated past commercial nexus to manufacture a sweeping federal civil-commitment power that is neither ``substantially linked'' (Alito/Kennedy) nor ``proper'' (\textit{NFIB})."),
    N(r"\item \textbf{Opposite-Side (Beyond Congress's Power): Commitment of People Never Charged.} Congress authorizes the Attorney General to seek federal civil commitment of any person whom the FBI investigated for a federal sex offense but decided not to charge, if a court finds the person sexually dangerous. The people covered were never convicted, never held by the Bureau of Prisons, and are not subject to any continuing federal obligation. \textit{Comstock} stressed that \S~4248 reached only a small class already in federal custody, which kept its link to enumerated powers from becoming too attenuated. Without that custodial link, the statute does not carry any enumerated power into execution; civil commitment of dangerous persons at large is the kind of general police power the Court said remains with the States."),
    N(r"\item \textbf{Fence-Sitter (Close Call): New Registration Duties for Long-Released Federal Offenders.} Congress requires every person ever convicted of a federal sex offense to register with federal authorities, including people who completed their sentences decades ago and were released without conditions, before any federal registration law existed. In \textit{Kebodeaux}, the Court upheld applying registration rules to a former serviceman because he remained subject to a preexisting federal registration obligation when released. Here, no such continuing obligation exists, so the link to the power that supported the original conviction is weaker. On the other hand, the statute addresses the consequences of federal convictions, is less intrusive than commitment, and builds on a federal registration tradition. Whether the link is close enough is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\textit{Comstock} exposes", to=r"\textbf{``Opposite Side'' Contrast")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: parallel citations, Briefing Book Placement, provisions list.",
  "Legacy section: opening framing sentence; final paragraph (Landor v. Louisiana Department of Corrections (2026) - tangential RLUIPA remedies case, and post-cutoff). Kept: NFIB and Kebodeaux paragraphs.",
  "Pedagogical section: 'Opposite Side' Contrast with NFIB - a comparison of decided cases (exam tip), covered by the NFIB Subsequent Developments item.",
  "Exam Hypothetical: 'How should a court rule?' question and 'Analysis:' label (text reused in Example 3).",
 ],
 "notes": [],
}

emit(__file__, FILL)
