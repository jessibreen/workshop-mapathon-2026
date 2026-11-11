"""Build the Facilitator Guide from the slide notes, so slide numbers always match the deck.

Usage: python3 scripts/make_guide.py   (run from the repository root)
Reads slides/slides.qmd and instructor/guide-front.md; writes instructor/facilitator-guide.md.
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
qmd = (root / "slides" / "slides.qmd").read_text(encoding="utf8")
front = (root / "instructor" / "guide-front.md").read_text(encoding="utf8")

body = qmd.split("\n---\n", 1)[1]  # drop the YAML header
body = re.sub(r"<!--.*?-->", "", body, flags=re.S)  # skip commented-out slides and lines
slides = re.split(r"\n(?=## )", "\n" + body)
slides = [s.strip() for s in slides if s.strip().startswith("## ")]

out = [front.rstrip(), "", "## Notes for every slide", ""]
for n, s in enumerate(slides, start=1):
    title = re.sub(r"\s*\{.*\}\s*$", "", s.splitlines()[0][3:]).strip()
    title = re.sub(r"\{\{< var [^>]+>\}\}", "", title).strip()
    if not title:
        m = re.search(r"<h2[^>]*>(.*?)</h2>", s)
        title = re.sub(r"<br\s*/?>", " ", m.group(1)) if m else ""
        title = re.sub(r"\{\{< var [^>]+>\}\}", "", title).strip()
        if not title:
            e = re.search(r'<p class="eyebrow">(.*?)</p>', s)
            title = e.group(1) if e else "Untitled"
    m = re.search(r"::: notes\n(.*?)\n:::", s, re.S)
    notes = m.group(1).strip() if m else "No notes."
    out.append(f"### Slide {n}: {title}")
    out.append("")
    for para in notes.split("\n\n"):
        para = para.strip()
        for label in ("Say:", "Why:", "Watch for:"):
            if para.startswith(label):
                para = f"**{label}**" + para[len(label):]
        out.append(para)
        out.append("")

(root / "instructor" / "facilitator-guide.md").write_text("\n".join(out), encoding="utf8")
print(f"Wrote notes for {len(slides)} slides.")
