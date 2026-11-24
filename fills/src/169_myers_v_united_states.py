"""Fill for 169_myers_v_united_states. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/272/52/"
C = "https://www.law.cornell.edu/supremecourt/text/272/52"
PS = "Pedagogical Critiques"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"When President Wilson fired Portland postmaster Frank Myers without the Senate consent an 1876 statute required, Chief Justice Taft's 6--3 opinion held that Article II gives the President an exclusive, illimitable power to remove executive officers he appoints with Senate consent, and that Congress may not reserve a share of removal to the Senate (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="On April 21, 1921, Myers sued")],
  "Procedural History": [SEC("Facts and Procedural History", frm="On April 21, 1921, Myers sued")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Court of Claims' judgment for the United States on constitutional grounds by a \textbf{6--3} vote. The case was argued on December 5, 1924, reargued on April 13--14, 1925, and decided on October 25, 1926 (\href{" + J + r"}{Justia}; \href{" + C + r"}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Taft delivered the opinion of the Court, joined by Justices Van Devanter, Sutherland, Butler, Sanford, and Stone.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Holmes (272 U.S.\ at 177), Justice McReynolds (272 U.S.\ at 178), and Justice Brandeis (272 U.S.\ at 240) each filed a separate dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Taft)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Holmes)}"),
    SEC("Concurring and Dissenting", frm=r"\textbf{Justice Holmes, dissenting}", to=r"\textbf{Justice McReynolds, dissenting}"),
    N(r"\subsection{Dissenting Opinion (Justice McReynolds)}"),
    SEC("Concurring and Dissenting", frm=r"\textbf{Justice McReynolds, dissenting}", to=r"\textbf{Justice Brandeis, dissenting}"),
    N(r"\subsection{Dissenting Opinion (Justice Brandeis)}"),
    SEC("Concurring and Dissenting", frm=r"\textbf{Justice Brandeis, dissenting}"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item", glue=" "),
    SEC("Doctrinal Significance", frm=r"\textbf{1. Retrenchment", to=r"\textbf{2. The Roberts Court"),
    N(r"\item", glue=" "),
    SEC("Doctrinal Significance", frm=r"\textbf{2. The Roberts Court", to=r"\textbf{3. Centennial Vindication"),
    N(r"\item", glue=" "),
    SEC("Doctrinal Significance", frm=r"\textbf{3. Centennial Vindication", to="Three nuances define"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Removal Restriction Invalid): For-Cause Protection for the Commissioners of a Federal AI Commission.}", glue=" "),
    S(r"Congress enacts the Artificial Intelligence Safety Act of 2026, establishing the five-member Federal AI Commission (FAIC), appointed by the President with Senate confirmation for staggered seven-year terms, with no more than three members from the same political party. The FAIC is empowered to promulgate binding safety rules for frontier AI models, investigate technology firms, adjudicate violations in-house, and seek billion-dollar civil penalties in federal court. The statute provides two removal clauses:", glue=" "),
    S(r"\textbf{Clause 1:} ``Commissioners may be removed by the President only for inefficiency, neglect of duty, or malfeasance in office.''", glue=" "),
    S(r"\textbf{Clause 2:} ``The FAIC's Chief Inspector---an inferior officer appointed by the FAIC Chair---may be removed by the Chair only upon a showing of good cause.''", glue=" "),
    S(r"The President fires two FAIC Commissioners solely for policy disagreements and orders the new Chair to fire the Chief Inspector at will. Both the Commissioners and the Chief Inspector sue."),
    S(r"Under \textit{Myers v.\ United States} as fully vindicated by \textit{Trump v.\ Slaughter} (2026), \textbf{Clause 1 is plainly unconstitutional}: the FAIC wields quintessential executive powers (binding rulemaking, investigations, in-house adjudication, and civil-penalty litigation), so its principal officers must be removable by the President at will, and \textit{Humphrey's Executor} is no longer good law. Nor can the FAIC claim the \textit{Trump v.\ Cook} historical carve-out applicable to the Federal Reserve."),
    N(r"\item \textbf{Same-Side (Removal Restriction Invalid): Congress Reserves Removal to Itself.} A statute creates a Comptroller of Federal Spending who certifies the amount of automatic budget cuts that the President must then order, and provides that the Comptroller may be removed only by joint resolution of Congress. Even on the narrow reading of \textit{Myers} adopted in \textit{Humphrey's Executor}, its core prohibition on congressional participation in removal survives: Congress may not draw to itself, or to either House, a power to remove an officer charged with executing the laws. \href{https://supreme.justia.com/cases/federal/us/478/714/}{\textit{Bowsher v.\ Synar}, 478 U.S.\ 714 (1986)}, invalidated a materially identical arrangement on exactly this ground, because Congress's control over removal would make the officer its subordinate."),
    N(r"\item \textbf{Opposite-Side (Restriction Likely Valid): An Inferior Officer Appointed and Protected by a Department Head.} Congress vests the appointment of a naval engineering officer in the Secretary of the Navy and provides that the officer may be dismissed in peacetime only by sentence of a court-martial; the Secretary serves at the President's pleasure. \textit{Myers} itself distinguished this situation: when Congress vests an inferior officer's appointment in a head of department under the Excepting Clause, it may limit that department head's power to remove, as \href{https://supreme.justia.com/cases/federal/us/116/483/}{\textit{United States v.\ Perkins}, 116 U.S.\ 483 (1886)}, held. Congress claims no share of removal for itself or the Senate, and the President still controls the Secretary, so the officer's tenure protection stands."),
    N(r"\item \textbf{Opposite-Side (Myers Not Triggered): Civil-Service Protection for a Non-Officer Employee.} A claims examiner in a federal agency, hired through competitive civil-service procedures, applies agency guidelines to routine benefit claims, exercises no significant authority under federal law, and by statute may be dismissed only for misconduct or poor performance after notice and a hearing before a personnel board. \textit{Myers} concerns the removal of \emph{officers} through whom the President executes the laws; an ordinary employee is not an officer under \href{https://supreme.justia.com/cases/federal/us/424/1/}{\textit{Buckley v.\ Valeo}, 424 U.S.\ 1 (1976)}, and \textit{Free Enterprise Fund} expressly declined to cast doubt on the civil-service system. The President's control runs through the agency's officers, who remain answerable to him, so the examiner's protection is valid."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Single-Layer Protection for the Commission's Chief Inspector.} Return to the Federal AI Commission and its Chief Inspector under Clause 2.", glue=" "),
    S(r"As to \textbf{Clause 2}, the Chief Inspector is an inferior officer whose appointment Congress vested in a Head of Department (the Commission/Chair) under Article II, \S~2's Excepting Clause. Under \textit{Myers}'s own discussion of \textit{United States v.\ Perkins}, 116 U.S.\ 483 (1886) (and \textit{Morrison v.\ Olson}), Congress may impose a \emph{single} layer of for-cause protection on an inferior officer appointed by a department head, provided the department head is removable at will by the President (avoiding the unconstitutional \emph{dual-layer} tenure problem of \textit{Free Enterprise Fund}). Once Clause 1 is severed under \textit{Slaughter}, the Chair is removable at will, meaning Clause 2 creates only a single layer of protection---though challengers could still argue under a maximalist reading of \textit{Myers} and \textit{Slaughter} that even single-layer limits on inferior officers exercising core enforcement power impair the President's Take Care duty."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"    \item \textbf{Originalist", to=r"\end{enumerate}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, duplicate \\url{} printouts (Justia and Cornell links kept in Judicial Votes); Trump v. Slaughter URL.",
  "Legacy section: introductory sentence; 'Three nuances' paragraph and its three bullets (Trump v. Cook carve-out, Gorsuch concurrence, Sotomayor dissent) - commentary on Slaughter rather than on Myers's holding. Kept: items 1 (Humphrey's Executor/Wiener/Morrison/Bowsher), 2 (Free Enterprise Fund/Seila Law), 3 (Trump v. Slaughter).",
  "'Opposite Side' Contrast (Myers/Slaughter vs. Cook/Morrison) - an exam tip, not a fact pattern; Examples 3 and 5 cover the inferior-officer side.",
 ],
 "notes": [
  "Neon's single FAIC hypothetical is split: Clause 1 analysis is Example 1 (Same-Side), Clause 2 analysis is Example 5 (Fence-Sitter); the fact pattern is moved once, in Example 1.",
  "Kept legacy item 3 and Examples 1 and 5 rely on Trump v. Slaughter (2026) and Trump v. Cook (2026) as described by Neon; these post-date the drafter's reliable knowledge and must be verified.",
 ],
}

emit(__file__, FILL)
