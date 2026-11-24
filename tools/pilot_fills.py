#!/usr/bin/env python3
"""Fills for the three pilot briefs. N() = new text; S() = verbatim source text;
SEC()/ITEMS() = verbatim slices of a Group B section. Writes fills/<stem>.json.  usage: pilot_fills.py fills/"""
import json, os, sys

def N(t, glue=None): return {"new": t, **({"glue": glue} if glue else {})}
def S(t, glue=None): return {"src": t, **({"glue": glue} if glue else {})}
def SEC(sec, frm=None, to=None, strip=None, glue=None, lc=False):
    d = {"sec": sec, **({"lcfirst": True} if lc else {})}
    if frm: d["from"] = frm
    if to: d["to"] = to
    if strip: d["strip"] = strip
    if glue: d["glue"] = glue
    return d
def ITEMS(sec, frm=None, to=None): return {"items": sec, "from": frm, "to": to}

FILLS = {}

# ---------------------------------------------------------------- McCardle
J = "https://supreme.justia.com/cases/federal/us/74/506/"
FILLS["166_ex_parte_mccardle"] = {
 "sections": {
  "Memory Jogger": [N(r"Congress may withdraw a statutory route of Supreme Court appellate jurisdiction even after a case has been argued: a unanimous Court dismissed a Reconstruction-era habeas appeal once Congress repealed the 1867 appellate provision, while noting that its older habeas jurisdiction under the Judiciary Act of 1789 remained intact (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="After a hearing, the Circuit Court remanded")],
  "Procedural History": [SEC("Facts and Procedural History", frm="After a hearing, the Circuit Court remanded")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{dismissed} the appeal for want of jurisdiction on April 12, 1869 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/74/506}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Chase delivered the opinion of a unanimous Court, joined by Justices Nelson, Grier, Clifford, Swayne, Miller, Davis, and Field (8--0).
    \item \textbf{Concurring Opinions:} None.
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
    S(r"(Historically, when the Court postponed decision in April 1868 after Congress passed the repealing statute, Justice Grier---joined by Justice Field---entered a sharp protest against the delay, warning that the Court was evading its duty to decide a case already argued; nevertheless, both Justices joined the unanimous dismissal in 1869 once the repealing statute was squarely argued.)"),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Chase)}"), SEC("Reasoning"),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Modern Jurisdiction-Stripping"),
    N(r"\item \textbf{Modern Reaffirmation:}", glue=" "),
    S(r"In \href{https://supreme.justia.com/cases/federal/us/583/16-498/}{\textit{Patchak v. Zinke}}, 583 U.S. 244 (2018), a plurality led by Justice Thomas reaffirmed \textit{McCardle} and upheld the Gun Lake Act's stripping of federal jurisdiction over pending suits relating to a specific parcel of tribal trust land, reasoning that stripping jurisdiction changes the law rather than exercising judicial power (over Chief Justice Roberts's dissent warning that targeting a single pending suit violates \textit{Klein})."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Jurisdiction Strip Upheld): Repealing a Direct-Appeal Route While Certiorari Remains.} Congress repeals a statute that allowed parties in a class of federal enforcement cases to appeal directly from a district court to the Supreme Court, makes the repeal applicable to appeals already docketed, and leaves in place the ordinary route of appeal to a court of appeals followed by certiorari. Like the 1868 Act, the repeal withdraws one statutory avenue of review in express terms without telling the Court how to decide any case. Under \textit{McCardle}'s rule that a repealed jurisdictional statute is treated as if it never existed, the pending direct appeals must be dismissed, and litigants still have another door into the Court (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Same-Side (Jurisdiction Strip Upheld): Barring Certiorari Review of Interlocutory Class-Certification Rulings.} Congress provides that the Supreme Court may not grant certiorari to review a court of appeals' decision on an interlocutory appeal from a class-certification order, but leaves full review available after final judgment. The statute regulates the timing and route of review rather than closing the Court to a category of cases, which places it comfortably within the Exceptions and Regulations Clause as \textit{McCardle} read it. The pattern matches \href{https://supreme.justia.com/cases/federal/us/518/651/}{\textit{Felker v. Turpin}, 518 U.S. 651 (1996)}, which upheld a bar on certiorari review of habeas gatekeeping orders because another route to the Court remained open."),
    N(r"\item \textbf{Opposite-Side (Strip Likely Invalid): An Outcome-Selective Strip of All Review.}", glue=" "),
    S(r"Congress enacts the ``Uniform Flag Protection Act,'' making flag burning a federal crime and adding Section 5: ``Pursuant to Article III, Section 2, the Supreme Court shall have no appellate jurisdiction, by certiorari, appeal, or original writ of habeas corpus, to review any federal or state court decision upholding a conviction under this Act, including cases currently pending.'' A defendant convicted in state court appeals to the U.S.\ Supreme Court, which already granted certiorari before Section 5 passed.", glue=" "),
    S(r"Unlike \textit{McCardle} and \textit{Felker}, Section 5 forecloses \emph{all} Supreme Court review (eliminating the \textit{Yerger} escape valve) and discriminates asymmetrically by stripping jurisdiction only over decisions \emph{upholding} convictions (raising \textit{Klein} rule-of-decision, Due Process, and First Amendment viewpoint-discrimination objections, as well as a Suspension Clause challenge to stripping habeas). Even if a court rejects the ``essential functions'' thesis under \textit{McCardle}'s plain-text rationale, Section 5 is vulnerable under external constitutional limits (First and Fifth Amendments and the Suspension Clause) and \textit{Klein}'s prohibition on Congress rigging outcomes while leaving courts open to decide in the government's favor."),
    N(r"\item \textbf{Opposite-Side (Strip Invalid): Eliminating Habeas Review for Detainees Without an Adequate Substitute.} Without suspending the writ, Congress provides that no court shall have jurisdiction to hear habeas petitions from noncitizens held as enemy combatants at a U.S. naval base abroad over which the United States exercises complete control, and substitutes only a limited military status review in which detainees cannot present exculpatory evidence gathered after the hearing. \textit{McCardle} does not save the statute: the Exceptions Clause power is subject to the Constitution's other commands, and \href{https://supreme.justia.com/cases/federal/us/553/723/}{\textit{Boumediene v. Bush}, 553 U.S. 723 (2008)}, held that a strip of this kind violates the Suspension Clause unless Congress provides an adequate substitute for habeas."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Stripping All Supreme Court Review of a Constitutional Subject.} Congress provides that the Supreme Court shall have no appellate jurisdiction, by any route, over cases challenging state laws on prayer in public schools, while leaving state courts and lower federal courts free to decide such cases. Read literally, \textit{McCardle}'s statement that the power to make exceptions ``is given by express words'' supports the statute, and the law is neutral on its face: it neither prescribes a rule of decision (\textit{Klein}) nor suspends habeas (\textit{Boumediene}). Unlike the 1868 Act, however, it leaves no alternative route to the Supreme Court and invites fifty state supreme courts to reach different answers on a federal constitutional question, squarely presenting Henry Hart's argument that exceptions may not destroy the Court's essential role in keeping federal law supreme and uniform. The Court has never decided whether Congress may close every door, so the outcome is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Broad vs.", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: argument dates, term, Chapter/Topic line, and duplicate \\url{} printouts (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory paragraph; Santos-Zacaria clear-statement discussion; 2026 Court-reform debate sentence (kept: Yerger/Felker, Klein, Boumediene, Patchak).",
  "Exam Hypothetical: 'Opposite Side Contrast' (McCardle vs. Klein) - an exam tip, not a hypothetical; its content is covered by the Klein item and Examples 3-5.",
 ],
}

# ---------------------------------------------------------------- Cooper
J = "https://supreme.justia.com/cases/federal/us/358/1/"
FILLS["167_cooper_v_aaron"] = {
 "sections": {
  "Memory Jogger": [N(r"Facing Arkansas's open defiance of \textit{Brown}, all nine Justices signed an opinion holding that disorder provoked by state officials cannot justify suspending a desegregation plan, and declaring that the Supreme Court's interpretation of the Fourteenth Amendment is ``the supreme law of the land'' binding every state official (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="On February 20, 1958")],
  "Procedural History": [SEC("Facts and Procedural History", frm="On February 20, 1958")],
  "Judicial Votes": [
    N(r"The Supreme Court unanimously \textbf{affirmed} the Eighth Circuit, 9--0, announcing its judgment in a per curiam order on September 12, 1958, and filing its full opinion on September 29, 1958 (\href{" + J + r"}{Justia}):"),
    N(r"\begin{itemize}"), N(r"\item \textbf{Opinion of the Court:}", glue=" "),
    S(r"Jointly signed by all nine Justices --- Chief Justice Earl Warren, and Justices Hugo L. Black, Felix Frankfurter, William O. Douglas, Harold H. Burton, Tom C. Clark, John M. Harlan II, William J. Brennan, Jr., and Charles E. Whittaker (the only time in Supreme Court history that every Justice personally signed the opinion of the Court)."),
    N(r"""\item \textbf{Concurring Opinion:} Justice Frankfurter filed a concurring opinion (358 U.S. at 20--26).
    \item \textbf{Dissenting Opinions:} None.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Joint Opinion of the Court}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Frankfurter)}"),
    SEC("Concurring and Dissenting", frm="Writing separately", to=r"\end{itemize}"),
    N(r"\subsection{Subsequent Developments}"),
    SEC("Doctrinal Significance", frm=r"\begin{itemize}", to=r"  \item \textbf{Judicial Supremacy vs."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Official Bound by the Court's Interpretation): A Non-Party Governor Refuses to Follow a Fourteenth Amendment Precedent.}", glue=" "),
    S(r"After the Supreme Court holds in \textit{State A v. Doe} that a state ban on a particular medical procedure violates the Fourteenth Amendment, the Governor of State B (not a party to \textit{Doe}) signs an executive order directing state prosecutors to continue enforcing State B's identical statute, declaring: ``My oath is to the Constitution, not to five Justices' mistaken reading of it; I will obey a federal court injunction directed at me, but until then I am not bound by \textit{Doe}.''", glue=" "),
    S(r"Under \textit{Cooper v. Aaron}'s strong judicial-supremacy framework, the Governor's refusal to treat the Court's Fourteenth Amendment holding as binding law violates Article VI and the Oath Clause; moreover, in any federal suit against State B's officials, lower federal courts are bound by vertical \textit{stare decisis} to enjoin enforcement immediately (and state officials face potential fee-shifting under 42 U.S.C.\ \S~1988 or loss of qualified immunity because the right is clearly established). Under a \textbf{departmentalist} view (invoking Lincoln's response to \textit{Dred Scott}), the Governor distinguishes between defying a direct court judgment (unlawful) and declining to treat a precedent involving other parties as automatically settling his independent constitutional judgment while seeking a test case to ask the Court to reconsider \textit{Doe}."),
    N(r"\item \textbf{Same-Side (No Excuse for Official Resistance): A County Clerk Stops Issuing Marriage Licenses.} After the Supreme Court holds that the Fourteenth Amendment requires States to license same-sex marriages, an elected county clerk stops issuing marriage licenses altogether, citing her personal objections and the fact that the decision arose from litigation against other States' officials. A federal court orders her to resume issuing licenses, and she refuses. Under \textit{Cooper}, the clerk acts for the State, is bound by the Court's interpretation through her Article VI oath, and cannot confine the ruling to the parties who litigated it; her disagreement, like the Arkansas officials' resistance, is no legal excuse, and continued refusal is punishable as contempt."),
    N(r"\item \textbf{Opposite-Side (Independent Judgment Permitted): A President Vetoes a Bill the Court Would Uphold.} Congress passes a bill chartering a national development bank. Supreme Court precedent establishes that Congress may charter such a bank, but the President vetoes the bill on the ground that, in his own judgment, it exceeds Congress's enumerated powers. \textit{Cooper} does not reach this situation: the veto defies no judgment and denies no right the Court has declared, and Andrew Jackson's 1832 veto of the Second Bank's recharter rested on exactly this reasoning. Even on a strong reading of \textit{Cooper}, the Court's interpretations bind officials who would act against declared constitutional rights; they do not oblige political officials to support every measure the Court has found permissible."),
    N(r"\item \textbf{Opposite-Side (No Supreme Court Interpretation to Obey): State Officials Decline to Follow Another State's District Court Ruling.} A federal district court in State C holds State C's voter-identification law unconstitutional and enjoins its enforcement. Officials in State D, which has a similar law, keep enforcing it. \textit{Cooper}'s Article VI reasoning attaches to the Supreme Court's exposition of the Constitution, not to every lower-court opinion: the State C judgment binds only the parties to that case, and its reasoning is at most persuasive authority in State D. State D's officials are not ``war[ring] against the Constitution'' by continuing to enforce their law until a court with authority over them rules."),
    N(r"\item \textbf{Fence-Sitter (Defiance or Legitimate Test Case?): A State Enacts a Law Designed to Invite Overruling.} A state legislature, persuaded that a Supreme Court precedent was wrongly decided, enacts a statute that conflicts with the precedent's core holding and openly announces that its purpose is to give the Court a vehicle to reconsider it. Read broadly, \textit{Cooper} condemns any legislator who would ``war against the Constitution'' as the Court has interpreted it, and the statute resembles the ``evasive schemes'' the Court denounced. Read alongside Justice Frankfurter's concurrence, which distinguished orderly efforts to change the law from defiance of it, the statute is a lawful request for reconsideration---the posture of the Mississippi law that led the Court to overrule \textit{Roe v. Wade} in \href{https://supreme.justia.com/cases/federal/us/597/19-1392/}{\textit{Dobbs v. Jackson Women's Health Organization}, 597 U.S. 215 (2022)}. Where testing a precedent ends and nullifying it begins remains unsettled."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Textual Slippage", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: argument dates, term, Chapter/Topic line, duplicate \\url{} printout.",
  "Legacy section: introductory paragraph; 'Judicial Supremacy vs. Departmentalism Through 2026' item (Trump v. CASA, Trump v. Barbara, 2024-25 law reviews) - tangential to Cooper. Kept: Nixon / City of Boerne item.",
  "Exam Hypothetical: 'Opposite Side Contrast' on departmentalism - repeats Critique item 1; Example 3 now covers the departmentalist side.",
 ],
}

# ---------------------------------------------------------------- West Virginia v. EPA
J = "https://supreme.justia.com/cases/federal/us/597/20-1530/"
FILLS["177_west_virginia_v_epa"] = {
 "sections": {
  "Memory Jogger": [N(r"Giving the ``major questions doctrine'' its name in a majority opinion for the first time, the Court held 6--3 that \S~111(d) of the Clean Air Act did not clearly authorize EPA's Clean Power Plan, which set carbon-dioxide limits premised on shifting electricity generation away from coal (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to=r"\textbf{Procedural History:}")],
  "Procedural History": [SEC("Facts and Procedural History", frm=r"\textbf{Procedural History:}", strip=r"\textbf{Procedural History:} ")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{reversed and remanded} by a \textbf{6--3} vote. The case was argued on February 28, 2022, and decided on June 30, 2022 (\href{" + J + r"}{Justia}; \href{https://www.law.cornell.edu/supremecourt/text/20-1530}{Cornell LII}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Chief Justice Roberts delivered the opinion of the Court, joined by Justices Thomas, Alito, Gorsuch, Kavanaugh, and Barrett.
    \item \textbf{Concurring Opinion:} Justice Gorsuch filed a concurring opinion, joined by Justice Alito.
    \item \textbf{Dissenting Opinion:} Justice Kagan filed a dissenting opinion, joined by Justices Breyer and Sotomayor.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Chief Justice Roberts)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Gorsuch)}"), N("Justice Gorsuch", glue=" "),
    SEC("Separate Opinions", frm="Framed the major", to=r"  \item \textbf{Justice Kagan", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Kagan)}"), N("Justice Kagan", glue=" "),
    SEC("Separate Opinions", frm="Criticized the majority", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    SEC("Constitutional Significance", frm=r"  \item \textbf{\href{https://supreme.justia.com/cases/federal/us/600/", to=r"  \item \textbf{\href{https://supreme.justia.com/cases/federal/us/603/"),
    SEC("Constitutional Significance", frm=r"  \item \textbf{\href{https://supreme.justia.com/cases/federal/us/607/"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (Rule Likely Invalid): Repurposing a 1974 Biosecurity Statute to License Frontier AI.}", glue=" "),
    S(r"In 1974, Congress enacted the Federal Biosecurity Preparedness Act, authorizing the Secretary of Health and Human Services to ``promulgate such standards and systems as the Secretary determines necessary to prevent catastrophic biological threats.'' For fifty years, HHS used the statute only to set lab-containment protocols for federal research facilities. Following a major public debate in which Congress repeatedly failed to pass a bill regulating artificial intelligence, the Secretary invokes the 1974 Act to issue a rule requiring every U.S. technology company training a frontier AI model above a specified compute threshold to obtain a federal license and submit model weights to HHS for biosecurity red-teaming, at an estimated industry compliance cost of \$18 billion per year.", glue=" "),
    S(r"Challengers have a textbook major-questions claim: (1) an unheralded, transformative expansion of authority discovered in a 50-year-old statute used only for physical labs; (2) vast economic (\$18 billion/year) and political significance; (3) a stark mismatch between HHS's public-health mission and comprehensive licensing of the frontier AI sector; and (4) conspicuous congressional failure to enact AI licensing legislation. Under Roberts/Gorsuch, ``standards and systems'' is an ``empty vessel'' lacking clear congressional authorization; under Barrett/Kagan, even ordinary text-in-context interpretation makes it implausible that Congress hid a national AI-licensing regime inside a 1974 lab-safety clause."),
    N(r"\item \textbf{Same-Side (Rule Likely Invalid): Using Ratemaking Authority to Phase Out Coal.} Relying on its decades-old authority to ensure that wholesale electricity rates are ``just and reasonable,'' a federal energy commission declares that any rate charged by a coal-fired plant after 2035 is unjust and unreasonable, effectively requiring every such plant to retire. As in \textit{West Virginia}, the agency would be using a long-standing, general provision to restructure the Nation's electricity mix---a decision of vast economic and political significance that Congress has debated without acting. Absent clear congressional authorization, a court applying the major questions doctrine would likely hold that the ratemaking provision does not reach so far (\href{" + J + r"}{Justia})."),
    N(r"\item \textbf{Opposite-Side (Rule Likely Valid Under the Statute): Clear Congressional Authorization for AI Licensing.} Return to the biosecurity hypothetical, but suppose", glue=" "),
    S(r"Congress in 2025 enacted the Artificial Intelligence Safety Act expressly granting a newly created AI Safety Agency authority to ``license and audit frontier AI models exceeding $10^{26}$ FLOPs to mitigate chemical, biological, radiological, or cyber risks,'' and the Agency sets detailed red-teaming standards under that statute. Here, the \textit{major questions doctrine does not defeat the rule}: Congress spoke clearly, the action sits squarely in the agency's core mission and expertise, and the statute is contemporaneous rather than an old ``backwater.'' Any challenge must therefore shift from statutory major-questions review to a constitutional \textit{nondelegation} claim---which, after \textit{FCC v. Consumers' Research}, 606 U.S. 656 (2025), will fail so long as Congress supplied an ``intelligible principle'' setting the general policy and boundaries of delegated authority."),
    N(r"\item \textbf{Opposite-Side (Doctrine Likely Not Triggered): A Traditional, Source-Specific Standard Under \S~111(d).} EPA issues \S~111(d) emissions guidelines for existing power plants based on control technology that each plant can install on site, so that every regulated plant can comply by operating more cleanly rather than by shifting generation elsewhere. That is the inside-the-fenceline, technology-based approach EPA had always used under \S~111(d), so the rule claims no ``unheralded'' power and the major questions doctrine likely does not apply. Challengers would instead have to argue under ordinary statutory standards---for example, that the technology is not ``adequately demonstrated'' or is unreasonably costly. \textit{West Virginia} itself expressly declined to decide whether \S~111(d) is limited to such measures."),
    N(r"\item \textbf{Fence-Sitter (Close Call): Mandatory Climate-Risk Disclosure by Public Companies.} Invoking its general authority to require disclosures ``necessary or appropriate in the public interest or for the protection of investors,'' the Securities and Exchange Commission requires public companies to report their greenhouse-gas emissions and climate-related financial risks. On one hand, disclosure rules sit within the agency's core expertise and long-standing practice, and the rule regulates what companies tell investors rather than how they produce energy. On the other hand, it imposes large compliance costs on a politically charged subject that Congress has not addressed, and it can be characterized as climate policy pursued through securities law. Whether a court treats the rule as an ordinary exercise of disclosure authority (as Justice Barrett's contextual reading of the doctrine in \textit{Biden v. Nebraska} might) or as a major question demanding clear authorization (as Justice Gorsuch's clear-statement approach might) could decide the case."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"  \item \textbf{Substantive Canon", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: consolidated docket numbers, Chapter/Topic line, SupremeCourt.gov page-proof link (Justia and Cornell links kept in Judicial Votes).",
  "Legacy section: introductory paragraph; Loper Bright / FCC v. Consumers' Research item (Consumers' Research still cited in Example 3). Kept: Biden v. Nebraska and Learning Resources v. Trump items.",
  "Exam hypothetical heading 'Major Questions Analysis (West Virginia / Nebraska / Learning Resources)' and 'Opposite Side Contrast' label (their text is reused in Examples 1 and 3).",
 ],
 "notes": ["Kept Learning Resources v. Trump (2026) item is post-June-2026-cutoff for the drafter of this pass; it must be verified first in the audit."],
}

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in FILLS.items():
    json.dump(v, open(os.path.join(out, k + ".json"), "w"), indent=1)
print("wrote", len(FILLS))
