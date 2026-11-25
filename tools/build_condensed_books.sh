#!/usr/bin/env bash
# Build the Four-, Two-, and One-Page Edition Briefing Books from condensed/<edition>/*.tex.
# Output: dist/condensed/conlaw_briefing_book_247_<edition>.{tex,pdf}
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist/condensed
for e in 4page 2page 1page; do
  case $e in 4page) N="Four-Page Edition";; 2page) N="Two-Page Edition";; 1page) N="One-Page Edition";; esac
  rm -f dist/condensed/briefs_$e.zip
  (cd condensed/$e && zip -q ../../dist/condensed/briefs_$e.zip *.tex)
  T=dist/condensed/conlaw_briefing_book_247_$e.tex
  python3 tools/update_briefing_book.py --zip dist/condensed/briefs_$e.zip \
    --manifest originals/cases_manifest_247.json --chapters book/chapters.json --out $T >/dev/null
  sed -i "s/Briefing Book (\([0-9]*\) Decisions)/Briefing Book, $N (\1 Decisions)/; s/pdftitle={Constitutional Law: Briefing Book}/pdftitle={Constitutional Law: Briefing Book, $N}/" $T
  # the book's 11pt font rebreaks lines written for 12pt; allow a little extra word spacing
  sed -i '0,/\\begin{document}/s//\\setlength{\\emergencystretch}{3em}\n\\begin{document}/' $T
  (cd dist/condensed && for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error $(basename $T) >/dev/null; done)
done
