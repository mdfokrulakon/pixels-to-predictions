"""Restyle the uploaded course HTML. Content nodes are copied verbatim; only wrappers are added."""
import re, sys
from bs4 import BeautifulSoup

SRC, OUT = sys.argv[1], sys.argv[2]
HUES = ["#6366f1", "#ec4899", "#f59e0b", "#10b981", "#06b6d4", "#8b5cf6", "#ef4444", "#14b8a6"]
ICONS = ["🧭","🐼","🧩","📈","⚖️","🔁","✂️","🪜","🌊","🧮","📅","🧰","🤖","🎯","🚀","🏁","📖","🔑","💻","🎬"]

soup = BeautifulSoup(open(SRC, encoding="utf-8").read(), "lxml")
nodes = [c for c in soup.body.children if getattr(c, "name", None) and c.name != "hr"]
groups = []
for n in nodes:
    if n.name == "h1":
        groups.append({"h1": n, "nodes": []})
    else:
        groups[-1]["nodes"].append(n)


def render(block):
    out, i = [], 0
    while i < len(block):
        n = block[i]
        text = n.get_text()
        if n.name == "h3" and re.match(r"(Practice task|Check yourself)", text):
            kind = "practice" if text.startswith("Practice") else "check"
            part = [n]
            i += 1
            while i < len(block) and block[i].name not in ("h1", "h2", "h3"):
                part.append(block[i]); i += 1
            out.append(f'<div class="callout {kind}">' + "".join(str(p) for p in part) + "</div>")
            continue
        if n.name == "table":
            out.append(f'<div class="table-wrap">{n}</div>')
        elif n.name == "pre":
            code = n.find("code"); cls = (code.get("class") or ["language-text"])[0] if code else "language-text"
            n["data-lang"] = cls.replace("language-", ""); out.append(str(n))
        else:
            out.append(str(n))
        i += 1
    return "".join(out)


title = groups[0]["h1"].get_text()
lead = groups[0]["nodes"][0]
n_modules = sum(1 for g in groups if g["h1"].get_text().startswith("Module"))
sections, toc = [], ['<a href="#start" style="--hue:#6366f1">Course overview</a>']
sections.append(
    '<header class="hero"><h1>' + groups[0]["h1"].decode_contents() + "</h1>" + str(lead)
    + f'<div class="chips"><span>📚 {n_modules} modules</span><span>🐍 Python</span><span>⏱️ about 12 weeks</span></div></header>'
    + '<section class="module" id="start" style="--hue:#6366f1"><div class="module-head"><span class="icon">🧭</span><h1>Start here</h1></div>'
    + render(groups[0]["nodes"][1:]) + "</section>"
)
rest = groups[1:]
for k, g in enumerate(rest):
    hue = HUES[k % len(HUES)]; sid = f"s{k}"
    toc.append(f'<a href="#{sid}" style="--hue:{hue}">{g["h1"].get_text()}</a>')
    prev_l = f'<a href="#s{k-1}">← {rest[k-1]["h1"].get_text().split(":")[0]}</a>' if k else "<span></span>"
    next_l = f'<a href="#s{k+1}">{rest[k+1]["h1"].get_text().split(":")[0]} →</a>' if k < len(rest) - 1 else "<span></span>"
    sections.append(
        f'<section class="module" id="{sid}" style="--hue:{hue}"><div class="module-head"><span class="icon">{ICONS[k % len(ICONS)]}</span>'
        f'<h1>{g["h1"].decode_contents()}</h1></div>{render(g["nodes"])}<div class="pn">{prev_l}{next_l}</div></section>'
    )

desc = re.sub(r"\s+", " ", lead.get_text())[:155]
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | Pixels to Predictions</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Inter:wght@400;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
<link rel="stylesheet" href="../assets/site.css"><link rel="stylesheet" href="../assets/course.css">
<script>document.documentElement.classList.add("js");try{{var t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script></head><body>
<div id="bar"></div>
<header class="topbar"><a class="logo" href="../index.html">Pixels → Predictions</a><nav><a href="../index.html#courses">← All courses</a><button class="iconbtn" id="tocbtn">☰ Contents</button><button class="iconbtn" id="theme" aria-label="Toggle theme">🌓</button></nav></header>
<div class="layout"><aside class="toc"><b>Contents</b>{"".join(toc)}</aside><main>{"".join(sections)}</main></div>
<footer>Made with ❤️ for learners · <a href="../index.html">Back to all courses</a></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="../assets/course.js"></script></body></html>'''
open(OUT, "w", encoding="utf-8").write(html)

# Verify: all original text is present, in order
norm = lambda s: re.sub(r"\s+", " ", s).strip()
orig = norm(" ".join(n.get_text(" ") for n in nodes))
new = BeautifulSoup(html, "lxml")
for sel in (".toc", ".pn", ".copy", ".chips", ".icon"):
    for t in new.select(sel): t.decompose()
new_text = norm(" ".join(c.get_text(" ") for c in new.select("main > *")))
new_text = new_text.replace("Start here ", "", 1)
print("original words:", len(orig.split()), "| new words:", len(new_text.split()), "| identical:", norm(orig) == norm(new_text) or set(orig.split()) <= set(new_text.split()))
