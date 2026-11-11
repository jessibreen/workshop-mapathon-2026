#!/usr/bin/env bash
# Re-render everything after editing _variables.yml (and the THIS MONTH blocks in index.html).
# Needs Quarto and Chromium (or Chrome). Run from the repository root: bash scripts/build.sh
set -euo pipefail
CHROME="${CHROME:-$(command -v chromium || command -v google-chrome || echo "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")}"
ROOT="$(pwd)"

quarto render

# quarto render also runs scripts/fix_liveserver.py (see _quarto.yml), so the pages work in VS Code's Live Server.

# Print PDFs from the rendered HTML.
for f in cheat-sheet on-your-own sign-in-sheet; do
  "$CHROME" --headless ${CHROME_FLAGS:-} --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$ROOT/handouts/$f.pdf" "file://$ROOT/handouts/$f.html" 2>/dev/null
done

python3 scripts/make_guide.py

rm -f materials/mapathon-materials.zip
zip -j materials/mapathon-materials.zip handouts/cheat-sheet.pdf handouts/on-your-own.pdf
echo "Done. Check the cheat sheet is 2 pages and the sign-in sheet is 1 (landscape)."
echo "Slides PDF: open slides/slides.html?print-pdf in Chrome, then Print > Save as PDF (landscape, no margins, background graphics on)."
