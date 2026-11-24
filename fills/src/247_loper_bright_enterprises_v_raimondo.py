"""Fill for 247_loper_bright_enterprises_v_raimondo. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/603/22-451/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Overruling \textit{Chevron}, the Court held 6--3 (6--2 in \textit{Loper Bright}) in a challenge to a rule making herring fishermen pay for federal observers that the APA requires courts to exercise independent judgment on whether an agency acted within its statutory authority, rather than deferring to an agency's reading of an ambiguous statute (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Two sets of family-owned Atlantic herring")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Two sets of family-owned Atlantic herring")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{vacated and remanded} both judgments, by a \textbf{6--3} vote in \textit{Relentless} and a \textbf{6--2} vote in \textit{Loper Bright} (Justice Jackson recused). The cases were argued on January 17, 2024, and decided on June 28, 2024 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/22-451}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Roberts delivered the opinion of the Court, joined by Justices Thomas, Alito, Gorsuch, Kavanaugh, and Barrett.
    \item \textbf{Concurring Opinions:} Justice Thomas filed a concurring opinion. Justice Gorsuch filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Kagan filed a dissenting opinion, joined by Justice Sotomayor, and by Justice Jackson as to \textit{Relentless}.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Question Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined the opinion in full", to=r"  \item \textbf{Justice Gorsuch", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Gorsuch)}"), N("Justice Gorsuch", glue=" "),
    SEC("Concurring and Dissenting", frm="Declared that", to=r"  \item \textbf{Justice Kagan", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Kagan)}"), N("Justice Kagan", glue=" "),
    SEC("Concurring and Dissenting", frm="Defended \\textit{Chevron}", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Clarified Boundaries", to=r"  \item \textbf{Rise of"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (No Deference): Defining a Statutory Term.} Suppose", glue=" "),
    S(r"Congress empowers the EPA to set emissions limits for ``emerging synthetic compounds'' and directs the agency to promulgate rules ``as the Administrator deems reasonable and necessary to protect public health.''", glue=" "),
    N(r"EPA", glue=" "),
    S(r"defines ``emerging synthetic compound'' to include a legacy chemical used since 1950", glue=""),
    N(r". Whether a chemical in use for seventy years is ``emerging'' is a question about the scope of EPA's statutory authority, not a choice within it. Under \textit{Loper Bright}, the court reviews the definition", glue=" "),
    S(r"\textit{de novo} using traditional statutory tools (granting at most \textit{Skidmore} persuasive weight)", glue=""),
    N(r", and if the best reading of ``emerging'' excludes legacy chemicals, EPA's definition falls even though the term is ambiguous."),
    N(r"\item \textbf{Same-Side (No Deference): Making Regulated Parties Pay for Inspectors.} A statute authorizes an agency to require inspectors aboard cargo barges and expressly allows the agency to charge barge operators for inspectors in two specified programs, but says nothing about charging operators in other programs. The agency issues a rule requiring all operators to pay for inspectors. Before \textit{Loper Bright}, a court might have found the silence ambiguous and upheld the rule as a permissible reading. Now the court must decide for itself the ``single, best meaning'' of the statute, and Congress's express authorization of fees in only two programs strongly suggests that the agency has no such power elsewhere. The agency's view receives at most \textit{Skidmore} respect (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Deference Survives): A Choice Within an Express Delegation.} Under the same emerging-compounds statute, EPA", glue=" "),
    S(r"chooses a 10-parts-per-billion threshold after weighing scientific studies and compliance costs", glue=""),
    N(r". Here", glue=" "),
    S(r"the court recognizes Congress's express ``reasonable and necessary'' delegation and reviews EPA's threshold deferentially for reasoned decisionmaking under APA \S~706(2)(A)", glue=""),
    N(r". \textit{Loper Bright} expressly preserved respect for statutes that delegate discretionary authority to an agency; the court polices the boundary of the delegation but does not substitute its own judgment about the right number."),
    N(r"\item \textbf{Opposite-Side (Prior Holding Stands): Relitigating a Rule Upheld Under \textit{Chevron}.} In 2010 the Supreme Court upheld a specific agency rule, applying \textit{Chevron} and deferring to the agency's reading of an ambiguous statute. After \textit{Loper Bright}, a company subject to the same rule sues, arguing that the rule must now be vacated because the precedent upholding it rested on the overruled deference framework. The challenge fails. \textit{Loper Bright} stated that it does not call into question prior cases that relied on \textit{Chevron}: their holdings that specific agency actions are lawful remain subject to statutory \textit{stare decisis}, and mere reliance on \textit{Chevron} is not a ``special justification'' for overruling them."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): An Agency Reverses Course.}", glue=" "),
    S(r"In 2012, a court of appeals upheld an FDA rule under \textit{Chevron} Step Two. In 2026, a new administration repeals that rule and adopts the opposite statutory interpretation. Under \textit{Loper Bright} (603 U.S. at 412), statutory \textit{stare decisis} protected the 2012 holding that the original rule was lawful---but without \textit{Chevron} and \textit{Brand X}, can the agency defend its new interpretation as merely ``permissible,'' or must the reviewing court now independently determine the single best meaning of the statute?", glue=" "),
    N(r"The 2012 decision held only that the old reading was permissible, not that it was the best reading, so it may not settle whether the opposite reading is lawful. If the court concludes the old reading was best, the reversal fails; if the new reading is best, the prior precedent may not stand in its way. \textit{Loper Bright} did not say how such a precedent binds a later, contrary interpretation."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{The ``Single Best Meaning''", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: consolidated docket, slip-opinion and other source links, lower-court citations, Chapter placement line (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory sentence; Corner Post / Ohio Telecom item (limitations period and a lower-court application - not this case's holding); 'Rise of Skidmore' item (litigation-trend commentary). Kept: Seven County / Urias-Orellana item.",
  "'Opposite Side Contrast: Chevron and Seven County' subsection - an exam tip comparing cases, not a fact pattern; its point is covered by Example 3 and the kept Subsequent Developments item.",
 ],
 "notes": ["Kept Seven County (2025) / Urias-Orellana v. Bondi (2026) item is beyond this drafter's ability to verify fully (particularly Urias-Orellana); it must be checked in the audit.",
           "Example 5 reuses Neon's hypothetical (which mentions a 2026 repeal as a hypothetical date) and adds an explanation of why the outcome is uncertain."],
}

emit(__file__, FILL)
