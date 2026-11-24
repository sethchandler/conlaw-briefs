"""Fill for 225_puerto_rico_v_branstad. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/483/219/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"When Iowa's Governor refused to extradite a man charged with murder in Puerto Rico, the Court unanimously overruled \textit{Kentucky v.\ Dennison} and held that federal courts may order a governor by mandamus to perform the mandatory duty to surrender a fugitive, and that Puerto Rico may enforce that duty under the federal Extradition Act (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="After the Supreme Court denied Puerto Rico leave")],
  "Procedural History": [SEC("Facts and Procedural History", frm="After the Supreme Court denied Puerto Rico leave")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the Eighth Circuit by a \textbf{9--0} vote on the judgment (6--3 as to Part II-B's constitutional holding). The case was argued on March 30, 1987, and decided on June 23, 1987 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Marshall delivered the opinion of the Court, joined in full by Chief Justice Rehnquist and Justices Brennan, White, Blackmun, and Stevens; joined in Parts I, II-A, II-C, and III by Justices Powell and O'Connor; and joined in part by Justice Scalia.
    \item \textbf{Concurring Opinions:} Justice O'Connor, joined by Justice Powell, filed an opinion concurring in part and concurring in the judgment. Justice Scalia filed an opinion concurring in part and concurring in the judgment.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Marshall)}"), SEC("Reasoning"),
    N(r"\subsection{Opinion Concurring in Part and in the Judgment (Justice O'Connor)}"), N("Justice O'Connor", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined Parts I, II-A, II-C, and III, but declined", to=r"  \item \textbf{Justice Scalia", lc=True),
    N(r"\subsection{Opinion Concurring in Part and in the Judgment (Justice Scalia)}"), N("Justice Scalia", glue=" "),
    SEC("Concurring and Dissenting", frm="Concurred in the result and solely", to=r"  \item \textbf{Dissents:}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{No Asylum-State Defenses:}", glue=" "),
    S(r"Eleven years later, in \emph{New Mexico ex rel. Ortiz v. Reed}, 524 U.S. 151, 155 (1998) (cited in \href{https://www.law.cornell.edu/constitution-conan/article-4/section-2/clause-2/overview-of-extradition-interstate-rendition-clause}{Cornell LII Constitution Annotated}), the Court unanimously applied \emph{Branstad} to forbid an asylum state from refusing extradition based on a fugitive's claim of duress or fear of unfair treatment in the demanding state."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Extradition Compelled): A Shield Law Cannot Protect an Actual Fugitive.}", glue=" "),
    S(r"State X indicts Dr. A for performing a procedure illegal in State X while Dr. A was physically operating a clinic in State X. Dr. A then moves to State Y, whose Governor refuses State X's facially valid extradition demand because State Y's legislature passed a statute prohibiting extradition for that offense.", glue=" "),
    S(r"State X will prevail in federal court via mandamus under \emph{Branstad} and \emph{Doran}. Dr. A was physically present in State X and fled; State Y's shield law is preempted by Article IV, \S~2, cl. 2 and 18 U.S.C. \S~3182, and the Tenth Amendment offers no defense."),
    N(r"\item \textbf{Same-Side (Extradition Compelled): Objection to the Demanding State's Punishment.} A man charged with capital murder in State X is arrested in State Y, which has abolished the death penalty. State X's extradition papers are in order, but State Y's Governor refuses to surrender him unless State X agrees not to seek a death sentence. Under \emph{Branstad}, the commands of the Extradition Clause are mandatory and leave the asylum State's executive no discretion, and \emph{Michigan v.\ Doran} limits the asylum State's review to whether the papers are in order and the person is the charged fugitive. The Governor's moral objection to the possible punishment, like Iowa's doubts about a fair trial in Puerto Rico, is no defense; State X may obtain a writ of mandamus, and the fugitive must raise his objections in State X's courts."),
    N(r"\item \textbf{Opposite-Side (No Mandatory Duty): A Non-Fugitive Telehealth Prescriber and a Commandeering Statute.}", glue=" "),
    S(r"Now suppose Dr. B has never set foot in State X; from an office in State Y, Dr. B prescribes medication via telehealth to a patient in State X. State X indicts Dr. B and demands extradition; State Y's Governor refuses under State Y's shield law. Congress then enacts a new federal statute under the Commerce Clause requiring every state governor to arrest and extradite any non-fugitive accused of a cross-border telehealth crime.", glue=" "),
    S(r"On the existing Extradition Clause and \S~3182, State Y wins because Dr. B never ``fled from Justice'' in State X, so \emph{Branstad}'s mandatory duty is never triggered. Moreover, the hypothetical Commerce Clause statute would likely be invalidated under \href{https://supreme.justia.com/cases/federal/us/521/898/}{\emph{Printz}} and \href{https://supreme.justia.com/cases/federal/us/584/16-476/}{\emph{Murphy}}: unlike \emph{Branstad}, where the Constitution itself directly imposed the duty on state governors, Congress cannot use Article I to commandeer state executives into enforcing a non-constitutional extradition mandate."),
    N(r"\item \textbf{Opposite-Side (No Mandatory Duty): A Demand From a Foreign Country.} A Canadian province charges a man with fraud and asks the Governor of a neighboring State, where he now lives, to surrender him. The Governor declines, and the province asks a federal court for mandamus under \emph{Branstad}. The request fails. \emph{Branstad} enforces a duty created by Article IV and the Extradition Act, and those provisions govern demands by States and, under \S~3182, by Territories; they say nothing about foreign nations. Extradition to another country runs through treaties and the national government, not through a governor's duty under Article IV, so no ministerial obligation exists for a federal court to compel."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Puerto Rico's Demand After \emph{Printz}.} Puerto Rico again demands the extradition of a fugitive who fled to a State, and the State's Governor refuses. Relying on \emph{Branstad}'s statutory holding, Puerto Rico seeks mandamus under \S~3182. The Governor answers that Article IV's Extradition Clause speaks only of ``States,'' so the duty to surrender fugitives to a Territory rests on an Act of Congress alone, and \emph{Printz} forbids Congress to commandeer state executive officers. \emph{Branstad} answers the remedial question in Puerto Rico's favor, but Justice Scalia expressly noted that no party had questioned Congress's power to require extradition from a State to a Territory, and the Court has not addressed it since the modern anti-commandeering cases, so the result is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm="First, notice the analytical mismatch", to=r"\textbf{Exam Hypothetical")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Briefing Book Placement, provisions list, duplicate links.",
  "Legacy section: opening sentences of first paragraph; second paragraph (anti-commandeering reconciliation with New York, Printz, Murphy - commentary; Printz and Murphy still appear in Examples 3 and 5); third paragraph (2025-2026 shield-law conflicts, Louisiana/New York Carpenter dispute, August 2026 Texas/Minnesota dispute, Vladeck commentary). Kept: Ortiz item.",
  "Exam Hypothetical: scenario labels and 'Analysis:' labels (texts reused in Examples 1 and 3).",
 ],
 "notes": [],
}

emit(__file__, FILL)
