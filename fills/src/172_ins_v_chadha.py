"""Fill for 172_ins_v_chadha. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/462/919/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"\textit{Chadha} struck down the one-House legislative veto: once Congress delegates authority to the Executive, it may alter the legal rights and duties of persons outside the Legislative Branch only by bicameral passage and presentment to the President (7--2) (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The Immigration Judge reopened proceedings")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The Immigration Judge reopened proceedings")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the Ninth Circuit by a \textbf{7--2} vote. The case was argued on February 22, 1982, reargued on December 7, 1982, and decided on June 23, 1983 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/462/919}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Burger delivered the opinion of the Court, joined by Justices Brennan, Marshall, Blackmun, Stevens, and O'Connor.
    \item \textbf{Concurring Opinion:} Justice Powell concurred in the judgment (462 U.S. at 959).
    \item \textbf{Dissenting Opinions:} Justice White filed a dissenting opinion (462 U.S. at 967). Justice Rehnquist filed a dissenting opinion, joined by Justice White (462 U.S. at 1013).
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Burger)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Judgment (Justice Powell)}"), N("Justice Powell", glue=" "),
    SEC("Concurring and Dissenting", frm="Warned that the majority", to=r"  \item \textbf{Justice White", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice White)}"), N("Justice White", glue=" "),
    SEC("Concurring and Dissenting", frm="Delivered a landmark", to=r"  \item \textbf{Justice Rehnquist", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Rehnquist)}"), N("Justice Rehnquist", glue=" "),
    SEC("Concurring and Dissenting", frm="Focused solely", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Two-House and Agency Vetoes:}", glue=" "),
    S(r"Two weeks later, the Court summarily affirmed D.C. Circuit rulings invalidating a two-House veto over independent agency rulemaking in \textit{Process Gas Consumers Group v. Consumer Energy Council of America}, 463 U.S. 1216 (1983), confirming that \textit{Chadha} bars one-House, two-House, and committee vetoes alike."),
    N(r"\item \textbf{Extensions and Severability:}", glue=" "),
    S(r"The Court extended \textit{Chadha}'s anti-circumvention logic in \textit{Bowsher v. Synar}, 478 U.S. 714 (1986) (barring Congress from assigning executive budget cuts to a legislatively removable Comptroller General), \textit{Alaska Airlines, Inc. v. Brock}, 480 U.S. 678 (1987) (holding legislative vetoes presumptively severable), and \textit{Metropolitan Washington Airports Authority v. Citizens for Abatement of Aircraft Noise, Inc.}, 501 U.S. 252 (1991) (invalidating a board of review staffed by Members of Congress acting in ``individual capacities'')."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Veto Invalid): A Two-House Disapproval Resolution With an Inseverability Clause.}", glue=" "),
    S(r"Congress enacts the Artificial Intelligence Safety Act of 2026, authorizing the Secretary of Commerce to issue binding national safety standards for frontier AI models. Section 12 provides that any standard shall take effect 60 days after submission to Congress unless both the House and Senate pass a concurrent resolution of disapproval within that window. Section 13 adds that if \S~12 is held invalid, the Secretary's rulemaking authority under the Act shall automatically terminate. The Secretary issues a binding rule; both Houses pass a concurrent resolution disapproving it without presenting it to the President. An AI developer sues to enforce the disapproval (or a safety group sues to enforce the rule).", glue=" "),
    S(r"Under \textit{Chadha} and \textit{Process Gas}, even a \emph{two-House} concurrent resolution violates Presentment (Art.~I, \S~7, cl.~3) because it alters legal rights and duties outside Congress without presidential presentment. However, unlike \textit{Chadha} and \textit{Alaska Airlines}, \S~13 contains an express \emph{inseverability} (fallback) clause, meaning a court must honor Congress's explicit text and invalidate the Secretary's underlying rulemaking authority as well."),
    N(r"\item \textbf{Same-Side (Veto Invalid): A Committee Approval Requirement for Federal Land Sales.} A statute authorizes the Secretary of the Interior to sell surplus federal land, but provides that no sale may close unless the House and Senate committees with jurisdiction over public lands first approve it by committee resolution. The committees refuse to approve a sale the Secretary has negotiated, and the buyer sues. Under \textit{Chadha}, the committees' refusal has the purpose and effect of altering the legal rights of the Secretary and the buyer, persons outside the Legislative Branch, so it is legislative action that must pass both Houses and be presented to the President. A committee veto is even further removed from Article I, \S~7 than the one-House veto in \textit{Chadha}. Under \textit{Alaska Airlines}, the court would presume the approval clause severable and let the sale proceed."),
    N(r"\item \textbf{Opposite-Side (Valid): A Report-and-Wait Provision With Disapproval by Joint Resolution.} A statute requires an agency to submit each new rule to Congress and provides that the rule may not take effect for 60 days; during that time Congress may block the rule only by passing a joint resolution of disapproval through both Houses and presenting it to the President. Nothing in this scheme lets Congress change anyone's legal rights without bicameralism and presentment. The waiting period merely gives Congress time to legislate, and any disapproval becomes law only through the Article I, \S~7 process. This is the kind of report-and-wait mechanism the Court treated as ``fully operative'' when it severed the veto from \S~244, and it is the model Congress later followed in the Congressional Review Act."),
    N(r"\item \textbf{Opposite-Side (Valid): The Senate Rejects a Nominee by a One-House Vote.} The President nominates a candidate to head a federal agency. The Senate votes to reject the nomination, and the nominee sues, arguing that under \textit{Chadha} a single House cannot take binding action that alters the legal rights of persons outside Congress. The claim fails. \textit{Chadha} recognized that the Framers expressly authorized certain unicameral actions with binding effect, including the Senate's power to give or withhold consent to appointments under Article II, \S~2, cl.~2. Those textual exceptions are precisely what made the Court conclude that no others may be implied; they do not cast doubt on the exceptions themselves. The Senate's vote is a constitutionally prescribed act, not an exercise of lawmaking power that bypasses presentment."),
    N(r"\item \textbf{Fence-Sitter (Unsettled): Requiring Affirmative Congressional Approval Before Major Rules Take Effect.} A statute provides that no ``major rule'' issued by any agency may take effect unless, within 70 legislative days, both Houses pass and the President signs a joint resolution approving it; if either House fails to act, the rule never takes effect. Defenders argue that the scheme complies with \textit{Chadha}: Congress has simply delegated authority to propose rules, and every rule that becomes binding passes through bicameralism and presentment. Critics answer that one House's inaction now has the same effect as the one-House veto struck down in \textit{Chadha}, because a single chamber can defeat an exercise of delegated power that the other House and the President support. Because the Court has not decided whether Congress may condition a delegation on later approval in this way, the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{Exam Hypothetical:}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket numbers, argument dates, Chapter/Topic line, duplicate \\url{} printouts (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory sentence ('foundational pillar'); the four-item 'Through 2026' enumerate (CRA, REINS Act, committee vetoes in 2026 appropriations, Consumers' Research/emergency powers) and the CRS June 2026 report and Harvard Law Review Blog links -- legislative practice and commentary, not decisions applying Chadha's holding. Kept: Process Gas; Bowsher / Alaska Airlines / MWAA sentence.",
  "Exam Hypothetical: 'Opposite Side' Contrast (Clinton v. City of New York, Mistretta, Consumers' Research) -- an exam tip, not a fact pattern.",
 ],
 "notes": ["Example 3 relies on the brief's own statement that \\S~244 remained a 'fully operative' report-and-wait mechanism; Example 5 tracks the REINS Act debate the original legacy section describes, without naming any bill."],
}

emit(__file__, FILL)
