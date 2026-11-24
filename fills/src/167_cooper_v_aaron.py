"""Fill for 167_cooper_v_aaron (pilot). See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/358/1/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Facing Arkansas's open defiance of \textit{Brown}, all nine Justices signed an opinion holding that disorder provoked by state officials cannot justify suspending a desegregation plan, and declaring that the Supreme Court's interpretation of the Fourteenth Amendment is ``the supreme law of the land'' binding every state official (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="On February 20, 1958")],
  "Procedural History": [SEC("Facts and Procedural History", frm="On February 20, 1958")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{affirmed} the Eighth Circuit, 9--0, announcing its judgment in a per curiam order on September 12, 1958, and filing its full opinion on September 29, 1958 (\href{" + J + r"}{Justia}):"),
    N(r"\begin{itemize}"), N(r"\item \textbf{Opinion of the Court:}", glue=" "),
    S(r"Jointly signed by all nine Justices --- Chief Justice Earl Warren, and Justices Hugo L. Black, Felix Frankfurter, William O. Douglas, Harold H. Burton, Tom C. Clark, John M. Harlan II, William J. Brennan, Jr., and Charles E. Whittaker (the only time in Supreme Court history that every Justice personally signed the opinion of the Court)."),
    N(r"""\item \textbf{Concurring Opinion:} Justice Frankfurter filed a concurring opinion on October 6, 1958 (358 U.S. at 20--26).
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Joint Opinion of the Court}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Frankfurter)}"),
    SEC("Concurring and Dissenting", frm="Writing separately", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Judicial Supremacy vs."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Official Bound by the Court's Interpretation): A Non-Party Governor Refuses to Follow a Fourteenth Amendment Precedent.}", glue=" "),
    S(r"After the Supreme Court holds in \textit{State A v. Doe} that a state ban on a particular medical procedure violates the Fourteenth Amendment, the Governor of State B (not a party to \textit{Doe}) signs an executive order directing state prosecutors to continue enforcing State B's identical statute, declaring: ``My oath is to the Constitution, not to five Justices' mistaken reading of it; I will obey a federal court injunction directed at me, but until then I am not bound by \textit{Doe}.''", glue=" "),
    S(r"Under \textit{Cooper v. Aaron}'s strong judicial-supremacy framework, the Governor's refusal to treat the Court's Fourteenth Amendment holding as binding law violates Article VI and the Oath Clause; moreover, in any federal suit against State B's officials, lower federal courts are bound by vertical \textit{stare decisis} to enjoin enforcement immediately (and state officials face potential fee-shifting under 42 U.S.C.\ \S~1988 or loss of qualified immunity because the right is clearly established). Under a \textbf{departmentalist} view (invoking Lincoln's response to \textit{Dred Scott}), the Governor distinguishes between defying a direct court judgment (unlawful) and declining to treat a precedent involving other parties as automatically settling his independent constitutional judgment while seeking a test case to ask the Court to reconsider \textit{Doe}."),
    N(r"\item \textbf{Same-Side (No Excuse for Official Resistance): A County Clerk Stops Issuing Marriage Licenses.} After the Supreme Court holds that the Fourteenth Amendment requires States to license same-sex marriages, an elected county clerk stops issuing marriage licenses altogether, citing her personal objections and the fact that the decision arose from litigation against other States' officials. A federal court orders her to resume issuing licenses, and she refuses. Under \textit{Cooper}, the clerk acts for the State, is bound by the Court's interpretation through her Article VI oath, and cannot confine the ruling to the parties who litigated it; her disagreement, like the Arkansas officials' resistance, is no legal excuse, and continued refusal is punishable as contempt."),
    N(r"\item \textbf{Opposite-Side (Independent Judgment Permitted): A President Vetoes a Bill the Court Would Uphold.} Congress passes a bill chartering a national development bank. Supreme Court precedent establishes that Congress may charter such a bank, but the President vetoes the bill on the ground that, in his own judgment, it exceeds Congress's enumerated powers. \textit{Cooper} does not reach this situation: the veto defies no judgment and denies no right the Court has declared, and Andrew Jackson's 1832 veto of the Second Bank's recharter rested on exactly this reasoning. Even on a strong reading of \textit{Cooper}, the Court's interpretations bind officials who would act against declared constitutional rights; they do not oblige political officials to support every measure the Court has found permissible."),
    N(r"\item \textbf{Opposite-Side (No Supreme Court Interpretation to Obey): State Officials Decline to Follow Another State's District Court Ruling.} A federal district court in State C holds State C's voter-identification law unconstitutional and enjoins its enforcement. Officials in State D, which has a similar law, keep enforcing it. \textit{Cooper}'s Article VI reasoning attaches to the Supreme Court's exposition of the Constitution, not to every lower-court opinion: the State C judgment binds only the parties to that case, and its reasoning is at most persuasive authority in State D. State D's officials are not ``war[ring] against the Constitution'' by continuing to enforce their law until a court with authority over them rules."),
    N(r"\item \textbf{Fence-Sitter (Defiance or Legitimate Test Case?): A State Enacts a Law Designed to Invite Overruling.} A state legislature, persuaded that a Supreme Court precedent was wrongly decided, enacts a statute that conflicts with the precedent's core holding and openly announces that its purpose is to give the Court a vehicle to reconsider it. Read broadly, \textit{Cooper} condemns any legislator who would ``war against the Constitution'' as the Court has interpreted it, and the statute resembles the ``evasive schemes'' the Court denounced. Read alongside Justice Frankfurter's concurrence, which distinguished orderly efforts to change the law from defiance of it, the statute is a lawful request for reconsideration---the posture of the Mississippi law that led the Court to overrule \textit{Roe v. Wade} in \href{https://supreme.justia.com/cases/federal/us/597/19-1392/}{\textit{Dobbs v. Jackson Women's Health Organization}, 597 U.S. 215 (2022)}. Where testing a precedent ends and nullifying it begins remains unsettled."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Textual Slippage", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: argument dates, term, Chapter/Topic line, duplicate \\url{} printout.",
  "Legacy section: introductory paragraph; 'Judicial Supremacy vs. Departmentalism Through 2026' item (Trump v. CASA, Trump v. Barbara, 2024-25 law reviews) - tangential to Cooper. Kept: Nixon / City of Boerne item.",
  "Exam Hypothetical: 'Opposite Side Contrast' on departmentalism - repeats Critique item 1; Example 3 now covers the departmentalist side.",
 ],
}

emit(__file__, FILL)
