"""Make rendered HTML safe for VS Code's Live Server.

Live Server adds its reload script at the first </body> (or </head>) it finds.
Quarto's self-contained slides carry reveal.js's speaker-view page inside a
script, so its </body> and </head> come before the real ones, and Live Server's
script lands inside that code and breaks the page. Inside a script, "<\\/body>"
means the same as "</body>", so this rewrites every copy except the real tags:
the first </head> and the last </body>.

Runs automatically after `quarto render` (post-render in _quarto.yml).
By hand: python3 scripts/fix_liveserver.py slides/slides.html handouts/*.html
"""
import os
import sys
from pathlib import Path

def fix(text, tag, keep):
    parts = text.split(tag)
    if len(parts) <= 2:
        return text, 0
    n = len(parts) - 1
    keep_i = 0 if keep == "first" else n - 1
    out = parts[0]
    for i in range(n):
        out += (tag if i == keep_i else tag.replace("</", "<\\/")) + parts[i + 1]
    return out, n - 1

paths = sys.argv[1:] or [
    p for p in os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").split("\n") if p.endswith(".html")
]
for path in paths:
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    s, a = fix(s, "</head>", "first")
    s, b = fix(s, "</body>", "last")
    if a or b:
        p.write_text(s, encoding="utf-8")
    print(f"{path}: escaped {a} </head> and {b} </body> inside scripts")
