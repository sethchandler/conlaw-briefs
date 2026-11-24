"""Fill for 231_united_states_v_belmont. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/301/324/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"The Court unanimously reversed and let the United States collect a New York bank deposit assigned to it by the Soviet Union in the Litvinov Assignment; Justice Sutherland's majority held that a sole executive agreement made incident to recognition needs no Senate consent and overrides contrary state law and policy (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="After August Belmont's death")],
  "Procedural History": [SEC("Facts and Procedural History", frm="After August Belmont's death")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the Second Circuit, \textbf{9--0} in the judgment. The case was argued on March 4, 1937, and decided on May 3, 1937 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/301/324}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Sutherland delivered the opinion of the Court, joined by Chief Justice Hughes and Justices Van Devanter, McReynolds, Butler, and Roberts.
    \item \textbf{Concurring Opinion:} Justice Stone filed an opinion concurring in the judgment, joined by Justices Brandeis and Cardozo.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Sutherland)}"), SEC("Reasoning"),
    N(r"\subsection{Opinion Concurring in the Judgment (Justice Stone)}"),
    SEC("Concurring and Dissenting", frm="Stone agreed that the United States"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Expansion in \textit{Pink}:}", glue=" "),
    S(r"Five years later, in \href{https://supreme.justia.com/cases/federal/us/315/203/}{\textit{United States v. Pink}, 315 U.S. 203 (1942)}, the Court solidified and expanded \textit{Belmont} over Chief Justice Stone's dissent, holding that the Litvinov Assignment overrode New York's distribution of a Russian insurer's assets even against competing foreign creditors."),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Claims Settlement", to=r"  \item \textbf{Modern Legacy"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (State Law Preempted): Claims Settlement Incident to Recognition.}", glue=" "),
    S(r"Following a coup and peace settlement in the Republic of Veridia, the President formally recognizes Veridia's new government and executes a sole executive agreement extinguishing all pending U.S. civil claims against Veridia's state-owned airline in exchange for a \$400 million lump-sum compensation fund administered by a federal commission. A state statute in New York purports to preserve New York residents' state-court tort suits against the airline regardless of federal settlement.", glue=" "),
    S(r"The New York statute is preempted under \textit{Belmont}, \textit{Pink}, \textit{Dames \& Moore}, and \textit{Garamendi}. Because the claims-settlement agreement directly accompanies diplomatic recognition and reflects a longstanding, congressionally acquiesced executive practice, it requires no Senate ratification and overrides conflicting state law."),
    N(r"\item \textbf{Same-Side (State Policy Cannot Block Collection): An Assigned Foreign Bank Claim.} On recognizing a new government in Country Z, the President accepts, by an exchange of diplomatic notes, that government's assignment to the United States of claims owed to Z's nationalized central bank by American debtors, so that the United States can fund settlements of Americans' claims against Z. A company in State Q owes the central bank on a loan. When the United States sues to collect, State Q's courts refuse, citing the State's policy against giving effect to foreign confiscations. Under \textit{Belmont}, the assignment is a valid sole executive agreement incident to recognition, and ``the external powers of the United States are to be exercised without regard to state laws or policies''; the United States may collect (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Agreement Not Preemptive): Directing State Criminal Courts.}", glue=" "),
    S(r"By contrast, suppose the President signs an unratified bilateral executive agreement with a foreign nation promising that U.S. state criminal courts will automatically vacate state felony convictions whenever local police fail to notify that nation's consulate, and issues a Presidential Memorandum directing state judges to ignore state procedural-default rules. Congress has enacted no implementing statute.", glue=" "),
    S(r"Unconstitutional and non-preemptive under \textit{Medell\'in v. Texas} and the limiting principles foreshadowed by Justice Stone's \textit{Belmont} concurrence. Unlike \textit{Belmont}'s narrow diplomatic claims settlement incident to recognition, dictating state criminal procedure lacks both exclusive Article II authority and historic congressional acquiescence; the President cannot unilaterally transform an international undertaking into supreme domestic law binding state courts without Congress or a self-executing Senate-ratified treaty."),
    N(r"\item \textbf{Opposite-Side (Statute Prevails): An Executive Agreement Contrary to a Federal Statute.} The President concludes a sole executive agreement with a trading partner promising to admit its steel free of the import duties that a federal statute requires, and directs customs officials to stop collecting the duties. An importer that competes with the foreign mills sues to compel collection. \textit{Belmont} held only that a valid sole executive agreement overrides \textit{state} law and policy; it did not suggest that the President, acting alone, may displace an Act of Congress. Because the agreement conflicts with a valid federal statute enacted under Congress's power over foreign commerce, the statute controls and the duties must be collected."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): Ending State Tort Suits Without a Compensation Fund.} The President, acting without Senate consent or new legislation, signs an agreement with a long-recognized foreign government that terminates all pending state-court suits by Americans against that government's state-owned chemical company over a factory disaster, in exchange for trade concessions but no compensation fund. The executive can invoke \textit{Belmont}, \textit{Pink}, and \textit{Dames \& Moore}: settling nationals' claims is a long-standing presidential practice, and state law must yield. But the agreement is not incident to recognition, provides no substitute remedy, and rests on whatever congressional acquiescence can be shown, which \textit{Medell\'in} said confines these precedents to a ``narrow set of circumstances.'' Whether it preempts the suits is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Bypassing", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: full caption, Chapter line, provisions line, duplicate source links (Justia and Cornell links kept in Judicial Votes).",
  "Concurring and Dissenting: lead-in sentence and the bold label before Justice Stone's concurrence (restated in Judicial Votes and the subsection heading).",
  "Legacy section: opening framing sentence; 'cabin-checked' lead-in; 'Modern Legacy Through 2026' item (Case-Zablocki, 2026 WHO-withdrawal commentary - not a decision applying Belmont). Kept: Pink, Dames & Moore, Garamendi, Medellin / Zivotofsky items.",
  "Exam Hypotheticals: headings and 'Analysis' labels.",
 ],
 "notes": ["Four Subsequent Developments items kept (Pink, Dames & Moore, Garamendi, Medellin) because each applied or narrowed Belmont's holding directly."],
}

emit(__file__, FILL)
