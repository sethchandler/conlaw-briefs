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

## Still open (for your judgment)

- **51_gonzales_v_raich**: Inline Ilya Somin quotation ('represents the broadest assertion of congressional power ...') is a scholarly quotation not checked against the article.
- **76_lujan_v_defenders_of_wildlife**: Inline Sunstein quotation 'a prominent contemporary version of early twentieth-century substantive due process' (91 Mich. L. Rev. 163) is scholarly; the source PDF could not be downloaded, so it is unverified.
- **239_chae_chan_ping_v_united_states**: Inline 'a domain where ordinary constitutional rules have never applied' is presented as what 'critics call', with no source. The scholarly origin was not found. Consider removing the quotation marks or adding a citation.
- **17_brown_v_board_of_education_ii**: Inline 'put the proverbial fox in charge of desegregating the plaintiffs' schoolhouse', attributed to unnamed scholars (Oyez; Cardozo J. Equal Rts. & Soc. Just. article): scholarly language. The Cardozo PDF could not be fetched from this environment, so it is unverified. It is not attributed to Brown II itself.
- **107_prigg_v_pennsylvania**: Inline '[n]one of Story's three arguments will bear close scrutiny' is attributed to David Currie (scholarship). The Chicago Unbound PDF was not checked.
- **59_heart_of_atlanta_motel_v_united_states**: Inline scholarly quotation attributed to Charles L. Black Jr. (The Civil Rights Cases are cut off the same bolt of historical cloth as Plessy v. Ferguson): could not locate in an available primary source; probably from Black, Foreword: State Action, Equal Protection, and California's Proposition 14, 81 Harv. L. Rev. 69 (1967), but wording unverified.
- **129_the_civil_rights_cases**: Inline scholarly quotation attributed to Charles L. Black Jr. (The Civil Rights Cases are cut off the same bolt of historical cloth as Plessy v. Ferguson): could not locate in an available primary source; probably from Black, Foreword: State Action, Equal Protection, and California's Proposition 14, 81 Harv. L. Rev. 69 (1967), but wording unverified.
- **213_moody_v_netchoice**: Concern: NetChoice v. Uthmeier (N.D. Fla. No. 4:21-cv-220-RH) summary-judgment denial on June 19, 2026. CourtListener RECAP confirms that cross-motions for summary judgment were filed in March-April 2026 before Judge Hinkle, but I could not confirm the date or content of the ruling (or the May 2025 motion-to-dismiss denial). The sentence in Subsequent Developments should be checked against the docket or softened.
- **104_pierce_v_society_of_sisters**: Local source sources/104.json is truncated at U.S. page 535; page 536 checked through CourtListener instead.
- **127_tennessee_v_lane**: Inline 'the right result---even though for the wrong reason,' attributed to Robert A. Levy (scholarly/commentary) not verified; not attributed to the Court.
- **233_tennessee_wine_and_spirits_retailers_assn_v_thomas**: Reporter cite '152 F.4th 961' for the amended Day v. Henry opinion could not be confirmed on CourtListener (no reporter cite listed); the amended opinion itself is real (Sept. 5, 2025).
- **135_trump_v_cook**: Inline Tarullo quote '[h]istorians will be struck by the superficial nature of the Chief Justice's account' (Brookings): scholarly commentary; brookings.edu is blocked by the proxy, so it could not be checked.
- **194_home_building_v_blaisdell**: Concern 4: the Sutherland 'slippery slope' dissent bullet cites a 2026 SCOTUSblog 'SCOTUStoday for Thursday, February 12' post, which is an unlikely source for a point about the 1934 dissent. scotusblog.com is blocked by the proxy, so it could not be checked. Consider replacing the link with the official dissent pages (290 U.S. at 448--483).

## Files

- `decisions.json`: every correction with its reason, source, and decision; every item verified; restores; unresolved items.
- `quote_check_before.json`, `quote_check_after.json`: the automatic quotation check before and after.
- `recent_citations.json`: the 2024–26 citations found and how each was matched.
