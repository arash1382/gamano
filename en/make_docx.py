# -*- coding: utf-8 -*-
"""Generate the editable DOCX edition of the English benchmark."""
import os, sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from en.content import (CRITERIA, PRODUCTS, PERSONAS, PERSONA_FIT, FINDINGS, WEIGHTED,
                        RANK, LANDSCAPE, PROFILES_EXTRA, ADJACENT, ACCESS,
                        COLOUR_NOTE, LAYOUT_MODELS, PRACTICE_ANATOMY, DASHBOARD_MODELS)
from en.ux import UX, ORDER

S = os.path.join(ROOT, "assets", "screens")
C = os.path.join(ROOT, "assets", "crops")
OUT = "/home/user/Roshana_Visual_UXUI_Benchmark_EN.docx"

BY = {p["key"]: p for p in PRODUCTS}
SHORT = {"discovery": "Discovery", "practice": "Practice", "feedback": "Feedback",
         "progress": "Progress", "dashboard": "Dashboard", "teacher": "Teacher",
         "visual": "Visual", "mobile": "Mobile"}

INK = RGBColor(0x16, 0x20, 0x3A)
MUTED = RGBColor(0x6E, 0x75, 0x83)
CORAL = RGBColor(0xE4, 0x57, 0x2E)
TEAL = RGBColor(0x1B, 0x8A, 0x83)


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def h1(doc, text, kicker=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(20)
    r.font.color.rgb = INK
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(2)
    if kicker:
        k = doc.add_paragraph()
        kr = k.add_run(kicker)
        kr.font.size = Pt(9.5)
        kr.font.color.rgb = MUTED
        kr.italic = True
        k.paragraph_format.space_after = Pt(10)


def h2(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = INK
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)


def h3(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = TEAL
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)


def para(doc, text, size=10, italic=False, color=None, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.italic = italic
    r.bold = bold
    if color:
        r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(6)
    return p


def bullets(doc, items, size=9.5):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(it)
        r.font.size = Pt(size)
        p.paragraph_format.space_after = Pt(2)


def table(doc, header, rows, widths=None, size=8.5):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, h in enumerate(header):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(size)
        shade(hdr[i], "F1EEE4")
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            r = p.add_run(str(v))
            r.font.size = Pt(size)
    if widths:
        for i, w in enumerate(widths):
            for row in t.rows:
                row.cells[i].width = Cm(w)
    return t


def norm(path):
    """Normalise any source image to a clean PNG/JPEG that python-docx can read."""
    from PIL import Image
    cache = "/tmp/docximg"
    os.makedirs(cache, exist_ok=True)
    base = os.path.splitext(os.path.basename(path))[0]
    out = os.path.join(cache, base + ".png")
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(path):
        im = Image.open(path)
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")
        im.save(out, "PNG")
    return out


def image(doc, folder, fname, width_cm=16.0, caption=None, tag=None, src=None):
    path = os.path.join(folder, fname)
    if not os.path.exists(path):
        return
    path = norm(path)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(path, width=Cm(width_cm))
    if tag:
        c = doc.add_paragraph()
        c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        tr = c.add_run("[" + tag + "]")
        tr.bold = True
        tr.font.size = Pt(8)
        tr.font.color.rgb = TEAL if tag.startswith("REAL") else CORAL
        if caption:
            cr = c.add_run("  " + caption)
            cr.font.size = Pt(8)
            cr.font.color.rgb = MUTED
    if src:
        s2 = doc.add_paragraph()
        s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        sr = s2.add_run("Source: " + src + "   |   Accessed: " + ACCESS)
        sr.font.size = Pt(7.5)
        sr.font.color.rgb = MUTED


def build():
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(10)

    sec = doc.sections[0]
    sec.top_margin = Cm(1.8)
    sec.bottom_margin = Cm(1.8)
    sec.left_margin = Cm(2.0)
    sec.right_margin = Cm(2.0)

    # ---------------------------------------------------------- title page
    t = doc.add_paragraph()
    tr = t.add_run("ROSHANA  /  PRODUCT DESIGN RESEARCH")
    tr.bold = True
    tr.font.size = Pt(10)
    tr.font.color.rgb = CORAL

    tt = doc.add_paragraph()
    tt_run = tt.add_run("Visual UX/UI Competitive Benchmark")
    tt_run.bold = True
    tt_run.font.size = Pt(30)
    tt_run.font.color.rgb = INK

    para(doc, "How eight learning products design discovery, practice, feedback, progress and the "
              "teacher's next action - and what Roshana should adopt, redesign or reject.", 12)
    para(doc, "English edition  |  data collected 2025-10-31  |  8 products, 8 weighted criteria, "
              "4 Roshana personas", 9.5, italic=True, color=MUTED)
    para(doc, "This DOCX is the editable twin of the PDF edition. Layout, figures and page composition "
              "live in the PDF; the text, tables and image captions here are fully editable.", 9.5,
         italic=True, color=MUTED)

    doc.add_page_break()

    # ---------------------------------------------------------- method
    h1(doc, "1. How this benchmark was built",
       "Scope, scoring model, evidence standards and the limits of what could be verified")
    h2(doc, "What we analysed")
    bullets(doc, [
        "Eight products: five global (IXL, Khan Academy, Mathletics, Prodigy, Quizizz) and three Iranian "
        "(Gama, MihanMaktab, Porsan).",
        "Two adjacent references - Duolingo and Khan Academy Kids - only for motivation and early-age patterns.",
        "36 screenshots plus 8 crops, each labelled REAL or SCHEMATIC, all included in this package.",
    ])
    h2(doc, "How we scored")
    bullets(doc, [
        "Eight criteria weighted by their impact on Roshana's three student personas and the teacher.",
        "Every product scored 1-10 per criterion against Roshana's needs, not against abstract quality.",
        "Weighted score = sum of score x weight. Weights are published in section 6.",
    ])
    h2(doc, "What we could not verify")
    bullets(doc, [
        "No paid or authenticated accounts, so flows are inferred from public pages, docs and videos.",
        "Iranian products publish no analytics dashboards; their scores rest on observable UX, not data.",
        "MihanMaktab publishes no real UI screenshot - it uses a schematic and is never treated as evidence.",
    ])

    # ---------------------------------------------------------- summary
    h1(doc, "2. Five findings that change Roshana's design",
       "Executive summary - each finding opens with visual evidence later in the document")
    for no, title, body, big, biglabel in FINDINGS:
        h3(doc, "Finding %s - %s" % (no, title))
        para(doc, body)
        para(doc, "%s  (%s)" % (big, biglabel), 9, bold=True, color=CORAL)
    para(doc, "Decision: if Roshana does one thing better than everyone, it should be the shortest path "
              "from a detected need to the right practice - and from there to a teacher's next action.", 10,
         bold=True)

    # ---------------------------------------------------------- market
    h1(doc, "3. Market landscape and the eight products", "Where the products sit and why these eight")
    for title, items, note in LANDSCAPE:
        h3(doc, title + " - " + ", ".join(items))
        para(doc, note)

    rows = [[p["name"], p["country"] + " / " + p["lang"], p["audience"], p["model"],
             PROFILES_EXTRA[p["key"]]] for p in PRODUCTS]
    table(doc, ["Product", "Country / language", "Audience", "Model", "One-line design character"],
          rows, widths=[2.6, 3.2, 2.6, 3.2, 5.6])

    h2(doc, "Adjacent references")
    bullets(doc, [a + " - " + b for a, b in ADJACENT])

    # ---------------------------------------------------------- evidence
    h1(doc, "4. Evidence bank", "Every image carries a REAL / SCHEMATIC tag and a dated source")
    para(doc, "REAL PRODUCT SCREENSHOT = captured or published by the vendor. SCHEMATIC RECONSTRUCTION = "
              "redrawn from public documents and never used to prove a UI detail. ROSHANA WIREFRAME = our "
              "own proposal.", 9.5, italic=True, color=MUTED)

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
        "gama": [("gama_home.webp", "Home: grade list, search and services competing for the same attention.", "gama.ir/ (screenshot via alexairan.com)", "REAL"),
                 ("gama_nav.png", "Navigation: exam, grade and subject filters on one bar.", "gama.ir/", "REAL")],
        "mihan": [("gama_home.webp", "Visual reference only - Gama.ir, not MihanMaktab. No MihanMaktab UI screenshot exists in public sources.", "gama.ir/ + mihanmaktab.com/", "REAL")],
        "porsan": [("porsan_feed.png", "Feed: subject and grade filters, question cards with photo answers.", "porsan.app/ (myket.ir/app/paadars.Porseman)", "REAL"),
                   ("porsan_q.png", "Question detail: answers as photos of handwriting, no verification.", "porsan.app/", "REAL")],
    }
    for key in ORDER:
        h2(doc, BY[key]["name"])
        for f, cap, src, tag in EV[key]:
            image(doc, S, f, 12.5, cap, tag, src)

    # ---------------------------------------------------------- visual system
    h1(doc, "5. Interface and visual systems",
       "Colour, typography, density, navigation patterns and the anatomy of a practice screen")
    h2(doc, "Colour systems")
    para(doc, "Each palette is described by what it optimises for, not by whether it looks pleasant. The "
              "hex value is the dominant brand hue sampled from the product's own screenshots.", 9.5,
         italic=True, color=MUTED)
    table(doc, ["Product", "Brand hue", "What the palette optimises for"],
          [[p["name"], "#" + p["tint"].upper(), COLOUR_NOTE[p["key"]]] for p in PRODUCTS],
          widths=[3.6, 2.6, 10.2], size=8.5)
    h3(doc, "Colour rule for Roshana")
    bullets(doc, [
        "Three role colours only: action, progress, caution. Topic colour is expressed by label, not hue.",
        "One accent reserved for the primary action, so colour means 'do this', not 'this is maths'.",
        "Body text above 7:1 contrast on white; no dark background for primary-school practice.",
    ])

    h2(doc, "Layout and navigation models")
    table(doc, ["Model", "What it does well", "What it costs"],
          [[t, body, "Depth per new topic" if "Library" in t else
            ("Skill findability" if "Session" in t else "Free exploration")] for t, body in LAYOUT_MODELS],
          widths=[4.4, 7.6, 4.4], size=8.5)
    para(doc, "Roshana: a task-first shell with the library inside. The home screen answers 'what should I "
              "do now'; the library is one tap away inside the practice tab rather than in the global "
              "navigation, which keeps the first screen to a single decision.", 10, bold=True)

    h2(doc, "Dashboards")
    for title, what, keep, fix in DASHBOARD_MODELS:
        h3(doc, title)
        para(doc, what)
        para(doc, "Copy: " + keep, 9.5)
        para(doc, "Fix: " + fix, 9.5)
    para(doc, "Roshana dashboard rule: a dashboard is a decision, not an overview. If a student cannot "
              "answer 'what now' in three seconds, the screen has failed regardless of how much data it "
              "shows.", 10, bold=True)

    h2(doc, "Typography and interface density")
    rows = [["IXL", "16 px", "High", "Dense list rows; question is visually secondary to the skill chrome"],
            ["Khan Academy", "17 px", "Low", "Generous whitespace; one action per card, short copy"],
            ["Mathletics", "18 px", "Medium", "Colour-blocked rows; the question sits in a game frame"],
            ["Prodigy", "20 px", "Medium", "The question is small inside a full-screen world"],
            ["Quizizz", "30 px", "Low", "The largest question text in the set; one question per screen"],
            ["Gama.ir", "12 px", "High", "Document-style density; text is set for reading, not answering"],
            ["MihanMaktab", "14 px", "High", "Slide captions; no interactive question canvas"],
            ["Porsan", "12 px", "High", "Feed density; answers arrive as photographed handwriting"]]
    table(doc, ["Product", "Question type size", "Text density", "What it does to attention"], rows,
          widths=[3.0, 3.2, 2.6, 6.6])

    h2(doc, "Type scale recommended for Roshana")
    table(doc, ["Level", "Size / line", "Use"], [
        ["Display", "32 / 40", "Page titles, one per screen"],
        ["Question", "24 / 32", "The question itself - never below 20 px on mobile"],
        ["Body", "16 / 26", "Instructions and feedback, maximum 60 characters per line"],
        ["Meta", "13 / 20", "Labels, chips, counters"]], widths=[3.4, 3.4, 8.6])
    para(doc, "Persian typography note: Persian needs a taller line height than Latin - 1.75x the font size "
              "for body copy. Vazirmatn at 16 px with 1.7 line height matches the legibility of Khan's 17 px "
              "Latin text, and Persian numerals must come from the same family to avoid a mixed-metric "
              "baseline.", 9.5, italic=True, color=MUTED)

    h2(doc, "Anatomy of a practice screen")
    bullets(doc, ["%s - %s" % (t, body) for t, body in PRACTICE_ANATOMY])
    image(doc, S, "quizizz_question.png", 13.0,
          "Quizizz answer screen, used as the reference frame for the anatomy.", "REAL",
          "edutopia.org/article/using-quizizz-engage-students")

    # ---------------------------------------------------------- personas & scoring
    h1(doc, "6. Personas, criteria, weights and scores",
       "Scoring is anchored to persona needs, not to taste")
    for p in PERSONAS:
        h3(doc, "%s (%s, %s)" % (p["name"], p["age"], p["grades"]))
        para(doc, "Need: " + p["need"])
        para(doc, "Priorities", 9, bold=True)
        bullets(doc, p["priorities"], 9)
        para(doc, "Frustrations", 9, bold=True)
        bullets(doc, p["frustrates"], 9)

    h2(doc, "Criteria and weights")
    table(doc, ["Criterion", "Weight", "Definition", "Why it matters for Roshana"],
          [[c[1], "%d%%" % round(c[2] * 100), c[3], c[4]] for c in CRITERIA],
          widths=[4.2, 1.8, 5.0, 5.4])

    h2(doc, "Score matrix")
    header = ["Product"] + [SHORT[c[0]] for c in CRITERIA] + ["Weighted"]
    rows = []
    for p in PRODUCTS:
        rows.append([p["name"]] + [str(v) for v in p["score"]] + ["%.2f" % WEIGHTED[p["key"]]])
    table(doc, header, rows, size=8)

    h2(doc, "Persona fit (0-10)")
    rows = [[p["name"]] + [str(v) for v in PERSONA_FIT[p["key"]]] for p in PRODUCTS]
    table(doc, ["Product", "Primary", "Lower sec.", "Upper sec.", "Teacher"], rows, widths=[4.5, 2.8, 2.8, 2.8, 2.8])

    h2(doc, "Weighted ranking")
    table(doc, ["Rank", "Product", "Weighted score"],
          [[str(RANK[p["key"]]), p["name"], "%.2f" % WEIGHTED[p["key"]]]
           for p in sorted(PRODUCTS, key=lambda x: RANK[x["key"]])],
          widths=[2.0, 6.0, 3.5])

    # ---------------------------------------------------------- product UX
    h1(doc, "7. Product UX analysis", "Two pages per product: analysis, then strengths, weaknesses and lessons")
    for key in ORDER:
        ux = UX[key]
        p = BY[key]
        h2(doc, p["name"])
        para(doc, ux["headline"], 11, bold=True)
        para(doc, "%s. Weighted score %.2f (rank %d of 8). %s" %
             (ux["sub"], WEIGHTED[key], RANK[key], ux["note"]), 9, italic=True, color=MUTED)
        for t, body in ux["blocks"]:
            h3(doc, t)
            para(doc, body)
        h3(doc, "What Roshana takes")
        bullets(doc, ux["take"])
        h3(doc, "What we reject")
        bullets(doc, ux["skip"])
        h3(doc, "Key user paths (inferred)")
        bullets(doc, ux["flows"])
        h3(doc, "Persona fit")
        para(doc, "Primary %d  |  Lower secondary %d  |  Upper secondary %d  |  Teacher %d" %
             tuple(PERSONA_FIT[key]), 9.5)
        image(doc, S, ux["shot"][0], 12.0, ux["shot"][1],
              "REAL" if ux["shot"][3] == "real" else "SCHEMATIC", ux["shot"][2])

    # ---------------------------------------------------------- flows
    h1(doc, "8. User flows", "Inferred from public documentation and screenshots")
    rows = [["IXL", "Login > Dashboard > From my teacher > Skill > Practice > Feedback > Skill report"],
            ["Khan Academy", "Login > Dashboard > My courses > Unit > Lesson > Exercise > Hint > Progress"],
            ["Mathletics", "Login > Dashboard > To Do > Activity > Question > Result > Meritopia"],
            ["Prodigy", "Login > Character > Map > Battle > Question > Answer > Reward"],
            ["Quizizz", "Join code > Waiting room > Question > Answer > Feedback > Next > Report"],
            ["Gama.ir", "Login > Grade > Subject > Chapter > Download file > Print"],
            ["MihanMaktab", "Login > Grade > Chapter > Slide > Video > Test"],
            ["Porsan", "Login > Feed > Filter subject > Question > Read answers"]]
    table(doc, ["Product", "Primary path"], rows, widths=[3.2, 12.4], size=8.5)

    h2(doc, "Three paths Roshana must ship in the MVP")
    table(doc, ["Persona path", "Steps"], [
        ["Student - daily practice", "Login with class code > Today > Teacher assignment > Practice > Feedback sheet > Next question"],
        ["Student - free practice", "Choose grade > Skill library > Filter by chapter > Short preview > Practice > Skill report"],
        ["Teacher - report to action", "Class dashboard > Student list > Weakest skill > Assign remedial set > Track completion"]],
        widths=[4.2, 11.4], size=8.5)
    para(doc, "Navigation contract: every screen must sit on one of these three paths; maximum five steps "
              "from login to the first question; the teacher path starts at a report and ends at an action; "
              "feedback stays on the practice screen.", 9.5, bold=True)

    # ---------------------------------------------------------- direction
    h1(doc, "9. Design direction and MVP", "Six rules, thirteen pages, three phases")
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
    for i, (t, body, ev) in enumerate(rules, 1):
        h3(doc, "Rule %d - %s" % (i, t))
        para(doc, body)
        para(doc, "Evidence: " + ev, 9, italic=True, color=MUTED)

    h2(doc, "MVP priorities")
    table(doc, ["Phase", "Pages", "Content"], [
        ["P0 - first release", "8", "Login with class code; Today dashboard; Skill library + chapter filter; "
         "Practice screen; Feedback sheet; Student skill report; Teacher dashboard; Remedial assignment"],
        ["P1 - phase two", "3", "Profile, badges, achievements; Skill search + suggested path; Parent weekly summary"],
        ["P2 - phase three", "2", "Class honour hall (no individual public rank); Reward shop and avatar"]],
        widths=[3.6, 1.6, 10.4], size=8.5)
    table(doc, ["Phase", "Weeks", "Goal"], [
        ["Phase 1", "0-8", "Full P0 + pilot with two classes"],
        ["Phase 2", "9-16", "P1 + parent panel"],
        ["Phase 3", "17-24", "P2 + motivation tuning"]], widths=[3.0, 3.0, 9.6], size=9)

    h2(doc, "MVP success measures")
    table(doc, ["Measure", "Target"], [
        ["Time to first practice", "90 seconds"],
        ["Weekly assignment completion", "70%"],
        ["Progress indicators per student", "One number"],
        ["Clicks from report to assignment", "Three"]], widths=[8.0, 5.0], size=9)

    # ---------------------------------------------------------- sources
    h1(doc, "10. Sources, evidence quality and limitations", "Access date for every source: 2025-10-31")
    table(doc, ["Source", "Publisher", "URL"], [
        ["IXL - student dashboard, quiz review, skill plans", "blog.ixl.com",
         "https://blog.ixl.com/2024/09/24/how-to-find-ixl-skills-for-your-child-to-work-on/"],
        ["Khan Academy - learner home, assignments, mobile keypad", "support.khanacademy.org",
         "https://support.khanacademy.org/hc/en-us/articles/360040168512"],
        ["Mathletics - student view and teacher console", "knowledgebase.mathletics.com",
         "https://knowledgebase.mathletics.com/"],
        ["Prodigy Math - game environment and keypad", "commonsensemedia.org",
         "https://www.commonsensemedia.org/app-reviews/prodigy-math-game"],
        ["Quizizz - question screen and authoring", "edutopia.org",
         "https://www.edutopia.org/article/using-quizizz-engage-students"],
        ["Gama.ir - question library and exam sheet", "gama.ir", "https://gama.ir/"],
        ["Porsan - question feed and answers", "porsan.app", "https://porsan.app/"],
        ["MihanMaktab - course structure (no public UI screenshot)", "mihanmaktab.com", "https://mihanmaktab.com/"],
    ], widths=[5.4, 3.6, 6.6], size=8)

    h2(doc, "Limitations")
    bullets(doc, [
        "No authenticated access to any product; all flows are inferred from public pages, docs and videos.",
        "Iranian products publish no analytics dashboards; their scores rest on observable UX, not measured data.",
        "MihanMaktab publishes no real interface screenshot - its page is schematic and never used as evidence.",
        "Scores are relative to Roshana's personas, not an absolute ranking of product quality.",
    ])
    para(doc, "If this document carries one message: Roshana should not build a bigger library, it should "
              "build the shortest path from a student's need to the right practice - and from there to a "
              "teacher's next action.", 10, bold=True)

    doc.save(OUT)
    print("docx ->", OUT)


if __name__ == "__main__":
    build()
