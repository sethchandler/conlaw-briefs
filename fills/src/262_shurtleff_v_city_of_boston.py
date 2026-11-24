"""Fill for 262_shurtleff_v_city_of_boston. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/596/20-1800/"
P = "Pedagogical"
CD = "Concurring and Dissenting"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"Boston had approved 284 straight private requests to fly flags on a City Hall flagpole but refused Camp Constitution's Christian flag; the Court held 9--0 that, because Boston did not actively control the flags' messages, the program was private speech, and the refusal was unconstitutional viewpoint discrimination (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="Shurtleff and Camp Constitution sued")],
  "Procedural History": [SEC("Facts and Procedural History", frm="Shurtleff and Camp Constitution sued")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{reversed and remanded} (9--0). The case was argued on January 18, 2022, and decided on May 2, 2022 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/20-1800}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Breyer delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Sotomayor, Kagan, Kavanaugh, and Barrett.
    \item \textbf{Concurring Opinions:} Justice Kavanaugh filed a concurring opinion. Justice Alito filed an opinion concurring in the judgment, joined by Justices Thomas and Gorsuch. Justice Gorsuch filed an opinion concurring in the judgment, joined by Justice Thomas.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Breyer)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Kavanaugh)}"), N("Justice Kavanaugh", glue=" "),
    SEC(CD, frm="Emphasized in a brief concurrence", to=r"  \item \textbf{Justice Alito", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Alito)}"), N("Justice Alito", glue=" "),
    SEC(CD, frm="Rejected the \\textit{Summum}", to=r"  \item \textbf{Justice Gorsuch", lc=True),
    N(r"\subsection{Concurring in the Judgment (Justice Gorsuch)}"), N("Justice Gorsuch", glue=" "),
    SEC(CD, frm="Traced Boston's error", to=r"\end{itemize}", lc=True),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Private Speech; Exclusion Invalid): The Library's Community Heritage Wall.}", glue=" "),
    SEC(P, frm="A municipal library installs", to=r"\textit{Analysis:}", glue=" "),
    SEC(P, frm=r"Under \textit{Shurtleff}, a self-serving written disclaimer", to=r"\textbf{``Opposite Side'' Contrast:}"),
    N(r"\item \textbf{Same-Side (Private Speech; Exclusion Invalid): Holiday Displays in the Town Green.} For fifteen years a town has issued a permit to any resident group that asks to place a seasonal display on its town green in December, without reviewing designs; it has approved nativity scenes, menorahs, and a local scout troop's snowman. When an atheist association applies to erect a sign celebrating the winter solstice and questioning religious belief, the town refuses, saying the sign is offensive. As in \textit{Shurtleff}, history alone cannot carry the day when the town has exercised no meaningful control over the displays' messages, so the green hosts private speech. Rejecting one group's display because of its views on religion is viewpoint discrimination that the Free Speech Clause forbids (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Government Speech): A Closed-List Flag Policy.} After \textit{Shurtleff}, a city adopts a written policy that its third flagpole will fly only the city flag or flags chosen by city council resolution to express the city's own messages, and it stops accepting applications from private groups. A religious group later asks to raise its flag and is refused. The policy is the kind of change Justice Breyer said nothing prevented Boston from making: the city now actively selects and controls every flag, the public has no access to the pole, and the history of flags at seats of government already favors the city. The flags are government speech, so the Free Speech Clause does not require the city to accept the group's flag."),
    N(r"\item \textbf{Opposite-Side (Government Speech): Actively Reviewed Specialty License Plates.} A state motor-vehicle board reviews every proposed specialty license-plate design, routinely rejects designs it finds inconsistent with state messaging, and owns the designs it approves. The board rejects a proposed plate bearing an advocacy group's political slogan. Under \textit{Walker v.\ Texas Div., Sons of Confederate Veterans, Inc.}, 576 U.S.\ 200 (2015), which \textit{Shurtleff} distinguished, plates are traditionally used to convey state messages, observers associate them with the State, and the board actively controls their content. All three factors point to government speech, so the board may reject the design without satisfying viewpoint neutrality."),
    N(r"\item \textbf{Fence-Sitter (Close Call): A Juried Public Mural Program.} A city invites artists to propose murals for the walls of city-owned buildings. A city arts commission reviews each proposal for artistic quality and site compatibility and has approved about 90 percent of them, but it has no written guidelines on content. It rejects a proposal featuring religious imagery. The commission's review is more active than Boston's rubber stamp, and murals on public buildings may be read as the city's own message, which points toward government speech under \textit{Summum}. Yet the high approval rate, the absence of content standards, and the program's open invitation resemble \textit{Shurtleff}'s come-one-come-all forum. Because \textit{Shurtleff}'s holistic inquiry gives no fixed weight to each factor, the result could go either way."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC(P, frm=r"\begin{itemize}", to=r"\textbf{Exam Hypothetical:}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, Chapter/Topic line, SupremeCourt.gov slip-opinion link (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section in full: 'Curbing Government-Speech Expansion' item (Boston's post-decision fee payment and policy change; unnamed 2026 appellate commentary on closed-list flag resolutions) and 'Foreshadowing Kennedy v. Bremerton' item (Kennedy abandoned Lemon but did not apply Shurtleff's government-speech holding; Cambridge Christian School and 2026 amicus filings are pending-litigation materials). No Supreme Court decision applying or limiting Shurtleff's holding is described; no Subsequent Developments subsection.",
  "Exam Hypothetical: 'Opposite Side' Contrast (Shurtleff vs. Summum and Walker) - a comparison of decided cases, not a hypothetical; its content is reflected in Examples 3--5.",
 ],
}

emit(__file__, FILL)
