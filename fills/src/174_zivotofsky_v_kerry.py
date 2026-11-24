"""Fill for 174_zivotofsky_v_kerry. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/576/1/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"A five-Justice majority held that the President alone holds the power to recognize foreign sovereigns and their territorial bounds. The Court invalidated \S~214(d)'s requirement that the Secretary of State list Israel on the passports of Jerusalem-born citizens upon request, with Justice Thomas supplying a sixth vote on different grounds---a presidential victory in \textit{Youngstown}'s lowest-ebb category (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Zivotofsky's parents sued the Secretary")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Zivotofsky's parents sued the Secretary")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the D.C. Circuit with five Justices joining the Court's recognition-power rationale and Justice Thomas separately concurring in the judgment as to passports (6--3 on passports) but dissenting as to consular reports of birth abroad. The case was argued on November 3, 2014, and decided on June 8, 2015 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Kennedy delivered the opinion of the Court, joined by Justices Ginsburg, Breyer, Sotomayor, and Kagan.
    \item \textbf{Concurring Opinions:} Justice Breyer filed a concurring opinion. Justice Thomas filed an opinion concurring in the judgment in part and dissenting in part.
    \item \textbf{Dissenting Opinions:} Chief Justice Roberts filed a dissenting opinion, joined by Justice Alito. Justice Scalia filed a dissenting opinion, joined by Chief Justice Roberts and Justice Alito.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kennedy)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Breyer)}"), N("Justice Breyer", glue=" "),
    SEC("Concurring and Dissenting", frm="Maintained his dissent", to=r"  \item \textbf{Justice Thomas", lc=True),
    N(r"\subsection{Opinion Concurring in the Judgment in Part and Dissenting in Part (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC("Concurring and Dissenting", frm="Rejected the majority's Reception", to=r"  \item \textbf{Chief Justice Roberts", lc=True),
    N(r"\subsection{Dissenting Opinion (Chief Justice Roberts)}"), N("Chief Justice Roberts", glue=" "),
    SEC("Concurring and Dissenting", frm="Emphasized that for the first 225", to=r"  \item \textbf{Justice Scalia", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Scalia)}"), N("Justice Scalia", glue=" "),
    SEC("Concurring and Dissenting", frm=r"Grounded \S~214(d)", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"  \item \textbf{Expansion of", to=r"  \item \textbf{Reaffirmation of"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Statute Invalid): Compelled Official Maps Contradicting Recognition.} The President recognizes Country A's sovereignty over a border province that Country B also claims. Congress directs the Secretary of State to publish official State Department maps, and the Department's annual country reports to foreign governments, depicting the province as part of Country B. Like \S~214(d), the statute does not itself recognize anyone, but it commands the Executive to make formal, foreign-facing statements that contradict the President's recognition determination. Under the majority's holding that the exclusive recognition power includes the President's control over official Executive Branch statements about a state's territorial bounds, the mandate is unconstitutional (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Statute Invalid): Ordering the Executive to Receive a Breakaway Government's Envoy.} A province of a recognized state declares independence. The President declines to recognize it. Congress enacts a statute directing the Secretary of State to accredit the breakaway government's representative as an ambassador and to exchange formal diplomatic notes acknowledging the new state. Receiving an ambassador was, for the founding-era jurists the Court relied on, the paradigm act of recognition, and the statute would force the Executive to perform that act against the President's judgment. Because the President's recognition power is ``conclusive and preclusive,'' this is \textit{Youngstown} Category Three in which the President prevails even more clearly than in \textit{Zivotofsky} itself."),
    N(r"\item \textbf{Opposite-Side (Appropriations Power Distinguished): Defunding an Embassy.}", glue=" "),
    S(r"Suppose the President formally recognizes the government of Country X as the sole legitimate sovereign over Disputed Island Y, refusing to recognize a breakaway republic on Island Y.", glue=" "),
    N(r"Congress responds with a statute that, among other things,", glue=" "),
    S(r"prohibits the expenditure of any federal funds to operate a U.S. Embassy in Country X's capital unless the President withdraws recognition of Country X's claim to Island Y.", glue=" "),
    S(r"Even under \textit{Zivotofsky}'s majority opinion, Justice Kennedy explicitly acknowledged that Congress retains its Appropriations Clause power (Art. I, \S~9, cl. 7) and that ``[t]he President, furthermore, could not build an American Embassy abroad without congressional appropriation of the necessary funds.'' Thus, refusing to fund an embassy is squarely within Congress's power of the purse. However, the President's counterargument would invoke the unconstitutional-conditions principle in separation of powers: Congress may not use an explicit condition tied directly to forcing a change in a formal recognition determination to coerce the President into surrendering an exclusive Article II prerogative."),
    N(r"\item \textbf{Opposite-Side (Congress Prevails): Sanctions on a Recognized Government.} Over the President's objection, Congress bars all imports from, and arms exports to, a foreign government that the President recognizes and wishes to court. The statute says nothing about sovereignty or territorial bounds and requires no Executive statement inconsistent with recognition; it regulates foreign commerce, an enumerated Article I power. The majority expressly confined its holding to recognition determinations, rejected the \textit{Curtiss-Wright} ``sole organ'' dicta, and stressed that ``[i]t is not for the President alone to determine the whole content of the Nation's foreign policy.'' The President must therefore enforce the sanctions, even though they cut against his diplomatic strategy."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): Customs Labels and Tariffs for an Unrecognized Territory.} Return to the Island Y hypothetical. The same statute also", glue=" "),
    S(r"directs U.S. Customs and Border Protection to classify all goods imported from Island Y as ``Products of the Independent Republic of Island Y'' on official customs entry invoices and to apply a 0\% preferential tariff rate rather than Country X's 25\% tariff rate", glue=""),
    N(r".", glue=" "),
    S(r"Under \textit{Zivotofsky}'s majority opinion, the President will argue that compelling Customs officials to print ``Independent Republic of Island Y'' on official government documents forces the Executive to contradict its formal recognition determination in an official communication affecting foreign sovereigns.", glue=" "),
    N(r"But", glue=" "),
    S(r"Congress (echoing Justice Scalia's dissent and Kennedy's own limits on \textit{Curtiss-Wright}) has a much stronger counterargument here than in \textit{Zivotofsky}: regulating tariffs and country-of-origin rules lies at the core of Congress's express Foreign Commerce Clause and Taxing Clause powers (Art. I, \S~8, cls. 1, 3)---a power reinforced by \textit{Learning Resources, Inc. v. Trump} (2026)---and Congress has historically enacted trade and statutory rules treating unrecognized entities (such as Taiwan under the Taiwan Relations Act) as distinct for commercial purposes without altering formal diplomatic recognition. A court might sever the 0\% tariff rate (valid under Article I) from any mandatory sovereignty label on official diplomatic-facing documents, or uphold Section A entirely as a commercial classification rather than an act of recognition.", glue=" "),
    N(r"The outcome turns on how far the President's control over ``official executive statements'' extends into documents that serve Congress's commerce powers---a line the majority did not draw."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{Exam Hypothetical")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: full case name, docket number, Chapter/Topic line, duplicate \\url{} printout (Justia link kept in Judicial Votes).",
  "Legacy section: two introductory paragraphs (framing; 2017 recognition and 2020 passport epilogue - history, not a later decision); Learning Resources v. Trump (2026) item (IEEPA tariff case - tangential to Zivotofsky's holding). Kept: Trump v. United States item.",
  "Exam Hypothetical: heading and 'Opposite Side Contrast' labels; the hypothetical's two sections are reused in Examples 3 and 5.",
 ],
 "notes": ["Example 4 quotes the Key Quotations passage 'It is not for the President alone...' (576 U.S. at 21) as it appears in the brief, with the first letter bracketed.",
           "Example 5 reuses Neon's text that mentions Learning Resources v. Trump (2026); that case is not independently verified here."],
}

emit(__file__, FILL)
