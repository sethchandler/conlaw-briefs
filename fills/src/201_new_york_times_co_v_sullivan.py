"""Fill for 201_new_york_times_co_v_sullivan. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/376/254/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"An Alabama jury awarded a Montgomery city commissioner \$500,000 against the \textit{New York Times} over a civil-rights advertisement with minor errors; the Court unanimously reversed, holding that a public official may recover for a defamatory falsehood about his official conduct only by proving ``actual malice''---knowing or reckless falsity (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Sullivan sued without replying")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Sullivan sued without replying")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{reversed and remanded} the judgment of the Supreme Court of Alabama, 9--0. The case was argued on January 6--7, 1964, and decided on March 9, 1964, together with \textit{Abernathy v.\ Sullivan} (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/376/254}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Brennan delivered the opinion of the Court, joined by Chief Justice Warren and Justices Clark, Harlan, Stewart, and White.
    \item \textbf{Concurring Opinions:} Justice Black filed a concurring opinion, joined by Justice Douglas. Justice Goldberg filed an opinion concurring in the result, joined by Justice Douglas.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Brennan)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Black)}"), N("Justice Black", glue=" "),
    SEC("Concurring and Dissenting", frm="Argued that the First and Fourteenth", to=r"  \item \textbf{Justice Goldberg", lc=True),
    N(r"\subsection{Opinion Concurring in the Result (Justice Goldberg)}"), N("Justice Goldberg", glue=" "),
    SEC("Concurring and Dissenting", frm="Likewise urged an absolute privilege", to=r"  \item \textbf{Dissents:}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Extensions and Limits of Actual Malice:}", glue=" "),
    S(r"The Court soon extended actual malice to ``public figures'' in \textit{Curtis Publishing Co. v. Butts}, 388 U.S. 130 (1967) (\href{https://www.law.cornell.edu/wex/defamation}{Cornell LII Wex}), drew the public/private boundary in \textit{\href{https://supreme.justia.com/cases/federal/us/418/323/}{Gertz v. Robert Welch, Inc.}}, 418 U.S. 323 (1974) (allowing states to set lower fault rules for private plaintiffs' actual damages while barring strict liability), applied \textit{Sullivan} to intentional infliction of emotional distress in \textit{\href{https://supreme.justia.com/cases/federal/us/485/46/}{Hustler Magazine, Inc. v. Falwell}}, 485 U.S. 46 (1988), and reinforced independent appellate review of actual malice in \textit{Bose Corp. v. Consumers Union}, 466 U.S. 485 (1984) (\href{https://www.law.cornell.edu/constitution-conan/amendment-1/defamation}{Constitution Annotated}) and \textit{\href{https://supreme.justia.com/cases/federal/us/491/657/}{Harte-Hanks Communications, Inc. v. Connaughton}}, 491 U.S. 657 (1989)."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (No Liability): A Careless Op-Ed About a State Attorney General.} A newspaper publishes a guest op-ed accusing the State Attorney General of dropping a corruption investigation to protect a donor. The op-ed misstates the dates and wrongly says the investigation was closed rather than suspended. The editors relied on the author's reputation and did not check the court docket, which would have revealed the errors. The Attorney General sues for libel. Under \textit{Sullivan}, he must prove with convincing clarity that the paper knew the statements were false or recklessly disregarded their falsity. Failing to check available records, like the \textit{Times}'s failure to consult its own news files, is at most negligence, so the claim fails."),
    N(r"\item \textbf{Same-Side (No Liability): Impersonal Criticism of a Government Office.} A civil-liberties group's website falsely states that guards at the county jail routinely beat inmates who file grievances. It names no individual. The elected sheriff, who oversees the jail, sues, arguing that readers will understand any criticism of the jail as an attack on him. \textit{Sullivan} forecloses that theory: Alabama's inference that criticism of the police necessarily referred to the commissioner who supervised them impermissibly transformed criticism of government into personal libel of an official. Without evidence that the statement was ``of and concerning'' the sheriff personally, and without proof of actual malice, the sheriff cannot recover."),
    N(r"\item \textbf{Opposite-Side (Actual Malice Shown): Purposeful Avoidance of the Truth.}", glue=" "),
    S(r"A local investigative blog publishes a story accusing the City Police Chief of shredding body-camera footage, relying solely on one anonymous tipster whose prior tips proved fabricated, and deliberately declines to review publicly posted audit logs that would refute the claim.", glue=" "),
    S(r"The Police Chief is a public official; while mere failure to investigate is negligence (\textit{Sullivan}), purposeful avoidance of the truth despite serious doubts about a known unreliable source can satisfy reckless disregard with convincing clarity (\textit{\href{https://supreme.justia.com/cases/federal/us/491/657/}{Harte-Hanks}})."),
    N(r"\item \textbf{Opposite-Side (Actual Malice Not Required): A Private-Figure Plaintiff.}", glue=" "),
    S(r"Suppose instead that an unverified social-media post falsely accuses a private-citizen neighborhood mechanic---who never spoke to the press or entered any public debate---of overbilling city residents during a hurricane cleanup, and the local newspaper negligently repeats the claim without checking receipts.", glue=" "),
    S(r"Unlike Commissioner Sullivan, the mechanic is a private figure who neither assumed the risk of public scrutiny nor commands media access to rebut falsehoods (\textit{\href{https://supreme.justia.com/cases/federal/us/418/323/}{Gertz}}, 418 U.S. at 344--45). Under \textit{Gertz}, the State may allow recovery of proven actual damages upon a showing of mere negligence, reserving \textit{Sullivan}'s actual-malice bar only for presumed or punitive damages on a matter of public concern."),
    N(r"\item \textbf{Fence-Sitter (Close Call): A Citizen Who Spoke Once at a Council Meeting.} A local business owner testifies at a single city council hearing against a proposed zoning change, and a short news clip of her testimony circulates online. A blogger then falsely reports that she bribed a council member to block the change; the blogger was careless but did not know the claim was false. Whether she must prove actual malice depends on whether she is a limited-purpose public figure under \textit{Gertz}---someone who voluntarily thrust herself into a particular public controversy to influence its outcome. One appearance at a public hearing points toward public-figure status on the zoning dispute, but her minimal role, lack of media access, and the blogger's own creation of the controversy point the other way, so the result is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm="Originalists (echoing Thomas)", to=r"\textbf{Exam Hypothetical 1")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: parallel citations, duplicate links (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: opening framing sentence; Counterman (true-threats mens rea, tangential); entire second paragraph (Thomas/Gorsuch calls to overrule in McKee, Berisha, Blankenship, Counterman dissent, 2026 Dershowitz cert-denial dissent; Wynn cert denial; Palin retrial; AI-era suits) - separate opinions and commentary, not changes in law. Kept: Curtis/Gertz/Hustler/Bose/Harte-Hanks sentence.",
  "Exam Hypotheticals: 'Analysis:' and 'Contrast:' labels and hypothetical headings (texts reused in Examples 3 and 4).",
 ],
 "notes": [],
}

emit(__file__, FILL)
