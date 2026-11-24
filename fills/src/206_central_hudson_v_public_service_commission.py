"""Fill for 206_central_hudson_v_public_service_commission. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/447/557/"
CD = "Concurring and Dissenting"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Striking down New York's total ban on promotional advertising by electric utilities 8--1, the Court announced the four-part intermediate-scrutiny test for restrictions on truthful commercial speech about lawful activity: a substantial interest, direct advancement, and a restriction no more extensive than necessary (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Central Hudson sued in New York state court")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Central Hudson sued in New York state court")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed} the New York Court of Appeals by an \textbf{8--1} vote. The case was argued on March 17, 1980, and decided on June 20, 1980 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/447/557}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Powell delivered the opinion of the Court, joined by Chief Justice Burger and Justices Stewart, White, and Marshall.
    \item \textbf{Concurring in the Judgment:} Justice Brennan filed an opinion concurring in the judgment (447 U.S. at 572). Justice Blackmun filed an opinion concurring in the judgment, joined by Justice Brennan (447 U.S. at 573). Justice Stevens filed an opinion concurring in the judgment, joined by Justice Brennan (447 U.S. at 579).
    \item \textbf{Dissenting Opinion:} Justice Rehnquist filed a dissenting opinion (447 U.S. at 583).
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Powell)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Judgment (Justice Blackmun)}"), N("Justice Blackmun", glue=" "),
    SEC(CD, frm="Criticized the majority's four-part", to=r"  \item \textbf{Justice Stevens", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Stevens)}"), N("Justice Stevens", glue=" "),
    SEC(CD, frm="Faulted Powell's first", to=r"  \item \textbf{Justice Brennan", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Brennan)}"), N("Justice Brennan", glue=" "),
    SEC(CD, frm="Joined both Stevens", to=r"  \item \textbf{Justice Rehnquist", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Rehnquist)}"), N("Justice Rehnquist", glue=" "),
    SEC(CD, frm="Mounted a sweeping", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Compelled Disclosures"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Restriction Invalid): Banning Truthful E-Cigarette Ads.}", glue=" "),
    SEC("Pedagogical", frm="To curb youth nicotine addiction", to=r"\textit{Analysis:}", glue=" "),
    SEC("Pedagogical", frm=r"Under \textit{Central Hudson}, (1) the ads", to=r"\textbf{``Opposite Side'' Contrast:}"),
    N(r"\item \textbf{Same-Side (Restriction Invalid): A Ban on Advertising Liquor Prices.} To promote temperance, a state forbids liquor retailers from advertising their prices anywhere except inside the store. A retailer that wants to advertise discounts sues. The ads are truthful and concern a lawful product, and reducing alcohol consumption is a substantial interest. But the State offers little evidence that hiding prices meaningfully reduces drinking, and it could pursue its goal directly through higher taxes, minimum prices, or education campaigns. As in \textit{Central Hudson}, the State seeks to influence conduct by keeping consumers uninformed, and the ban is more extensive than necessary; \href{https://supreme.justia.com/cases/federal/us/517/484/}{\textit{44 Liquormart, Inc.\ v.\ Rhode Island}, 517 U.S.\ 484 (1996)}, struck down a similar ban."),
    N(r"\item \textbf{Opposite-Side (Restriction Valid): Advertising an Unlawful Transaction.} A state in which online sports betting remains a crime fines a website operator for running ads urging state residents to place bets on its offshore platform. The operator claims the ads are truthful commercial speech. \textit{Central Hudson}'s first prong ends the inquiry: commercial speech is protected only if it concerns lawful activity and is not misleading. An advertisement proposing a transaction that is illegal where the audience would complete it receives no First Amendment protection, so the State need not show a substantial interest, direct advancement, or tailoring (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Restriction Valid): A Short Waiting Period for Lawyer Solicitation Letters.} A state bar forbids personal-injury lawyers from sending targeted direct-mail solicitations to accident victims or their families within 30 days of the accident. The rule restricts truthful speech about lawful services, but it serves substantial interests in protecting victims' privacy and the reputation of the legal profession, the bar supports it with survey evidence showing that such letters are widely seen as intrusive, and it is limited in time and leaves other forms of advertising open. Applying \textit{Central Hudson} as refined by \textit{Fox}, \href{https://supreme.justia.com/cases/federal/us/515/618/}{\textit{Florida Bar v.\ Went For It, Inc.}, 515 U.S.\ 618 (1995)}, upheld such a rule as a reasonable fit."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): Billboard Ban for State-Legal Marijuana.} A state that has legalized recreational marijuana bans billboard and television advertising by licensed dispensaries in order to reduce youth use. A dispensary challenges the ban. The first prong is the problem: the product is lawful under state law but remains illegal under federal law, and \textit{Central Hudson} protects only speech concerning lawful activity. If a court treats the activity as lawful because the State permits it, the ban faces the same direct-advancement and fit problems as the e-cigarette ban in Example 1. If it treats federal illegality as controlling, the ads may receive no protection at all. The Supreme Court has not resolved which sovereign's law defines lawful activity in this setting."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC("Pedagogical", frm=r"\begin{itemize}", to=r"\textbf{Exam Hypothetical:}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, lower-court citation, Chapter/Topic line (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory sentence and Cornell LII citation; 'Compelled Disclosures (Zauderer) vs. Restrictions (Central Hudson) Through 2026' item (Zauderer/NIFLA disclosure doctrine, DoorDash v. City of New York and U.S. Chamber of Commerce v. Sanchez lower-court cases) - concerns compelled disclosure and unverifiable 2025--2026 lower-court rulings rather than Central Hudson's holding. Kept: Fox/44 Liquormart and Sorrell items.",
  "Exam Hypothetical: 'Opposite Side' Contrast (Central Hudson vs. Zauderer and Consolidated Edison) - an exam tip, not a fact pattern.",
 ],
}

emit(__file__, FILL)
