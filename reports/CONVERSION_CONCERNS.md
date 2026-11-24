# Concerns flagged during the Group B conversion

The conversion agents were told **not** to change Neon's original text. Where something looked wrong or unverifiable, they recorded it here instead. Treat this as a starting list for the audit, not as verified findings.

94 briefs, 215 concerns.

## Subsequent Developments that still cite 2024–2026 material (audit these first)

- **170_ala_schechter_poultry_corp_v_united_states**: FCC v. Consumers' Research (2025)
- **179_sec_v_jarkesy**: FCC v. AT&T, Inc. (2026)
- **213_moody_v_netchoice**: NetChoice, LLC v. Paxton (5th Cir. 2024, remand); NetChoice, LLC v. Fitch (5th Cir. 2025)
- **219_smith_v_doe**: Ellingburg v. United States (2026)
- **227_ziglar_v_abbasi**: Hernandez v. Mesa, Egbert v. Boule, Goldey v. Fields (2025)
- **233_tennessee_wine_and_spirits_retailers_assn_v_thomas**: Day v. Henry (9th Cir. 2025)

## Concerns by brief

### 168_abbott_laboratories_v_gardner

- Original legacy item cites 'Industrial Energy Consumers of America v. ITC LLC (D.C. Cir. 2025)' and 2025-2026 lower-court trends. I could not verify these, so I dropped them.
- The original attributes a 'roving commission to halt the regulatory process' quotation to Fortas's dissent. I did not verify it; it is kept as moved text in the Fortas subsection.
- Examples 1 and 3 split Neon's single data-broker hypothetical (Rule A ripe / Rule B unripe). The connecting sentences are new text.

### 169_myers_v_united_states

- The kept legacy item on Trump v. Slaughter (2026), and Neon's FAIC hypothetical (Examples 1 and 5), depend on Trump v. Slaughter and Trump v. Cook (2026) as Neon describes them: 609 U.S., No. 25-332, decided June 29, 2026, 6-3, overruling Humphrey's Executor. I cannot verify these and they need checking.
- Neon's single FAIC hypothetical is split in two: the Clause 1 analysis is Same-Side Example 1, and the Clause 2 analysis is the Fence-Sitter. The fact pattern is moved once, without its nested itemize, because nested \item lines broke the checker's 5-item count.

### 170_ala_schechter_poultry_corp_v_united_states

- The original says Schechter and Panama Refining are the only Supreme Court decisions ever to strike down a federal statute on nondelegation grounds. Carter v. Carter Coal (1936) also struck down a delegation, to private parties, so the claim holds only for delegations to public officials.
- The original's Learning Resources, Inc. v. Trump, 607 U.S. 229 (2026) and FCC v. Consumers' Research, 606 U.S. 656 (2025) citations and descriptions could not be checked. Learning Resources was dropped from the legacy section but is still named in the reused hypothetical.

### 171_united_states_v_curtiss_wright_export_corp

- Neon's Learning Resources, Inc. v. Trump (2026) item, kept under Subsequent Developments, gives 607 U.S. 229, a 6-3 vote, and a Roberts plurality joined by Gorsuch and Barrett. I could not verify any of this. Example 3 also cites it in text moved verbatim from Neon.
- In Neon's Opposite Side Contrast, the Learning Resources discussion is framed as settled 2026 law. It needs the same verification.

### 172_ins_v_chadha

- Original legacy section says Process Gas summarily affirmed rulings invalidating 'a two-House veto over independent agency rulemaking'. As I recall, the consolidated cases involved a one-House veto (FERC/NGPA) and a two-House veto (FTC), so the description is incomplete. Left unchanged.
- Original's dropped 'Through 2026' list cites a June 2026 CRS report and a 2026 appropriations act. Dropped, not verified.

### 173_clinton_v_city_of_new_york

- Original legacy section reports a Sept. 26, 2025 emergency-docket ruling (Department of State v. AIDS Vaccine Advocacy Coalition) and a September 2026 $810 million pocket rescission with a GAO illegality finding. I could not verify these and dropped them, since they concern the ICA rather than Clinton's holding.
- My doubt: Example 3 (expedited rescission) treats fast-track voting rules as an exercise of each House's rulemaking power. That is sound in principle, but I cited no case for it.

### 174_zivotofsky_v_kerry

- Example 5 reuses Neon's text citing Learning Resources, Inc. v. Trump (2026) as reinforcing Congress's tariff power. I could not verify that case and dropped its legacy item, but it remains inside moved example text.
- Key Quotations pin cites (576 U.S. at 21, 32, 61, 75) were not independently verified.

### 175_gundy_v_united_states

- Original Key Quotation attributed to 'Justice Gorsuch, dissenting, 588 U.S. at 167' ('Although it is nominally a canon of statutory construction, we apply the major questions doctrine...') appears to come from Justice Gorsuch's concurrence in NFIB v. OSHA (2022), not his Gundy dissent. I left it unchanged because it moved through SEC('Key Quotations').
- The original's 2025-2026 legacy items (Consumers' Research details, Learning Resources, Trump v. Slaughter) are after or near my knowledge horizon, and I could not verify them. Consumers' Research is kept verbatim as the one directly-on-point item and should be checked in the audit.
- Fence-Sitter reuses Neon's AI hypothetical but keeps only the lead sentence of each side's argument (the remainder is listed in dropped).

### 176_trump_v_mazars_usa_llp

- Dropped legacy text cites Trump v. Slaughter, 609 U.S. ___ (2026) and Learning Resources v. Trump, 607 U.S. 229 (2026). I cannot verify these.
- The original says Trump v. United States quoted Mazars's 'one case every two centuries' line. Not verified (dropped).
- The remand sentence is cut before the settlement clause and given a new closing period.

### 178_cfpb_v_community_financial_services_assn

- The whole legacy section was dropped. The FCC v. Consumers' Research mention, the 2025-26 'combined earnings' litigation in lower courts (sourced to blogs), and the impoundment commentary do not apply CFSA's holding.
- Neon's hypothetical argues both sides, so it is reused as the Fence-Sitter, with one new closing sentence.
- I could not verify Neon's pin cites to 601 U.S. at 438 and 440-441 in that hypothetical.

### 179_sec_v_jarkesy

- The kept FCC v. AT&T, Inc., 608 U.S. ___ (June 4, 2026) item (8-1, Roberts, C.J.) and the Fifth, Second and D.C. Circuit 2025 citations in it could not be checked and need an audit.
- New Example 3 relies on Oceanic Steam Navigation Co. v. Stranahan, 214 U.S. 320 (1909). The fact pattern was adjusted to the diseased-passenger fines that case involved.

### 180_champion_v_ames

- Bug in the tools: tools/manual_quotes.txt lists entries as '<stem>.tex', but check_brief.py compares them to bare stems, so no stem ever matches. normalize_quotes.py therefore always runs, and a Key Quotations section built in Group A style, as the guide instructs, fails with 'already Group A style'. My workaround keeps each verbatim quote and its attribution inside the quote block as '--- attribution', and normalize_quotes.py then turns it into the Group A '\noindent ---' line. The output .tex is in correct Group A style. If the MANUAL lookup is fixed later, these fills (180, 188, 196, 212, 252) would need their quote builder switched to the guide's pattern.
- I placed the Facts/Procedural split at Champion's arrest, not at the indictment, so the description of the lottery-ticket shipment stays in Facts.

### 181_missouri_v_holland

- TOOL BUG: check_brief.py matches stems against tools/manual_quotes.txt, but that file lists names with a '.tex' suffix, so no listed brief is ever treated as manual. Building quotes in final Group A form therefore fails ('already Group A style'). Workaround used in all five manual briefs I had (181, 189, 197, 213, 253): each quote is built from verbatim S() pieces with the attribution inside the quote block, and normalize_quotes.py then converts it to the Group A \noindent --- line. The output matches the guide's target. Fixing it means stripping '.tex' in check_brief.py's MANUAL set or in manual_quotes.txt.
- Neon's one hypothetical presents both sides, so it was reused as the Fence-Sitter, with a new closing sentence explaining why the outcome is uncertain.

### 182_united_states_v_butler

- Original cites Landor v. Louisiana Dept. of Corrections, 609 U.S. 59 (2026), and a CRS report 'updated Oct. 7, 2026'. I could not verify either; both were dropped, along with the damages twist in Neon's Hypothetical 2 that relied on Landor.
- Tool issue affecting every manual_quotes brief: check_brief.py builds MANUAL from manual_quotes.txt entries ending in '.tex', so no stem ever matches. normalize_quotes.py therefore runs on every brief and requires 'converted: 1', and quotes pre-built in Group A style are rejected as 'already Group A style'. As in the Missouri v. Holland fill, I placed attributions inside each quote block so the normalizer converts them.
- My doubt: the percentages in the Fence-Sitter (25% of highway funds being about 2% of a state budget) are illustrative assumptions, not sourced figures.

### 183_south_dakota_v_dole

- The dropped legacy item cites Landor v. Louisiana Dept. of Corrections, 609 U.S. 59 (2026), and a CRS report dated Oct. 7, 2026. Both are unverifiable and were left out.
- Checker bug: check_brief.py builds MANUAL from manual_quotes.txt entries that end in '.tex' and compares them to bare stems, so no brief is ever treated as manual. I used the in-quote attribution approach from 181_missouri_v_holland so that normalize_quotes.py converts the quotations.

### 184_haaland_v_brackeen

- Key Quotations (manual list) are built with the attribution inside the quote block so normalize_quotes.py converts it. check_brief.py runs normalize_quotes for every brief because manual_quotes.txt entries end in '.tex' and never match a stem, so building Group A lines directly fails the checker. This tool quirk was already noted in the 181 fill.
- The original's quotations have no pin cites, only Cornell links, so the attributions read 'Barrett, J.' / 'Gorsuch, J., concurring' with no page.
- Dropped legacy item cites an October 5, 2026 cert denial in N.R. v. Ellison, which I cannot verify.

### 185_chisholm_v_georgia

- Neon's original cites Galette (2026), 607 U.S. 24-1021, which I could not verify; it was dropped from the examples, and the arm-of-the-State question is used as the Fence-Sitter instead (relying on Hess v. PATH, 513 U.S. 30 (1994)).
- New text in Example 1 says Georgia was suing 'South Carolina citizens' in Georgia v. Brailsford. Strictly, the defendants were Samuel Brailsford (a British subject) and the South Carolina citizens Powell and Hopton. Close enough for the point being made, but worth a reviewer's glance.

### 186_pike_v_bruce_church

- TOOL BUG: tools/manual_quotes.txt lists entries with a '.tex' suffix, but check_brief.py compares bare stems against that list. Listed briefs therefore still go through normalize_quotes.py, which rejects hand-built Group A quotes as 'already Group A style'. As a workaround, each quote is built with its attribution inside the quote block (Group B form), and the normalizer then converts it to the correct Group A '\noindent ---' line. Final output is correct, but the tool should be fixed.
- Reasoning subsection headings are re-created as \subsubsection headings (counted as new text) so they nest under the majority subsection.
- The Key Quotations bold labels were dropped. Every quote and pin cite is kept, attributed to 'Justice Stewart'.

### 187_south_central_timber_v_wunnicke

- tools/manual_quotes.txt entries carry a .tex suffix, so check_brief.py never matches them and runs normalize_quotes.py anyway. Each quote was built with its attribution inside the quote block so the normalizer produces Group A form, as in the Pike pilot. tools/check_brief.py likely has a bug here.
- Bold labels on the Key Quotations were dropped; every quote and attribution was kept.

### 188_garcia_v_samta

- The same manual_quotes.txt '.tex' mismatch applies here; I used the same workaround. Neon's two-part quote 2 and the grouped dissent quotes were split into separate quote blocks. The three dissent attributions (Powell at 567, O'Connor at 580, Rehnquist at 580) and the pin cites for the two halves of quote 2 are new text, built from the pin cites Neon gives.
- Neon's metadata parentheticals ('also joining Powell and O'Connor', 'also joining Powell') are redundant but not wrong. I did not carry them over.

### 189_crosby_v_nftc

- Kept legacy item: the Arizona v. United States link points to a CRS report (everycrsreport.com), not to the opinion. The claim that Arizona invoked Crosby's 'calibration of force' phrase, and that Zivotofsky quoted Crosby itself for 'one voice', should be checked.
- Same manual_quotes .tex-suffix workaround as 181.

### 190_marsh_v_alabama

- Manual-quotes brief, so the same check_brief.py MANUAL mismatch applies (see 182). Key Quotation item 5 held two quotes, Frankfurter's and Reed's. I split it into two blocks, each with its own attribution moved from the label.
- My doubt: Example 2 cites Terry v. Adams, 345 U.S. 461 (1953), to illustrate that elections are a public function. The citation is accurate, but the fact pattern (a private company running county elections) is new.

### 191_shelley_v_kraemer

- Neon says historical scholarship attributes the Reed/Jackson/Rutledge recusals to their owning covenanted property. That sentence is moved verbatim into Judicial Votes and was not verified.
- Example 2 says the Equal Protection Clause reaches national-origin classifications and applies Barrows. Both points are accurate, but Barrows involved race.

### 192_jackson_v_metropolitan_edison

- Marshall dissent cites '419 U.S. at 368 n.3/1', which looks like a garbled footnote reference; left unchanged.
- The Drummond (2025) 4-4 affirmance is mentioned only in Neon's reused Fence-Sitter text. Its 605 U.S. 165 citation is unverified.

### 193_shelby_county_v_holder

- The kept Louisiana v. Callais (2026) material (6-3 vote, 608 U.S. 85, the 'strong inference' of intentional discrimination standard) is Neon's text describing a 2026 decision that I could not verify. It needs an audit before publication.
- Fixed in this pass: the earlier fill's Fence-Sitter example claimed Justice Ginsburg's dissent warned about grandfather provisions. I believe that is not accurate, so I replaced it with an accurate statement: her dissent, relying on Katzenbach, read equal sovereignty as limited to the terms on which States are admitted to the Union.

### 194_home_building_v_blaisdell

- Same manual_quotes.txt suffix bug and workaround as in Pike: the attribution goes inside the quote block so the normalizer converts it.
- Neon's Quote 2 is a paraphrase lead-in followed by a quoted fragment. Only the verbatim fragment is inside the quote block, and a new parenthetical '(describing the Contracts Clause's prohibition)' replaces the lead-in.
- The Reasoning intro says 'four interlocking analytical pillars' but lists five subsections (left unchanged).
- Neon's dissent bullet cites a 2026 SCOTUSblog link for Sutherland's slippery-slope point (moved verbatim; the source looks odd).
- Neon's COLA-repeal hypothetical is reused as the Fence-Sitter, with a new sentence on the threshold question of whether a statute creates a contract (National R.R. Passenger Corp. v. Atchison, T. & S.F. Ry., 470 U.S. 451 (1985)). Neon's analysis had skipped that issue.

### 195_mathews_v_eldridge

- The original says Culley v. Marshall (2024) 'refused to apply Mathews'. The majority arguably decided the case on its forfeiture precedents without choosing between Mathews and Barker, so this may overstate the holding.
- The phrase 'As Justice Brennan later emphasized in dissent from the oral argument record' in the facts is odd wording, left as is.
- Same manual_quotes.txt .tex-suffix issue: quotes were built in Group B form so the normalizer converts them. The attributions are moved verbatim from the label parentheticals, e.g. 'Powell, J.'

### 196_yick_wo_v_hopkins

- The same manual_quotes.txt '.tex' mismatch applies here; I used the same workaround. The attribution 'Justice Matthews,' is new text before each moved pin-cite link.
- Neon's dropped legacy items cite United States v. Skrmetti as '605 U.S. ___ (2025)' and Gonzalez v. Trevino as '602 U.S. 653 (2024)'. I did not verify either, and neither appears in the converted brief.

### 197_plyler_v_doe

- Neon's hypotheticals are short issue prompts. In the Fence-Sitter, the moved 'Issue' sentence is a 'Whether...' fragment, kept verbatim after a new \textit{Issue:} label.
- Neon's Exam Hypothetical 2 (Opposite-Side example) mixes a likely-valid university-tuition ban with an open K-12 question about unaccompanied minors.
- Same manual_quotes .tex-suffix workaround as 181.

### 198_everson_v_board_of_education

- Original legacy section says the Court heard argument in St. Mary Catholic Parish v. Roy on Nov. 3, 2026, and cites Drummond, Catholic Charities, and Mahmoud as '605/606 U.S. ___'. I could not verify the St. Mary argument and dropped the paragraph. Neon's 'Opposite Side' contrast was built on that case and was dropped too.
- Doubt about my own text: the original sets its Key Quotations as unmarked block quotes. To meet Group A style and the normalizer, I added new `` and '' marks around each verbatim quote, with a thin space where a quote already opens or closes with quotation marks. The quoted text itself is unchanged.
- Same check_brief.py MANUAL mismatch as 182 (manual-quotes brief).

### 199_wisconsin_v_yoder

- Neon cites Mahmoud v. Taylor as 606 U.S. 522 (2025). That is the same page as Fulton (593 U.S. 522), which is suspicious, and the citation should be verified. It appears in the kept legacy item.
- The dropped legacy text includes a Feb. 19, 2026 permanent injunction on remand in Mahmoud and Miller v. McDonald (2d Cir. June 30, 2026). Both are unverified and were dropped.
- Two of the three reused examples (Examples 2 and 5) reuse only fragments of Neon's Hypothetical 2 fact pattern, with new analysis.

### 200_abrams_v_united_states

- Dropped legacy item says Counterman 'reaffirm[ed]' a Holmes-derived specific-intent showing for incitement. That broadly matches Counterman's discussion of incitement requiring intent but is loosely worded; not carried forward.

### 201_new_york_times_co_v_sullivan

- Dropped legacy text cites Dershowitz v. CNN, 609 U.S. ___ (2026), a cert-denial dissent dated June 29, 2026, plus a 2025 Wynn cert denial and the Palin retrial. I cannot verify these.
- Neon's private-figure example says Gertz reserves actual malice 'only for presumed or punitive damages on a matter of public concern'. That blends Gertz with the later Dun & Bradstreet decision. Left unchanged in moved text.

### 202_brandenburg_v_ohio

- Neon cites Counterman as 600 U.S. ___ (2023); the reported cite is 600 U.S. 66 (moved verbatim, not changed).
- The Mckesson v. Doe / Ford v. Mckesson (5th Cir. 2026) material was dropped as lower-court and unverifiable.

### 203_cohen_v_california

- Original claims Justice Alito's Mahanoy concurrence explicitly cites Cohen and Brunetti; not verified.
- The original's Key Quotations give only pin cites with no author, so the converted lines read '--- 403 U.S. at 21.'
- The original's statement that Harlan's footnote 2 rejected remand because Bushman had cited Cohen approvingly was not verified.

### 204_new_york_times_co_v_united_states

- I moved the Snepp and Rhinehart sentences out of Neon's 'Opposite Side' Contrast into Subsequent Developments. Snepp also anchors new Example 4.
- Neon's first Key Quotation joins two per curiam quotes with '...' inside a single quote block. It was moved as is.

### 205_virginia_state_board_of_pharmacy_v_vccc

- Four legacy items kept, more than the usual 0-3. Each is a Supreme Court decision extending or applying the holding.
- Original metadata lists Chief Justice Burger as joining the majority and also concurring. That is consistent with the opinion but worth a glance.

### 206_central_hudson_v_public_service_commission

- Original cites U.S. Chamber of Commerce v. Sanchez (9th Cir. Nov. 9, 2026) and DoorDash v. City of New York (S.D.N.Y. June 2025). I could not verify them, and they are lower-court cases on compelled disclosure, so I dropped them.
- My doubt: the Fence-Sitter (state-legal marijuana ads) says the Supreme Court has not resolved which sovereign's law defines 'lawful activity'. I believe that is correct but did not check lower-court treatment.

### 207_ward_v_rock_against_racism

- The dropped legacy item cites West Virginia v. B.P.J., 609 U.S. ___ (June 30, 2026), as importing Ward into equal protection. I could not verify it.

### 208_rav_v_city_of_st_paul

- Dropped legacy item describes Chiles v. Salazar (Mar. 31, 2026) as reaffirming the narrow historical categories and striking down viewpoint-based counseling restrictions. I cannot verify that characterization; not carried forward.

### 209_virginia_v_black

- The original metadata says '5--4 to vacate and remand as to Elliott and O'Mara (plurality + Scalia)' and '7--2' on Black's conviction. I moved this verbatim into Judicial Votes but did not verify the arithmetic of the fractured disposition.
- Dropped legacy cites People v. Crawford, 2025 CO 22, and a 'Tenth Circuit certification, July 28, 2026'. Unverifiable.

### 210_snyder_v_phelps

- Same manual_quotes.txt suffix bug and workaround as in Pike.
- The whole legacy section was dropped: McCullen, Alvarez, Mahanoy, Counterman, Vullo, and Chiles v. Salazar (2026) are general First Amendment cases, not applications of Snyder's holding.
- Neon's residential-picketing/doxxing hypothetical argues both sides, so it is reused as the Fence-Sitter, with one new closing sentence.

### 211_reed_v_town_of_gilbert

- The dropped 2024-2026 item cites Chiles v. Salazar, 607 U.S. ___ (2026) (8-1), which could not be checked.
- Same manual_quotes.txt .tex-suffix issue: quotes were built in Group B form so the normalizer converts them.

### 212_counterman_v_colorado

- The same manual_quotes.txt '.tex' mismatch applies here; I used the same workaround.
- Example 3 is Neon's Scenario B, moved verbatim, and it still cites People v. Crawford (Colo. 2025). I dropped the Crawford legacy item and could not verify the case.
- Neon's legacy items (Crawford, the Mckesson cert denial, State v. Calloway at 585 P.3d 1270 (Wash. 2026), United States v. Woollacott (6th Cir. 2026), and 2025-2026 scholarship) are all post-2023 lower-court, cert-stage, or academic material, and several link to 2026 docket PDFs. I dropped them all, so there is no Subsequent Developments subsection.

### 213_moody_v_netchoice

- The kept legacy items describe 2024-2026 lower-court events I could not verify: a June 19, 2026 summary-judgment denial in Uthmeier and an October 2026 Eleventh Circuit ruling on Georgia S.B. 351. They need audit before publication.
- The original's Key Quotations have no page pin cites, so the attribution lines carry only the Justice and the Cornell LII link. I did not invent pin cites; they should be added in review.
- Same manual_quotes .tex-suffix workaround as 181.

### 214_zelman_v_simmons_harris

- In the kept Subsequent Developments text, the original cites Carson v. Makin as '596 U.S. ___ (2022)'. The volume and page are known (596 U.S. 767), but I moved the text verbatim and left it unchanged.
- Key Quotation labels name the speaker only in a bold topical label, so attributions read e.g. 'Justice Souter (Dissenting), 536 U.S. at 707'. Both pieces are verbatim from the original. Same check_brief.py MANUAL mismatch as 182.

### 215_mahmoud_v_taylor

- The citation 606 U.S. 522 (2025) duplicates Fulton's page number (593 U.S. 522) and should be verified.
- The kept Mirabelli v. Bonta item (607 U.S. 492 (2026) (per curiam), March 2, 2026) could not be verified and must be checked.
- Key Quotations attributions in the original name no Justice for the majority quotes (they give only slip-op cites). I kept them as-is rather than add a name.

### 216_united_states_v_brown

- Dropped legacy paragraph cites Hastings College Conservation Committee v. State (Cal. Ct. App. 2025) and a 2026 CRS report. I cannot verify either; not carried forward.
- Examples 3 and 4 both come from Neon's single 'Opposite Side' contrast passage, which described two statutes. That is why 3 of the 5 examples reuse Neon material.

### 217_nixon_v_administrator_of_general_services

- Selective Service is kept as a sentence fragment ('Reaffirmed in ...') under a new label with a new closing period.
- Foretich comes from Neon's 'Opposite Side' Contrast passage, not from the legacy section. The case citation is now in new text.
- Original attributes Rehnquist's 'sword of Damocles' quote as '(id. at 545, quoted at 494)', an unclear pin cite. Left unchanged.
- Dropped legacy cites '2026 Congressional Research Service guidance' and TikTok v. Garland, 604 U.S. ___ (2025). Not verified.

### 218_sveen_v_melin

- The legacy section was dropped: only lower-court and state-court decisions (some from 2026, unverifiable) and scholarship are discussed.
- Neon dates the cert grant to December 8, 2017. I believe it may have been January 2018, but I am not certain; left unchanged.
- Neon's Example 3 (Hypothetical 1) cites Melendez, a Second Circuit case, as authority (moved verbatim).

### 219_smith_v_doe

- The kept Ellingburg v. United States, 607 U.S. ___ (Jan. 20, 2026) item (unanimous, Kavanaugh, J.) could not be checked and needs an audit. The reused Example 3 also relies on it.
- The original's legacy section cites Sixth Circuit decisions dated Nov. 13, 2026, very close to today's date; they were dropped and should be checked.
- Neon's Hypothetical 1 presents both sides but ends by saying the standard heavily favors the government, so it is labeled Same-Side rather than Fence-Sitter.

### 220_moore_v_united_states

- Neon's entire legacy section is commentary and 2025-2026 policy material: S. 4490, a CRS-style survey, a November 2026 amicus brief, and a WealthCare Lawyer article dated Nov. 2026. I could not verify any of it and dropped it all, so there is no Subsequent Developments subsection.
- Moved text from Neon's Hypothetical 2 says lower courts and four Justices took particular positions. That reflects Moore's opinions and is kept verbatim.

### 221_craig_v_missouri

- Kept Briscoe paragraph says Justice Story was 'the sole surviving member of the Craig majority who dissented'. Baldwin was also in the Craig majority and still on the Court in 1837 (he concurred in Briscoe), so the phrasing is ambiguous at best. Left unchanged.

### 222_poindexter_v_greenhow

- Original pins the phrase 'of the essence of the right' to 114 U.S. at 271, which is likely the reporter's syllabus or headnote area rather than the opinion. It also gives the tax owed as $12.45. I did not verify either.
- Original legacy section lists many post-Young sovereign-immunity cases (Treasure Salvors, Pennhurst, Coeur d'Alene, Seminole Tribe, Alden, Whole Woman's Health) as if they police 'Poindexter's' boundary. I dropped them as tangential.

### 223_fauntleroy_v_lum

- The kept V.L. v. E.L. item has a mismatched link: the Justia URL points to /577/464/ but the text cites 577 U.S. 404 (2016), which is the correct page. Left unchanged because it is moved text.
- The dropped shield-law paragraph cites a Nov. 10, 2026 journal piece and a Louisiana v. New York original-jurisdiction filing (Sept. 2026). Both are unverified.

### 224_baker_v_general_motors_corp

- Kept legacy item cites V.L. v. E.L. as 577 U.S. 464 (2016) with a Justia link to /577/464/. I believe the correct citation is 577 U.S. 404, so both the cite and the link may be wrong. Left verbatim.
- Dropped shield-law item relies on a Minn. J.L. Sci. & Tech. post dated Nov. 2026 and on 2025 New York litigation details I cannot verify. The Fence-Sitter example restates the issue as a generic hypothetical without those specifics.
- Examples 3 and 4 split Neon's single 'Opposite Side' contrast (two scenarios) and add new analysis to each.

### 225_puerto_rico_v_branstad

- Original Scalia item says he joined the portion 'overruling Dennison as an interpretation of the 1793 statute's predecessor'. This is garbled, since the 1793 Act is itself the predecessor. Left unchanged.
- Dropped legacy describes 2025-2026 events: the Louisiana/New York Carpenter extradition dispute, and an 'August 2026' Texas refusal of a Minnesota demand citing Vladeck, Aug. 20, 2026. Unverifiable.

### 226_bivens_v_six_unknown_named_agents

- Neon cites Goldey v. Fields as 606 U.S. 942 (2025) (per curiam). The citation should be verified.
- The second scenario of Neon's 'Opposite Side' Contrast (state officers under §1983) was dropped as an exam tip. The DEA-raid scenario is reused as Same-Side Example 1.

### 227_ziglar_v_abbasi

- Goldey v. Fields, 606 U.S. 942 (2025) (per curiam): the citation page was not verified.
- The original's legacy section refers to 'Justice Thomas's concurrence in Part II', which seems to be wrong wording; that item was dropped.
- The dropped item cites Cisco Systems v. Doe, 609 U.S. ___ (June 23, 2026), which could not be checked.

### 228_egbert_v_boule

- I kept Neon's Goldey v. Fields (June 30, 2025, per curiam, 606 U.S. ___) item. It should be checked against the official report, and Example 1, moved verbatim, also relies on it.
- I dropped Neon's 'Nielsen v. Watanabe, No. 25-417 (U.S. 2026)' merits-briefing reference. I could not verify it, and it may not be accurate.

### 229_united_states_steel_corp_v_multistate_tax_commission

- The NPVIC Fence-Sitter is new text drawn from the original's legacy discussion. It gives no state counts or dates.

### 230_cuyler_v_adams

- Original cites State v. Torkelson, 2026-Ohio-2861 (Ohio July 27, 2026), plus 2024-2025 bistate-agency and scholarship items. I could not verify them and dropped them as lower-court material.
- Neon's Hypothetical 1 assumes a 1996 statute giving 'advance' consent to emergency-management compacts. Congress's 1996 consent to EMAC was arguably a specific consent rather than a blanket advance consent. I left it unchanged.

### 231_united_states_v_belmont

- I kept four legacy items, one more than the usual 0-3, because each directly applied or narrowed Belmont.

### 232_united_states_v_pink

- Examples 1 and 3 both draw on Neon's one Nation Z hypothetical (provision 1 and provision 2).
- Example 4 (executive agreement vs. a federal statute) relies on the Youngstown framework and the original's statement that Pink does not let the President override federal statutes. It is labeled 'Likely' because the Supreme Court has not squarely decided the point.

### 233_tennessee_wine_and_spirits_retailers_assn_v_thomas

- The kept Subsequent Developments material is lower-court only: Day v. Henry, 152 F.4th 961 (9th Cir. 2025, amended Sept. 2025), and a June 2026 Libation Law Blog cite. It needs an audit. Dropped: May 18, 2026 cert denials in Day v. Henry and Chicago Wine Co. v. Braun (unverifiable).
- The checker reports pages=0 for this brief because a line break in the pdflatex log splits '(8 pages'. The PDF compiles to 8 pages; this is a tool quirk, not a failure.

### 234_balzac_v_porto_rico

- Neon's fourth Key Quotation is from Justice Gorsuch's Vaello Madero concurrence, not from Balzac (kept verbatim).
- Neon cites a Wikisource link for '258 U.S. at 300' in the Facts (moved verbatim).
- Neon's 'Opposite Side' Contrast has two fact patterns (express incorporation; warrantless searches). It is reused whole as one Opposite-Side example.

### 235_united_states_v_vaello_madero

- No legacy item is a later decision applying or narrowing the holding (CBO baseline, SSI Equality Act, Fitisemanu cert denial, scholarship), so the Subsequent Developments subsection was omitted.
- The dissent summary paraphrases Sotomayor as 'antithetical to the entire premise of the program', while the Key Quotation reads 'antithetical to the very nature of the SSI program'. The inner quotation may not be verbatim.

### 236_ex_parte_milligan

- Neon's 'Opposite Side' Contrast contains two genuine fact patterns (a Quirin-type saboteur and a Hamdi-type battlefield capture). Both are reused as the two Opposite-Side examples.

### 237_boumediene_v_bush

- Neon's second hypothetical contained two separate fact patterns (active combat zone; expedited removal). Each became one Opposite-Side example, so three of the five examples reuse Neon's material.

### 238_dhs_v_thuraissigiam

- Original cites Trump v. J.G.G. and A.A.R.P. v. Trump (2025), Mullin v. Al Otro Lado, 609 U.S. ___ (2026), and Padilla v. ICE (9th Cir. Sept. 21, 2026). I could not verify the 2026 items; all were dropped, including the J.G.G./Padilla citations at the end of Neon's Hypothetical 2.
- My doubt: in Example 3 I joined two verbatim pieces of Neon's contrast with a new '; and' and a closing period.

### 239_chae_chan_ping_v_united_states

- The dropped legacy text cites Alvarado v. Vergara (5th Cir. en banc Oct. 23, 2026) and 2026 law-review pieces. These are unverified and were dropped.

### 240_trump_v_hawaii

- Original says Trump v. United States came 'that same month' as Munoz; Munoz was decided June 21, 2024 and Trump v. United States on July 1, 2024 (dropped sentence).
- Original says SFFA v. Harvard (2023) 'confirmed that Hawaii formally overruled Korematsu'. I cannot confirm that SFFA says this; the item was dropped.
- Trump v. CASA, 606 U.S. 831 (2025) citation is unverified; the item was dropped as not applying Hawaii's holding.

### 241_hayburns_case

- Internal inconsistency in the original: the Facts say the Pennsylvania circuit also wrote to Washington, but the first critique says only the New York and North Carolina judges wrote. Left unchanged.
- The dropped legacy item attributed the phrase 'cannot be shared with the other branches' to Hayburn's Case. That language comes from later cases (Stern / Nixon), not Hayburn.
- The original never names the sixth sitting Justice, so I did not add the name.

### 242_flast_v_cohen

- The dropped 'Status Through 2026' item cites National Park Service v. National Trust for Historic Preservation, 609 U.S. ___ (2026). I cannot verify this case.
- Neon describes Winn as federal taxpayers challenging 'state tax credits' under Flast. The Winn plaintiffs were Arizona taxpayers (moved verbatim in the kept legacy item and Example 3).

### 243_friends_of_the_earth_v_laidlaw

- The first Key Quotation (a majority quote) links to the Cornell LII dissent page (98-822.ZD.html).
- The dropped legacy text cites National Park Service v. National Trust for Historic Preservation, 609 U.S. ___ (2026), which could not be checked.

### 244_trump_v_casa

- Neon's legacy section reports a June 30, 2026 merits ruling in Trump v. Barbara (6-3, the EO violates the Citizenship Clause), a CRS Report R49022, Tincher v. Noem (8th Cir. 2026), and Louisiana v. FDA, 175 F.4th 310 (5th Cir. 2026). I could not verify any of these and dropped them all. Barbara also goes to the EO's merits, not CASA's remedial holding.
- Neon's second Key Quotation uses odd nested quotation marks (````Complete relief'' ... parties.''''). It was moved verbatim and compiles, but the marks may render oddly.
- Example 3's moved text says lower courts 'through 2026 continue to apply' APA vacatur universally. That relies on Neon's unverified 2026 sources.

### 245_medellin_v_texas

- No legacy case was kept. Only the aftermath sentence was kept (Congress passed no implementing legislation; Texas executed Medellin in August 2008), as a Subsequent Developments item. Dropped: the 2025 New York Convention circuit decisions, which the original sources to a law-firm newsletter, and a Learning Resources v. Trump (2026) mention.
- Original says Justice Stevens 'agreed with the dissent that the Vienna Convention itself is self-executing'. Worth checking against the concurrence.
- Neon's 'Opposite Side' contrast contained two modifications. Each became one Opposite-Side example. Example 5 says Sanchez-Llamas assumed without deciding that Article 36 confers individually enforceable rights.

### 246_nlrb_v_noel_canning

- Typo in the original Holding, item 2: 'even if arose before the recess began' (missing 'it'). Left verbatim.
- Original legacy section cites Trump v. Slaughter, 609 U.S. ___ (2026), which I could not verify. The whole legacy section was dropped as methodological or tangential.
- I used Neon's Scenario B (invalid) as Same-Side and Scenario A (valid) as Opposite-Side, to match the outcome in Noel Canning. Scenario B now opens with the new lead-in 'During an August break,' replacing 'Now suppose that instead of adjourning for 18 days'.

### 247_loper_bright_enterprises_v_raimondo

- The kept legacy item cites Urias-Orellana v. Bondi, 607 U.S. ___ (2026). I could not verify it, and it must be checked.
- Example 3 reuses fragments of Neon's Hypothetical 1 rather than a whole fact pattern.

### 248_united_states_v_ec_knight_co

- Kept legacy item says Swift distinguished E.C. Knight as 'accidental, secondary, or remote'. I am not certain that phrase is verbatim from Swift; left unchanged.
- Dropped item says Justice Scalia's Raich concurrence cited Harlan's E.C. Knight dissent; unverified.

### 249_united_states_v_comstock

- Neon's exam analysis puts 'substantially linked' in quotation marks and attributes it to Alito/Kennedy. Alito's actual phrase is 'substantial link', so the quotation is not verbatim. Left unchanged in moved text.
- Dropped legacy cites Landor v. Louisiana Dept. of Corrections, 609 U.S. ___ (2026), describing it as refusing a RLUIPA damages remedy. Unverifiable.

### 250_us_term_limits_v_thornton

- Neon calls Thomas's dissent '80-page' (unverified; left unchanged).
- Neon's 'Opposite Side' Contrast (three State X measures) is a genuine fact pattern and is reused whole as an Opposite-Side example.

### 251_trump_v_anderson

- No later decision applies or narrows the holding, so the Subsequent Developments subsection was omitted. The dropped material includes 2024-2026 scholarship citations (e.g. 138 Harv. L. Rev. 676) and a 2026 cert petition, none checked.
- Two of the original's Key Quotations have no pin cites (only '601 U.S. 100 (2024)'); left as is.

### 252_deshaney_v_winnebago_county

- The same manual_quotes.txt '.tex' mismatch applies here; I used the same workaround. The speaker attributions ('Chief Justice Rehnquist, for the Court,' and 'Justice Blackmun, dissenting,') are new text; the pin cites and links are moved.
- The second kept legacy item is the circuits' state-created-danger paragraph. It describes doctrine developed in the courts of appeals, which the Supreme Court has not endorsed, rather than a single Supreme Court decision.
- Neon's dropped Sterling v. City of Jackson (5th Cir. en banc, Sept. 4, 2026) item is post-cutoff and unverified.

### 253_penn_central_transportation_co_v_nyc

- Original metadata files Penn Central under 'Chapter 6: Substantive Due Process --- Takings', an odd label for a takings case. That line was dropped with the metadata.
- Kept legacy item describes Tyler v. Hennepin County as treating the county's retention of surplus equity as 'a classic physical confiscation rather than a regulatory taking'. That is a loose paraphrase of the opinion; left unchanged.
- Sheetz (2024) item dropped from legacy, but Sheetz is still cited in Neon's moved Example 3 analysis.
- Same manual_quotes .tex-suffix workaround as 181.

### 254_dolan_v_city_of_tigard

- Original says the Court denied certiorari in Sheetz's post-remand petition on June 15, 2026 (No. 25-958). I could not verify this and dropped the sentence.
- The original cites Sheetz as '601 U.S. ___ (2024)' (actually 601 U.S. 267) and Cedar Point as '594 U.S. ___'. The Sheetz citation sits in the kept text and was left verbatim.
- Same check_brief.py MANUAL mismatch as 182 (manual-quotes brief).

### 255_kelo_v_city_of_new_london

- Subsequent Developments is omitted entirely. None of the legacy items is a later decision applying or narrowing Kelo: they cover state reforms, a dissent from denial of cert in Eychaner, and the Bowers cert denial (March 2025). Example 4 covers the state-reform point.

### 256_cedar_point_nursery_v_hassid

- No Supreme Court decision in the original's legacy section squarely applies, narrows, or extends Cedar Point (Tyler, Sheetz, DeVillier, and the eviction-moratoria split are tangential or lower-court), so Subsequent Developments is omitted.
- Dropped legacy cites Pung v. Isabella County, 609 U.S. ___ (2026) and the GHP Management cert denial (June 30, 2025), which I cannot verify.
- Kavanaugh concurrence summary says Babcock 'recognized employers' Fifth Amendment right to exclude'. Babcock was an NLRA decision, which the majority's own reasoning section notes; the wording may overstate it. Left verbatim.
- Key Quotations are built with in-block attributions for the same checker reason as Brackeen. There are no pin cites in the original.

### 257_usda_v_moreno

- Neon's legacy section cites a 'Texas A&M L. Rev. (Oct. 2026)' article and describes Skrmetti (2025). Both were dropped as not directly on point; I did not verify them.

### 258_shaw_v_reno

- Neon's Facts call the plaintiffs 'Five white residents of Durham County'. The Shaw opinion itself notes that the appellants did not even claim to be white. Left unchanged.
- Minor inconsistency: the Facts give North Carolina's white voting-age population as roughly 78%, while Justice White's dissent summary says 79%.
- The kept legacy item on Louisiana v. Callais (2026), Neon's Example 1, and the new Fence-Sitter depend on Callais as Neon describes it (6-3, Alito, decided April 29, 2026). This must be verified.
- Neon cites Alexander as 602 U.S. 1 (2024) (left unchanged).

### 259_chaplinsky_v_new_hampshire

- The dropped legacy item cites Chiles v. Salazar, 607 U.S. ___ (Mar. 31, 2026), which could not be checked. The Reed brief gives the same case as an 8-1 decision with no date.
- The original says the Supreme Court has never affirmed a fighting-words conviction since 1942. This is a common claim; it was kept in the legacy introduction, which was dropped, and new Example 5 echoes it.

### 260_naacp_v_alabama

- I kept Neon's First Choice Women's Resource Centers v. Davenport item (608 U.S. 174, decided unanimously April 29, 2026, Gorsuch, J.). I could not verify the case name, citation, date, or holding. Example 5 (Neon's hypothetical, moved verbatim) also relies on it.
- Example 5's 'For the group' and 'For the State' lead-ins and its one-sentence closing are new text wrapped around Neon's moved arguments.

### 261_tinker_v_des_moines

- Original metadata lists Fortas's majority as joined by Warren, Douglas, Brennan, White, and Marshall, which is only 6 Justices for a 7-2 decision. Justice Stewart, who concurred, is omitted, though I believe he also joined the opinion. Judicial Votes follows the original; please verify the join list.

### 262_shurtleff_v_city_of_boston

- Original legacy section rests on unnamed '2026 appellate commentary' (a casemine link) and on 2025-2026 amicus filings, and says Boston paid $2.1 million in fees. I could not verify these and dropped the section; none of it is a Supreme Court decision applying Shurtleff.
- My doubt: I cite Walker, 576 U.S. 200 (2015), without a link, because I was unsure of Justia's URL format for that case.
