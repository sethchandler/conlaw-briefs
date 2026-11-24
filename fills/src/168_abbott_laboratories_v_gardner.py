"""Fill for 168_abbott_laboratories_v_gardner. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/387/136/"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Drug makers sued to block an FDA ``every time'' generic-name labeling rule before any enforcement; the Court held 5--3 that final agency action is presumptively reviewable and that a pre-enforcement challenge is ripe when the issue is fit for decision and withholding review would cause hardship (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Before the FDA initiated any enforcement action")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Before the FDA initiated any enforcement action")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{5--3} vote. The case was argued on January 16, 1967, and decided on May 22, 1967 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Harlan delivered the opinion of the Court, joined by Justices Black, Douglas, Stewart, and White.
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} Justice Fortas filed a dissenting opinion, joined by Chief Justice Warren and Justice Clark, published in the companion case \textit{Gardner v.\ Toilet Goods Ass'n, Inc.}, 387 U.S.\ 167, 174 (1967). Justice Clark also filed a separate dissenting opinion (387 U.S.\ at 201).
    \item \textbf{Not Participating:} Justice Brennan took no part in the consideration or decision of the case.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Harlan)}"), SEC("Reasoning"),
    N(r"\subsection{Dissenting Opinion (Justice Fortas)}"),
    SEC("Concurring and Dissenting", frm="Fortas concurred in the companion case", to=r"\textbf{Justice Clark, dissenting separately}"),
    N(r"\subsection{Dissenting Opinion (Justice Clark)}"),
    SEC("Concurring and Dissenting", frm="Joining Fortas's dissent"),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"    \item \textbf{Jurisdictional Clarification:}", to=r"    \item \textbf{Tension Between"),
    N(r"\item \textbf{Prudential Ripeness Questioned:}", glue=" "),
    S(r"In \textit{MedImmune, Inc.\ v.\ Genentech, Inc.}, 549 U.S.\ 118, 128 n.8 (2007), the Court observed that pre-enforcement justiciability problems can often be framed interchangeably in terms of Article III standing or \textit{Abbott Laboratories} ripeness.", glue=" "),
    S(r"More pointedly, in \textit{Susan B.\ Anthony List v.\ Driehaus}, 573 U.S.\ 149, 167 (2014), the Court questioned the ``continuing vitality of the prudential ripeness doctrine,'' noting its tension with the principle reaffirmed in \textit{Lexmark International, Inc.\ v.\ Static Control Components, Inc.}, 572 U.S.\ 118, 125--126 (2014), that federal courts have a ``virtually unflagging'' obligation to hear cases within their Article III jurisdiction."),
    N(r"\item \textbf{Statutory Channeling:}", glue=" "),
    S(r"While \textit{Abbott Laboratories} remains the baseline for pre-enforcement review, \textit{Thunder Basin Coal Co.\ v.\ Reich}, 510 U.S.\ 200 (1994), established an important counterweight where comprehensive statutory review schemes impliedly channel pre-enforcement challenges into agency adjudication."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Ripe): A Self-Executing Data-Deletion Rule.}", glue=" "),
    S(r"Suppose Congress enacts the Federal Digital Privacy Act authorizing the FTC to promulgate rules prohibiting ``deceptive data-brokerage practices.''", glue=" "),
    N(r"After notice and comment, the FTC issues a final rule, effective in 30 days, under which", glue=" "),
    S(r"\textbf{Rule A} mandates that every data broker overhaul its database architecture to delete consumer location histories every 24 hours, backed by civil penalties of \$50,000 per violation.", glue=" "),
    N(r"A trade association sues before any enforcement, arguing that the rule exceeds the FTC's statutory authority.", glue=" "),
    S(r"Under \textit{Abbott Laboratories}, \textbf{Rule A is ripe}: the statutory-authority question is purely legal, the rule is final agency action, and brokers face the classic compliance-or-penalty dilemma requiring immediate, costly operational overhauls."),
    N(r"\item \textbf{Same-Side (Ripe): A Mandatory Equipment-Installation Rule.} After notice and comment, a federal transportation agency issues a final rule requiring every interstate trucking company to install a specified electronic monitoring device in each truck within 90 days, with civil penalties for each noncompliant vehicle. Carriers sue at once, arguing only that the governing statute does not authorize the mandate. As in \textit{Abbott}, the issue is a purely legal question of statutory construction, the rule is formally promulgated and immediately effective, and the carriers must either spend heavily on equipment now or risk penalties later. Nothing in the statute shows by clear and convincing evidence that Congress meant to bar pre-enforcement review, so the challenge may proceed in district court."),
    N(r"\item \textbf{Opposite-Side (Unripe): A Discretionary Audit-and-Suspension Rule.} Return to the data-privacy hypothetical, but suppose the FTC's rule is instead", glue=" "),
    S(r"\textbf{Rule B} announces that the FTC ``may, in its discretion, audit the algorithmic training logs of any data broker suspected of non-compliance'' and ``may suspend the broker's federal registry license'' if the broker refuses access.", glue=" "),
    S(r"Under \textit{Toilet Goods}, \textbf{Rule B is unripe}: enforcement is discretionary and contingent on future factual circumstances (whether and how an audit is demanded), and the rule imposes no immediate change in primary conduct pending an actual audit request.", glue=" "),
    S(r"Students should also note the post-\textit{Driehaus}/\textit{Lexmark} nuance: if the brokers can establish an imminent Article III injury-in-fact as to Rule B, they may argue that prudential ripeness cannot independently bar a court from exercising statutory jurisdiction."),
    N(r"\item \textbf{Opposite-Side (Review Channeled Elsewhere): A Statutory Review Scheme Displaces District Court Suit.} A federal mine-safety statute directs that challenges to agency orders be heard first by an independent review commission, with review afterward in a court of appeals. Before any citation issues, a mine operator sues in district court to enjoin the agency from enforcing a new compliance requirement. Although \textit{Abbott} presumes that final agency action is reviewable, the presumption yields when Congress's scheme shows an intent to channel review elsewhere. In \textit{Thunder Basin Coal Co.\ v.\ Reich}, 510 U.S.\ 200 (1994), the Court held that a comprehensive review structure of this kind implicitly precluded district court jurisdiction, so the operator must raise its objections through the statutory path."),
    N(r"\item \textbf{Fence-Sitter (Close Call): An Agency Guidance Document Backed by Warning Letters.} A federal agency publishes a guidance document, without notice and comment, stating its view that certain dietary supplements are unapproved drugs, and sends warning letters to several sellers saying that it ``may'' take enforcement action. The sellers sue, arguing that the products are not drugs. The question is largely legal, and sellers face pressure to pull products or risk seizure. But the guidance and letters appear to impose no legal obligations or consequences of their own. The pressure to comply can bear on hardship under \textit{Abbott}, but it does not by itself supply final agency action under the APA. The case becomes closer if a letter changes a seller's legal position or triggers an immediate legal consequence."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Blurry Line", to=r"\end{enumerate}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, \\url{} printouts (Justia link kept in Memory Jogger and Judicial Votes).",
  "Legacy section: introductory paragraph (companion cases); Driehaus item's sentence on 2025-2026 lower-court/scholarly trends, Trump v. New York, and Industrial Energy Consumers of America v. ITC (D.C. Cir. 2025) citation; universal-vacatur debate sentence. Kept: Califano v. Sanders item, MedImmune/Driehaus sentences, Thunder Basin sentence.",
  "Pedagogical section: 'Opposite Side' Contrast (Abbott vs. Toilet Goods) - a description of the companion case and exam tip, not a hypothetical; its rule is applied in Example 3.",
  "Exam Hypothetical: intro clause 'After notice and comment, the FTC issues two final rules effective in 30 days:' and the 'A trade association ... files a pre-enforcement ... suit' sentence (paraphrased in new text to split the hypothetical into Examples 1 and 3).",
 ],
 "notes": [
  "Examples 1 and 3 split Neon's single data-broker hypothetical (Rule A ripe / Rule B unripe).",
 ],
}

emit(__file__, FILL)
