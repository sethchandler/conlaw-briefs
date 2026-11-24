"""Fill for 176_trump_v_mazars_usa_llp. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/591/19-715/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"When House committees subpoenaed a sitting President's personal financial records from his accountants and banks, the Court held 7--2 that neither the heightened standard the President proposed by analogy to executive-privilege cases nor the House's deferential standard governs; courts must weigh four separation-of-powers considerations before such a subpoena is enforced (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="President Trump (suing in his personal capacity)")],
  "Procedural History": [SEC("Facts and Procedural History", frm="President Trump (suing in his personal capacity)")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{vacated and remanded} by a \textbf{7--2} vote. The case was argued on May 12, 2020, and decided on July 9, 2020, together with No.\ 19-760, \textit{Trump v.\ Deutsche Bank AG} (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/19-715}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Roberts delivered the opinion of the Court, joined by Justices Ginsburg, Breyer, Sotomayor, Kagan, Gorsuch, and Kavanaugh.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Thomas filed a dissenting opinion. Justice Alito filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC("Concurring and Dissenting", frm="Argued from original meaning", to=r"  \item \textbf{Justice Alito", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Alito)}"), N("Justice Alito", glue=" "),
    SEC("Concurring and Dissenting", frm="Assumed arguendo", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Application on Remand:}", glue=" "),
    S(r"On remand in \href{https://law.justia.com/cases/federal/appellate-courts/cadc/21-5176/21-5176-2022-07-08.html}{\textit{Trump v. Mazars USA, LLP}, 39 F.4th 774 (D.C. Cir. 2022)}, the D.C. Circuit held that heightened separation-of-powers concerns persisted even after Donald Trump left office, applied the four \textit{Mazars} factors, upheld the Oversight Committee's authority to obtain certain 2016--2018 financial records in aid of presidential-ethics legislation, and narrowed the subpoena's scope", glue=""),
    N(r"."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Heightened Scrutiny Limits the Subpoena): The President's Family Resort as a ``Case Study.''}", glue=" "),
    S(r"Suppose the House Committee on Ways and Means is considering a bill to cap foreign-government hotel and resort payments to any federal official, including the President. The Committee issues a subpoena to a private hospitality management firm for all booking ledgers, guest lists, and pricing contracts from 2018--2026 for a resort owned by the sitting President's family trust, asserting that ``examining the President's resort operations will illuminate industry loopholes.'' The President sues in his personal capacity to enjoin the firm from complying, without invoking executive privilege.", glue=" "),
    S(r"The President's personal capacity and the third-party custodian do not eliminate separation-of-powers scrutiny. Under Factor 1, the House cannot use the President as a ``case study'' for general hospitality or ethics legislation if public filings, other officials' disclosures, or industry data could reasonably supply the needed information. Under Factor 2, an eight-year demand for all guest lists and contracts is likely overbroad relative to foreign-government payments. Under Factor 3, because regulating the President raises sensitive constitutional questions (e.g., Emoluments Clause enforcement), the Committee must offer detailed, substantial evidence tying these specific records to a valid legislative aim rather than disguised law enforcement. Under Factor 4, the court must weigh the institutional burden and partisan-leverage risk."),
    N(r"\item \textbf{Same-Side (Heightened Scrutiny Limits the Subpoena): A Decade of Presidential Medical Records.} A Senate committee drafting legislation on procedures for determining presidential disability subpoenas a hospital for ten years of the sitting President's complete medical records. The committee's only stated justification is that the records will show how presidential health issues arise in practice. Under \textit{Mazars}, the committee must show why the President's own records are needed when expert testimony and historical accounts could inform a general disability statute; a ten-year demand for complete records is far broader than the legislative aim requires; and generic statements of purpose are thin evidence. Medical records are exactly the kind of personal papers the Court warned could otherwise be swept in, so the court should refuse to enforce the subpoena as written."),
    N(r"\item \textbf{Opposite-Side (\textit{Mazars} Inapplicable): A State Grand Jury Subpoena.} A state prosecutor investigating possible business-records fraud by a hotel company has a grand jury subpoena the company's outside accountants for financial records relating to the sitting President's businesses. The President sues to block compliance. The four \textit{Mazars} factors do not apply, because the subpoena comes from criminal process rather than from a rival political branch seeking information for legislation. Under \href{https://www.law.cornell.edu/supremecourt/text/19-635}{\textit{Trump v. Vance}, 591 U.S. 786 (2020)}, decided the same day as \textit{Mazars}, the President has no absolute immunity from a state criminal subpoena and the prosecutor need not show heightened need; the President may raise only the defenses available to any citizen, plus arguments that the subpoena would impede his Article II functions."),
    N(r"\item \textbf{Opposite-Side (Ordinary Legislative-Purpose Review): A Subpoena for a Private Executive's Records.} A House committee drafting bank-capital legislation subpoenas a large bank for the personal account records of its chief executive, who has no government position. The executive objects that the committee is really trying to embarrass him. Because the subpoena does not seek a President's information, \textit{Mazars}'s special separation-of-powers balancing is not triggered. The court asks only whether the subpoena serves a valid legislative purpose on a subject on which legislation could be had, is not aimed at law enforcement or exposure for its own sake, and respects the witness's constitutional rights---the traditional framework of \textit{McGrain v.\ Daugherty}, 273 U.S.\ 135 (1927), and \textit{Watkins v.\ United States}, 354 U.S.\ 178 (1957). If the committee can show how the executive's accounts bear on the bill---for example, on the compensation or risk practices it is considering regulating---that deferential test is likely satisfied."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): A Narrow Subpoena Aimed at a Former President.} After a President leaves office, a House committee drafting amendments to presidential financial-disclosure laws subpoenas his former accounting firm for three years of financial statements, citing specific discrepancies between those statements and his public disclosure forms. The subpoena is narrow and tied to concrete evidence of a legislative need, satisfying several \textit{Mazars} factors. But it is unclear whether the factors still apply with full force once the President is a private citizen, and whether a committee may still not treat an individual President as a case study. The D.C. Circuit on remand in \textit{Mazars} held that heightened concerns persisted after the President left office, but the Supreme Court has not decided the question, so the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Indeterminacy", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket numbers, Chapter/Topic line, SupremeCourt.gov slip-opinion link (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory paragraph on Trump v. Vance (Vance now cited in Example 3); settlement and dismissal details and delay commentary in the remand paragraph; 'Through 2026' paragraph (Trump v. United States, Trump v. Slaughter, West Virginia v. EPA, Biden v. Nebraska, Learning Resources v. Trump) - tangential to Mazars. Kept: D.C. Circuit remand application.",
  "Exam Hypothetical: 'Majority / Mazars Analysis' label (its text reused in Example 1) and 'Opposite Side' Contrast passage (an exam tip on three channels; the Vance channel is now Example 3).",
 ],
 "notes": [
  "Subsequent Developments item is the remand sentence cut before the settlement clause, with a new closing period.",
 ],
}

emit(__file__, FILL)
