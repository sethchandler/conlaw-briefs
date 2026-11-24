# Constitutional Law Briefing Book: case briefs

Standalone LaTeX case briefs (247 decisions) for Seth J. Chandler's Constitutional Law Briefing Book.

| Folder | Contents |
|---|---|
| `originals/` | The 247 briefs and manifest exactly as received (`conlaw_briefs_1_247_tex_master.zip`). Never edited. |
| `briefs/` | Working set. Every brief is being brought into the Group A / case-briefer nine-section template. |
| `fills/` | Per-brief instructions used to rebuild a Group B brief: which original passages move where, plus any new text. |
| `tools/` | `assemble.py` rebuilds a brief from its fill and rejects it if any moved passage does not match the original exactly. |
| `reports/` | Conversion and audit reports. |

PDFs and zips are build products and are not stored here.

## Rebuild one brief
```
python3 tools/assemble.py originals/briefs/166_ex_parte_mccardle.tex fills/166_ex_parte_mccardle.json briefs/166_ex_parte_mccardle.tex
```
