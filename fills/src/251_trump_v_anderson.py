"""Fill for 251_trump_v_anderson. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/601/23-719/"
FS = "Facts and Procedural History"
SO = "Concurring and Dissenting"
PS = "Pedagogical Critiques"
EX = r"Suppose in 2028 a State Secretary of State excludes a former U.S.\ Senator from the U.S.\ Senate primary ballot after a state administrative hearing finds the candidate ``gave aid or comfort'' to a domestic rebellion, while simultaneously barring a former county sheriff from running for Governor on the exact same factual record."
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Colorado's Supreme Court removed Donald Trump from the 2024 presidential primary ballot under Section~3 of the Fourteenth Amendment; the Court unanimously reversed, holding that States may disqualify state officers and candidates but have no power to enforce Section~3 against federal offices, which a five-Justice majority assigned to Congress (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="Following a five-day trial")],
  "Procedural History": [SEC(FS, frm="Following a five-day trial")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{reversed} the Colorado Supreme Court, \textbf{9--0} in the judgment, dividing \textbf{5--4} on whether congressional legislation under Section~5 is the exclusive federal mechanism for enforcing Section~3. The case was argued on February 8, 2024, and decided on March 4, 2024 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/23-719}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Per Curiam Opinion:} Joined in full by Chief Justice Roberts and Justices Thomas, Alito, Gorsuch, and Kavanaugh.
    \item \textbf{Concurring Opinions:} Justice Barrett filed an opinion concurring in part (joining Parts I and II--B) and concurring in the judgment. Justices Sotomayor, Kagan, and Jackson filed a joint opinion concurring in the judgment.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Per Curiam Opinion}"), SEC("Reasoning"),
    N(r"\subsection{Opinion Concurring in Part and in the Judgment (Justice Barrett)}"), N("Justice Barrett", glue=" "),
    SEC(SO, frm="Joined Parts I and II--B", to=r"\textbf{Justices Sotomayor", lc=True),
    N(r"\subsection{Joint Opinion Concurring in the Judgment (Justices Sotomayor, Kagan, and Jackson)}"), N("Justices Sotomayor, Kagan, and Jackson", glue=" "),
    SEC(SO, frm="Agreed unanimously on federalism", lc=True),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (State Lacks Power): Excluding a U.S.\ Senate Candidate.}", glue=" "),
    S(EX, glue=" "),
    N(r"Consider first the Senate candidate.", glue=" "),
    S(r"Under \emph{Trump v. Anderson}, the exclusion from the \emph{U.S.\ Senate} ballot is unconstitutional because States lack authority to enforce Section~3 against federal candidates; enforcement belongs exclusively to Congress (via Section~5 legislation or the Senate's Article~I, \S 5 judging power)."),
    N(r"\item \textbf{Same-Side (State Lacks Power): A Voter Challenge to a Sitting Representative.} Voters in a congressional district petition a state court under the state election code to remove their incumbent U.S.\ Representative from the general-election ballot, presenting evidence that he helped plan an armed attack on a federal building. The state court finds that he engaged in insurrection and orders him off the ballot. Under \textit{Anderson}, the finding does not matter: a seat in the House is a federal office, and States have no power to enforce Section~3 with respect to federal offices. Any disqualification must come through legislation enacted by Congress or the House's own power to judge its Members' qualifications, so the order must be reversed."),
    N(r"\item \textbf{Opposite-Side (State Power Preserved): Barring a Former Sheriff From the Governor's Race.} In the same hypothetical, the State also acts against the former sheriff.", glue=" "),
    S(r"By contrast, barring the former sheriff from the \emph{gubernatorial} ballot is constitutionally permissible under the Court's explicit carve-out preserving state power over state offices---subject, of course, to Fourteenth Amendment due-process constraints."),
    N(r"\item \textbf{Opposite-Side (Likely Permissible): Excluding an Underage Presidential Candidate.} A 29-year-old files to appear on a State's presidential primary ballot, and the Secretary of State refuses because Article~II requires the President to be at least 35. The candidate invokes \textit{Anderson}'s holding that States may not enforce Section~3 against presidential candidates. \textit{Anderson} addressed only Section~3, a disability that requires fact-intensive findings and that Congress may remove by a two-thirds vote; an age requirement is objective, categorical, and cannot be waived by Congress, so state enforcement creates no risk of a conflicting state-by-state patchwork. Lower courts have allowed States to keep constitutionally ineligible candidates off the ballot, as in \textit{Hassan v.\ Colorado} (a naturalized citizen), so the exclusion is likely valid."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Enforcing the Two-Term Limit.} A former President who has already been elected twice files to run again, and a State keeps him off its presidential ballot under the Twenty-Second Amendment. Like the age requirement, the two-term limit is objective and turns on public records rather than disputed findings about conduct, and Congress has no power to waive it, which suggests that \textit{Anderson}'s concerns do not apply. On the other hand, \textit{Anderson} stressed the uniquely important national interest in presidential elections and the chaos of state-by-state ballot decisions, reasoning that could be read to bar any single State from deciding a presidential candidate's eligibility. Because the Court has never addressed the question, the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC(PS, to=r"\textbf{``Opposite Side''", strip=r"\textbf{Key Critiques:} ")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, court line, Briefing Book placement, slip-opinion link.",
  "Entire Legacy section (state-office enforcement example, Maine/Illinois aftermath, Trump v. United States and 2024 election backdrop, absence of new Section 5 legislation, Baude/Paulsen and Somin scholarship, pending certiorari petition): no later decision overruling, narrowing, extending, or applying the holding, so no Subsequent Developments subsection.",
  "'Opposite Side' Contrast (Chiafalo v. Washington and Hassan v. Colorado) - an exam tip comparing real cases; its themes inform new Examples 4 and 5.",
  "Exam Hypothetical was split into its Senate-candidate and sheriff halves (Examples 1 and 3); its fact pattern is moved verbatim once, in Example 1.",
 ],
 "notes": ["Example 4 cites Hassan v. Colorado (10th Cir. 2012) only as a lower-court decision already discussed in the brief."],
}

emit(__file__, FILL)
