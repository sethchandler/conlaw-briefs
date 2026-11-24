"""Fill for 166_ex_parte_mccardle (pilot). See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/74/506/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Congress may withdraw a statutory route of Supreme Court appellate jurisdiction even after a case has been argued: a unanimous Court dismissed a Reconstruction-era habeas appeal once Congress repealed the 1867 appellate provision, while noting that its older habeas jurisdiction under the Judiciary Act of 1789 remained intact (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="After a hearing, the Circuit Court remanded")],
  "Procedural History": [SEC("Facts and Procedural History", frm="After a hearing, the Circuit Court remanded")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{dismissed} the appeal for want of jurisdiction on April 12, 1869 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/74/506}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Chase delivered the opinion of a unanimous Court, joined by Justices Nelson, Grier, Clifford, Swayne, Miller, Davis, and Field (8--0).
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
    S(r"(Historically, when the Court postponed decision in April 1868 after Congress passed the repealing statute, Justice Grier---joined by Justice Field---entered a sharp protest against the delay, warning that the Court was evading its duty to decide a case already argued; nevertheless, both Justices joined the unanimous dismissal in 1869 once the repealing statute was squarely argued.)"),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Chase)}"), SEC("Reasoning"),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Modern Jurisdiction-Stripping"),
    N(r"\item \textbf{Modern Reaffirmation:}", glue=" "),
    S(r"In \href{https://supreme.justia.com/cases/federal/us/583/16-498/}{\textit{Patchak v. Zinke}}, 583 U.S. 244 (2018), a plurality led by Justice Thomas reaffirmed \textit{McCardle} and upheld the Gun Lake Act's stripping of federal jurisdiction over pending suits relating to a specific parcel of tribal trust land, reasoning that stripping jurisdiction changes the law rather than exercising judicial power (over Chief Justice Roberts's dissent warning that targeting a single pending suit violates \textit{Klein})."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Jurisdiction Strip Upheld): Repealing a Direct-Appeal Route While Certiorari Remains.} Congress repeals a statute that allowed parties in a class of federal enforcement cases to appeal directly from a district court to the Supreme Court, makes the repeal applicable to appeals already docketed, and leaves in place the ordinary route of appeal to a court of appeals followed by certiorari. Like the 1868 Act, the repeal withdraws one statutory avenue of review in express terms without telling the Court how to decide any case. Under \textit{McCardle}'s rule that a repealed jurisdictional statute is treated as if it never existed, the pending direct appeals must be dismissed, and litigants still have another door into the Court (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Jurisdiction Strip Upheld): Barring Certiorari Review of Interlocutory Class-Certification Rulings.} Congress provides that the Supreme Court may not grant certiorari to review a court of appeals' decision on an interlocutory appeal from a class-certification order, but leaves full review available after final judgment. The statute regulates the timing and route of review rather than closing the Court to a category of cases, which places it comfortably within the Exceptions and Regulations Clause as \textit{McCardle} read it. The pattern matches \href{https://supreme.justia.com/cases/federal/us/518/651/}{\textit{Felker v. Turpin}, 518 U.S. 651 (1996)}, which upheld the bar on certiorari review of habeas gatekeeping orders and separately concluded that the statute left the Court's original habeas authority intact."),
    N(r"\item \textbf{Opposite-Side (Strip Likely Invalid): An Outcome-Selective Strip of All Review.}", glue=" "),
    S(r"Congress enacts the ``Uniform Flag Protection Act,'' making flag burning a federal crime and adding Section 5: ``Pursuant to Article III, Section 2, the Supreme Court shall have no appellate jurisdiction, by certiorari, appeal, or original writ of habeas corpus, to review any federal or state court decision upholding a conviction under this Act, including cases currently pending.'' A defendant convicted in state court appeals to the U.S.\ Supreme Court, which already granted certiorari before Section 5 passed.", glue=" "),
    S(r"Unlike \textit{McCardle} and \textit{Felker}, Section 5 forecloses \emph{all} Supreme Court review (eliminating the \textit{Yerger} escape valve) and discriminates asymmetrically by stripping jurisdiction only over decisions \emph{upholding} convictions (raising \textit{Klein} rule-of-decision, Due Process, and First Amendment viewpoint-discrimination objections, as well as a Suspension Clause challenge to stripping habeas). Even if a court rejects the ``essential functions'' thesis under \textit{McCardle}'s plain-text rationale, Section 5 is vulnerable under external constitutional limits (First and Fifth Amendments and the Suspension Clause) and \textit{Klein}'s prohibition on Congress rigging outcomes while leaving courts open to decide in the government's favor."),
    N(r"\item \textbf{Opposite-Side (Strip Invalid): Eliminating Habeas Review for Detainees Without an Adequate Substitute.} Without suspending the writ, Congress provides that no court shall have jurisdiction to hear habeas petitions from noncitizens held as enemy combatants at a U.S. naval base abroad over which the United States exercises complete control, and substitutes only a limited military status review in which detainees cannot present exculpatory evidence gathered after the hearing. \textit{McCardle} does not save the statute: the Exceptions Clause power is subject to the Constitution's other commands, and \href{https://supreme.justia.com/cases/federal/us/553/723/}{\textit{Boumediene v. Bush}, 553 U.S. 723 (2008)}, held that a strip of this kind violates the Suspension Clause unless Congress provides an adequate substitute for habeas."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Stripping All Supreme Court Review of a Constitutional Subject.} Congress provides that the Supreme Court shall have no appellate jurisdiction, by any route, over cases challenging state laws on prayer in public schools, while leaving state courts and lower federal courts free to decide such cases. Read literally, \textit{McCardle}'s statement that the power to make exceptions ``is given by express words'' supports the statute, and the law is neutral on its face: it neither prescribes a rule of decision (\textit{Klein}) nor suspends habeas (\textit{Boumediene}). Unlike the 1868 Act, however, it leaves no alternative route to the Supreme Court and invites fifty state supreme courts to reach different answers on a federal constitutional question, squarely presenting Henry Hart's argument that exceptions may not destroy the Court's essential role in keeping federal law supreme and uniform. The Court has not resolved whether Congress may eliminate every route to Supreme Court appellate review of this class of constitutional challenges while leaving lower courts open, so the outcome is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Broad vs.", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: argument dates, term, Chapter/Topic line, and duplicate \\url{} printouts (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory paragraph; Santos-Zacaria clear-statement discussion; 2026 Court-reform debate sentence (kept: Yerger/Felker, Klein, Boumediene, Patchak).",
  "Exam Hypothetical: 'Opposite Side Contrast' (McCardle vs. Klein) - an exam tip, not a hypothetical; its content is covered by the Klein item and Examples 3-5.",
 ],
}

emit(__file__, FILL)
