"""Fill for 227_ziglar_v_abbasi. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/582/15-1358/"
FS = "Facts and Procedural History"
RS = "Reasoning"
SO = "Concurring and Dissenting"
LG = "Doctrinal Significance"
PS = "Pedagogical Critiques"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Post-9/11 immigration detainees sued the Attorney General, FBI Director, and jail wardens for damages; the Court held 4--2 that extending \textit{Bivens} is disfavored, that claims arising in a new context fail if special factors counsel hesitation, and that no \textit{Bivens} remedy lay for challenges to high-level detention policy (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="Respondents brought a putative class action")],
  "Procedural History": [SEC(FS, frm="Respondents brought a putative class action")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed in part and vacated and remanded in part} by a \textbf{4--2} vote. The case was argued on January 18, 2017, and decided on June 19, 2017 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/15-1358}{Cornell LII}):"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Majority Opinion:} Justice Kennedy delivered the opinion of the Court", glue=" "),
    S(r"(opinion of the Court as to Parts I, II, III, IV--A, and V, joined by Chief Justice Roberts and Justices Thomas and Alito; plurality opinion as to Part IV--B, joined by Chief Justice Roberts and Justice Alito)", glue=""),
    N("."),
    N(r"""\item \textbf{Concurring Opinion:} Justice Thomas filed an opinion concurring in part and concurring in the judgment.
    \item \textbf{Dissenting Opinion:} Justice Breyer filed a dissenting opinion, joined by Justice Ginsburg.
    \item \textbf{Not Participating:}""", glue=" "),
    S(r"Justices Sotomayor, Kagan, and Gorsuch took no part in the consideration or decision of the cases", glue=""),
    N("."),
    N(r"\end{itemize}"),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kennedy)}"),
    N(r"\subsubsection{The Shift Away from Implied Remedies and the Two-Step Test (Parts II--III)}"),
    SEC(RS, frm="Justice Kennedy framed", to=r"\subsection{Warden Hasty"),
    N(r"\subsubsection{Warden Hasty and \S~1985(3) Qualified Immunity (Parts IV--V)}"),
    SEC(RS, frm="On the guard-abuse claim"),
    N(r"\subsection{Opinion Concurring in Part and in the Judgment (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC(SO, frm="Joined Parts I, II, III", to=r"  \item \textbf{Justice Breyer", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Breyer)}"), N("Justice Breyer, joined by Justice Ginsburg,", glue=" "),
    SEC(SO, frm="Argued the claims arose", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    SEC(LG, frm=r"\begin{itemize}", to=r"  \item \textbf{Broader Separation-of-Powers"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (No \textit{Bivens} Remedy): An Emergency Directive From a Cabinet Secretary.} Suppose", glue=" "),
    S(r"the DHS Secretary issues an emergency directive ordering warrantless electronic sweeps of airports after a cyber-threat", glue=""),
    N(r", and travelers whose devices were searched sue the Secretary for damages (claim (b)).", glue=" "),
    S(r"Claim (b) is squarely barred under \textit{Abbasi}: high-level executive policy, national security, and prospective injunctive alternatives all counsel hesitation."),
    N(r"\item \textbf{Same-Side (No \textit{Bivens} Remedy): First Amendment Retaliation by a Federal Agent.} After a motel owner complains to an agent's supervisors about the agent's conduct on his property, the agent asks other agencies to investigate the owner's business. The owner sues the agent for damages, alleging retaliation for protected speech. The Court has never recognized a First Amendment \textit{Bivens} claim, so the case differs in a meaningful way from \textit{Bivens}, \textit{Davis}, and \textit{Carlson} and arises in a new context. Because Congress is better positioned to decide whether retaliation claims against federal officers should exist, special factors counsel hesitation; \textit{Egbert v.\ Boule} rejected a retaliation claim on similar facts."),
    N(r"\item \textbf{Opposite-Side (\textit{Bivens} Likely Available): A Warrantless Home Entry by a Line Agent.} Suppose", glue=" "),
    S(r"a federal ATF agent breaks down a citizen's front door without a warrant during a domestic firearms investigation and punches the homeowner", glue=""),
    N(r" (claim (a)).", glue=" "),
    S(r"Under \textit{Abbasi}, claim (a) closely parallels \textit{Bivens} (line-level officer, domestic Fourth Amendment search/seizure, clear judicial guidance; cf. \textit{Snowden}), though defendants will still argue even minor differences (agency or statutory mandate) create a new context under \textit{Egbert}."),
    N(r"\item \textbf{Opposite-Side (\textit{Bivens} Likely Available): Denial of Medical Care to a Convicted Prisoner.} Officials at a federal prison know that a convicted inmate suffers from severe asthma, yet they keep him in the facility against doctors' advice, delay his treatment, and give him contraindicated drugs, and he dies after an attack. His estate sues the officials for damages under the Eighth Amendment. These facts track \textit{Carlson v.\ Green} itself, one of the three cases in which the Court recognized a \textit{Bivens} remedy. Because the claim involves the same constitutional right, the same kind of line-level prison officials, and the same mechanism of injury, it does not differ in a meaningful way from \textit{Carlson}, and \textit{Abbasi}'s new-context bar should not apply."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Abuse of a Federal Pretrial Detainee.}", glue=" "),
    S(r"Suppose a federal Marshal beats a pretrial detainee in a courthouse holding cell and denies him insulin for 48 hours. Students should separate the two theories under \textit{Abbasi} and \textit{Goldey v. Fields} (2025): the excessive-force claim fails as a new context foreclosed by special factors, while the medical-indifference claim tests whether the Fifth Amendment (pretrial detainee) vs. Eighth Amendment (convicted prisoner in \textit{Carlson}) distinction alone creates a ``new context'' under \textit{Abbasi} Part IV--A.", glue=" "),
    N(r"The medical claim is genuinely uncertain: \textit{Abbasi} treated a Fifth Amendment prisoner-abuse claim as a new context, yet a denial of insulin is the same harm \textit{Carlson} remedied."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"  \item \textbf{The Rights", to=r"\subsection{``Opposite Side''")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: consolidated case names, citation links, court line, Chapter Placement line.",
  "Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection.",
  "Legacy section: introductory sentence; 'Broader Separation-of-Powers Reach Through 2026' item (Cisco Systems v. Doe, pending Nielsen v. Watanabe, legislative proposals) and 'Qualified Immunity Debate' item - tangential. Kept: Hernandez / Egbert / Goldey item.",
  "'Opposite Side' Contrast (Bivens and Snowden v. Henning, 7th Cir.) - a lower-court contrast and exam tip, not a hypothetical.",
  "Exam Hypothetical 1 was split into its two fact patterns (Examples 1 and 3); its connecting words 'Suppose (a) ... while (b)' were replaced.",
 ],
 "notes": ["Example 4 (Carlson facts) restates the facts of Carlson v. Green, 446 U.S. 14 (1980), which the brief already cites.", "Example 2 closely follows the facts of Egbert v. Boule (cited in the brief's legacy item)."],
}

emit(__file__, FILL)
