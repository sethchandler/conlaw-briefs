# Audit of the original drafts against primary sources

Covers what the earlier reviews did not: quotations and pin cites in all 247 briefs, the 2024–26 citations (current and dropped), and the 215 concerns raised during conversion.

## Method

1. **Official text for every case** (`tools/audit/fetch_sources.py`): Library of Congress and GovInfo U.S. Reports PDFs, Supreme Court preliminary prints and slip opinions, 246 of 247 cases (*Corfield v. Coryell*, a circuit-court case, was checked on CourtListener).
2. **Automatic quotation check** (`tools/audit/check_quotes.py`): every Key Quotation and every inline quotation of eight or more words matched against the case's own opinion, distinguishing scan (OCR) noise from real wording differences, and Key Quotation pin cites checked against the official page.
3. **2024–26 citations** (`tools/audit/recent_cites.py`): Supreme Court decisions checked against the Court's own decision lists; the rest reviewed.
4. **Eight review agents** worked every flagged item against the sources (opinion text, CourtListener, Cornell, supremecourt.gov) and proposed exact find/replace corrections. Each correction was validated (exact, unique text; no headings or example labels touched) before it was applied; converted briefs carry theirs in `fills/corrections/`, so rebuilds keep them.

## Results

- **Corrections applied: 147** (19 moderate, 128 minor; none critical). By type: quote 65, pin 40, fact 16, attribution 13, recent_case 9, other 4.
- **Items checked and found correct:** 655 (most automatic flags were scan noise, footnotes interrupting a quotation, running heads, or a passage also printed in the syllabus).
- **Restored 2024–26 Supreme Court decisions** (each squarely applies or limits the brief's case; written fresh from the verified opinion): *Landor v. Louisiana Dept. of Corrections* (2026) in *South Dakota v. Dole*; *Chiles v. Salazar* (2026) in *Reed v. Town of Gilbert*; *Trump v. Cook* (2026) in *Myers v. United States*. Declined: *West Virginia v. B.P.J.* in *Ward* (it borrows *Ward*'s fit principle for an equal-protection case). Every other dropped citation was a lower-court ruling, a cert-stage order, scholarship, or a false hit.

### Key Quotations (1,155), automatic check before and after

| | Before | After |
|---|---|---|
| Verified word for word | 935 | 959 |
| Wording flags | 109 | 98 |
| Not found in the case's own opinion | 111 | 98 |
| Pin cites confirmed on the official page | 696 | 727 |
| Pin cites flagged | 33 | 21 |

The remaining flags were each reviewed: they are quotations correctly drawn from another printing (e.g., a concurrence printed with a companion case), passages that also appear in the syllabus or are quoted back in a separate opinion, scan noise in older volumes, or explicit slip-opinion page cites.

## Notable errors fixed

- Quotations that were not the Court's words: *Dred Scott* (the Reporter's headnote quoted as Taney), *Yick Wo* and *Trump v. Hawaii* (syllabus quoted as opinion), *Mahmoud* phrase in *Yoder* (syllabus), *Christian Legal Society* (a sentence attributed to Justice Kennedy that is not in the opinion), *Myers* (a Holmes sentence not in his dissent), *Brown II* (a paraphrase of *Alexander v. Holmes County* in quotation marks).
- Quotations credited to the wrong case: *Katzenbach v. McClung* concurrences (printed in *Heart of Atlanta*), Justice White's "raw judicial power" (*Doe v. Bolton*, not *Roe*), Justice Fortas in *Abbott* (*Gardner v. Toilet Goods*), Justice Fortas in *Duncan* (*Bloom v. Illinois*), *Craig v. Missouri* (Justice Story's paraphrase in *Briscoe* quoted as Marshall).
- Overstatements: *Schechter* (not the only nondelegation invalidations — *Carter Coal*), *Emilee Carpenter* in *303 Creative*, *Culley v. Marshall* in *Mathews*, *New York v. United States* in *Luther v. Borden*.
- Pin cites corrected against the official pages (e.g., *McDonald*, *Boumediene*, *Bakke*, *Comstock*, *Thuraissigiam*) and missing pins added (*Moody*, *Trump v. Anderson*, *West Virginia v. EPA*, *Rucho*).

## Formerly open items: resolved by instruction (Nov. 25, 2026)

At Seth Chandler's direction, every unverified item was removed or revised:

- Unverified scholarly quotations deleted: Ilya Somin (*Raich*), Cass Sunstein (*Lujan*, quoted clause only), the "proverbial fox" (*Brown II*; the verified Brown II phrase "primary responsibility" kept), David Currie (*Prigg*), Charles L. Black Jr. (*Heart of Atlanta*; *The Civil Rights Cases*, quoted clause only), Robert A. Levy (*Tennessee v. Lane*), Daniel Tarullo (*Trump v. Cook*).
- *Chae Chan Ping*: quotation marks removed from the unsourced phrase "a domain where ordinary constitutional rules have never applied."
- Unverified non-quotations: the June 19, 2026 summary-judgment ruling in *NetChoice v. Uthmeier* deleted (*Moody*); the unconfirmed reporter cite "152 F.4th 961" for *Day v. Henry* removed and the link pointed to the amended opinion (*Tennessee Wine*); an off-point SCOTUSblog link replaced with a cite to Sutherland's dissent, 290 U.S. at 448–483 (*Blaisdell*).
- *Pierce v. Society of Sisters*: no change needed (the note concerned the downloaded source file, not the brief).

## Files

- `decisions.json`: every correction with its reason, source, and decision; every item verified; restores; unresolved items.
- `quote_check_before.json`, `quote_check_after.json`: the automatic quotation check before and after.
- `recent_citations.json`: the 2024–26 citations found and how each was matched.
