"""Fill for 211_reed_v_town_of_gilbert. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/576/155/"
FS = "Facts and Procedural History"
SO = "Concurring and Dissenting"
LG = "Doctrinal Significance"
PS = "Pedagogical Critiques"

def Q(text, attrib):
    # Attribution placed inside the quote block (Group B form) so that
    # tools/normalize_quotes.py converts it to Group A form (see notes).
    return [N(r"\begin{quote}", glue="\n"), S(text, glue="\n"),
            N("---", glue=" "), S(attrib, glue="\n"), N(r"\end{quote}")]

QUOTES = (
  Q(r"``Content-based laws---those that target speech based on its communicative content---are presumptively unconstitutional and may be justified only if the government proves that they are narrowly tailored to serve compelling state interests.''", r"Thomas, J., 576 U.S.\ at 163")
  + Q(r"``A law that is content based on its face is subject to strict scrutiny regardless of the government's benign motive, content-neutral justification, or lack of `animus toward the ideas contained' in the regulated speech.''", r"Thomas, J., 576 U.S.\ at 165")
  + Q(r"``Thus, a speech regulation targeted at specific subject matter is content based even if it does not discriminate among viewpoints within that subject matter.''", r"Thomas, J., 576 U.S.\ at 169")
  + Q(r"``The Town of Gilbert's defense of its sign ordinance---most notably, the law's distinctions between directional signs and others---does not pass strict scrutiny, or intermediate scrutiny, or even the laugh test. \dots\ This Court may soon find itself a veritable Supreme Board of Sign Review.''", r"Kagan, J., concurring in the judgment, 576 U.S.\ at 184--85")
)

FILL = {
 "sections": {
  "Memory Jogger": [N(r"A town sign code gave a church's temporary directional signs harsher size and time limits than ideological or political signs; the Court held that a law distinguishing speech on its face by subject matter, function, or purpose is content based and triggers strict scrutiny regardless of benign motive, and struck the code (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC(FS, to="After accommodation efforts failed")],
  "Procedural History": [SEC(FS, frm="After accommodation efforts failed")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{reversed and remanded} the Ninth Circuit, \textbf{9--0} in the judgment, with a \textbf{6--3} majority opinion. The case was argued on January 12, 2015, and decided on June 18, 2015 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Thomas delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Scalia, Kennedy, Alito, and Sotomayor.
    \item \textbf{Concurring Opinions:} Justice Alito filed a concurring opinion, joined by Justices Kennedy and Sotomayor. Justice Breyer filed an opinion concurring in the judgment. Justice Kagan filed an opinion concurring in the judgment, joined by Justices Ginsburg and Breyer.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Thomas)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Alito)}"), N("Justice Alito", glue=" "),
    SEC(SO, frm="Joined the majority in full", to=r"  \item \textbf{Justice Breyer", lc=True),
    N(r"\subsection{Opinion Concurring in the Judgment (Justice Breyer)}"), N("Justice Breyer", glue=" "),
    SEC(SO, frm="Joined Justice Kagan and argued", to=r"  \item \textbf{Justice Kagan", lc=True),
    N(r"\subsection{Opinion Concurring in the Judgment (Justice Kagan)}"), N("Justice Kagan", glue=" "),
    SEC(SO, frm="Warned that automatic", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    SEC(LG, frm=r"\begin{itemize}", to=r"  \item \textbf{2024--2026 Refinement"),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Content Based; Fails Strict Scrutiny): Oakridge's Topic-Based Lawn-Sign Exemptions.}", glue=" "),
    S(r"To reduce roadside clutter, the City of Oakridge bans all temporary lawn signs except (a) ``real estate'' signs (up to 12 sq.\ ft., permitted until sale), (b) ``civic festival'' signs (up to 8 sq.\ ft., permitted 14 days before an event), and (c) ``neighborhood garage sale'' signs (up to 4 sq.\ ft., permitted 24 hours before the sale). A local resident cited for posting a 10 sq.\ ft.\ sign advertising a weekend charity bake sale challenges the ordinance.", glue=" "),
    S(r"Under \textit{Reed}, the ordinance is facially content based because an inspector must classify the sign's \textit{subject matter} (real estate vs.\ civic festival vs.\ garage sale vs.\ charity bake sale) to determine permissible size and duration. Oakridge's benign anti-clutter motive is irrelevant at Step One. Under strict scrutiny, the code fails as fatally underinclusive because a 12 sq.\ ft.\ real estate sign creates as much visual clutter as a 10 sq.\ ft.\ bake-sale sign."),
    N(r"\item \textbf{Same-Side (Content Based; Fails Strict Scrutiny): A School-Zone Picketing Ban Exempting Labor Disputes.} A city bans picketing on public sidewalks within 150 feet of a school during school hours, but exempts peaceful picketing of a school involved in a labor dispute. A student protesting the school's discipline policy is arrested. Whether picketing is allowed turns entirely on its subject matter, so the ordinance is content based on its face even though it favors no viewpoint and the city's motive is to prevent disruption. Labor picketing is no less disruptive than other picketing, so the exemption is fatally underinclusive. The Court struck down an essentially identical ordinance in \textit{Police Department of Chicago v.\ Mosley}, 408 U.S.\ 92 (1972), and \textit{Reed} confirms that result."),
    N(r"\item \textbf{Opposite-Side (Content Neutral; Survives): Oakridge's Revised Ordinance.}", glue=" "),
    S(r"Oakridge repeals all topic-based categories and instead allows any non-illuminated temporary sign up to 6 sq.\ ft.\ on private residential property for up to 30 days per year, completely bans digital billboards displaying \textit{off-premises} messages (while permitting digital \textit{on-premises} signs identifying activities occurring on the same lot), and bars all private signs on city utility poles.", glue=" "),
    S(r"All three rules are facially content neutral. The size, lighting, and 30-day limits apply identically regardless of message (\textit{Reed}, Part IV; Alito concurrence). The on-/off-premises digital billboard distinction is location-based rather than topic-based under \textit{City of Austin v.\ Reagan National Advertising}, 596 U.S.\ 61 (2022), even though officials must read a sign to tell whether it refers to an on-site activity. And the evenhanded ban on utility-pole postings satisfies \textit{Taxpayers for Vincent}. Subject only to intermediate scrutiny---and assuming no illicit censorial purpose under \textit{Ward}---the revised ordinance is narrowly tailored to significant aesthetic and safety interests while leaving ample alternative channels of communication."),
    N(r"\item \textbf{Opposite-Side (Outside \textit{Reed}): The Town's Own Holiday Banners.} A town hangs its own banners on downtown light poles promoting a town-sponsored holiday festival and civic slogans, and has never opened the poles to private messages. A resident whose request to hang a banner criticizing the town council was refused argues that the town is favoring its own subject matter. \textit{Reed}'s strict-scrutiny rule governs regulations of private speech; the Free Speech Clause does not restrict the government's own expression, a point Justice Alito's concurrence expressly preserved. Because the banners are the town's speech on property it controls, choosing their content is not content discrimination against private speakers, and the refusal stands unless the town has opened the poles to private messages."),
    N(r"\item \textbf{Fence-Sitter (Close Call): A Uniform Time Limit on Event Signs.} Responding to \textit{Reed}, a city allows temporary signs advertising any one-time event, whatever its subject, to be posted no more than seven days before the event and removed within a day after it. A church argues that officials must still read a sign to know whether it advertises an event, the very feature for which Gilbert's rule was struck. The city answers that Justice Alito's concurrence, joined by two members of the six-Justice majority, listed time limits on signs advertising a one-time event as permissible, and \textit{City of Austin} rejected the view that a need to read a sign makes a rule content based. Because Justice Kagan identified this tension and the Court has not resolved it, the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS(PS, frm=r"  \item \textbf{Overbreadth", to=r"\end{enumerate}")],
  "Key Quotations": QUOTES,
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, Cornell Constitution Annotated link (Justia link kept).",
  "Legacy section: introductory sentence and '2024--2026 Refinement and Continued Bite' item (Vidal v. Elster, TikTok v. Garland, Chiles v. Salazar) - trademark, divestiture and professional-speech cases only loosely tied to Reed's holding. Kept: Barr v. AAPC and City of Austin.",
  "Exam Hypothetical 2 lead-in ('Now revise Oakridge's ordinance on the opposite side of the doctrinal line') - replaced by a new label; the fact pattern and analysis are moved verbatim.",
  "Key Quotations: the four bold quotation labels dropped; every quote and its author/pin cite kept.",
 ],
 "notes": ["tools/manual_quotes.txt entries carry a .tex suffix, so check_brief.py still runs normalize_quotes.py; each quote is rebuilt with its attribution (moved verbatim from the label parenthetical) inside the quote block so the normalizer produces the Group A form."],
}

emit(__file__, FILL)
