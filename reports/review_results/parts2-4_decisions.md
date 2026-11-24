# Independent review, parts 2–4 (ChatGPT): decisions

ChatGPT proposed 159 items for briefs 191–262 (raw output in `part2_chatgpt.jsonl` … `part4_chatgpt.jsonl`).

- **Applied:** 155 corrections (25 CRITICAL, the rest MODERATE/MINOR).
- **Declined:** 3 requests to restore 2026 lower-court decisions (kept for the audit, below).
- **Handled differently:** 1 (the *Trump v. CASA* restore request; see below).

## How they were applied

Every correction is stored with its reason and source in `fills/corrections/<brief>.json`. `tools/assemble.py` applies them to the assembled brief and refuses any whose text does not appear exactly once, so they survive rebuilds. This works for both newly written text and text reused from the original drafts. All 155 applied corrections were confirmed in the final briefs, and all 97 converted briefs pass `tools/check_brief.py`.

## Checked independently before accepting

- *Chae Chan Ping*: 8–0, not 9–0 (Justice Matthews died before argument).
- *Moore v. United States*: five-Justice majority; Barrett and Alito concurred in the judgment.
- *DHS v. Thuraissigiam*: five-Justice majority; Breyer and Ginsburg concurred in the judgment.
- *Virginia v. Black*: the prima facie ruling had four votes.
- *Counterman*: vacated and remanded (not a new trial).
- Corrections that changed an example's outcome were checked against its Same-Side / Opposite-Side / Fence-Sitter label; each keeps its direction or is narrowed because the case law does not support a firmer result.

## Trump v. CASA (restore request 4.10)

ChatGPT asked to restore Neon's dropped discussion of *Trump v. Barbara* and the Ninth Circuit's *Washington v. Trump*. *Trump v. Barbara*, No. 25-365 (June 30, 2026), was verified on CourtListener: Roberts, C.J., for five Justices (Sotomayor, Kagan, Barrett, Jackson); Kavanaugh, J., concurring in the judgment and dissenting in part; Thomas, Alito, and Gorsuch, JJ., dissenting; judgment affirmed. Neon's sentence said only "6–3," so one new, precise sentence was written under Subsequent Developments instead of restoring it verbatim. *Washington v. Trump* (a lower-court ruling) was not added.

## Deferred to the audit (declined restore requests)

- **219_smith_v_doe** (3.7): Restore the dropped discussion of the November 2026 Tennessee decision. On remand from the 2024 decision cited in Example 3, the Sixth Circuit held the retroactive classification provisions nonpunitive and dismissed the geographical-restriction claims against the bureau director for lack of standing. The different treatment of classifications and geographic restrictions matters to the current application of Smith. — *Declined: asks to restore a November 2026 Sixth Circuit decision. Lower-court legacy material is kept out unless directly on point; flagged for the audit instead.*
- **238_dhs_v_thuraissigiam** (3.57): In the dropped Through 2026 item, restore Padilla v. U.S. Immigration & Customs Enforcement, 192 F.4th 894 (9th Cir. 2026), with its limited holding. It verifies that Thuraissigiam does not foreclose due process challenges to prolonged detention by noncitizens apprehended in the interior well after entry. That distinction directly supports Example 3 and does not imply a right to a new asylum interview. — *Declined: asks to restore a 2026 Ninth Circuit decision (Padilla v. ICE). Lower-court legacy material is kept out; flagged for the audit.*
- **252_deshaney_v_winnebago_county** (4.27): Restore the dropped Fifth Circuit update in corrected form. Sterling's 2025 panel opinion recognized state-created danger, but the grant of rehearing en banc vacated it. The September 2026 en banc majority affirmed dismissal without adopting the doctrine. That sequence is necessary to explain the current circuit treatment of Example 3. — *Declined: asks to restore 2025-26 Fifth Circuit rulings (Sterling). Lower-court legacy material is kept out; flagged for the audit.*

## All items

| ID | Brief | Section | Severity | Decision |
|---|---|---|---|---|
| 2.1 | 191_shelley_v_kraemer | Examples: Future Applications | CRITICAL | APPLIED |
| 2.2 | 191_shelley_v_kraemer | Examples: Future Applications | CRITICAL | APPLIED |
| 2.3 | 192_jackson_v_metropolitan_edison | Memory Jogger | MODERATE | APPLIED |
| 2.4 | 192_jackson_v_metropolitan_edison | Examples: Future Applications | MODERATE | APPLIED |
| 2.5 | 193_shelby_county_v_holder | Examples: Future Applications | MODERATE | APPLIED |
| 2.6 | 193_shelby_county_v_holder | Examples: Future Applications | CRITICAL | APPLIED |
| 2.7 | 194_home_building_v_blaisdell | Examples: Future Applications | MODERATE | APPLIED |
| 2.8 | 195_mathews_v_eldridge | Examples: Future Applications | MODERATE | APPLIED |
| 2.9 | 195_mathews_v_eldridge | Examples: Future Applications | CRITICAL | APPLIED |
| 2.10 | 196_yick_wo_v_hopkins | Examples: Future Applications | MODERATE | APPLIED |
| 2.11 | 196_yick_wo_v_hopkins | Examples: Future Applications | MODERATE | APPLIED |
| 2.12 | 197_plyler_v_doe | Examples: Future Applications | MODERATE | APPLIED |
| 2.13 | 198_everson_v_board_of_education | Examples: Future Applications | MODERATE | APPLIED |
| 2.14 | 199_wisconsin_v_yoder | Memory Jogger | MODERATE | APPLIED |
| 2.15 | 199_wisconsin_v_yoder | Examples: Future Applications | CRITICAL | APPLIED |
| 2.16 | 199_wisconsin_v_yoder | Examples: Future Applications | MODERATE | APPLIED |
| 2.17 | 200_abrams_v_united_states | Examples: Future Applications | MODERATE | APPLIED |
| 2.18 | 201_new_york_times_co_v_sullivan | Judicial Votes | MODERATE | APPLIED |
| 2.19 | 201_new_york_times_co_v_sullivan | Examples: Future Applications | MODERATE | APPLIED |
| 2.20 | 202_brandenburg_v_ohio | Examples: Future Applications | MODERATE | APPLIED |
| 2.21 | 202_brandenburg_v_ohio | Examples: Future Applications | MODERATE | APPLIED |
| 2.22 | 203_cohen_v_california | Memory Jogger | MODERATE | APPLIED |
| 2.23 | 203_cohen_v_california | Examples: Future Applications | MODERATE | APPLIED |
| 2.24 | 203_cohen_v_california | Examples: Future Applications | MODERATE | APPLIED |
| 2.25 | 204_new_york_times_co_v_united_states | Examples: Future Applications | MODERATE | APPLIED |
| 2.26 | 204_new_york_times_co_v_united_states | Examples: Future Applications | CRITICAL | APPLIED |
| 2.27 | 204_new_york_times_co_v_united_states | Examples: Future Applications | CRITICAL | APPLIED |
| 2.28 | 205_virginia_state_board_of_pharmacy_v_vccc | Examples: Future Applications | MODERATE | APPLIED |
| 2.29 | 206_central_hudson_v_public_service_commission | Memory Jogger | MODERATE | APPLIED |
| 2.30 | 207_ward_v_rock_against_racism | Memory Jogger | MODERATE | APPLIED |
| 2.31 | 207_ward_v_rock_against_racism | Examples: Future Applications | MODERATE | APPLIED |
| 2.32 | 207_ward_v_rock_against_racism | Examples: Future Applications | MODERATE | APPLIED |
| 2.33 | 208_rav_v_city_of_st_paul | Memory Jogger | MODERATE | APPLIED |
| 2.34 | 209_virginia_v_black | Memory Jogger | CRITICAL | APPLIED |
| 2.35 | 209_virginia_v_black | Judicial Votes | MODERATE | APPLIED |
| 2.36 | 209_virginia_v_black | Examples: Future Applications | MODERATE | APPLIED |
| 2.37 | 209_virginia_v_black | Examples: Future Applications | CRITICAL | APPLIED |
| 2.38 | 209_virginia_v_black | Examples: Future Applications | MODERATE | APPLIED |
| 2.39 | 210_snyder_v_phelps | Memory Jogger | CRITICAL | APPLIED |
| 2.40 | 210_snyder_v_phelps | Examples: Future Applications | CRITICAL | APPLIED |
| 2.41 | 211_reed_v_town_of_gilbert | Memory Jogger | MODERATE | APPLIED |
| 2.42 | 211_reed_v_town_of_gilbert | Examples: Future Applications | MODERATE | APPLIED |
| 2.43 | 212_counterman_v_colorado | Memory Jogger | CRITICAL | APPLIED |
| 2.44 | 212_counterman_v_colorado | Examples: Future Applications | MODERATE | APPLIED |
| 2.45 | 212_counterman_v_colorado | Examples: Future Applications | MODERATE | APPLIED |
| 2.46 | 213_moody_v_netchoice | Examples: Future Applications | MODERATE | APPLIED |
| 2.47 | 214_zelman_v_simmons_harris | Examples: Future Applications | MINOR | APPLIED |
| 2.48 | 214_zelman_v_simmons_harris | Examples: Future Applications | MODERATE | APPLIED |
| 2.49 | 215_mahmoud_v_taylor | Memory Jogger | CRITICAL | APPLIED |
| 2.50 | 215_mahmoud_v_taylor | Examples: Future Applications | MODERATE | APPLIED |
| 2.51 | 215_mahmoud_v_taylor | Examples: Future Applications | MODERATE | APPLIED |
| 3.1 | 216_united_states_v_brown | Judicial Votes | MODERATE | APPLIED |
| 3.2 | 216_united_states_v_brown | Examples: Future Applications | MODERATE | APPLIED |
| 3.3 | 216_united_states_v_brown | Examples: Future Applications | MODERATE | APPLIED |
| 3.4 | 217_nixon_v_administrator_of_general_services | Memory Jogger | MODERATE | APPLIED |
| 3.5 | 219_smith_v_doe | Examples: Future Applications | MODERATE | APPLIED |
| 3.6 | 219_smith_v_doe | Examples: Future Applications | MODERATE | APPLIED |
| 3.7 | 219_smith_v_doe | Dropped | MODERATE | Declined |
| 3.8 | 220_moore_v_united_states | Memory Jogger | CRITICAL | APPLIED |
| 3.9 | 220_moore_v_united_states | Examples: Future Applications | MODERATE | APPLIED |
| 3.10 | 220_moore_v_united_states | Examples: Future Applications | MODERATE | APPLIED |
| 3.11 | 220_moore_v_united_states | Examples: Future Applications | MODERATE | APPLIED |
| 3.12 | 221_craig_v_missouri | Judicial Votes | CRITICAL | APPLIED |
| 3.13 | 221_craig_v_missouri | Examples: Future Applications | MODERATE | APPLIED |
| 3.14 | 222_poindexter_v_greenhow | Examples: Future Applications | MODERATE | APPLIED |
| 3.15 | 223_fauntleroy_v_lum | Memory Jogger | MODERATE | APPLIED |
| 3.16 | 223_fauntleroy_v_lum | Examples: Future Applications | MODERATE | APPLIED |
| 3.17 | 224_baker_v_general_motors_corp | Examples: Future Applications | MODERATE | APPLIED |
| 3.18 | 225_puerto_rico_v_branstad | Memory Jogger | MODERATE | APPLIED |
| 3.19 | 225_puerto_rico_v_branstad | Judicial Votes | MODERATE | APPLIED |
| 3.20 | 225_puerto_rico_v_branstad | Examples: Future Applications | MODERATE | APPLIED |
| 3.21 | 226_bivens_v_six_unknown_named_agents | Memory Jogger | CRITICAL | APPLIED |
| 3.22 | 227_ziglar_v_abbasi | Examples: Future Applications | MODERATE | APPLIED |
| 3.23 | 228_egbert_v_boule | Memory Jogger | MODERATE | APPLIED |
| 3.24 | 228_egbert_v_boule | Examples: Future Applications | MODERATE | APPLIED |
| 3.25 | 228_egbert_v_boule | Examples: Future Applications | MODERATE | APPLIED |
| 3.26 | 228_egbert_v_boule | Examples: Future Applications | MODERATE | APPLIED |
| 3.27 | 229_united_states_steel_corp_v_multistate_tax_commission | Examples: Future Applications | MODERATE | APPLIED |
| 3.28 | 229_united_states_steel_corp_v_multistate_tax_commission | Examples: Future Applications | MODERATE | APPLIED |
| 3.29 | 229_united_states_steel_corp_v_multistate_tax_commission | Examples: Future Applications | MODERATE | APPLIED |
| 3.30 | 230_cuyler_v_adams | Examples: Future Applications | MODERATE | APPLIED |
| 3.31 | 230_cuyler_v_adams | Examples: Future Applications | MODERATE | APPLIED |
| 3.32 | 230_cuyler_v_adams | Examples: Future Applications | MODERATE | APPLIED |
| 3.33 | 230_cuyler_v_adams | Examples: Future Applications | MODERATE | APPLIED |
| 3.34 | 230_cuyler_v_adams | Examples: Future Applications | MODERATE | APPLIED |
| 3.35 | 231_united_states_v_belmont | Memory Jogger | CRITICAL | APPLIED |
| 3.36 | 231_united_states_v_belmont | Examples: Future Applications | MODERATE | APPLIED |
| 3.37 | 232_united_states_v_pink | Examples: Future Applications | MODERATE | APPLIED |
| 3.38 | 232_united_states_v_pink | Examples: Future Applications | MODERATE | APPLIED |
| 3.39 | 233_tennessee_wine_and_spirits_retailers_assn_v_thomas | Examples: Future Applications | MODERATE | APPLIED |
| 3.40 | 233_tennessee_wine_and_spirits_retailers_assn_v_thomas | Examples: Future Applications | MODERATE | APPLIED |
| 3.41 | 234_balzac_v_porto_rico | Examples: Future Applications | CRITICAL | APPLIED |
| 3.42 | 235_united_states_v_vaello_madero | Memory Jogger | MODERATE | APPLIED |
| 3.43 | 235_united_states_v_vaello_madero | Examples: Future Applications | MODERATE | APPLIED |
| 3.44 | 235_united_states_v_vaello_madero | Examples: Future Applications | MODERATE | APPLIED |
| 3.45 | 235_united_states_v_vaello_madero | Examples: Future Applications | MODERATE | APPLIED |
| 3.46 | 236_ex_parte_milligan | Judicial Votes | MODERATE | APPLIED |
| 3.47 | 236_ex_parte_milligan | Examples: Future Applications | MODERATE | APPLIED |
| 3.48 | 236_ex_parte_milligan | Examples: Future Applications | MODERATE | APPLIED |
| 3.49 | 236_ex_parte_milligan | Examples: Future Applications | MODERATE | APPLIED |
| 3.50 | 236_ex_parte_milligan | Examples: Future Applications | CRITICAL | APPLIED |
| 3.51 | 237_boumediene_v_bush | Memory Jogger | MODERATE | APPLIED |
| 3.52 | 237_boumediene_v_bush | Examples: Future Applications | MODERATE | APPLIED |
| 3.53 | 237_boumediene_v_bush | Examples: Future Applications | MODERATE | APPLIED |
| 3.54 | 238_dhs_v_thuraissigiam | Memory Jogger | CRITICAL | APPLIED |
| 3.55 | 238_dhs_v_thuraissigiam | Examples: Future Applications | MODERATE | APPLIED |
| 3.56 | 238_dhs_v_thuraissigiam | Examples: Future Applications | MODERATE | APPLIED |
| 3.57 | 238_dhs_v_thuraissigiam | Dropped | MODERATE | Declined |
| 3.58 | 239_chae_chan_ping_v_united_states | Judicial Votes | CRITICAL | APPLIED |
| 3.59 | 239_chae_chan_ping_v_united_states | Judicial Votes | MODERATE | APPLIED |
| 3.60 | 239_chae_chan_ping_v_united_states | Examples: Future Applications | MODERATE | APPLIED |
| 3.61 | 240_trump_v_hawaii | Memory Jogger | CRITICAL | APPLIED |
| 3.62 | 240_trump_v_hawaii | Examples: Future Applications | MODERATE | APPLIED |
| 4.1 | 241_hayburns_case | Judicial Votes | MODERATE | APPLIED |
| 4.2 | 241_hayburns_case | Examples: Future Applications | MODERATE | APPLIED |
| 4.3 | 242_flast_v_cohen | Examples: Future Applications | MODERATE | APPLIED |
| 4.4 | 242_flast_v_cohen | Examples: Future Applications | MODERATE | APPLIED |
| 4.5 | 242_flast_v_cohen | Examples: Future Applications | MODERATE | APPLIED |
| 4.6 | 243_friends_of_the_earth_v_laidlaw | Examples: Future Applications | MODERATE | APPLIED |
| 4.7 | 243_friends_of_the_earth_v_laidlaw | Examples: Future Applications | MODERATE | APPLIED |
| 4.8 | 244_trump_v_casa | Examples: Future Applications | MODERATE | APPLIED |
| 4.9 | 244_trump_v_casa | Examples: Future Applications | MODERATE | APPLIED |
| 4.10 | 244_trump_v_casa | Dropped | MODERATE | Handled differently |
| 4.11 | 245_medellin_v_texas | Examples: Future Applications | MODERATE | APPLIED |
| 4.12 | 245_medellin_v_texas | Examples: Future Applications | MODERATE | APPLIED |
| 4.13 | 245_medellin_v_texas | Examples: Future Applications | MODERATE | APPLIED |
| 4.14 | 245_medellin_v_texas | Examples: Future Applications | MODERATE | APPLIED |
| 4.15 | 246_nlrb_v_noel_canning | Memory Jogger | MODERATE | APPLIED |
| 4.16 | 247_loper_bright_enterprises_v_raimondo | Examples: Future Applications | MODERATE | APPLIED |
| 4.17 | 248_united_states_v_ec_knight_co | Memory Jogger | MODERATE | APPLIED |
| 4.18 | 248_united_states_v_ec_knight_co | Examples: Future Applications | MODERATE | APPLIED |
| 4.19 | 249_united_states_v_comstock | Examples: Future Applications | CRITICAL | APPLIED |
| 4.20 | 250_us_term_limits_v_thornton | Examples: Future Applications | MODERATE | APPLIED |
| 4.21 | 250_us_term_limits_v_thornton | Examples: Future Applications | MODERATE | APPLIED |
| 4.22 | 251_trump_v_anderson | Examples: Future Applications | MODERATE | APPLIED |
| 4.23 | 251_trump_v_anderson | Examples: Future Applications | MODERATE | APPLIED |
| 4.24 | 252_deshaney_v_winnebago_county | Memory Jogger | CRITICAL | APPLIED |
| 4.25 | 252_deshaney_v_winnebago_county | Examples: Future Applications | MODERATE | APPLIED |
| 4.26 | 252_deshaney_v_winnebago_county | Examples: Future Applications | MODERATE | APPLIED |
| 4.27 | 252_deshaney_v_winnebago_county | Dropped | MODERATE | Declined |
| 4.28 | 253_penn_central_transportation_co_v_nyc | Examples: Future Applications | MODERATE | APPLIED |
| 4.29 | 254_dolan_v_city_of_tigard | Examples: Future Applications | MODERATE | APPLIED |
| 4.30 | 254_dolan_v_city_of_tigard | Examples: Future Applications | MODERATE | APPLIED |
| 4.31 | 254_dolan_v_city_of_tigard | Examples: Future Applications | MODERATE | APPLIED |
| 4.32 | 254_dolan_v_city_of_tigard | Examples: Future Applications | MODERATE | APPLIED |
| 4.33 | 255_kelo_v_city_of_new_london | Examples: Future Applications | MODERATE | APPLIED |
| 4.34 | 256_cedar_point_nursery_v_hassid | Examples: Future Applications | MODERATE | APPLIED |
| 4.35 | 257_usda_v_moreno | Examples: Future Applications | MODERATE | APPLIED |
| 4.36 | 258_shaw_v_reno | Examples: Future Applications | MODERATE | APPLIED |
| 4.37 | 258_shaw_v_reno | Examples: Future Applications | MODERATE | APPLIED |
| 4.38 | 258_shaw_v_reno | Examples: Future Applications | MODERATE | APPLIED |
| 4.39 | 259_chaplinsky_v_new_hampshire | Examples: Future Applications | MODERATE | APPLIED |
| 4.40 | 259_chaplinsky_v_new_hampshire | Examples: Future Applications | MODERATE | APPLIED |
| 4.41 | 260_naacp_v_alabama | Memory Jogger | MODERATE | APPLIED |
| 4.42 | 260_naacp_v_alabama | Examples: Future Applications | MODERATE | APPLIED |
| 4.43 | 261_tinker_v_des_moines | Memory Jogger | MODERATE | APPLIED |
| 4.44 | 261_tinker_v_des_moines | Examples: Future Applications | CRITICAL | APPLIED |
| 4.45 | 262_shurtleff_v_city_of_boston | Memory Jogger | MODERATE | APPLIED |
| 4.46 | 262_shurtleff_v_city_of_boston | Examples: Future Applications | MODERATE | APPLIED |
