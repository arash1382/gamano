# -*- coding: utf-8 -*-
"""Generate the HTML edition: one self-contained file + an html/assets bundle."""
import os, sys, base64, io, zipfile, html as H
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from en.content import (CRITERIA, PRODUCTS, PERSONAS, PERSONA_FIT, FINDINGS, WEIGHTED,
                        RANK, LANDSCAPE, PROFILES_EXTRA, ADJACENT, ACCESS,
                        COLOUR_NOTE, LAYOUT_MODELS, PRACTICE_ANATOMY, DASHBOARD_MODELS)
from en.ux import UX, ORDER

S = os.path.join(ROOT, "assets", "screens")
C = os.path.join(ROOT, "assets", "crops")
OUT_HTML = "/home/user/Roshana_Visual_UXUI_Benchmark_EN.html"
BUNDLE = "/home/user/Roshana_Benchmark_EN_html_assets.zip"

BY = {p["key"]: p for p in PRODUCTS}
SHORT = {"discovery": "Discovery", "practice": "Practice", "feedback": "Feedback",
         "progress": "Progress", "dashboard": "Dashboard", "teacher": "Teacher",
         "visual": "Visual", "mobile": "Mobile"}
MAXW = 1000

_cache = {}
_rel = {}


def data_uri(path):
    key = path
    if key in _cache:
        return _cache[key]
    im = Image.open(path)
    if im.mode != "RGB":
        im = im.convert("RGB")
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    _cache[key] = uri
    _rel[uri] = "assets/screens/" + os.path.basename(path)
    return uri


def esc(t):
    return H.escape(str(t))


def fig(fname, caption, tag, src, folder=S):
    path = os.path.join(folder, fname)
    if not os.path.exists(path):
        return ""
    uri = data_uri(path)
    cls = "real" if tag.upper().startswith("REAL") else "schem"
    return f'''
<figure>
  <img src="{uri}" alt="{esc(caption)}">
  <figcaption><span class="tag {cls}">{esc(tag.upper())}</span> {esc(caption)}
  <span class="src">Source: {esc(src)} &middot; accessed {ACCESS}</span></figcaption>
</figure>'''


def table(header, rows, cls=""):
    head = "".join("<th>%s</th>" % esc(h) for h in header)
    body = ""
    for r in rows:
        body += "<tr>" + "".join("<td>%s</td>" % esc(c) for c in r) + "</tr>"
    return '<table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (cls, head, body)


CSS = """
:root{--ink:#16203a;--ink2:#3b4457;--muted:#6e7583;--coral:#e4572e;--teal:#1b8a83;
--soft:#f5f2e9;--line:#e2ded2;--paper:#fff}
*{box-sizing:border-box}
body{margin:0;background:#efede6;color:var(--ink);
font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Helvetica,Arial,sans-serif;
-webkit-font-smoothing:antialiased}
.wrap{max-width:1040px;margin:0 auto;padding:0 28px 90px;background:var(--paper);
box-shadow:0 0 60px rgba(20,25,40,.10)}
header.cover{background:var(--ink);color:#fff;margin:0 -28px 0;padding:64px 56px 48px}
.kick{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:#f0a58f;font-weight:700}
h1{font-size:46px;line-height:1.06;letter-spacing:-.02em;margin:14px 0 12px;font-weight:800}
header.cover p{color:#c9cfdd;max-width:62ch;margin:0 0 18px;font-size:16.5px}
.meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.meta span{border:1px solid rgba(255,255,255,.25);border-radius:999px;padding:5px 13px;
font-size:12px;color:#e7eaf2}
nav.toc{display:flex;flex-wrap:wrap;gap:8px;padding:22px 0 6px;border-bottom:1px solid var(--line)}
nav.toc a{font-size:12.5px;color:var(--ink2);text-decoration:none;border:1px solid var(--line);
border-radius:999px;padding:5px 12px}
nav.toc a:hover{border-color:var(--teal);color:var(--teal)}
section{padding-top:44px}
.sechead{display:flex;align-items:baseline;gap:14px;border-top:3px solid var(--ink);padding-top:12px}
.sechead .num{font-size:12px;font-weight:800;letter-spacing:.16em;color:var(--coral)}
h2{font-size:31px;line-height:1.14;letter-spacing:-.01em;margin:6px 0 6px;font-weight:800}
.sub{color:var(--muted);font-size:15px;margin:0 0 26px}
h3{font-size:18px;margin:28px 0 6px;font-weight:700}
h4{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);margin:20px 0 4px}
p{margin:0 0 12px;color:var(--ink2);max-width:78ch}
ul{margin:6px 0 14px;padding-left:20px;color:var(--ink2)}
li{margin-bottom:5px}
table{border-collapse:collapse;width:100%;margin:14px 0 24px;font-size:13.5px}
th{background:var(--soft);text-align:left;font-size:12px;letter-spacing:.05em;text-transform:uppercase;
color:#4a5162;padding:9px 10px;border-bottom:1px solid var(--line)}
td{padding:8px 10px;border-bottom:1px solid #efeee8;color:var(--ink2);vertical-align:top}
tr:hover td{background:#fbfaf6}
.small td,.small th{font-size:12.5px}
figure{margin:18px 0 26px}
figure img{width:100%;border:1px solid var(--line);border-radius:6px;display:block}
figcaption{font-size:12.5px;color:var(--muted);margin-top:8px;line-height:1.5}
figcaption .src{display:block;font-size:11.5px;color:#9aa0ac;margin-top:2px}
.tag{display:inline-block;font-size:10px;font-weight:800;letter-spacing:.09em;padding:2px 7px;
border-radius:4px;color:#fff;margin-right:6px;vertical-align:1px}
.tag.real{background:var(--teal)}
.tag.schem{background:var(--coral)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin:16px 0 26px}
.card{background:var(--soft);border-radius:8px;padding:16px 18px;border:1px solid var(--line)}
.card h5{margin:0 0 6px;font-size:14px;letter-spacing:.04em;text-transform:uppercase;color:#5a6070}
.card .big{font-size:30px;font-weight:800;letter-spacing:-.02em;color:var(--coral);line-height:1.1}
.card p{font-size:13.5px;margin:6px 0 0}
.callout{border-left:4px solid var(--coral);background:#fbf1ec;padding:14px 18px;border-radius:0 8px 8px 0;
margin:22px 0 8px;font-weight:600;color:#7a3320;font-size:15px}
.note{border-left:3px solid var(--teal);padding:10px 16px;background:#f2f8f7;border-radius:0 8px 8px 0;
font-size:14px;color:#295c58;margin:16px 0}
.persona{border:1px solid var(--line);border-radius:8px;padding:16px 18px;margin:14px 0}
.persona .who{font-weight:800;font-size:16px;margin-bottom:2px}
.persona .age{font-size:12px;color:var(--muted);letter-spacing:.06em;text-transform:uppercase}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.stack{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
.mini{font-size:13px;color:var(--muted)}
footer{margin-top:56px;border-top:1px solid var(--line);padding:20px 0 0;font-size:12px;color:var(--muted)}
a{color:var(--teal)}
@media(max-width:720px){header.cover{padding:40px 26px 34px;margin:0 -28px}h1{font-size:32px}
.two,.stack{grid-template-columns:1fr}.wrap{padding:0 18px 60px}}
@media print{body{background:#fff}.wrap{box-shadow:none;max-width:none}
section{page-break-inside:avoid}figure{page-break-inside:avoid}}
"""


def build():
    b = []
    a = b.append
    a('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
    a('<meta name="viewport" content="width=device-width, initial-scale=1">')
    a('<title>Roshana - Visual UX/UI Competitive Benchmark (English)</title>')
    a("<style>%s</style></head><body><div class='wrap'>" % CSS)

    # cover
    a('''<header class="cover">
<div class="kick">Roshana / Product design research</div>
<h1>Visual UX/UI<br>Competitive Benchmark</h1>
<p>How eight learning products design discovery, practice, feedback, progress and the teacher's next
action - and what Roshana should adopt, redesign or reject.</p>
<div class="meta"><span>English edition</span><span>8 products</span><span>8 weighted criteria</span>
<span>4 Roshana personas</span><span>Data collected %s</span></div>
</header>''' % ACCESS)

    a('<nav class="toc">')
    for sid, label in [("method", "1 Method"), ("summary", "2 Findings"), ("market", "3 Landscape"),
                       ("evidence", "4 Evidence"), ("system", "5 Interface"), ("scores", "6 Weights &amp; scores"),
                       ("ux", "7 Product UX"), ("flows", "8 Flows"), ("direction", "9 Direction"),
                       ("sources", "10 Sources")]:
        a('<a href="#%s">%s</a>' % (sid, label))
    a("</nav>")

    # 1 method
    a('<section id="method"><div class="sechead"><span class="num">01</span></div>')
    a("<h2>How this benchmark was built</h2>")
    a('<p class="sub">Scope, scoring model, evidence standards and the limits of what could be verified</p>')
    a('<div class="stack">')
    a('<div class="card"><h5>What we analysed</h5><p>Eight products: five global (IXL, Khan Academy, '
      'Mathletics, Prodigy, Quizizz) and three Iranian (Gama, MihanMaktab, Porsan), plus two adjacent '
      'references. 36 screenshots and 8 crops, each tagged REAL or SCHEMATIC.</p></div>')
    a('<div class="card"><h5>How we scored</h5><p>Eight criteria weighted by their impact on Roshana\'s '
      'three student personas and the teacher. Every product scored 1-10 against Roshana\'s needs, not '
      'against abstract quality.</p></div>')
    a('<div class="card"><h5>What we could not verify</h5><p>No paid or authenticated accounts, so flows are '
      'inferred from public pages, docs and videos. Iranian products publish no analytics; MihanMaktab has '
      'no real screenshot and is never used as evidence.</p></div>')
    a("</div></section>")

    # 2 findings
    a('<section id="summary"><div class="sechead"><span class="num">02</span></div>')
    a("<h2>Five findings that change Roshana's design</h2>")
    a('<p class="sub">Executive summary - each finding opens with visual evidence later in the document</p>')
    for no, title, body, big, biglabel in FINDINGS:
        a('<div class="card" style="margin-bottom:12px"><h5>Finding %s</h5><h3 style="margin:2px 0 6px">%s</h3>'
          '<p>%s</p><div class="big" style="font-size:20px">%s <span class="mini" style="font-weight:400">%s</span>'
          "</div></div>" % (esc(no), esc(title), esc(body), esc(big), esc(biglabel)))
    a('<div class="callout">Decision: if Roshana does one thing better than everyone, it should be the '
      "shortest path from a detected need to the right practice - and from there to a teacher's next "
      "action.</div></section>")

    # 3 market
    a('<section id="market"><div class="sechead"><span class="num">03</span></div>')
    a("<h2>Market landscape and the eight products</h2>")
    a('<p class="sub">Where the products sit and why exactly these eight were chosen</p>')
    for title, items, note in LANDSCAPE:
        a("<h4>%s</h4><p><strong>%s</strong> - %s</p>" % (esc(title), esc(", ".join(items)), esc(note)))
    a(table(["Product", "Country / language", "Audience", "Model", "Design character"],
            [[p["name"], p["country"] + " / " + p["lang"], p["audience"], p["model"],
              PROFILES_EXTRA[p["key"]]] for p in PRODUCTS], "small"))
    a("<h4>Adjacent references</h4><ul>" + "".join(
        "<li><strong>%s</strong> - %s</li>" % (esc(x), esc(y)) for x, y in ADJACENT) + "</ul></section>")

    # 4 evidence
    EV = {
        "ixl": [("ixl_skill_plans.png", "Skill plans: a ready-made weekly path on top of grade and textbook.", "blog.ixl.com/2024/09/24/", "REAL"),
                ("ixl_dashboard.png", "Student dashboard: assignments, recent work, next badge.", "blog.ixl.com/2025/04/11/", "REAL"),
                ("ixl_quiz_review.png", "Quiz review: skill and correct answer side by side.", "blog.ixl.com/2023/12/14/", "REAL")],
        "khan": [("khan_assign.png", "Role selection and content assignment - the teacher entry point.", "support.khanacademy.org/hc/en-us/articles/360040168512", "REAL"),
                 ("khan_dashboard.png", "Learner home: My courses as the anchor, assignments secondary.", "support.khanacademy.org/", "REAL"),
                 ("khan_mobile_exercise.png", "Mobile exercise with a dedicated maths keypad.", "support.khanacademy.org/hc/en-us/articles/202896260", "REAL")],
        "math": [("math_todo.png", "To Do list: three tabs above, course rows below, status per row.", "mathletics.com/blog/parent/how-to-use-mathletics", "REAL"),
                 ("math_explore.png", "Explore: assignable activities with topic colour coding.", "knowledgebase.mathletics.com/", "REAL"),
                 ("math_console_map.png", "Teacher console: class, activity and assignment in one map.", "knowledgebase.mathletics.com/", "REAL")],
        "prodigy": [("prodigy_env.png", "Battle screen: the question sits inside the game frame, keypad at the bottom.", "commonsensemedia.org/app-reviews/prodigy-math-game", "REAL"),
                    ("prodigy_env_mobile.jpg", "Mobile: keypad and confirm button anchored to the thumb zone.", "prodigygame.com/", "REAL"),
                    ("prodigy_membership.webp", "Membership upsell shown to a child mid-session.", "fairplayforkids.org/", "REAL")],
        "quizizz": [("quizizz_question.png", "Answer screen: one question, four large cards, timer and progress.", "edutopia.org/article/using-quizizz-engage-students", "REAL"),
                    ("quizizz_authoring.png", "Authoring: question types and AI rewrite tools.", "quizizz.com/home", "REAL"),
                    ("quizizz_audio.png", "Audio response question - accessibility beyond typing.", "quizizz.com/home", "REAL")],
        "gama": [("gama_home.webp", "Home: grade list, search and services competing for the same attention.", "gama.ir/", "REAL"),
                 ("gama_nav.png", "Navigation: exam, grade and subject filters on one bar.", "gama.ir/", "REAL")],
        "mihan": [("gama_home.webp", "Visual reference only - Gama.ir, not MihanMaktab. No MihanMaktab UI screenshot exists in public sources.", "gama.ir/ + mihanmaktab.com/", "REAL")],
        "porsan": [("porsan_feed.png", "Feed: subject and grade filters, question cards with photo answers.", "porsan.app/", "REAL"),
                   ("porsan_q.png", "Question detail: answers as photos of handwriting, no verification.", "porsan.app/", "REAL")],
    }
    a('<section id="evidence"><div class="sechead"><span class="num">04</span></div>')
    a("<h2>Evidence bank</h2>")
    a('<p class="sub">Every image carries a REAL / SCHEMATIC tag and a dated source</p>')
    a('<div class="note">REAL PRODUCT SCREENSHOT = captured or published by the vendor. SCHEMATIC '
      'RECONSTRUCTION = redrawn from public documents, never used to prove a UI detail. ROSHANA WIREFRAME = '
      "Roshana's own proposal.</div>")
    for key in ORDER:
        a("<h3>%s</h3>" % esc(BY[key]["name"]))
        for f, cap, src, tag in EV[key]:
            a(fig(f, cap, tag, src))
    a("</section>")

    # 5 interface
    a('<section id="system"><div class="sechead"><span class="num">05</span></div>')
    a("<h2>Interface and visual systems</h2>")
    a('<p class="sub">Colour, typography, density, navigation patterns and the anatomy of a practice screen</p>')
    a("<h4>Colour systems</h4>")
    a(table(["Product", "Brand hue", "What the palette optimises for"],
            [[p["name"], "#" + p["tint"].upper(), COLOUR_NOTE[p["key"]]] for p in PRODUCTS], "small"))
    a('<div class="note">Colour rule for Roshana: three role colours only - action, progress, caution. '
      "Topic colour is expressed by label, not hue, and one accent is reserved for the primary "
      "action.</div>")
    a("<h4>Layout and navigation models</h4>")
    a(table(["Model", "What it does well"],
            [[t, body] for t, body in LAYOUT_MODELS], "small"))
    a('<div class="callout">Roshana: a task-first shell with the library inside. The home screen answers '
      "'what should I do now'; the library is one tap away inside the practice tab rather than in the "
      "global navigation.</div>")
    a("<h4>Dashboards</h4>")
    for title, what, keep, fix in DASHBOARD_MODELS:
        a("<p><strong>%s</strong> - %s</p><p class='mini'>Copy: %s</p><p class='mini'>Fix: %s</p>" %
          (esc(title), esc(what), esc(keep), esc(fix)))
    a('<div class="callout">Dashboard rule: a dashboard is a decision, not an overview. If a student '
      "cannot answer 'what now' in three seconds, the screen has failed.</div>")
    a("<h4>Typography and interface density</h4>")
    a(table(["Product", "Question type size", "Text density", "Effect on attention"], [
        ["IXL", "16 px", "High", "Dense list rows; the question is visually secondary to the skill chrome"],
        ["Khan Academy", "17 px", "Low", "Generous whitespace; one action per card, short copy"],
        ["Mathletics", "18 px", "Medium", "Colour-blocked rows; the question sits in a game frame"],
        ["Prodigy", "20 px", "Medium", "The question is small inside a full-screen world"],
        ["Quizizz", "30 px", "Low", "The largest question text in the set; one question per screen"],
        ["Gama.ir", "12 px", "High", "Document-style density; text is set for reading, not answering"],
        ["MihanMaktab", "14 px", "High", "Slide captions; no interactive question canvas"],
        ["Porsan", "12 px", "High", "Feed density; answers arrive as photographed handwriting"]], "small"))
    a("<h4>Type scale recommended for Roshana</h4>")
    a(table(["Level", "Size / line", "Use"], [
        ["Display", "32 / 40", "Page titles, one per screen"],
        ["Question", "24 / 32", "The question itself - never below 20 px on mobile"],
        ["Body", "16 / 26", "Instructions and feedback, maximum 60 characters per line"],
        ["Meta", "13 / 20", "Labels, chips, counters"]], "small"))
    a('<div class="note">Persian needs a taller line height than Latin - 1.75x the font size for body copy. '
      "Vazirmatn at 16 px with 1.7 line height matches the legibility of Khan's 17 px Latin text, and "
      "Persian numerals must come from the same family to avoid a mixed-metric baseline.</div>")
    a("<h4>Anatomy of a practice screen</h4>")
    a("<ul>" + "".join("<li><strong>%s</strong> - %s</li>" % (esc(t), esc(s2))
                       for t, s2 in PRACTICE_ANATOMY) + "</ul>")
    a(fig("quizizz_question.png", "Quizizz answer screen, used as the reference frame for the anatomy.",
          "REAL", "edutopia.org/article/using-quizizz-engage-students"))
    a("</section>")

    # 6 personas & scores
    a('<section id="scores"><div class="sechead"><span class="num">06</span></div>')
    a("<h2>Personas, criteria, weights and scores</h2>")
    a('<p class="sub">Scoring is anchored to persona needs, not to taste</p>')
    a('<div class="two">')
    for p in PERSONAS:
        a('<div class="persona"><div class="who">%s</div><div class="age">%s &middot; %s</div>'
          "<p style='margin:8px 0 6px'><strong>Need:</strong> %s</p>"
          "<div class='mini'><strong>Priorities</strong></div><ul>%s</ul>"
          "<div class='mini'><strong>Frustrations</strong></div><ul>%s</ul></div>" % (
              esc(p["name"]), esc(p["age"]), esc(p["grades"]), esc(p["need"]),
              "".join("<li>%s</li>" % esc(x) for x in p["priorities"]),
              "".join("<li>%s</li>" % esc(x) for x in p["frustrates"])))
    a("</div>")
    a("<h4>Criteria and weights</h4>")
    a(table(["Criterion", "Weight", "Definition", "Why it matters for Roshana"],
            [[c[1], "%d%%" % round(c[2] * 100), c[3], c[4]] for c in CRITERIA], "small"))
    a("<h4>Score matrix (1-10)</h4>")
    a(table(["Product"] + [SHORT[c[0]] for c in CRITERIA] + ["Weighted"],
            [[p["name"]] + [str(v) for v in p["score"]] + ["%.2f" % WEIGHTED[p["key"]]] for p in PRODUCTS],
            "small"))
    a("<h4>Persona fit (0-10)</h4>")
    a(table(["Product", "Primary", "Lower secondary", "Upper secondary", "Teacher"],
            [[p["name"]] + [str(v) for v in PERSONA_FIT[p["key"]]] for p in PRODUCTS], "small"))
    a("<h4>Weighted ranking</h4>")
    a(table(["Rank", "Product", "Weighted score"],
            [[str(RANK[p["key"]]), p["name"], "%.2f" % WEIGHTED[p["key"]]]
             for p in sorted(PRODUCTS, key=lambda x: RANK[x["key"]])], "small"))
    a("</section>")

    # 7 product ux
    a('<section id="ux"><div class="sechead"><span class="num">07</span></div>')
    a("<h2>Product UX analysis</h2>")
    a('<p class="sub">Two pages per product in the PDF: analysis, then strengths, weaknesses and lessons</p>')
    for key in ORDER:
        ux = UX[key]
        p = BY[key]
        a('<div style="border-top:1px solid #e6e2d6;margin-top:30px;padding-top:12px">')
        a("<h3>%s</h3>" % esc(p["name"]))
        a("<p style='font-size:17px;font-weight:700;color:#16203a'>%s</p>" % esc(ux["headline"]))
        a("<p class='mini'>%s &middot; weighted score %.2f, rank %d of 8 &middot; %s</p>" %
          (esc(ux["sub"]), WEIGHTED[key], RANK[key], esc(ux["note"])))
        a('<div class="two">')
        a("<div>" + "".join("<h4>%s</h4><p>%s</p>" % (esc(t), esc(bd)) for t, bd in ux["blocks"]) + "</div>")
        a("<div>" + fig(ux["shot"][0], ux["shot"][1],
                         "REAL" if ux["shot"][3] == "real" else "SCHEMATIC", ux["shot"][2]) + "</div>")
        a("</div>")
        a('<div class="two"><div><h4>What Roshana takes</h4><ul>%s</ul></div>'
          "<div><h4>What we reject</h4><ul>%s</ul></div></div>" %
          ("".join("<li>%s</li>" % esc(x) for x in ux["take"]),
           "".join("<li>%s</li>" % esc(x) for x in ux["skip"])))
        a("<h4>Key user paths (inferred)</h4><ul>%s</ul>" %
          "".join("<li>%s</li>" % esc(x) for x in ux["flows"]))
        a("<p class='mini'>Persona fit - primary %d, lower secondary %d, upper secondary %d, teacher %d</p>" %
          tuple(PERSONA_FIT[key]))
        a("</div>")
    a("</section>")

    # 8 flows
    a('<section id="flows"><div class="sechead"><span class="num">08</span></div>')
    a("<h2>User flows</h2>")
    a('<p class="sub">Inferred from public documentation and screenshots; labelled as inference</p>')
    a(table(["Product", "Primary path"], [
        ["IXL", "Login > Dashboard > From my teacher > Skill > Practice > Feedback > Skill report"],
        ["Khan Academy", "Login > Dashboard > My courses > Unit > Lesson > Exercise > Hint > Progress"],
        ["Mathletics", "Login > Dashboard > To Do > Activity > Question > Result > Meritopia"],
        ["Prodigy", "Login > Character > Map > Battle > Question > Answer > Reward"],
        ["Quizizz", "Join code > Waiting room > Question > Answer > Feedback > Next > Report"],
        ["Gama.ir", "Login > Grade > Subject > Chapter > Download file > Print"],
        ["MihanMaktab", "Login > Grade > Chapter > Slide > Video > Test"],
        ["Porsan", "Login > Feed > Filter subject > Question > Read answers"]], "small"))
    a("<h4>Three paths Roshana must ship in the MVP</h4>")
    a(table(["Persona path", "Steps"], [
        ["Student - daily practice", "Login with class code > Today > Teacher assignment > Practice > Feedback sheet > Next question"],
        ["Student - free practice", "Choose grade > Skill library > Filter by chapter > Short preview > Practice > Skill report"],
        ["Teacher - report to action", "Class dashboard > Student list > Weakest skill > Assign remedial set > Track completion"]], "small"))
    a('<div class="callout">Navigation contract: every screen must sit on one of these three paths; maximum '
      "five steps from login to the first question; the teacher path starts at a report and ends at an "
      "action; feedback stays on the practice screen.</div></section>")

    # 9 direction
    a('<section id="direction"><div class="sechead"><span class="num">09</span></div>')
    a("<h2>Design direction and MVP</h2>")
    a('<p class="sub">Six rules, thirteen pages, three phases</p>')
    rules = [
        ("One decision per screen", "Every screen has one primary action; everything else is secondary.",
         "Khan's single-action cards and Mathletics' whitespace."),
        ("Three shells, one product", "Same architecture for primary, secondary and teacher; only density, "
         "touch size and tone change.", "Prodigy: 10/10 for primary, 3/10 for upper secondary."),
        ("Feedback in place", "After an answer, the worked solution opens in a bottom sheet; the user never "
         "changes page.", "IXL is the only product with 'Learn with an example' in place."),
        ("One number, with a reason", "One mastery score (0-100) plus one plain sentence explaining why it "
         "moved.", "SmartScore is legible but unexplained."),
        ("Assignment level with free practice", "Two equal tabs at the top of the dashboard: 'My assignment' "
         "and 'Practice freely'.", "Khan hides Assignments; Mathletics adds a pending counter."),
        ("Report equals next action", "Every teacher report row carries an 'assign remedial practice' button, "
         "not just a number.", "IXL walks from list to assignment; Gama and MihanMaktab have no analytical report."),
    ]
    a('<div class="cards">')
    for i, (t, bd, ev) in enumerate(rules, 1):
        a('<div class="card"><h5>Rule %d</h5><h3 style="margin:0 0 6px">%s</h3><p>%s</p>'
          "<p class='mini'>Evidence: %s</p></div>" % (i, esc(t), esc(bd), esc(ev)))
    a("</div>")
    a("<h4>MVP priorities</h4>")
    a(table(["Phase", "Pages", "Content"], [
        ["P0 - first release", "8", "Login with class code; Today dashboard; Skill library + chapter filter; "
         "Practice screen; Feedback sheet; Student skill report; Teacher dashboard; Remedial assignment"],
        ["P1 - phase two", "3", "Profile, badges, achievements; Skill search + suggested path; Parent weekly summary"],
        ["P2 - phase three", "2", "Class honour hall (no individual public rank); Reward shop and avatar"]], "small"))
    a(table(["Phase", "Weeks", "Goal"], [["Phase 1", "0-8", "Full P0 + pilot with two classes"],
                                         ["Phase 2", "9-16", "P1 + parent panel"],
                                         ["Phase 3", "17-24", "P2 + motivation tuning"]], "small"))
    a("<h4>MVP success measures</h4>")
    a('<div class="cards">')
    for big, lab in [("90 s", "to first practice"), ("70%", "weekly assignment completion"),
                     ("1 number", "progress indicator per student"), ("3 clicks", "report to assignment")]:
        a('<div class="card"><div class="big">%s</div><p>%s</p></div>' % (esc(big), esc(lab)))
    a("</div></section>")

    # 10 sources
    a('<section id="sources"><div class="sechead"><span class="num">10</span></div>')
    a("<h2>Sources, evidence quality and limitations</h2>")
    a('<p class="sub">Access date for every source: %s</p>' % ACCESS)
    rows = [
        ("IXL - student dashboard, quiz review, skill plans", "blog.ixl.com",
         "https://blog.ixl.com/2024/09/24/how-to-find-ixl-skills-for-your-child-to-work-on/"),
        ("Khan Academy - learner home, assignments, mobile keypad", "support.khanacademy.org",
         "https://support.khanacademy.org/hc/en-us/articles/360040168512"),
        ("Mathletics - student view and teacher console", "knowledgebase.mathletics.com",
         "https://knowledgebase.mathletics.com/"),
        ("Prodigy Math - game environment and keypad", "commonsensemedia.org",
         "https://www.commonsensemedia.org/app-reviews/prodigy-math-game"),
        ("Quizizz - question screen and authoring", "edutopia.org",
         "https://www.edutopia.org/article/using-quizizz-engage-students"),
        ("Gama.ir - question library and exam sheet", "gama.ir", "https://gama.ir/"),
        ("Porsan - question feed and answers", "porsan.app", "https://porsan.app/"),
        ("MihanMaktab - course structure (no public UI screenshot)", "mihanmaktab.com",
         "https://mihanmaktab.com/"),
    ]
    a('<table class="small"><thead><tr><th>Source</th><th>Publisher</th><th>URL</th></tr></thead><tbody>')
    for t, pub, url in rows:
        a('<tr><td>%s</td><td>%s</td><td><a href="%s" target="_blank" rel="noopener">%s</a></td></tr>' %
          (esc(t), esc(pub), esc(url), esc(url)))
    a("</tbody></table>")
    a("<h4>Limitations</h4><ul>" + "".join("<li>%s</li>" % esc(x) for x in [
        "No authenticated access to any product; all flows are inferred from public pages, docs and videos.",
        "Iranian products publish no analytics dashboards; their scores rest on observable UX, not measured data.",
        "MihanMaktab publishes no real interface screenshot - its page is schematic and never used as evidence.",
        "Scores are relative to Roshana's personas, not an absolute ranking of product quality."]) + "</ul>")
    a('<div class="callout">If this document carries one message: Roshana should not build a bigger library, '
      "it should build the shortest path from a student's need to the right practice - and from there to a "
      "teacher's next action.</div>")
    a('<footer>Roshana &middot; Visual UX/UI Competitive Benchmark &middot; English edition &middot; '
      "data collected %s &middot; all screenshots embedded in this single file</footer>" % ACCESS)
    a("</section></div></body></html>")

    doc = "".join(b)
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(doc)
    print("html ->", OUT_HTML, round(len(doc.encode()) / 1048576, 2), "MB")

    # bundle: html that points at an assets/ folder + the assets themselves
    bundle_html = doc
    for uri, rel in _rel.items():
        bundle_html = bundle_html.replace(uri, rel)
    names = set()
    for f, *_ in [v for arr in EV.values() for v in arr]:
        names.add(f)
    for key in ORDER:
        names.add(UX[key]["shot"][0])
    names.add("quizizz_question.png")
    with zipfile.ZipFile(BUNDLE, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("Roshana_Visual_UXUI_Benchmark_EN.html", bundle_html)
        z.writestr("READ ME.txt",
                   "Roshana - Visual UX/UI Competitive Benchmark (English edition)\n"
                   "Data collected 2025-10-31.\n\n"
                   "This folder holds two ways to read the report:\n"
                   "  1. Roshana_Visual_UXUI_Benchmark_EN.html - open this file; it uses the images\n"
                   "     in assets/screens and assets/crops, so keep the folder structure intact.\n"
                   "  2. A single-file version with every image embedded is supplied separately\n"
                   "     (Roshana_Visual_UXUI_Benchmark_EN.html), which needs no assets folder.\n\n"
                   "assets/screens - 28 source screenshots used in the evidence pages.\n"
                   "assets/crops    - 8 detail crops used to argue a specific point.\n")
        for n in sorted(names):
            pth = os.path.join(S, n)
            if os.path.exists(pth):
                z.write(pth, "assets/screens/" + n)
        for n in sorted(os.listdir(C)):
            pth = os.path.join(C, n)
            if os.path.isfile(pth):
                z.write(pth, "assets/crops/" + n)
    print("bundle ->", BUNDLE, round(os.path.getsize(BUNDLE) / 1048576, 2), "MB")


if __name__ == "__main__":
    build()
