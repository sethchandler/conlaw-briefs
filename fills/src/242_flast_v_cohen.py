"""Fill for 242_flast_v_cohen. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/392/83/"
FS = "Facts and Procedural History"
SO = "Concurring and Dissenting"
DS = "Doctrinal Significance"
PS = "Pedagogical Critiques"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Federal taxpayers challenged federal education grants that funded instruction and textbooks in religious schools; an 8--1 Court, narrowing \textit{Frothingham v.\ Mellon}, held that taxpayers have standing when they attack an exercise of Congress's taxing and spending power as exceeding a specific constitutional limit on that power---here, the Establishment Clause (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to=r"Relying on \textit{Frothingham v. Mellon}")],
  "Procedural History": [SEC(FS, frm=r"Relying on \textit{Frothingham v. Mellon}")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the three-judge District Court by an \textbf{8--1} vote. The case was argued on March 12, 1968, and decided on June 10, 1968 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Warren delivered the opinion of the Court, joined by Justices Black, Douglas, Brennan, Stewart, White, Fortas, and Marshall.
    \item \textbf{Concurring Opinions:} Justice Douglas, Justice Stewart, and Justice Fortas each filed a concurring opinion.
    \item \textbf{Dissenting Opinion:} Justice Harlan filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Warren)}"),
    SEC("Reasoning", to=r"\subsection{Reinterpreting"),
    N(r"\subsubsection{Reinterpreting Article III Standing and \textit{Frothingham}}"),
    SEC("Reasoning", frm="Warren noted that commentators", to=r"\subsection{The Double-Nexus Test}"),
    N(r"\subsubsection{The Double-Nexus Test}"),
    SEC("Reasoning", frm="To distinguish proper taxpayer suits"),
    N(r"\subsection{Concurring Opinion (Justice Douglas)}"), N("Justice Douglas", glue=" "),
    SEC(SO, frm="Joined the opinion but predicted", to=r"  \item \textbf{Justice Stewart", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Stewart)}"), N("Justice Stewart", glue=" "),
    SEC(SO, frm="Emphasized that the Court held", to=r"  \item \textbf{Justice Fortas", lc=True),
    N(r"\subsection{Concurring Opinion (Justice Fortas)}"), N("Justice Fortas", glue=" "),
    SEC(SO, frm="Agreed that \\textit{Flast} must", to=r"  \item \textbf{Justice Harlan", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Harlan)}"), N("Justice Harlan", glue=" "),
    SEC(SO, frm="Delivered a classic critique", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC(DS, frm=r"  \item \textbf{Property Clause", to=r"  \item \textbf{Status Through 2026"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Standing Exists): Express Appropriation for Sanctuary Repairs.}", glue=" "),
    S(r"Congress passes the ``Community Heritage Act'' under Article I, \S\ 8, expressly appropriating \$50 million to the Department of Housing and Urban Development with a statutory directive to distribute direct repair grants to churches and synagogues for sanctuary renovations. A federal income taxpayer with no other connection to the program sues in federal court under the Establishment Clause. \textit{Analysis:} The taxpayer \textit{has standing} under \textit{Flast} and \href{https://supreme.justia.com/cases/federal/us/487/589/}{\textit{Bowen v. Kendrick}}. Both nexuses are met: (1) the challenge targets an express congressional spending enactment under Article I, \S\ 8 (not general executive overhead or a regulatory statute), and (2) the challenge invokes the Establishment Clause, the sole recognized specific constitutional limitation on taxing and spending."),
    N(r"\item \textbf{Same-Side (Standing Exists): An As-Applied Challenge to a Grant Program Open to Religious Groups.} Congress enacts a spending statute authorizing the Secretary of Health and Human Services to award grants to public and private organizations, expressly including religious organizations, to provide counseling on adolescent health. Taxpayers allege that some religious grantees are using the federal money to teach religious doctrine and sue under the Establishment Clause. Although an agency selects the grantees, the challenge is still to the operation of a congressional spending program under Article I, \S\ 8, and it invokes the Establishment Clause, so both \textit{Flast} nexuses are satisfied. \href{https://supreme.justia.com/cases/federal/us/487/589/}{\textit{Bowen v.\ Kendrick}, 487 U.S.\ 589 (1988)}, upheld taxpayer standing for exactly this kind of as-applied challenge (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (No Standing): Outside \textit{Flast}'s Window.}", glue=" "),
    S(r"Suppose instead that (a) a federal taxpayer challenges a \$50 million congressional appropriation funding foreign military aid as violating Article I, \S\ 8's Declare War Clause or the Tenth Amendment, \textit{or} (b) a federal taxpayer brings an Establishment Clause challenge against either a new federal tax credit for donations to religious charities or a cabinet secretary's use of general agency operating funds to host sectarian prayer rallies. \textit{Contrast:} In every one of these scenarios, the suit must be dismissed for lack of Article III standing. Scenario (a) fails \textit{Flast}'s second nexus under \textit{Frothingham}, \href{https://supreme.justia.com/cases/federal/us/418/166/}{\textit{Richardson}}, and \href{https://supreme.justia.com/cases/federal/us/418/208/}{\textit{Schlesinger}} because no clause other than the Establishment Clause qualifies as a specific spending limitation. Scenario (b) fails \textit{Flast}'s first nexus under \href{https://supreme.justia.com/cases/federal/us/563/125/}{\textit{Winn}} (tax credits do not ``extract and spend'' taxpayer funds) and \href{https://supreme.justia.com/cases/federal/us/551/587/}{\textit{Hein}} (discretionary executive spending from general appropriations is not an express congressional spending mandate)."),
    N(r"\item \textbf{Opposite-Side (No Standing): Donating a Surplus Federal Building to a Seminary.} Acting under a statute that lets agencies dispose of surplus federal property, the General Services Administration conveys a closed federal office building, without charge, to a religious seminary. A taxpayers' group sues, claiming the gift violates the Establishment Clause. The claim fails \textit{Flast}'s first nexus twice over: the conveyance is an executive decision rather than a congressional spending enactment, and the authority for it rests on the Property Clause of Article IV, not the Taxing and Spending Clause of Article I, \S\ 8. \href{https://supreme.justia.com/cases/federal/us/454/464/}{\textit{Valley Forge Christian College}, 454 U.S.\ 464 (1982)}, denied taxpayer standing on materially identical facts."),
    N(r"\item \textbf{Fence-Sitter (Congressional Mandate or Executive Discretion?): A Recovery-Services Appropriation.} Congress appropriates \$20 million for grants to community organizations, including faith-based organizations, to provide addiction-recovery services; the statute does not require that any grantee be religious. The agency awards most of the money to churches whose programs incorporate worship, and taxpayers sue. If the grants are viewed as carrying out Congress's own spending program, \textit{Bowen} supports standing. If they are viewed as the agency's discretionary choices under a general appropriation, the plurality in \textit{Hein} would deny it. And with several Justices having urged that \textit{Flast} be overruled, the result is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"  \item \textbf{Formalism", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Cornell ConAn link, lower-court line, provisions line.",
  "Reasoning subsection headings re-created as \\subsubsection headings (new text) so they nest under the majority subsection.",
  "Legacy section: introductory paragraph (incl. Bowen v. Kendrick, reused in Examples 1-2); Richardson/Schlesinger item (cited in Example 3); 'Status Through 2026' item (incl. National Park Service v. National Trust (2026), a general standing case). Kept: Valley Forge, Hein, Winn items.",
 ],
 "notes": [
  "Neon's Hypothetical 2 ('Opposite Side' Contrast) contains genuine fact patterns (scenarios a and b) and is reused whole as Example 3.",
 ],
}

emit(__file__, FILL)
