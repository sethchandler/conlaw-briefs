# Constitutional Law Briefing Book: case briefs

Standalone LaTeX case briefs (247 decisions) for Seth J. Chandler's Constitutional Law Briefing Book.
Every brief uses the nine-section case-briefer template (Group A).

```
conlaw-briefs/
├── briefs/          247 .tex briefs: THE CURRENT VERSION (edit and build from here)
├── originals/       briefs/ + cases_manifest_247.json exactly as first received; never edited
├── book/            chapters.json (parts, chapters, topic → chapter map)
├── fills/           how each of the 97 converted Group B briefs is rebuilt
│   ├── src/         <brief>.py: which original passages go where, plus new text
│   └── <brief>.json generated from src/; read by tools/assemble.py
├── reports/
│   ├── NEW_TEXT_FOR_REVIEW.md   newly written text only, for independent review
│   ├── CONVERSION_CONCERNS.md   possible errors in the originals, flagged but not fixed
│   ├── PILOT_REPORT.md          the three-brief pilot
│   └── all_changes.diff         every change to briefs/ since the original import
└── tools/
    ├── update_briefing_book.py  builds the combined Briefing Book .tex/.pdf
    ├── preflight_audit.py       hygiene, URL and recent-case scan
    ├── assemble.py              rebuilds a converted brief from its fill (moved text verified verbatim)
    ├── check_brief.py           builds one converted brief and runs every acceptance check
    ├── fillkit.py               helpers used by fills/src/*.py
    ├── normalize_quotes.py      Group A quotation attributions
    ├── add_speakers.py          names the speaker where an original gave only a page cite
    ├── standardize_preamble.py  common preamble and title block
    ├── review_export.py         writes reports/NEW_TEXT_FOR_REVIEW.md
    ├── manual_quotes.txt        converted briefs whose fills build quotations by hand
    └── CONVERSION_GUIDE.md      rules the conversion agents followed
```

PDFs and zips are build products and are not stored here.

## Build the Briefing Book
```
cd briefs && zip -q ../conlaw_briefs_1_247_tex_master_v2.zip *.tex && cd ..
python3 tools/update_briefing_book.py --zip conlaw_briefs_1_247_tex_master_v2.zip \
    --manifest originals/cases_manifest_247.json --chapters book/chapters.json \
    --out conlaw_briefing_book_247.tex --compile
```

## Rebuild and check one converted brief
```
python3 tools/check_brief.py 166_ex_parte_mccardle
```
