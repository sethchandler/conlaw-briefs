"""Fill for 246_nlrb_v_noel_canning. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/573/513/"
P = "Pedagogical"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"The Recess Appointments Clause reaches intra-session as well as inter-session recesses and vacancies that arose before the recess, but a break of fewer than 10 days is presumptively too short, and the Senate is in session when it says it is; so President Obama's January 2012 NLRB appointments, made during a three-day gap between pro forma sessions, were invalid (9--0 in judgment) (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="The D.C. Circuit vacated the NLRB order")],
  "Procedural History": [SEC("Facts and Procedural History", frm="The D.C. Circuit vacated the NLRB order")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{affirmed} the D.C. Circuit's judgment (9--0), though it divided 5--4 on the scope of the Recess Appointments Clause. The case was argued on January 13, 2014, and decided on June 26, 2014 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/12-1281}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Breyer delivered the opinion of the Court, joined by Justices Kennedy, Ginsburg, Sotomayor, and Kagan.
    \item \textbf{Concurring in the Judgment:} Justice Scalia filed an opinion concurring in the judgment, joined by Chief Justice Roberts and Justices Thomas and Alito.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Breyer)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring in the Judgment (Justice Scalia)}"), N("Justice Scalia", glue=" "),
    SEC("Concurring and Dissenting", frm="Agreed unanimously", to=r"  \item \textbf{Dissents:}", lc=True),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Appointment Invalid): Pro Forma Sessions and a Short Holiday Break.}", glue=" "),
    N(r"During an August break,", glue=" "),
    SEC(P, frm="the Senate convenes every Tuesday and Friday", to=r"\emph{Analysis:} Invalid on both", glue=" "),
    SEC(P, frm="Invalid on both counts", to=r"\end{itemize}"),
    N(r"\item \textbf{Same-Side (Agency Order Void): A Quorum That Depends on an Invalid Appointee.} During a five-day break in the middle of a session, with no pro forma sessions, the President recess-appoints a member to a three-member federal commission that needs two members for a quorum. The new member and one Senate-confirmed member then issue an order fining a shipping company. The company petitions for review, arguing that the commission lacked a quorum. Under \textit{Noel Canning}, a recess of fewer than ten days is presumptively too short, and nothing unusual justified the appointment. The appointee therefore never lawfully held office, the commission acted without a quorum, and---as with the NLRB order against Noel Canning---the order must be set aside (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Appointment Valid): An 18-Day Summer Recess.}", glue=" "),
    SEC(P, frm="A Cabinet Secretary resigns on June 1", to=r"\emph{Analysis:} Valid under", glue=" "),
    SEC(P, frm=r"Valid under \emph{Noel Canning}. Even though", to=r"  \item \textbf{Scenario B"),
    N(r"\item \textbf{Opposite-Side (Appointment Valid): The Break Between Sessions.} The Senate's first session ends on December 20, and the second session is scheduled to begin on January 5; the Senate schedules no pro forma sessions. On December 28, the President recess-appoints an ambassador to a post that has been vacant for eight months because the nomination stalled in committee. Justice Scalia's view that the vacancy must first arise during the recess would doom the appointment, but the majority's holdings sustain it: the Clause covers vacancies that already exist during the recess, and an inter-session recess of more than ten days is long enough to trigger the President's power. The appointee may serve until the end of the Senate's next session."),
    N(r"\item \textbf{Fence-Sitter (Uncertain): A Catastrophe During a Nine-Day Recess.} During a nine-day intra-session recess, a terrorist attack kills the Secretary of Homeland Security and her deputy, and the Senate cannot promptly reconvene. The President recess-appoints a new Secretary. A nine-day break is presumptively too short under \textit{Noel Canning}, but the Court left room for very unusual circumstances such as a national catastrophe, while making clear that Senate political opposition does not qualify. A court would have to decide whether the emergency truly prevented the Senate from acting and whether temporary acting officials could have filled the gap. Because the Court has never applied the exception, the outcome is uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [SEC(P, frm=r"First, \emph{Noel Canning}", to=r"\textbf{Exam Hypothetical")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: docket number, court line, Briefing Book placement, constitutional-provisions line (Justia and Cornell links kept in Judicial Votes).",
  "Separate opinions: 'Dissents: None.' item (stated in Judicial Votes).",
  "Legacy section in full: FVRA / NLRB v. SW General (statutory vacancies case that distinguished Noel Canning, not an application of its holding); post-2024 recess-appointment commentary (Volokh Conspiracy, Center for Renewing America); methodological 'liquidation' paragraph (Zivotofsky, Mazars, CFPB, Seila Law, Trump v. Slaughter) - these cite Noel Canning's historical-practice method rather than applying or limiting its Recess Appointments holding, and Trump v. Slaughter (2026) could not be verified. No Subsequent Developments subsection.",
  "Pedagogical Critiques: the bold lead-in label.",
  "Exam Hypothetical: headings and Scenario labels (both scenarios and analyses reused in Examples 1 and 3).",
 ],
 "notes": ["Neon's Scenario B (invalid) is used as Same-Side and Scenario A (valid) as Opposite-Side, matching the outcome in Noel Canning."],
}

emit(__file__, FILL)
