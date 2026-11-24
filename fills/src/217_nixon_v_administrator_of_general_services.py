"""Fill for 217_nixon_v_administrator_of_general_services. See tools/fillkit.py."""
from fillkit import *

J = "https://supreme.justia.com/cases/federal/us/433/425/"
CD = "Concurring and Dissenting"
FILL = {
 "sections": {
  "Memory Jogger": [N(r"After Watergate, Congress seized former President Nixon's papers and tapes for archival screening; the Court held 7--2 that the Act was not a bill of attainder (Nixon was a legitimate ``class of one'' and was not punished) and did not violate separation of powers, presidential privilege, privacy, or association rights (\href{" + J + r"}{Justia}).")],
  "Detailed Case Facts": [SEC("Facts and Procedural History", to="On December 20, 1974, Nixon sued")],
  "Procedural History": [SEC("Facts and Procedural History", frm="On December 20, 1974, Nixon sued")],
  "Judicial Votes": [
    N(r"The Supreme Court \textbf{affirmed} the three-judge District Court by a \textbf{7--2} vote. The case was argued on April 20, 1977, and decided on June 28, 1977 (\href{" + J + r"}{Justia}):"),
    N(r"""\begin{itemize}
    \item \textbf{Majority Opinion:} Justice Brennan delivered the opinion of the Court, joined in full by Justices Stewart, Marshall, and Stevens; by Justice White in all but Part VII; by Justice Powell in all but Parts IV and V; and by Justice Blackmun as to Part VII.
    \item \textbf{Concurring Opinions:} Justice Stevens filed a concurring opinion. Justices White, Blackmun, and Powell each filed an opinion concurring in part and concurring in the judgment.
    \item \textbf{Dissenting Opinions:} Chief Justice Burger and Justice Rehnquist each filed a dissenting opinion.
\end{itemize}"""),
  ],
  "Holding": [N(r"\textbf{Questions Presented:}"), SEC("Issue"), N(r"\textbf{Holding:}", glue=" "), SEC("Holding")],
  "Analysis of Opinions": [
    N(r"\subsection{Majority Opinion (Justice Brennan)}"), SEC("Reasoning"),
    N(r"\subsection{Concurring Opinion (Justice Stevens)}"), N("Justice Stevens", glue=" "),
    SEC(CD, frm="Joined the majority opinion but stressed", to=r"  \item \textbf{Justice White", lc=True),
    N(r"\subsection{Opinion Concurring in Part and in the Judgment (Justice White)}"), N("Justice White", glue=" "),
    SEC(CD, frm="Joined all but Part VII, relying", to=r"  \item \textbf{Justice Blackmun", lc=True),
    N(r"\subsection{Opinion Concurring in Part and in the Judgment (Justice Blackmun)}"), N("Justice Blackmun", glue=" "),
    SEC(CD, frm="Joined Part VII and largely agreed", to=r"  \item \textbf{Justice Powell", lc=True),
    N(r"\subsection{Opinion Concurring in Part and in the Judgment (Justice Powell)}"), N("Justice Powell", glue=" "),
    SEC(CD, frm="Joined all but Parts IV and V;", to=r"  \item \textbf{Chief Justice Burger", lc=True),
    N(r"\subsection{Dissenting Opinion (Chief Justice Burger)}"), N("Chief Justice Burger", glue=" "),
    SEC(CD, frm="Condemned the decision", to=r"  \item \textbf{Justice Rehnquist", lc=True),
    N(r"\subsection{Dissenting Opinion (Justice Rehnquist)}"), N("Justice Rehnquist", glue=" "),
    SEC(CD, frm="Focused on separation of powers and executive", to=r"\end{itemize}", lc=True),
    N(r"\subsection{Subsequent Developments}"),
    N(r"\begin{itemize}"),
    N(r"\item \textbf{Bill of Attainder Test Reaffirmed:}", glue=" "),
    S(r"Reaffirmed in \href{https://supreme.justia.com/cases/federal/us/468/841/}{\textit{Selective Service System v. Minnesota Public Interest Research Group}}, 468 U.S. 841 (1984)", glue=""),
    N(r"."),
    N(r"\item \textbf{A Targeted Statute That Failed \textit{Nixon}'s Test:} The D.C. Circuit applied \textit{Nixon} in \href{https://law.justia.com/cases/federal/appellate-courts/F3/351/1198/525998/}{\textit{Foretich v.\ United States}}, 351 F.3d 1198 (D.C. Cir.\ 2003).", glue=" "),
    S(r"There, Congress passed the Elizabeth Morgan Act---narrowly drafted so it applied only to a single notorious D.C. custody dispute---stripping Dr. Eric Foretich of parental visitation rights without a judicial finding of abuse. Applying \textit{Nixon}, the D.C. Circuit invalidated the statute as an unconstitutional bill of attainder: unlike the PRMPA's compensated archival custody, the Act imposed a severe, permanent deprivation of parental rights disproportionate to any nonpunitive purpose (failing the functional test) and rested on legislative condemnation of Foretich as an abuser (failing the motivational test)."),
    N(r"\item \textbf{Presidential Records and Former-President Privilege:}", glue=" "),
    S(r"Congress promptly enacted the Presidential Records Act of 1978, 44 U.S.C. \S\S~2201--2209, vesting public ownership of official presidential records in the United States. Decades later, \textit{Nixon}'s rule that an incumbent President's waiver of executive privilege outweighs a former President's objection proved decisive in \textit{Trump v. Thompson}, 20 F.4th 10 (D.C. Cir. 2021), \textit{stay denied}, 595 U.S. \_\_\_ (2022), permitting the National Archives to release January 6 White House records to Congress."),
    N(r"\end{itemize}"),
  ],
  "Examples: Future Applications": [
    N(r"\begin{enumerate}"),
    N(r"\item \textbf{Same-Side (No Bill of Attainder): A Procurement Ban Naming One Company.}", glue=" "),
    S(r"Suppose Congress enacts a statute naming ``Apex AI Corp.'' and (a) prohibiting federal agencies from contracting with Apex due to documented foreign-intelligence vulnerabilities", glue=""),
    N(r". Under \textit{Nixon},", glue=" "),
    S(r"provision (a) likely survives all three punishment prongs as prophylactic procurement regulation", glue=""),
    N(r": declining to buy from a vendor is not a traditional attainder sanction, the ban reasonably serves the nonpunitive goal of protecting federal systems, and a record of documented security risks shows regulatory concern rather than legislative condemnation. Like Nixon, Apex may be a legitimate class of one if it alone presents the identified risk."),
    N(r"\item \textbf{Same-Side (No Bill of Attainder): Securing One Official's Records.} After a former Cabinet secretary leaves office, Congress learns that she conducted official business on a private email server and that her personal attorney plans to delete messages. Congress passes a statute naming her and directing the National Archives to take custody of the server, have career archivists separate official from personal messages, return personal messages to her, and pay just compensation for any property taken. As in \textit{Nixon}, she is a legitimate class of one because only her records face imminent destruction; custody and screening are not traditional punishments; the statute furthers the nonpunitive goal of preserving public records; and the compensation and return provisions negate any inference of punitive confiscation."),
    N(r"\item \textbf{Opposite-Side (Bill of Attainder): Uncompensated Forfeiture Amid Condemnation.} Suppose the same statute also contains a provision", glue=" "),
    S(r"(b) forfeiting all of Apex's U.S. patents to the Treasury without compensation after floor speeches branding Apex's founders ``traitors.''", glue=" "),
    N(r"Under \textit{Nixon},", glue=" "),
    S(r"provision (b) fails both the historical test (uncompensated punitive confiscation) and the motivational/functional tests", glue=""),
    N(r", much as the Elizabeth Morgan Act failed in \textit{Foretich}. Unlike the PRMPA, which provided just compensation and served evidence-preservation goals, the forfeiture is a severe deprivation that does nothing to address the security risk and rests on legislative condemnation."),
    N(r"\item \textbf{Opposite-Side (Separation-of-Powers Problem): Congress Takes the Records Itself.} Congress passes a statute transferring custody of a departing President's records to a House committee, which may review and publish any record it chooses, including privileged national-security advice. The incumbent President, who supports the outgoing President's privilege claims, objects. \textit{Nixon} upheld the PRMPA because the records stayed under Executive Branch control, screening was done by career archivists, Congress received no privileged access, and the incumbent supported the law. Each of those features is missing here. A court applying \textit{Nixon}'s disruption test would likely find that the statute prevents the Executive Branch from protecting confidential communications without an overriding need to justify it."),
    N(r"\item \textbf{Fence-Sitter (Unresolved): Waiver by a Hostile Successor.}", glue=" "),
    S(r"Suppose a newly elected President waives executive privilege over a predecessor's candid Oval Office national-security memos so a congressional committee can publish them, despite no active criminal trial or pending legislation. Students should analyze whether \textit{Nixon}'s diminished-weight rule for former Presidents (\href{https://supreme.justia.com/cases/federal/us/433/425/}{433 U.S. at 449}) controls, or whether Justice Blackmun's hostile-transition warning and modern Article II formalism (\textit{Trump v. Mazars}; \textit{Trump v. United States}) demand heightened judicial scrutiny.", glue=" "),
    N(r"The incumbent's support favors disclosure under \textit{Nixon}, but unlike in \textit{Nixon}, publication rather than archival screening is at stake and no evidentiary need is present, so the outcome is genuinely uncertain."),
    N(r"\end{enumerate}"),
  ],
  "Critique": [ITEMS("Pedagogical", frm=r"\item \textbf{Retreat from", to=r"\end{itemize}")],
  "Key Quotations": [SEC("Key Quotations")],
 },
 "dropped": [
  "Case Metadata: case name, lower-court citation (in Procedural History), Chapter Placement, Cornell Constitution Annotated link.",
  "Legacy section: lead-in sentence; remainder of attainder item (2026 CRS guidance, ACORN, Kaspersky, TikTok v. Garland applications); final sentence on tension with Trump v. United States. Kept: Selective Service reaffirmation (fragment), Presidential Records Act and Trump v. Thompson sentences, and the Foretich application moved from the Contrast passage.",
  "'Opposite Side' Contrast: Foretich intro sentence (its substance moved to Subsequent Developments).",
  "Exam Hypothetical 1: the 'cf. Kaspersky; TikTok' and 'cf. Foretich' parentheticals (split into Examples 1 and 3); hypothetical headings.",
 ],
 "notes": [],
}

emit(__file__, FILL)
