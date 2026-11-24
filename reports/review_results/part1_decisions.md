# Independent review, part 1 of 4 (ChatGPT): decisions

ChatGPT's corrections are in `part1_chatgpt.jsonl`. Each was applied to the brief's fill file (`fills/src/`), so rebuilds keep it, and every corrected brief was rechecked with `tools/check_brief.py` (20 of 20 pass).

| # | Brief | Severity | Decision |
|---|---|---|---|
| 0 | 166_ex_parte_mccardle | MODERATE | APPLIED |
| 1 | 166_ex_parte_mccardle | MODERATE | APPLIED |
| 2 | 167_cooper_v_aaron | MODERATE | APPLIED |
| 3 | 168_abbott_laboratories_v_gardner | MODERATE | APPLIED |
| 4 | 169_myers_v_united_states | CRITICAL | APPLIED WITH CHANGES |
| 5 | 170_ala_schechter_poultry_corp_v_united_states | CRITICAL | APPLIED |
| 6 | 171_united_states_v_curtiss_wright_export_corp | MODERATE | REJECTED |
| 7 | 172_ins_v_chadha | MODERATE | APPLIED |
| 8 | 172_ins_v_chadha | MODERATE | APPLIED |
| 9 | 172_ins_v_chadha | MODERATE | APPLIED |
| 10 | 174_zivotofsky_v_kerry | CRITICAL | APPLIED |
| 11 | 174_zivotofsky_v_kerry | CRITICAL | APPLIED |
| 12 | 174_zivotofsky_v_kerry | CRITICAL | APPLIED |
| 13 | 175_gundy_v_united_states | MODERATE | APPLIED |
| 14 | 176_trump_v_mazars_usa_llp | MODERATE | APPLIED |
| 15 | 176_trump_v_mazars_usa_llp | MODERATE | APPLIED WITH CHANGES |
| 16 | 178_cfpb_v_community_financial_services_assn | MODERATE | APPLIED |
| 17 | 179_sec_v_jarkesy | MODERATE | APPLIED |
| 18 | 181_missouri_v_holland | MODERATE | APPLIED |
| 19 | 181_missouri_v_holland | MODERATE | APPLIED |
| 20 | 183_south_dakota_v_dole | MODERATE | APPLIED |
| 21 | 183_south_dakota_v_dole | MODERATE | APPLIED |
| 22 | 184_haaland_v_brackeen | MODERATE | APPLIED |
| 23 | 184_haaland_v_brackeen | CRITICAL | APPLIED |
| 24 | 184_haaland_v_brackeen | MODERATE | APPLIED |
| 25 | 185_chisholm_v_georgia | MODERATE | APPLIED |
| 26 | 185_chisholm_v_georgia | MODERATE | APPLIED |
| 27 | 185_chisholm_v_georgia | CRITICAL | APPLIED |
| 28 | 185_chisholm_v_georgia | MODERATE | RESTORED |
| 29 | 186_pike_v_bruce_church | MODERATE | APPLIED |
| 30 | 186_pike_v_bruce_church | MODERATE | APPLIED |
| 31 | 187_south_central_timber_v_wunnicke | MODERATE | APPLIED |
| 32 | 187_south_central_timber_v_wunnicke | MODERATE | APPLIED |
| 33 | 188_garcia_v_samta | MODERATE | APPLIED |
| 34 | 189_crosby_v_nftc | MODERATE | APPLIED |

## Corrections not applied exactly as proposed

**#4 169_myers_v_united_states** (APPLIED WITH CHANGES)

- ChatGPT: Myers invalidated a Senate-consent requirement for removal of an executive postmaster. Illimitable elevates the opinion's broader reasoning into a universal holding and overlooks surviving limits.
- Action: exclusive power to remove executive officers he appoints with Senate consent---here, a first-class postmaster---so Congress could not require the Senate's consent to the removal

**#6 171_united_states_v_curtiss_wright_export_corp** (REJECTED)

- ChatGPT: The Court's closely analogous decision bears directly on the speech claim while leaving the delegation and the direct ban on these facts open.
- Action: Rejected: the example is built to test Curtiss-Wright's external/internal distinction; the replacement drops that framing and adds a 2025 case (TikTok v. Garland). The example stays as written.

**#15 176_trump_v_mazars_usa_llp** (APPLIED WITH CHANGES)

- ChatGPT: The legitimate-legislative-purpose inquiry also tests the relation between the information sought and the legislative purpose. The hypothetical supplies no link between the personal accounts and the bill.
- Action: If the committee can show how the executive's accounts bear on the bill---for example, on the compensation or risk practices it is considering regulating---that deferential test is likely satisfied.

**#28 185_chisholm_v_georgia** (RESTORED)

- ChatGPT: Restore the discussion of Galette. It supplies the current Supreme Court framework for deciding whether a state-created corporation is an arm of the State, including the weight given to separate incorporation, formal liability, subsidies, and control.
- Action: Galette sentence moved back verbatim from the original as a Subsequent Developments item.

## Checks made before deciding

- *Galette v. New Jersey Transit Corp.*, No. 24-1021 (Mar. 4, 2026): confirmed on CourtListener. Justice Sotomayor for the Court; a state-created corporation that can sue and be sued and is liable for its own judgments is presumptively not an arm of the State, and state control "does not meaningfully affect" that. The old *Chisholm* fence-sitter, built on the *Hess* factors, was no longer a close call.
- *Chisholm v. Georgia* decision date: CourtListener gives February 19, 1793, agreeing with ChatGPT's sources.
- *Zivotofsky v. Kerry*: five Justices joined the recognition-power rationale; Justice Thomas concurred in the judgment in part on different grounds.
