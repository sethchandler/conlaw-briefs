"""Fill for 193_shelby_county_v_holder. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/570/529/"
C = "https://www.law.cornell.edu/supremecourt/text/12-96"

def quote(text, attrib):
    return [N(r"\begin{quote}", glue="\n"), S(text, glue="\n"), N(r"\end{quote}", glue="\n"),
            N(r"\noindent ---", glue=" "), S(attrib, glue=""), N(".")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"An Alabama county challenged the Voting Rights Act's preclearance regime; the Court held 5--4 that the \S~4(b) coverage formula, still based on decades-old data, could no longer justify subjecting some States to \S~5 preclearance, because current burdens must be justified by current needs and the equal sovereignty of the States (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to=r"\subsection{Litigation Below}")],
  "Procedural History": [SEC("Facts and Procedural History", frm=r"\subsection{Litigation Below}", strip=r"\subsection{Litigation Below}")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the D.C. Circuit by a \textbf{5--4} vote. The case was argued on February 27, 2013, and decided on June 25, 2013 (\href{" + J + r"}{Justia}; \href{" + C + r"}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Roberts delivered the opinion of the Court, joined by Justices Scalia, Kennedy, Thomas, and Alito.
    \item \textbf{Concurring Opinion:} Justice Thomas filed a concurring opinion, joining the Court's opinion in full.
    \item \textbf{Dissenting Opinion:} Justice Ginsburg filed a dissenting opinion, joined by Justices Breyer, Sotomayor, and Kagan.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"),
    SEC("Concurring and Dissenting", frm="Justice Thomas joined the Court's opinion in full", to=r"\subsection{Dissenting Opinion"),
    N(r"\subsection{Dissenting Opinion (Justice Ginsburg)}"),
    SEC("Concurring and Dissenting", frm="Justice Ginsburg delivered a forceful"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Preclearance Inoperable:}", glue=" "),
    S(r"Although \emph{Shelby County} formally left \S~5 intact, invalidating \S~4(b) immediately terminated federal preclearance across all nine covered States and dozens of covered local subdivisions."),
    N(r"\item \textbf{\emph{Louisiana v. Callais} (2026):}", glue=" "),
    S(r"Following October 2025 reargument, a 6--3 Court (per Justice Alito) struck down Louisiana's remedial congressional map (SB8) as an unconstitutional racial gerrymander and held that---to remain congruent and proportional under the Fifteenth Amendment---``\S~2 imposes liability only when the evidence supports a strong inference'' of intentional racial discrimination (\href{https://supreme.justia.com/cases/federal/us/608/24-109/}{Justia: \emph{Callais}}; \href{https://www.scotusblog.com/2026/04/in-major-voting-rights-act-case-supreme-court-strikes-down-redistricting-map-challenged-as-racia/}{SCOTUSblog})."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Formula Invalid): A Coverage Formula Pegged to Old History.} Congress enacts a statute requiring every State that used a poll tax in federal elections before 1964 to obtain federal approval before changing its voter-identification rules. The statute rests on that history alone, and the legislative record contains no current data comparing those States with others. Under \emph{Shelby County}, the formula fails: ``history did not end in 1965,'' the Fifteenth Amendment is not designed to punish for the past, and a law that treats States differently must justify its current burdens by current needs. Selecting States by practices long since abolished nationwide is exactly the kind of outdated criterion the Court held could no longer support preclearance."),
    N(r"\item \textbf{Same-Side (Formula Invalid): Current Data That Does Not Track the Problem.} Congress responds to \emph{Shelby County} with a formula that uses only current data: any State in which overall turnout fell below 50\% in the most recent presidential election must preclear changes to its voting laws. The data are fresh, but the trigger measures low turnout of all voters rather than racial discrimination in voting. \emph{Shelby County}, applying \emph{Northwest Austin}, requires that a statute's ``disparate geographic coverage is sufficiently related to the problem that it targets.'' Because a turnout trigger could sweep in States with no record of discrimination and omit States with serious problems, a court would likely hold it insufficiently related to the Fifteenth Amendment harm that justifies so drastic a departure from equal sovereignty."),
    N(r"\item \textbf{Opposite-Side (Formula Likely Valid): A Rolling Trigger Based on Adjudicated Violations.}", glue=" "),
    S(r"Suppose Congress enacts a nationwide, rolling 15-year preclearance formula triggered whenever any State incurs five or more final federal judgments of intentional Fourteenth or Fifteenth Amendment voting violations, with expedited 5-year bailout.", glue=" "),
    S(r"Unlike the 1965 formula in \emph{Shelby County}, this trigger uses current data, tracks adjudicated constitutional violations, and treats all States symmetrically on its face, strongly satisfying equal sovereignty. A challenger's best counterargument---echoing Justice Thomas's concurrence---is that prior federal restraint under \S~5 remains unconstitutional absent \emph{Katzenbach}-level systemic defiance."),
    N(r"\item \textbf{Opposite-Side (Preclearance by Court Order): Judicial ``Bail-In'' After Intentional Discrimination.} After \emph{Shelby County}, voters sue a formerly covered county, and a federal court finds after trial that the county intentionally moved polling places to make voting harder for Black residents. The court invokes \S~3(c) of the Voting Rights Act, 52 U.S.C.\ \S~10302(c), and orders the county to obtain approval before making further voting changes for a period of years. \emph{Shelby County} does not bar the order: the Court invalidated only the \S~4(b) coverage formula and expressly left \S~5 and \S~2 in place. A bail-in order rests on a present-day judicial finding of a constitutional violation in that jurisdiction, not on decades-old data, so it answers the Court's demand that burdens be justified by current needs."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Equal Sovereignty Outside Voting.} A federal statute bars States from authorizing new forms of sports wagering but allows two States that already licensed it before a set date to continue. A State excluded by the cutoff sues, arguing that the law violates the equal sovereignty of the States. \emph{Shelby County} said equal sovereignty ``remains highly pertinent in assessing subsequent disparate treatment of States,'' which supports the challenge. But the Court applied the principle to a law requiring some States to seek federal permission before legislating, and Justice Ginsburg warned that the majority's reasoning threatened grandfather provisions of exactly this kind. Whether the principle reaches ordinary federal regulation that treats States differently, and what level of justification it demands, is genuinely unsettled."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm="Critics note", to=r"\subsection{Exam Hypothetical}")],
  "Key Quotations": [
    S(r"All quotations below are verified verbatim against the primary opinion text (\href{https://www.law.cornell.edu/supremecourt/text/12-96}{Cornell LII}; \href{https://tile.loc.gov/storage-services/service/ll/usrep/usrep570/usrep570529/usrep570529.pdf}{570 U.S. 529 (2013)}):"),
  ] + quote(r"``The Voting Rights Act of 1965 employed extraordinary measures to address an extraordinary problem. Section 5 of the Act required States to obtain federal permission before enacting any law related to voting---a drastic departure from basic principles of federalism. And \S~4 of the Act applied that requirement only to some States---an equally dramatic departure from the principle that all States enjoy equal sovereignty.''", "Chief Justice Roberts, 570 U.S. at 534--35")
    + quote(r"``In \emph{Northwest Austin}, we stated that `the Act imposes current burdens and must be justified by current needs.' 557 U. S., at 203. And we concluded that `a departure from the fundamental principle of equal sovereignty requires a showing that a statute's disparate geographic coverage is sufficiently related to the problem that it targets.' \emph{Ibid.}''", "Chief Justice Roberts, 570 U.S. at 542")
    + quote(r"``But history did not end in 1965. By the time the Act was reauthorized in 2006, there had been 40 more years of it. \ldots{} The Fifteenth Amendment commands that the right to vote shall not be denied or abridged on account of race or color, and it gives Congress the power to enforce that command. The Amendment is not designed to punish for the past; its purpose is to ensure a better future.''", "Chief Justice Roberts, 570 U.S. at 552--53")
    + quote(r"``Our decision in no way affects the permanent, nationwide ban on racial discrimination in voting found in \S~2. We issue no holding on \S~5 itself, only on the coverage formula. Congress may draft another formula based on current conditions. \ldots{} Our country has changed, and while any racial discrimination in voting is too much, Congress must ensure that the legislation it passes to remedy that problem speaks to current conditions.''", "Chief Justice Roberts, 570 U.S. at 557")
    + quote(r"``Throwing out preclearance when it has worked and is continuing to work to stop discriminatory changes is like throwing away your umbrella in a rainstorm because you are not getting wet.''", "Justice Ginsburg, Dissenting, 570 U.S. at 590"),
 },
 "dropped": [
  "Case Metadata table: full case name, parallel citations, lower-court citations (in Procedural History), provisions list, LOC PDF link in metadata (still in Key Quotations lead-in).",
  "Legacy section: rest of intro paragraph (post-2013 state laws, stalled John Lewis VRAA bills incl. 2025-2026 S. 2523, state VRAs); 'With Section 5 immobilized' lead-in; Brnovich item (Section 2 vote-denial, not Shelby's holding); Allen v. Milligan (2023) item (Kavanaugh concurrence only echoes Shelby); remainder of Callais item (Gingles updates, Kagan dissent, June 2026 Milligan interim relief). Kept: preclearance-inoperable sentence; Callais holding sentence (resolves the Katzenbach/Boerne question Shelby left open, as the Critique notes).",
  "Exam Hypothetical: 'Analysis:' label (text reused in Example 3). 'Opposite Side' Contrast itemize - restates the two doctrinal camps (exam tip, not a fact pattern).",
  "Key Quotations: descriptive topic labels before each quote (speaker and pin cite moved into Group A attribution lines).",
 ],
 "notes": [
  "Kept Callais (2026) sentence describes a decision after the drafter's verification horizon; verify holding, vote, and 608 U.S. 85 citation in audit.",
  "Key Quotations built manually in Group A style (stem listed in tools/manual_quotes.txt).",
 ],
}

emit(__file__, FILL)
