"""Fill for 238_dhs_v_thuraissigiam. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/591/19-161/"
P = "Pedagogical"
CD = "Concurring and Dissenting"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"A Sri Lankan asylum seeker caught 25 yards inside the border could not use habeas to challenge his negative credible-fear finding: the Court held 7--2 that the Suspension Clause protects release from unlawful custody, not further review of a claim to stay, and that an alien at the threshold of entry has only the procedural rights Congress grants (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Thuraissigiam filed a federal habeas petition")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Thuraissigiam filed a federal habeas petition")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded with instructions to dismiss} by a \textbf{7--2} vote. The case was argued on March 2, 2020, and decided on June 25, 2020 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/19-161}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Alito delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Thomas, Gorsuch, and Kavanaugh.
    \item \textbf{Concurring Opinions:} Justice Thomas filed a concurring opinion. Justice Breyer filed an opinion concurring in the judgment, joined by Justice Ginsburg.
    \item \textbf{Dissenting Opinion:} Justice Sotomayor filed a dissenting opinion, joined by Justice Kagan.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Alito)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC(CD, frm="Joined the majority and explored", to=r"  \item \textbf{Justice Breyer", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Breyer)}"), N("Justice Breyer", glue=" "),
    SEC(CD, frm="Criticized the majority for sweeping", to=r"  \item \textbf{Justice Sotomayor", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Sotomayor)}"), N("Justice Sotomayor", glue=" "),
    SEC(CD, frm="Charged the majority", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Preserving Core Habeas"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (No Habeas Review): A Border-Adjacent Credible-Fear Denial.}", glue=" "),
    SEC(P, frm="A Guatemalan migrant crosses", to=r"\textit{Analysis:} Under \textit{Thuraissigiam}, the district", glue=" "),
    SEC(P, frm=r"Under \textit{Thuraissigiam}, the district court must dismiss", to=r"\textbf{Hypothetical 2"),
    N(r"\item \textbf{Same-Side (No Habeas Review): An Asylum Seeker at a Port of Entry.} A noncitizen without valid documents presents herself at a land port of entry and asks for asylum. She is placed in expedited removal, and an asylum officer and an immigration judge find no credible fear. In a habeas petition she argues that her interview was conducted through an interpreter who spoke a different dialect, and she asks for a new interview. Like Thuraissigiam, she seeks another chance at admission rather than simple release, so the Suspension Clause does not require review. And because she has never entered the United States, she has only the procedural rights Congress has provided by statute; the Court stressed that a clandestine entrant should not receive more process than such a port-of-entry applicant (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Habeas Available): Core Release From Interior Detention.}", glue=" "),
    SEC(P, frm="Suppose instead DHS arrests a noncitizen", to=r"\textit{Contrast:}", glue=" "),
    S(r"Unlike \textit{Thuraissigiam}, this statute violates both the Suspension Clause and the Due Process Clause. The petitioner seeks \textit{simple release from unlawful executive detention}---the indisputable 1789 core of the Great Writ recognized in \textit{Thuraissigiam}, \textit{St. Cyr}, and \href{https://supreme.justia.com/cases/federal/us/553/723/}{\textit{Boumediene}}", glue=""),
    N(r"; and", glue=" "),
    S(r"an established U.S. resident (or citizen) inside the country holds full Fifth Amendment due process protections against arbitrary detention and summary removal", glue=""),
    N(r"."),
    N(r"\item \textbf{Opposite-Side (Habeas Available): A Claim of Citizenship.} A man apprehended near the border is placed in expedited removal and ordered removed after a negative credible-fear finding. In a habeas petition he asserts that he is a United States citizen, born in Texas, and offers a birth certificate. Section 1252(e)(2) itself permits habeas review of whether the petitioner is an alien and whether he is a lawful permanent resident, refugee, or asylee, so the district court has jurisdiction to decide his citizenship claim. Nothing in \textit{Thuraissigiam} forecloses that inquiry: a citizen wrongly subjected to expedited removal is not an alien seeking initial admission, and his challenge is to the Executive's power to hold and remove him at all."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Expedited Removal Deep in the Interior.} DHS arrests a noncitizen in Chicago who entered without inspection and has lived there for eighteen months, places him in expedited removal under the statute's two-year presence limit, and denies his credible-fear claim. He files a habeas petition arguing that the asylum officer applied the wrong legal standard and that he is entitled to full due process. The Suspension Clause holding cuts against him because he seeks further review rather than release. But the due process holding rested on Thuraissigiam's status at the threshold of initial entry, and the Court did not say when presence inside the country matures into an entry carrying fuller constitutional protection (see \textit{Zadvydas v.\ Davis}, 533 U.S.\ 678 (2001)). Whether eighteen months of residence is enough remains open."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(P, frm=r"  \item \textbf{Anachronistic", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: lower-court citations, SupremeCourt.gov slip-opinion link, constitutional-provisions line (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory sentence; Trump v. J.G.G. / A.A.R.P. v. Trump item (Alien Enemies Act notice rulings - not applications of Thuraissigiam's holding); 'Through 2026' item (Mullin v. Al Otro Lado and the Ninth Circuit's Padilla decision - unverifiable 2026 decisions, the latter a lower-court ruling). Kept: Jones v. Hendrix.",
  "Exam Hypothetical 2: its closing citations to Trump v. J.G.G. (2025) and Padilla v. ICE (9th Cir. 2026); the fact pattern and the rest of the contrast analysis are reused in Example 3. Hypothetical headings and 'Analysis:'/'Contrast:' labels dropped.",
 ],
 "notes": ["Example 3 joins two verbatim pieces of Neon's contrast analysis with a new '; and' and closing period, omitting the parenthetical J.G.G./Padilla citations."],
}

emit(__file__, FILL)
