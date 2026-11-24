"""Fill for 213_moody_v_netchoice. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/603/22-277/"
LII = r"(\href{https://www.law.cornell.edu/supremecourt/text/22-277}{Cornell LII})"

def Q(quote, who):
    # Attribution placed inside the quote block; tools/normalize_quotes.py then moves it to a
    # Group A "\noindent ---" line (check_brief.py does not match manual_quotes.txt's ".tex" names).
    return [N(r"\begin{quote}", glue="\n"), S(quote, glue="\n"), N(r"---", glue=" "),
            S(who, glue=" "), S(LII, glue="\n"), N(r"\end{quote}")]

FILL = {
 "sections": {
  "Memory Jogger": [N(r"The Court unanimously vacated both lower-court judgments because neither court applied the demanding test for facial First Amendment challenges; a majority (Kagan, J.) added that curating third-party posts in a feed is protected editorial expression that a State may not override to rebalance the marketplace of ideas (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="NetChoice, LLC and the Computer")],
  "Procedural History": [SEC("Facts and Procedural History", frm="NetChoice, LLC and the Computer")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{vacated and remanded} the judgments of the Eleventh and Fifth Circuits by a \textbf{9--0} vote on the judgment. The case was argued on February 26, 2024, and decided on July 1, 2024 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/22-277}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Kagan delivered the opinion of the Court, joined in full by Chief Justice Roberts and Justices Sotomayor, Kavanaugh, and Barrett, and by Justice Jackson as to Parts I, II, and III--A.
    \item \textbf{Concurring Opinions:} Justice Barrett filed a concurring opinion. Justice Jackson filed an opinion concurring in part and concurring in the judgment. Justice Thomas filed an opinion concurring in the judgment. Justice Alito filed an opinion concurring in the judgment, joined by Justices Thomas and Gorsuch.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Kagan)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Barrett)}"), N("Justice Barrett", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined the majority in full, warning", to=r"    \item \textbf{Justice Jackson", lc=True),
    N(r"\subsection{Concurring in Part and in the Judgment (Justice Jackson)}"), N("Justice Jackson", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined Parts I, II", to=r"    \item \textbf{Justice Thomas", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Thomas)}"), N("Justice Thomas", glue=" "),
    SEC("Concurring and Dissenting", frm="Joined Justice Alito in full", to=r"    \item \textbf{Justice Alito", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Alito)}"), N("Justice Alito", glue=" "),
    SEC("Concurring and Dissenting", frm="Dismissed the majority's", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Doctrinal Significance", frm=r"    \item \textbf{Remand Litigation", to=r"    \item \textbf{Supreme Court Follow-On"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Facial Challenge Fails; As-Applied Claim Succeeds): A Viewpoint-Neutrality Mandate for ``All Large Online Platforms.''}", glue=" "),
    S(r"A State enacts a statute barring ``all large online platforms'' from demoting or labeling user posts about climate policy based on viewpoint. A trade association brings a facial suit focusing solely on one member's curated newsfeed without addressing the statute's application to email providers, payment apps, or unmoderated message boards.", glue=" "),
    S(r"Under \textit{Moody}, the court must reject facial invalidation until the challenger maps the statute's full scope and proves unconstitutional applications substantially outweigh constitutional ones; however, as applied to a curated newsfeed enforcing editorial guidelines, the statute violates the First Amendment because correcting ideological balance fails even intermediate scrutiny."),
    N(r"\item \textbf{Same-Side (Unconstitutional As Applied): A Must-Carry Rule for Candidates' Posts.} A State requires video-sharing platforms to host every post by a candidate for state office and forbids them to remove, demote, or label any such post. A video platform whose published guidelines bar election misinformation brings an \emph{as-applied} challenge after the State fines it for labeling a candidate's false claim about voting dates. Under \textit{Moody}, the platform's decisions about what to include, exclude, and label in its curated feed are protected editorial judgment, just as the newspaper's choices were in \textit{Tornillo}. Compelling it to carry and present candidates' posts unaltered changes its expressive product. The State's interest in giving candidates an equal voice is the kind of rebalancing interest \textit{Moody} held cannot justify overriding private editorial choices."),
    N(r"\item \textbf{Opposite-Side (Likely Valid): Political-Affiliation Protection for Payment Apps and Messaging Conduits.}", glue=" "),
    S(r"Now suppose a State enacts a narrowly tailored statute applying \emph{solely} to private peer-to-peer payment apps and encrypted direct-messaging conduits (expressly excluding curated social-media feeds), prohibiting them from blocking financial transfers or private texts based on the sender's political affiliation, and requiring an automated one-line notice when a transaction is declined. An individual payment app brings an \emph{as-applied} challenge.", glue=" "),
    S(r"Here, the outcome flips: (1) unlike Facebook's News Feed, a neutral payment conduit or direct-messaging pipe does not compile third-party speech into an expressive product (tracking \textit{PruneYard}, \textit{FAIR}, and \textit{Moody}'s own distinction between feeds and direct messaging); (2) regulating non-expressive conduit access invokes traditional common-carrier principles rather than \textit{Tornillo}/\textit{Hurley}; and (3) a brief, automated factual notice of a declined transfer easily satisfies \textit{Zauderer} without chilling protected expression."),
    N(r"\item \textbf{Opposite-Side (Likely Valid): Protecting Ride-Share Drivers From Deactivation for Political Views.} A State law forbids ride-share companies to deactivate drivers because of political opinions they express off the app. A ride-share company sues, arguing under \textit{Moody} that the law interferes with its editorial judgment. The argument is weak. \textit{Moody}'s protection attaches to compiling and presenting third-party speech as a curated expressive product, such as a news feed. A ride-share service matches riders with drivers; deciding which drivers may use the app does not express any message, and the law does not require the company to display or endorse anyone's speech. As in \textit{PruneYard} and \textit{FAIR}, the regulated party is not engaged in its own expression, so the law is ordinary economic regulation outside \textit{Moody}'s editorial-discretion holding."),
    N(r"\item \textbf{Fence-Sitter (Open Question): A Feed Ranked Only by an Engagement Algorithm.} A State forbids platforms to rank posts on their main feeds based on the viewpoint expressed. A platform challenges the law as applied to a feed ranked entirely by an algorithm that maximizes predicted user engagement and applies no content standards or community guidelines of its own. For the platform: designing the algorithm is an editorial choice about how to present speech, and \textit{Moody} protects compiling and organizing third-party posts into a distinctive product. For the State: the Court expressly reserved feeds driven solely by user-engagement algorithms without independent content standards, and Justice Barrett questioned whether such automated sorting reflects any human expressive judgment. Because \textit{Moody} left the question open, the result is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"    \item \textbf{Holding vs.", to=r"\end{itemize}")],
  "Key Quotations":
    Q(r"``In sum, there is much work to do below on both these cases, given the facial nature of NetChoice's challenges. But that work must be done consistent with the First Amendment, which does not go on leave when social media are involved.''", "Kagan, J.")
    + Q(r"``Deciding on the third-party speech that will be included in or excluded from a compilation---and then organizing and presenting the included items---is expressive activity of its own. And that activity results in a distinctive expressive product.''", "Kagan, J.")
    + Q(r"``On the spectrum of dangers to free expression, there are few greater than allowing the government to change the speech of private actors in order to achieve its own conception of speech nirvana.''", "Kagan, J.")
    + Q(r"``The holding in these cases is narrow: NetChoice failed to prove that the Florida and Texas laws they challenged are facially unconstitutional. Everything else in the opinion of the Court is nonbinding dicta.''", "Alito, J., concurring in the judgment"),
 },
 "dropped": [
  "Case Metadata: full case name, docket numbers, cert-grant date, lower-court citations, SupremeCourt.gov slip-opinion and page-proof links (Justia and Cornell links kept).",
  "Legacy section: introductory sentence; 'Supreme Court Follow-On Cases (2025)' item (TikTok v. Garland, Free Speech Coalition v. Paxton -- they cite or echo Moody on tangential points). Kept: remand litigation item and lower-court applications of Moody's facial-challenge standard.",
  "Exam Hypotheticals: 'Analysis' and 'Opposite Side Contrast Analysis' lead-in labels (their text is reused in Examples 1 and 3).",
  "Key Quotations: the bold topic labels on each list item (the Justice part of each label is kept as the attribution).",
 ],
 "notes": ["Key Quotations rebuilt from verbatim pieces (manual_quotes list); all four quotations kept, none added. The original gives no page pin cites for these quotations, so the attribution lines carry the Justice and the Cornell LII link only; pin cites should be added in review. Attributions are emitted inside each quote block and converted by normalize_quotes.py because check_brief.py compares stems against manual_quotes.txt entries that end in .tex.",
           "Kept legacy items describe 2024--2026 lower-court events (NetChoice v. Paxton remand, NetChoice v. Uthmeier June 19, 2026 order, NetChoice v. Fitch, an October 2026 Eleventh Circuit Georgia S.B. 351 ruling); these were not verified by the drafter and should be checked in the audit."],
}

emit(__file__, FILL)
