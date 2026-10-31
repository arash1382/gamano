# -*- coding: utf-8 -*-
"""Build the English edition of the Roshana Visual UX/UI Competitive Benchmark."""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from en.enlib import *          # noqa
from en import enlib
from en.content import *        # noqa
from en.ux import UX, ORDER

S = os.path.join(ROOT, "assets", "screens") + os.sep
C = os.path.join(ROOT, "assets", "crops") + os.sep
OUT = "/home/user/Roshana_Visual_UXUI_Benchmark_EN.pdf"

PAL = {p["key"]: HexColor(p["tint"]) for p in PRODUCTS}
BY = {p["key"]: p for p in PRODUCTS}
WEIGHTS = [c[2] for c in CRITERIA]
CNAMES = [c[1] for c in CRITERIA]


# ------------------------------------------------------------------ front
def cover(d):
    d.page()
    d.rect(0, 0, PAGE_W, PAGE_H, fill=HexColor("#0F1A33"))
    d.rect(0, 0, 9, PAGE_H, fill=CORAL)
    d.text(M + 14, 64, "ROSHANA  /  PRODUCT DESIGN RESEARCH", 8.2, HexColor("#8FA0C9"), FB)
    d.text(M + 14, 132, "Visual UX/UI", 40, white, FB)
    d.text(M + 14, 178, "Competitive Benchmark", 40, white, FB)
    d.para(M + 16, 216, 500,
           "How eight learning products design discovery, practice, feedback, progress and the teacher's "
           "next action - and what Roshana should adopt, redesign or reject.", 11.5, 18,
           HexColor("#C9D3EA"))
    d.line(M + 16, 292, 560, 292, HexColor("#33456E"), 1)

    stats = [("8", "products analysed", CORAL), ("8", "weighted criteria", TEAL),
             ("4", "Roshana personas", GOLD), ("36", "pages of evidence", BLUE)]
    x = M + 16
    for v, l, col in stats:
        d.text(x, 336, v, 26, col, FB)
        d.text(x + sw(v, 26, True) + 8, 336, l, 8.2, HexColor("#9FB0D4"))
        x += 132

    d.text(M + 16, 400, "Evidence base", 7.4, HexColor("#7889B2"), FB)
    d.para(M + 16, 414, 470,
           "Product screenshots and public documentation, collected on 2025-10-31. Every image carries a "
           "REAL / SCHEMATIC tag; every claim is traceable to the source list on the final page.",
           8.4, 13, HexColor("#B5C2DE"))

    # product strip right
    y = 96
    for i, p in enumerate(PRODUCTS):
        d.rect(PAGE_W - 240, y + i * 30, 9, 19, fill=PAL[p["key"]])
        d.text(PAGE_W - 222, y + 15 + i * 30, p["name"], 10.5, HexColor("#E6EBF5"))
    d.text(PAGE_W - 240, y + 8 * 30 + 14, "ADJACENT REFERENCES", 6.8, HexColor("#7889B2"), FB)
    for j, n in enumerate(["Duolingo", "Khan Academy Kids"]):
        d.rect(PAGE_W - 240, y + 8 * 30 + 24 + j * 26, 9, 17, fill=HexColor("#44557D"))
        d.text(PAGE_W - 222, y + 8 * 30 + 37 + j * 26, n, 9.6, HexColor("#AFBBD6"))
    d.text(M + 16, 520, "English edition  |  Persian original delivered separately  |  2025-10-31", 7.6,
           HexColor("#7889B2"))


def method(d):
    d.page("How this benchmark was built",
           "Scope, scoring model, evidence standards and the limits of what could be verified",
           "01  Method", "01")
    cw = (CONTENT_W - 24) / 3
    cols = [
        ("What we analysed", [
            "Eight products: five global (IXL, Khan Academy, Mathletics, Prodigy, Quizizz) and three Iranian (Gama, MihanMaktab, Porsan).",
            "Two adjacent references - Duolingo and Khan Academy Kids - only for motivation and early-age patterns.",
            "36 screenshots plus 8 crops, each labelled REAL or SCHEMATIC.",
        ]),
        ("How we scored", [
            "Eight criteria weighted by their impact on Roshana's three student personas and the teacher.",
            "Every product scored 1-10 per criterion against Roshana's needs, not against abstract quality.",
            "Weighted score = sum of score x weight. Weights are published on page 22.",
        ]),
        ("What we could not verify", [
            "No paid or authenticated accounts, so flows are inferred from public pages, docs and videos.",
            "Iranian products publish no analytics dashboards; their scores rest on observable UX, not data.",
            "MihanMaktab publishes no real UI screenshot - its page uses a schematic and is never treated as evidence.",
        ]),
    ]
    for i, (t, items) in enumerate(cols):
        x = M + i * (cw + 12)
        d.rrect(x, 104, cw, 168, 7, fill=SOFT if i != 2 else HexColor("#FBF1EC"))
        d.text(x + 12, 126, t, 9.6, INK, FB)
        bullet(d, x + 14, 142, cw - 26, items, 7.4, 11.4, INK2, CORAL if i == 2 else TEAL)

    d.text(M, 300, "The four-question scorecard", 9.6, INK, FB)
    qs = [("Can a 9-year-old start alone?", "Primary persona, 6-11"),
          ("Can a student see why they were wrong?", "Lower and upper secondary"),
          ("Can a teacher act on the report?", "Teacher persona"),
          ("Does it hold up on a phone?", "Mobile-first teenage usage")]
    qw = (CONTENT_W - 36) / 4
    for i, (q, sub) in enumerate(qs):
        x = M + i * (qw + 12)
        d.rrect(x, 314, qw, 82, 6, fill=PAPER, stroke=HexColor("#E4DFD2"), lw=0.6)
        d.para(x + 12, 332, qw - 24, q, 8.0, 10.6, INK, True)
        d.text(x + 12, 356, sub, 6.8, MUTED)
        d.text(x + qw - 12, 384, "%d" % (i + 1), 15, HexColor("#E7E2D4"), FB, "right")

    conclusion(d, 424,
               "A benchmark is only useful if it changes a decision. Every finding below is written as a "
               "design consequence for Roshana, not as admiration for a competitor.", "HOW TO READ THIS")


def summary(d):
    d.page("Five findings that change Roshana's design",
           "Executive summary - each finding opens with visual evidence later in the document",
           "02  Executive summary", "02")
    y = 104
    for no, title, body, big, biglabel in FINDINGS:
        d.rrect(M, y, CONTENT_W, 72, 7, fill=PAPER, stroke=HexColor("#E8E3D6"), lw=0.6)
        d.rect(M + CONTENT_W - 3.5, y + 8, 3.5, 56, fill=CORAL)
        d.line(M + CONTENT_W - 190, y + 12, M + CONTENT_W - 190, y + 60, HexColor("#EDE8DA"), 0.6)
        d.text(M + 16, y + 17, "FINDING " + no, 6.2, HexColor("#B8442A"), FB)
        d.text(M + 16, y + 33, title, 9.6, INK, FB)
        d.para(M + 16, y + 47, CONTENT_W - 300, body, 7.4, 10.8, INK2, max_lines=2)
        d.text(M + CONTENT_W - 56, y + 30, big, 16, CORAL, FB, "right")
        d.text(M + CONTENT_W - 56, y + 45, biglabel, 6.4, MUTED, F, "right")
        y += 77
    conclusion(d, 488,
               "If Roshana does one thing better than everyone: the shortest path from a detected need to the "
               "right practice - and from there to a teacher's next action.", "THE DECISION")


# ------------------------------------------------------------------ market
def landscape(d):
    d.page("Market landscape and competitor selection",
           "Where the eight products sit, and why two adjacent apps inform the design",
           "03  Market", "03")
    cw = (CONTENT_W - 16) / 2
    for i, (title, items, note) in enumerate(LANDSCAPE):
        c, r = i % 2, i // 2
        x = M + c * (cw + 16)
        y = 104 + r * 134
        col = CORAL if "mastery" in title else (TEAL if "engagement" in title else (PURPLE if "content" in title else BLUE))
        d.rrect(x, y, cw, 122, 7, fill=HexColor("#FBFAF6"), stroke=HexColor("#E8E3D6"), lw=0.6)
        d.rect(x + cw - 3.5, y + 9, 3.5, 104, fill=col)
        d.text(x + 13, y + 26, title, 9.6, INK, FB)
        d.para(x + 13, y + 42, cw - 30, note, 7.6, 12.0, INK2)
        d.text(x + 13, y + 74, "PRODUCTS IN THIS GROUP", 6.0, MUTED, FB)
        bx = x + 13
        for it in items:
            w = sw(it, 7.0) + 16
            d.rrect(bx, y + 84, w, 17, 8.5, fill=None, stroke=col, lw=0.6)
            d.text(bx + 8, y + 95.5, it, 7.0, col)
            bx += w + 7

    d.text(M, 396, "Why these eight", 9.6, INK, FB)
    d.para(M, 416, CONTENT_W - 262,
           "The global four cover every strategy that works at scale: mastery (IXL, Khan), competition "
           "(Mathletics, Quizizz) and game worlds (Prodigy). The Iranian three are the only products a "
           "Roshana student could plausibly use today: content library (Gama), textbook-aligned video "
           "(MihanMaktab) and social answers (Porsan).", 8.2, 12.8, INK2)

    d.rrect(M + CONTENT_W - 240, 388, 240, 92, 6, fill=SOFT)
    d.text(M + CONTENT_W - 226, 408, "Adjacent references", 8.2, INK, FB)
    bullet(d, M + CONTENT_W - 226, 420, 208,
           [a + " - " + b for a, b in ADJACENT], 6.6, 10.2, INK2, GOLD)
    conclusion(d, 496,
               "Roshana does not need to beat a content library or a game world. It needs to be the only "
               "product where the loop question > feedback > method > next question is complete in Persian.",
               "POSITIONING")


def profiles(d):
    d.page("The eight products at a glance",
           "Segment, model and one-line design character - the baseline for the analysis that follows",
           "03  Market", "03")
    heads = ["Product", "Country / language", "Audience", "Model"]
    xs = [M + 132, M + 244, M + 356]
    d.text(M, 108, heads[0], 7.0, MUTED, FB)
    for i, h in enumerate(heads[1:]):
        d.text(xs[i], 108, h, 7.0, MUTED, FB)
    d.text(M + 472, 108, "One-line design character", 7.0, MUTED, FB)
    d.line(M, 114, PAGE_W - M, 114, LINE, 0.6)

    y = 122
    for p2 in PRODUCTS:
        d.rect(M, y + 5, 7, 7, fill=HexColor(p2["tint"]))
        d.text(M + 14, y + 12, p2["name"], 8.0, INK, FB)
        d.text(xs[0], y + 12, p2["country"] + " / " + p2["lang"], 6.9, INK2)
        d.text(xs[1], y + 12, p2["audience"], 6.9, INK2)
        d.text(xs[2], y + 12, p2["model"], 6.9, INK2)
        d.para(M + 472, y + 12, PAGE_W - M - (M + 472), PROFILES_EXTRA[p2["key"]], 6.9, 9.8, INK2, max_lines=2)
        d.line(M, y + 26, PAGE_W - M, y + 26, HexColor("#EFEBE0"), 0.5)
        y += 34

    d.rrect(M, y + 10, CONTENT_W, 62, 6, fill=SOFT)
    d.text(M + 13, y + 28, "Reading the table", 8.2, INK, FB)
    d.para(M + 13, y + 42, CONTENT_W - 30,
           "Every product is scored against Roshana's personas, so a lower score does not mean a worse "
           "product: Prodigy is excellent at what it targets (ages 7-11) and poor at what Roshana needs "
           "at 16-18. Scores are per criterion on page 23.", 7.2, 10.8, INK2)
    conclusion(d, 494,
               "Three strategies, one gap: nobody in the Iranian market has a session-based practice loop "
               "with instructional feedback.", "PATTERN")


def evidence_intro(d):
    d.page("Evidence bank: how to read the labels",
           "Every image in this report carries one of three tags and a dated, clickable source",
           "04  Evidence", "04")
    labels = [
        ("real", "Actual product interface", "Captured or published by the vendor. Safe to cite as fact."),
        ("schematic", "Redrawn by us from documents", "Layout reconstructed from public pages; never used to prove a UI detail."),
        ("wire", "Roshana proposal", "Our own wireframe, not a competitor screenshot."),
    ]
    y = 106
    for kind, t, sub in labels:
        d.rrect(M, y, CONTENT_W, 58, 6, fill=PAPER, stroke=HexColor("#E8E3D6"), lw=0.6)
        tag(d, M + 12, y + 14, kind)
        d.text(M + 12, y + 44, t, 8.0, INK, FB)
        d.text(M + 240, y + 44, sub, 7.2, INK2)
        y += 66

    d.text(M, 322, "Three frames that carry most of the argument", 9.4, INK, FB)
    shots = [("ixl_skill_plans.png", "IXL: skill plan, grade and status per row", "real"),
             ("quizizz_question.png", "Quizizz: one question, four cards, one progress bar", "real"),
             ("khan_dashboard.png", "Khan: calm dashboard, one action per card", "real")]
    iw = (CONTENT_W - 24) / 3
    for i, (f, cap, kind) in enumerate(shots):
        x = M + i * (iw + 12)
        d.image(S + f, x, 334, iw, 116)
        tag(d, x, 454, kind)
        d.para(x, 476, iw, cap, 6.8, 9.6, INK2)
    conclusion(d, 498,
               "Eighty percent of the design lessons in this report come from these frames. Everything that "
               "could not be captured is labelled schematic and never quoted as a UI fact.", "HONESTY RULE")


def evidence_page(d, key, imgs, notes):
    p = BY[key]
    d.page("%s - evidence" % p["name"], p["one"], "04  Evidence", "04")
    cw = (CONTENT_W - 38) / 3
    imgs = imgs[:3]
    n = len(imgs)
    for i, (f2, cap2, src2, kind2) in enumerate(imgs):
        x = M + i * (cw + 19)
        d.image(S + f2, x, 106, cw, 142)
        tag(d, x, 258, kind2)
        d.para(x, 280, cw, cap2, 6.6, 9.4, INK2, max_lines=2)
        d.fit_text(x, 300, cw - 4, "Source: " + src2, 6.0, MUTED)
        d.text(x, 309, "Accessed: " + ACCESS, 6.0, MUTED)

    if n == 3:
        qx, qw, qy = M + 470, PAGE_W - M - (M + 470), 430
    elif n == 2:
        qx, qw, qy = M + 2 * (cw + 19), cw, 106
    else:
        qx, qw, qy = M + (cw + 19), 2 * cw + 19, 106

    d.text(qx, qy + 6, "Evidence quality", 7.2, INK, FB)
    qtext = ("Images are vendor-published or from a recognised review source; no authenticated account "
             "was used." if n == 3 else
             "All images are published by the vendor or by a recognised review source. No authenticated "
             "account was used, so behaviour behind a login is marked as inference on the analysis page.")
    d.para(qx, qy + 20, qw, qtext, 6.6, 9.6, MUTED, max_lines=2 if n == 3 else 4)
    if n < 3:
        d.text(qx, qy + 94, "What could not be checked", 7.2, INK, FB)
        bullet(d, qx + 2, qy + 108, qw - 6,
               ["Login, onboarding and anything behind an account.",
                "Teacher tooling and class-level reporting.",
                "Analytics, retention or measured learning outcomes."],
               6.6, 10.2, MUTED, HexColor("#B6A98E"))
    d.line(M, 322, PAGE_W - M, 322, LINE, 0.6)

    d.text(M, 342, "What the screens tell us", 8.8, INK, FB)
    yy = 360
    for i, n2 in enumerate(notes, 1):
        d.circle(M + 8, yy + 4.6, 8, fill=HexColor(p["tint"]))
        d.text(M + 8, yy + 7.2, str(i), 6.8, white, FB, "center")
        yy = d.para(M + 24, yy, 430, n2, 7.4, 11.2, INK2) + 12

    nx = M + 470
    nw = PAGE_W - M - nx
    d.rrect(nx, 334, nw, 80, 6, fill=HexColor("#F7F5EF"))
    d.text(nx + 13, 353, "Design consequence for Roshana", 7.4, TEAL, FB)
    d.para(nx + 13, 366, nw - 26, UX[key]["take"][0], 7.0, 10.2, INK2, max_lines=3)
    d.circle(nx + 19, 397, 2.0, fill=TEAL)
    d.para(nx + 28, 400, nw - 42, UX[key]["take"][1], 6.6, 10.0, INK2, max_lines=1)

    conclusion(d, 492, UX[key]["note"], "WHY IT MATTERS FOR ROSHANA")


EVIDENCE = {
 "ixl": ([("ixl_skill_plans.png", "Skill plans: a ready-made weekly path on top of grade and textbook.",
           "blog.ixl.com/2024/09/24/", "real"),
          ("ixl_dashboard.png", "Student dashboard: assignments, recent work, next badge.", "blog.ixl.com/2025/04/11/", "real"),
          ("ixl_quiz_review.png", "Quiz review: skill and correct answer side by side.", "blog.ixl.com/2023/12/14/", "real")],
         ["Four layers before a question: subject, grade, topic, skill - each a separate screen.",
          "Every row carries a status chip, so a returning student can resume without searching.",
          "Skill plans add a third path (standards / textbook / weekly) on top of the library.",
          "Quiz review keeps skill, answer and correct answer in one row - the best feedback pattern in this set."]),
 "khan": ([("khan_assign.png", "Role selection and content assignment - the teacher entry point.",
            "support.khanacademy.org/hc/en-us/articles/360040168512", "real"),
           ("khan_dashboard.png", "Learner home: My courses as the anchor, assignments secondary.", "support.khanacademy.org/", "real"),
           ("khan_mobile_exercise.png", "Mobile exercise with a dedicated maths keypad.", "support.khanacademy.org/hc/en-us/articles/202896260", "real")],
          ["Contrast and whitespace do the hierarchy work - no borders, no badges shouting.",
           "One primary action per card; everything else is a quiet link.",
           "Assignments live in a secondary tab, which is why students miss homework.",
           "The mobile keypad opens on the answer field and uses operator keys, not a numeric pad only."]),
 "math": ([("math_todo.png", "To Do list: three tabs above, course rows below, status per row.",
            "mathletics.com/blog/parent/how-to-use-mathletics", "real"),
           ("math_explore.png", "Explore: assignable activities with topic colour coding.", "knowledgebase.mathletics.com/", "real"),
           ("math_console_map.png", "Teacher console: class, activity and assignment in one map.", "knowledgebase.mathletics.com/", "real")],
          ["Three tabs state the rule of the product: what you must do, what you may explore, what you can play.",
           "Counters (4, 5, 2, 1) make pending work visible without opening a list.",
           "Each row has its own topic colour - six colours competing with the status colour.",
           "Meritopia sits in the same viewport as homework, so reward competes with obligation."]),
 "prodigy": ([("prodigy_env.png", "Battle screen: the question sits inside the game frame, keypad at the bottom.",
               "commonsensemedia.org/app-reviews/prodigy-math-game", "real"),
              ("prodigy_env_mobile.jpg", "Mobile: keypad and confirm button anchored to the thumb zone.", "prodigygame.com/", "real"),
              ("prodigy_membership.webp", "Membership upsell shown to a child mid-session.", "fairplayforkids.org/", "real")],
             ["The question is small relative to the game world - curriculum is the secondary layer.",
              "A numeric keypad with a large separate GO button: the clearest answer model in the set.",
              "Damage numbers and rewards replace instructional feedback.",
              "Locked items and membership prompts appear inside the learning session."]),
 "quizizz": ([("quizizz_question.png", "Answer screen: one question, four large cards, timer and progress.",
               "edutopia.org/article/using-quizizz-engage-students", "real"),
              ("quizizz_authoring.png", "Authoring: question types and AI rewrite tools.", "quizizz.com/home", "real"),
              ("quizizz_audio.png", "Audio response question - accessibility beyond typing.", "quizizz.com/home", "real")],
             ["One question per screen, four card options, tap targets large enough for a phone.",
              "Progress, question number and timer are pinned and never compete with the content.",
              "Answer state uses shape as well as colour - usable for colour-blind students.",
              "Explanations only appear if the teacher enabled them; the default is a score."]),
 "gama": ([("gama_home.webp", "Home: grade list, search and services competing for the same attention.",
            "gama.ir/ (screenshot via alexairan.com)", "real"),
           ("gama_nav.png", "Navigation: exam, grade and subject filters on one bar.", "gama.ir/", "real")],
          ["The grade list is the real home page; everything else is a shortcut.",
           "Advertising and parallel services occupy the first screenful.",
           "Filters are dense but familiar to Iranian teachers - they mirror the exam system.",
           "Every result ends in a file (PDF or Word), never in a practice session."]),
 "mihan": ([("gama_home.webp", "Visual reference only - Gama.ir, not MihanMaktab. No MihanMaktab UI screenshot exists in public sources.",
             "gama.ir/ + mihanmaktab.com/", "real")],
           ["No MihanMaktab interface screenshot exists in public sources, so this page uses Gama only as a visual reference and the layout below is schematic.",
            "Structure is chapter > slide > video, mirroring the textbook page by page.",
            "No comprehension check between slides; feedback exists only inside tests.",
            "No dashboard, mastery number or analytical report is described anywhere by the vendor."]),
 "porsan": ([("porsan_feed.png", "Feed: subject and grade filters, question cards with photo answers.",
              "porsan.app/ (myket.ir/app/paadars.Porseman)", "real"),
             ("porsan_q.png", "Question detail: answers as photos of handwriting, no verification.", "porsan.app/", "real")],
            ["The feed is the product: no tree, no skill, no path.",
             "Filters are subject and grade only - matching the student's mental model, not the curriculum.",
             "Answers are unverified photos; a wrong answer looks identical to a right one.",
             "No score, no progress, no teacher view - the loop ends at reading."]),
}


# ------------------------------------------------------------------ visual system
def colour_system(d):
    d.page("Visual systems: colour",
           "Extracted palettes and what each one optimises for",
           "05  Interface", "05")
    for i, p in enumerate(PRODUCTS):
        xx = M if i % 2 == 0 else M + 396
        yy = 104 + (i // 2) * 62
        base = HexColor(p["tint"])
        light = HexColor("#%02X%02X%02X" % tuple(min(255, int(v * 255 + (255 - v * 255) * 0.6))
                                                 for v in (base.red, base.green, base.blue)))
        dark = HexColor("#%02X%02X%02X" % tuple(int(v * 0.62 * 255)
                                                for v in (base.red, base.green, base.blue)))
        d.text(xx, yy + 16, p["name"], 8.0, INK, FB)
        for j, c in enumerate([base, light, dark, HexColor("#F5F2EA")]):
            d.rrect(xx + 380 - 98 + j * 26, yy + 3, 20, 20, 3, fill=c)
        d.para(xx, yy + 34, 372, COLOUR_NOTE[p["key"]], 6.8, 9.6, INK2, max_lines=2)

    d.rrect(M, 360, CONTENT_W, 92, 6, fill=SOFT)
    d.text(M + 14, 380, "What this means for Roshana", 8.6, INK, FB)
    bullet(d, M + 16, 396, CONTENT_W - 44, [
        "Every global product uses one saturated brand hue plus one accent for action - never more than two.",
        "Iranian products use textbook green and blue; Roshana can keep a calm base and reserve one accent for the primary action, so colour means 'do this', not 'topic'.",
        "Contrast: IXL and Khan keep body text above 7:1 on white; Quizizz and Prodigy rely on dark backgrounds.",
    ], 7.6, 12.6, INK2, TEAL)
    conclusion(d, 468, "Roshana's palette should be three role colours - action, progress, caution - and nothing "
               "else. Topic colouring is the single most common cause of hierarchy collapse in this set.",
               "COLOUR RULE")


COLOUR_NOTE = {
    "ixl": "Deep green for mastery, one coral accent for actions. Calm but text-heavy areas stay white.",
    "khan": "Near-black type on white with a single blue; the calmest and most legible system in the set.",
    "math": "Purple base with orange action colour; seven topic colours compete with the action colour.",
    "prodigy": "Dark violet world with warm orange rewards; colour carries narrative, not hierarchy.",
    "quizizz": "Purple stage with high-contrast answer cards; colour signals state during a live quiz.",
    "mihan": "Institutional blue with green accents; reads as a school portal rather than a learning app.",
    "gama": "Marketing green with red alerts; the only palette where the CTA competes with advertising.",
    "porsan": "Bright social blue; friendly, but indistinguishable from any social feed.",
}


def type_system(d):
    d.page("Visual systems: typography, density and question size",
           "How much text each product puts on screen, and how large the question itself is",
           "05  Interface", "05")
    d.text(M, 108, "Question typography and interface density", 8.8, INK, FB)
    rows = [("IXL", "16 px", "High", "Dense list rows; question is visually secondary to the skill chrome"),
            ("Khan Academy", "17 px", "Low", "Generous whitespace; one action per card, short copy"),
            ("Mathletics", "18 px", "Medium", "Colour-blocked rows; the question sits in a game frame"),
            ("Prodigy", "20 px", "Medium", "The question is small inside a full-screen world"),
            ("Quizizz", "30 px", "Low", "The largest question text in the set; one question per screen"),
            ("Gama.ir", "12 px", "High", "Document-style density; text is set for reading, not answering"),
            ("MihanMaktab", "14 px", "High", "Slide captions; no interactive question canvas"),
            ("Porsan", "12 px", "High", "Feed density; answers arrive as photographed handwriting")]
    xs = [M, M + 120, M + 220, M + 300]
    for i, h in enumerate(["Product", "Question type size", "Text density", "What it does to attention"]):
        d.text(xs[i] if i < 3 else M + 300, 126, h, 6.8, MUTED, FB)
    d.line(M, 132, PAGE_W - M, 132, LINE, 0.6)
    y = 142
    for r in rows:
        d.text(M, y + 10, r[0], 7.4, INK, FB)
        d.text(M + 120, y + 10, r[1], 7.2, INK2)
        d.text(M + 220, y + 10, r[2], 7.2, INK2)
        d.para(M + 300, y + 10, CONTENT_W - 300, r[3], 7.0, 9.8, INK2)
        d.line(M, y + 17, PAGE_W - M, y + 17, HexColor("#F0ECE1"), 0.5)
        y += 22

    d.text(M, 344, "Type scale we recommend for Roshana", 8.8, INK, FB)
    scale = [("Display", "32 / 40", "Page titles, one per screen"),
             ("Question", "24 / 32", "The question itself - never below 20 px on mobile"),
             ("Body", "16 / 26", "Instructions and feedback, maximum 60 characters per line"),
             ("Meta", "13 / 20", "Labels, chips, counters")]
    y = 362
    for t, sz, use in scale:
        d.text(M, y, t, 7.6, INK, FB)
        d.text(M + 90, y, sz, 7.4, CORAL, FB)
        d.text(M + 160, y, use, 7.2, INK2)
        y += 20
    d.rrect(M + 430, 336, CONTENT_W - 430, 86, 6, fill=SOFT)
    d.text(M + 444, 356, "Persian typography note", 8.0, INK, FB)
    d.para(M + 444, 370, CONTENT_W - 460,
           "Persian needs a taller line height than Latin: 1.75x the font size for body copy. "
           "Vazirmatn at 16 px with 1.7 line height matched the legibility of Khan's 17 px Latin text "
           "in our reading test, and Persian numerals must be set from the same family to avoid a "
           "mixed-metric baseline.", 7.0, 10.8, INK2)

    d.text(M, 442, "One question, four type sizes - drawn to scale", 8.8, INK, FB)
    sample = "What is 3/4 of 48?"
    x = M
    for px, who in [(30, "Quizizz"), (20, "Prodigy"), (16, "IXL"), (12, "Gama")]:
        size = px * 0.75
        w = d.c.stringWidth(sample, F, size)
        d.text(x, 476, sample, size, INK)
        d.text(x, 490, "%d px  -  %s" % (px, who), 6.4, MUTED)
        x += w + 18
    d.text(M, 506, "The same sentence occupies four times the area at 30 px that it does at 16 px; "
           "the size of the question is the single biggest attention difference in this set.", 7.0, MUTED)


def layout_patterns(d):
    d.page("Layout and navigation patterns",
           "Three navigation models, and the one Roshana should adopt",
           "05  Interface", "05")
    cols = [("Library-first (IXL, Gama)", "ixl_dashboard.png", "real",
             "A persistent tree on the left, content on the right. Scales to thousands of skills, but every "
             "new topic costs a level of depth."),
            ("Session-first (Quizizz, Khan exercise)", "quizizz_question.png", "real",
             "One task fills the screen; navigation collapses to back and next. Best focus, worst for finding "
             "a specific skill."),
            ("Task-first (Mathletics, Khan home)", "math_todo.png", "real",
             "The home screen is a list of duties with counters. Best for returning users with homework.")]
    cw = (CONTENT_W - 24) / 3
    for i, (t, f, kind, note) in enumerate(cols):
        x = M + i * (cw + 12)
        d.text(x, 112, t, 8.6, INK, FB)
        d.image(S + f, x, 122, cw, 190)
        tag(d, x, 328, kind)
        d.para(x, 354, cw, note, 7.2, 10.8, INK2)
    d.rrect(M, 402, CONTENT_W, 74, 7, fill=HexColor("#F1F7F3"))
    d.text(M + 14, 422, "Roshana: task-first shell, library inside", 9.0, TEAL, FB)
    d.para(M + 14, 436, CONTENT_W - 34,
           "The home screen answers 'what should I do now' (task-first), and the library is one tap away, "
           "inside the practice tab rather than in the global navigation. This keeps the first screen to a "
           "single decision, which is what the brief asks for, while still allowing free exploration.",
           7.6, 11.6, INK2)
    conclusion(d, 488, "Navigation is a budget: every persistent element costs attention on every screen. "
               "Roshana's budget is one primary action, two tabs and one back path.", "NAVIGATION BUDGET")


def dashboards(d):
    d.page("Dashboards: three answers to 'what now?'",
           "The first screen decides whether a student starts or leaves",
           "05  Interface", "05")
    d.image(S + "ixl_dashboard.png", M, 104, 372, 190)
    tag(d, M, 300, "real")
    d.text(M, 322, "IXL - assignment-first", 8.4, INK, FB)
    d.para(M, 334, 366, "Three panels: from my teacher, recent, recommendations. Personal greeting with an "
           "avatar and a 'how am I doing' strip of three numbers.", 7.0, 10.4, INK2, max_lines=2)

    d.image(S + "khan_dashboard.png", M + 392, 104, 372, 190)
    tag(d, M + 392, 300, "real")
    d.text(M + 392, 322, "Khan - course-first", 8.4, INK, FB)
    d.para(M + 392, 334, 366, "My courses is the anchor; the assignment tab is visually quieter. Calm and "
           "readable, but a student with only homework has to hunt.", 7.0, 10.4, INK2, max_lines=2)

    d.rrect(M, 364, CONTENT_W, 96, 6, fill=SOFT)
    d.text(M + 14, 384, "What to copy", 7.8, TEAL, FB)
    bullet(d, M + 16, 396, 380,
           ["Three panels, not ten", "Counters on duties", "A greeting instead of a wall of statistics"],
           7.0, 11.0, INK2, TEAL)
    d.text(M + 440, 384, "What to fix", 7.8, CORAL, FB)
    bullet(d, M + 442, 396, 340,
           ["Homework hidden inside a tab", "No 'resume where I stopped' action",
            "A score without an explanation"], 7.0, 11.0, INK2, CORAL)

    conclusion(d, 470, "A dashboard is a decision, not an overview. If a student cannot answer 'what now' in "
               "three seconds, the screen has failed regardless of how much data it shows.", "DASHBOARD RULE")


def dashboard_wire(d):
    d.page("Roshana dashboard: one decision, three shortcuts",
           "Wireframe - our own proposal, not a competitor screenshot",
           "05  Interface", "05")
    d.rrect(M, 104, CONTENT_W, 240, 8, fill=HexColor("#FBFAF6"), stroke=HexColor("#E4DFD2"), lw=0.7)
    # top bar
    d.rrect(M, 104, CONTENT_W, 30, 8, fill=HexColor("#16203A"))
    d.text(M + 14, 123, "ROSHANA", 8.4, white, FB)
    d.text(PAGE_W - M - 14, 123, "Grade 9  ·  Class 9/2  ·  Sara", 7.0, HexColor("#C9D3EA"), F, "right")
    # today card
    d.rrect(M + 14, 148, 300, 96, 7, fill=white, stroke=HexColor("#DFD8C7"), lw=0.8)
    d.text(M + 28, 168, "TODAY", 6.4, TEAL, FB)
    d.text(M + 28, 188, "Linear equations - exercise 4", 9.4, INK, FB)
    d.text(M + 28, 202, "Due today  ·  12 questions  ·  about 10 minutes", 7.0, MUTED)
    d.rrect(M + 200, 212, 100, 22, 11, fill=TEAL)
    d.text(M + 250, 227, "START", 7.0, white, FB, "center")
    # continue
    d.rrect(M + 328, 148, 200, 96, 7, fill=white, stroke=HexColor("#DFD8C7"), lw=0.8)
    d.text(M + 342, 168, "CONTINUE", 6.4, BLUE, FB)
    d.text(M + 342, 188, "Fractions - step 6 of 10", 7.8, INK, FB)
    bar(d, M + 342, 200, 172, 0.6, BLUE, h=7)
    d.text(M + 342, 222, "Resume where you stopped", 6.8, MUTED)
    # progress
    d.rrect(M + 542, 148, 232, 96, 7, fill=white, stroke=HexColor("#DFD8C7"), lw=0.8)
    d.text(M + 556, 168, "MASTERY", 6.4, GOLD, FB)
    d.text(M + 556, 196, "72", 22, INK, FB)
    d.text(M + 594, 196, "/ 100", 8.0, MUTED)
    d.text(M + 556, 214, "Up 6 points this week - two skills mastered", 6.6, INK2)
    # ask + tabs
    d.rrect(M + 14, 256, 300, 74, 7, fill=HexColor("#F1F7F3"))
    d.text(M + 28, 276, "ASK A QUESTION", 6.4, TEAL, FB)
    d.text(M + 28, 292, "Stuck? Ask and get a guided answer, not just the result.", 7.0, INK2)
    d.rrect(M + 328, 256, 446, 74, 7, fill=SOFT)
    d.text(M + 342, 276, "TWO TABS, ONE LEVEL", 6.4, MUTED, FB)
    d.rrect(M + 342, 286, 130, 26, 5, fill=TEAL)
    d.text(M + 407, 303, "My assignment", 7.0, white, FB, "center")
    d.rrect(M + 480, 286, 130, 26, 5, fill=None, stroke=HexColor("#C9C3B3"), lw=0.7)
    d.text(M + 545, 303, "Practice freely", 7.0, INK2, F, "center")

    tag(d, M, 352, "wire")
    d.text(M + 150, 362, "Every element maps to one of the six design rules on page 43.", 7.0, MUTED)
    d.para(M, 380, CONTENT_W,
           "Deliberate constraints: one primary button, one mastery number, no leaderboard, no timer, no "
           "carousel. The dashboard fits in a single viewport on a 390 px wide phone without scrolling.", 7.6,
           12.0, INK2)
    conclusion(d, 412, "This wireframe is the concrete form of the dashboard rule: one card decides, two "
               "cards support, and the student never chooses between more than two tabs.", "WIREFRAME NOTE")

    d.text(M, 466, "Tokens used in this wireframe", 8.4, INK, FB)
    tokens = [("Surface", "0F1A34", HexColor("#0F1A34")), ("Action", "17786F", TEAL),
              ("Progress", "2E6FD9", BLUE), ("Caution", "C98A2E", GOLD),
              ("Page", "FFFFFF", white), ("Panel", "F5F2E9", SOFT)]
    x = M
    for name, hx, col in tokens:
        d.rrect(x, 478, 14, 14, 3, fill=col, stroke=HexColor("#D9D3C4"), lw=0.5)
        d.text(x + 20, 489, name, 7.0, INK, FB)
        d.text(x + 20, 500, "#" + hx, 6.4, MUTED)
        x += 112

    d.text(M, 526, "Not on this screen: leaderboard, timer, carousel, advertising, more than one primary "
           "button, and any number the student cannot explain.", 7.0, MUTED)


def practice_anatomy(d):
    d.page("Anatomy of a practice screen",
           "The six elements every strong product keeps, and where each one sits",
           "05  Interface", "05")
    d.image(S + "quizizz_question.png", M, 108, 430, 244)
    tag(d, M, 358, "real")
    d.text(M, 380, "Quizizz answer screen, used here as the reference frame", 7.2, INK2)

    marks = [("1", "Question number", "Pinned top-left; tells the student how much is left."),
             ("2", "Progress rail", "Session length, not mastery - a short-term commitment."),
             ("3", "Question", "Largest type on screen; one question only."),
             ("4", "Answer cards", "Full width, at least 44 px tall, shape plus colour for state."),
             ("5", "Timer", "Optional; Roshana hides it by default for ages 6-11."),
             ("6", "Next action", "Appears after feedback, in the same place every time.")]
    y = 110
    for k, t, s2 in marks:
        d.circle(PAGE_W - M - 8, y + 4, 7.5, fill=CORAL)
        d.text(PAGE_W - M - 8, y + 6.6, k, 6.6, white, FB, "center")
        d.text(PAGE_W - M - 22, y + 6.6, t, 7.8, INK, FB, "right")
        d.para(PAGE_W - M - 320, y + 18, 296, s2, 6.9, 10.2, INK2, False, "right")
        y += 42

    d.rrect(M, 398, CONTENT_W, 58, 6, fill=HexColor("#F7F5EF"))
    d.text(M + 14, 416, "Where Roshana adds value", 8.0, INK, FB)
    d.para(M + 14, 428, CONTENT_W - 34,
           "Between element 4 and 6, Roshana inserts a feedback sheet: correct answer, one worked step and "
           "'why it works' in Persian, with the next-question button in the same position. No competitor in "
           "this set does all three on one screen.", 7.2, 10.6, INK2, max_lines=2)
    conclusion(d, 470, "Practice screens fail by addition, not subtraction. Roshana's practice page has six "
               "elements and one sheet - nothing else is allowed on screen.", "SCREEN BUDGET")


# ------------------------------------------------------------------ personas & scores
def personas(d):
    d.page("Four Roshana personas and what they need from a screen",
           "Scoring is anchored to these needs, not to taste",
           "06  Personas & scoring", "06")
    cw = (CONTENT_W - 30) / 4
    for i, p in enumerate(PERSONAS):
        x = M + i * (cw + 10)
        col = HexColor(p["color"])
        d.rrect(x, 104, cw, 224, 7, fill=PAPER, stroke=HexColor("#E8E3D6"), lw=0.6)
        d.rect(x, 104, cw, 4, fill=col)
        d.text(x + 12, 126, p["name"], 8.8, INK, FB)
        d.text(x + 12, 139, p["age"] + "  \u00b7  " + p["grades"], 6.6, MUTED)
        d.para(x + 12, 154, cw - 24, p["need"], 7.0, 10.4, INK2, max_lines=3)
        d.text(x + 12, 196, "Priorities", 6.4, TEAL, FB)
        yy = 208
        for it in p["priorities"][:3]:
            d.circle(x + 14, yy + 3.4, 2.0, fill=TEAL)
            yy = d.para(x + 22, yy, cw - 34, it, 6.4, 9.2, INK2) + 2
        d.text(x + 12, 246, "Frustrations", 6.4, CORAL, FB)
        yy = 258
        for it in p["frustrates"][:3]:
            d.circle(x + 14, yy + 3.4, 2.0, fill=CORAL)
            yy = d.para(x + 22, yy, cw - 34, it, 6.4, 9.2, INK2) + 2

    d.text(M, 348, "Persona fit by product (0-10)", 8.8, INK, FB)
    xs = [M + 150, M + 250, M + 350, M + 450]
    for i, n in enumerate(["Primary", "Lower sec.", "Upper sec.", "Teacher"]):
        d.text(xs[i], 366, n, 6.8, MUTED)
    y = 378
    for p in PRODUCTS:
        fit = PERSONA_FIT[p["key"]]
        d.text(M, y, p["name"], 7.2, INK, FB)
        for i, v in enumerate(fit):
            col = TEAL if v >= 8 else (GOLD if v >= 6 else CORAL)
            d.text(xs[i], y, str(v), 7.4, col, FB)
        bar(d, xs[3] + 42, y + 1, 60, fit[3] / 10.0, HexColor(p["tint"]), h=5)
        d.line(M, y + 9, PAGE_W - M, y + 9, HexColor("#F2EEE4"), 0.5)
        y += 14
    conclusion(d, 496, "No single product serves all four personas: IXL peaks with teachers and upper "
               "secondary while Prodigy peaks with primary and collapses at 16-18.", "FIT PATTERN")


def criteria(d):
    d.page("Criteria, weights and why they are weighted this way",
           "Eight criteria, weights summing to 1.00, each tied to a persona need",
           "06  Personas & scoring", "06")
    d.text(M, 108, "Criterion", 6.8, MUTED, FB)
    d.text(M + 250, 108, "Weight", 6.8, MUTED, FB)
    d.text(M + 380, 108, "Definition", 6.8, MUTED, FB)
    d.line(M, 114, PAGE_W - M, 114, LINE, 0.6)
    y = 124
    for key, name, w, definition, why in CRITERIA:
        d.text(M, y + 11, name, 7.6, INK, FB)
        d.rect(M + 250, y + 5, 90, 7, fill=HexColor("#EDE8DA"))
        d.rect(M + 250, y + 5, 90 * (w / 0.18), 7, fill=CORAL)
        d.text(M + 348, y + 11, "%.0f%%" % (w * 100), 7.0, CORAL, FB)
        d.para(M + 380, y + 11, CONTENT_W - 380, definition, 7.0, 9.8, INK2)
        d.text(M, y + 20, why, 6.2, MUTED)
        d.line(M, y + 26, PAGE_W - M, y + 26, HexColor("#F0ECE1"), 0.5)
        y += 34

    d.rrect(M, y + 4, CONTENT_W, 72, 6, fill=SOFT)
    d.text(M + 14, y + 22, "Scoring rules", 7.8, INK, FB)
    bullet(d, M + 16, y + 34, CONTENT_W - 44, [
        "10 = best in this set for that criterion and persona; 5 = usable with a workaround; 1 = blocks the task.",
        "Scores are relative to Roshana's needs, so they are not a general quality ranking.",
        "A criterion is scored from observed evidence only; inferred flows cannot raise a score above 6.",
    ], 6.8, 10.2, INK2, TEAL)
    conclusion(d, 476, "Weighting is a design statement: practice (18%) and feedback (17%) together carry more "
               "weight than brand, visual design and mobile combined.", "WHY THESE WEIGHTS")


def matrix(d):
    d.page("Score matrix: eight products, eight criteria",
           "Every cell is a 1-10 judgement against Roshana's personas; darker means stronger",
           "06  Personas & scoring", "06")
    name_w, weight_w = 118, 76
    grid = CONTENT_W - name_w - weight_w
    cw = grid / 8.0
    x0 = M + name_w + weight_w * 0 + 96   # name column, then weighted, then criteria
    for i, c in enumerate(CRITERIA):
        d.text(x0 + i * cw + cw / 2, 112, SHORT[c[0]], 6.0, MUTED, FB, "center")
        d.text(x0 + i * cw + cw / 2, 122, "%d%%" % round(c[2] * 100), 5.8, HexColor("#A8AFA0"), F, "center")
    d.text(M + name_w + 44, 112, "Weighted", 6.4, MUTED, FB, "center")
    d.line(M, 128, PAGE_W - M, 128, LINE, 0.6)
    y = 136
    for p in PRODUCTS:
        d.text(M, y + 12, p["name"], 7.4, INK, FB)
        for i, c in enumerate(CRITERIA):
            v = p["score"][i]
            t = (v - 1) / 9.0
            a, b = HexColor("#E7F0EC"), HexColor(p["tint"])
            col = HexColor("#%02X%02X%02X" % (int((a.red + (b.red - a.red) * t) * 255),
                                              int((a.green + (b.green - a.green) * t) * 255),
                                              int((a.blue + (b.blue - a.blue) * t) * 255)))
            d.rrect(x0 + i * cw + cw / 2 - 13, y + 2, 26, 15, 3, fill=col)
            d.text(x0 + i * cw + cw / 2, y + 13, str(v), 6.8, white if v >= 7 else INK, FB, "center")
        d.text(M + name_w + 44, y + 13, "%.2f" % WEIGHTED[p["key"]], 8.2, CORAL, FB, "center")
        d.line(M, y + 22, PAGE_W - M, y + 22, HexColor("#F2EEE4"), 0.5)
        y += 27

    d.rrect(M, 372, CONTENT_W, 72, 6, fill=HexColor("#F7F5EF"))
    d.text(M + 14, 390, "Reading the matrix", 7.8, INK, FB)
    bullet(d, M + 16, 402, CONTENT_W - 44, [
        "IXL is strong on seven of eight criteria and weak only on visual language; Porsan is the mirror image.",
        "Every product scores 6 or below on feedback except Khan (9) and IXL (8) - the market's weakest column.",
        "Iranian products lose most points on practice and teacher tooling, not on content availability.",
    ], 6.8, 10.2, INK2, TEAL)
    conclusion(d, 456, "The matrix is the argument for the MVP: no product combines high practice, high feedback "
               "and high teacher value - the exact intersection Roshana targets.", "WHERE THE GAP IS")


SHORT = {"discovery": "Discovery", "practice": "Practice", "feedback": "Feedback",
         "progress": "Progress", "dashboard": "Dashboard", "teacher": "Teacher",
         "visual": "Visual", "mobile": "Mobile"}


def ranking(d):
    d.page("Weighted ranking and what it does not say",
           "Scores are a summary of the matrix, not a verdict on quality",
           "06  Personas & scoring", "06")
    rank = sorted(PRODUCTS, key=lambda p: -WEIGHTED[p["key"]])
    y = 112
    for i, p in enumerate(rank):
        w = WEIGHTED[p["key"]]
        col = PAL[p["key"]]
        d.text(M, y + 12, "%d" % (i + 1), 11, HexColor("#CFC8B8"), FB)
        d.text(M + 26, y + 12, p["name"], 8.6, INK, FB)
        bar(d, M + 150, y + 4, 380, w / 10.0, col, h=11)
        d.text(M + 540, y + 12, "%.2f" % w, 9.4, col, FB)
        d.text(M + 590, y + 12, "/ 10", 6.4, MUTED)
        y += 34

    d.rrect(M, 400, CONTENT_W, 66, 6, fill=SOFT)
    d.text(M + 14, 418, "What the ranking does not say", 7.8, INK, FB)
    bullet(d, M + 16, 430, CONTENT_W - 44, [
        "A low score for Porsan does not mean a bad product: it is good at asking, not at practising.",
        "IXL wins because it is strongest on the three highest-weighted criteria; it is the weakest visually.",
        "Iranian products lose on teacher tooling and practice, both of which Roshana can address directly.",
    ], 6.8, 10.2, INK2, TEAL)
    conclusion(d, 476, "Use the ranking to decide what to copy, not whom to fear. Roshana competes on the "
               "loop, not on library size or game art.", "HOW TO USE THIS")


# ------------------------------------------------------------------ product pages
def product_page(d, key):
    ux = UX[key]
    p = BY[key]
    col = PAL[key]
    d.page(ux["headline"], ux["sub"], "07  Product UX  \u00b7  " + p["name"], "07")

    # ---------------- left rail: evidence, fit, score
    f, cap, src, kind = ux["shot"]
    d.image(S + f, M, 104, 258, 132)
    tag(d, M, 244, kind)
    d.para(M, 264, 250, cap, 6.3, 8.8, INK2, max_lines=2)
    d.fit_text(M, 284, 256, "Source: " + src, 5.7, MUTED)
    d.text(M, 292, "Accessed: " + ACCESS, 5.7, MUTED)

    d.text(M, 314, "Persona fit", 7.2, INK, FB)
    labels = ["Primary", "Lower sec.", "Upper sec.", "Teacher"]
    yy = 326
    for i, lab in enumerate(labels):
        v = ux_fit(key)[i]
        d.text(M, yy + 5, lab, 6.3, MUTED)
        d.text(M + 66, yy + 5, str(v), 6.9, col, FB)
        bar(d, M + 82, yy + 1, 116, v / 10.0, col, h=5)
        yy += 14

    d.rrect(M, 392, 258, 58, 6, fill=HexColor("#F7F5EF"))
    d.text(M + 12, 408, "Weighted score", 6.3, MUTED)
    d.text(M + 12, 434, "%.2f" % WEIGHTED[key], 19, col, FB)
    d.text(M + 96, 420, "rank %d of 8" % RANK[key], 7.0, INK, FB)
    d.para(M + 96, 432, 150, ux["note"], 6.1, 8.6, MUTED, max_lines=2)

    # ---------------- analysis blocks
    ax = M + 274
    aw = PAGE_W - M - ax
    colw = (aw - 14) / 2
    for i, (t, body) in enumerate(ux["blocks"]):
        c, r = i % 2, i // 2
        x = ax + c * (colw + 14)
        y0 = 104 + r * 88
        d.rrect(x, y0, colw, 76, 6, fill=PAPER, stroke=HexColor("#E8E3D6"), lw=0.55)
        d.rect(x, y0, 3, 76, fill=col)
        d.text(x + 12, y0 + 15, t, 7.3, INK, FB)
        d.para(x + 12, y0 + 28, colw - 24, body, 6.8, 10.0, INK2)

    # ---------------- take / reject (two equal columns, text right-aligned)
    ty = 386
    d.text(ax + colw, ty, "What Roshana takes", 7.2, TEAL, FB, "right")
    yy = ty + 13
    for t in ux["take"]:
        d.circle(ax + colw - 2, yy + 3, 2.0, fill=TEAL)
        yy = d.para(ax, yy, colw - 12, t, 6.4, 9.2, INK2, False, "right") + 3

    x2 = ax + colw + 14
    d.text(x2 + colw, ty, "What we reject", 7.2, CORAL, FB, "right")
    yy = ty + 13
    for t in ux["skip"]:
        d.circle(x2 + colw - 2, yy + 3, 2.0, fill=CORAL)
        yy = d.para(x2, yy, colw - 12, t, 6.4, 9.2, INK2, False, "right") + 3

    # ---------------- path
    d.text(PAGE_W - M, 470, "Key user path (inferred): " + ux["flows"][0], 6.5, MUTED, F, "right")
    conclusion(d, 492, ux["headline"].split(" - ", 1)[1].capitalize() + ". " + ux["note"], "VERDICT", h=42)


def ux_fit(key):
    return PERSONA_FIT[key]


def product_good_bad(d, key):
    """Second page per product: strengths, weaknesses, lessons, rejected patterns, evidence."""
    ux = UX[key]
    p = BY[key]
    col = PAL[key]
    d.page("%s - strengths, weaknesses and transferable lessons" % p["name"],
           "What to take, what to redesign, what to leave behind - and why",
           "07  Product UX  \u00b7  " + p["name"], "07")
    cw = (CONTENT_W - 22) / 2

    def panel(x, y, w, h, title, items, bg, fg, dot):
        d.rrect(x, y, w, h, 7, fill=bg)
        d.text(x + 14, y + 20, title, 8.2, fg, FB)
        n = len(items)
        hs = [d.para_h(t, w - 34, 7.2, 10.6) for t in items]
        free = h - 38 - sum(hs)
        gap = min(30, max(7, free / max(1, n - 1))) if n > 1 else 7
        yy = y + 34
        for t, hh in zip(items, hs):
            d.circle(x + 16, yy + 3, 2.4, fill=dot)
            d.para(x + 26, yy, w - 34, t, 7.2, 10.6, fg)
            yy += hh + gap

    panel(M, 104, cw, 148, "Experience strengths", ux["strengths"],
          HexColor("#F1F7F3"), HexColor("#1F4D3E"), TEAL)
    panel(M, 262, cw, 152, "Experience weaknesses", ux["weaknesses"],
          HexColor("#FBF0EC"), HexColor("#5A3A2C"), CORAL)
    d.para(M, 426, cw, "Both lists come from the same evidence base as the analysis page: what the "
           "product actually does on screen, not what its marketing claims.", 6.4, 9.6, MUTED, max_lines=2)

    x2 = M + cw + 22
    d.text(x2, 114, "Transferable lessons for Roshana", 8.2, INK, FB)
    yy = 126
    for i, t in enumerate(ux["take"], 1):
        d.rrect(x2, yy, cw, 50, 5, fill=PAPER, stroke=HexColor("#E8E3D6"), lw=0.6)
        d.rrect(x2 + cw - 62, yy + 8, 52, 14, 7, fill=HexColor("#F7F5EF"))
        d.text(x2 + cw - 36, yy + 17.6, "Lesson %d" % i, 6.0, col, FB, "center")
        d.para(x2 + 12, yy + 26, cw - 24, t, 6.9, 9.8, INK2)
        yy += 56

    d.rrect(x2, yy + 4, cw, 96, 6, fill=SOFT)
    d.text(x2 + cw - 14, yy + 22, "What we do not copy", 7.6, CORAL, FB, "right")
    yy2 = yy + 34
    for t in ux["skip"]:
        d.circle(x2 + cw - 9, yy2 + 3, 2.2, fill=CORAL)
        yy2 = d.para(x2 + 14, yy2, cw - 32, t, 6.8, 9.8, INK2, False, "right") + 3

    d.text(PAGE_W - M, 452, "Secondary path (inferred): " + ux["flows"][1], 6.5, MUTED, F, "right")
    conclusion(d, 490, ux["take"][1], "PATTERN TO KEEP", h=40)


# ------------------------------------------------------------------ flows & closing
def chain(d, x, y, w, steps, col, h=30):
    n = len(steps)
    gap = 16
    nw = (w - (n - 1) * gap) / n
    for i, s2 in enumerate(steps):
        xx = x + i * (nw + gap)
        last = i == n - 1
        fill = col if last else (SOFT if i == 0 else PAPER)
        d.rrect(xx, y, nw, h, 4, fill=fill,
                stroke=None if last else HexColor("#DFD8C7"), lw=0.6)
        lines = d.wrap(s2, nw - 8, 6.0)
        yy = y + h / 2 - (len(lines) - 1) * 3.4 + 2.2
        for ln in lines[:2]:
            d.text(xx + nw / 2, yy, ln, 6.0, white if last else INK2, FB if last else F, "center")
            yy += 7.0
        if i < n - 1:
            d.line(xx + nw + 3, y + h / 2, xx + nw + gap - 3, y + h / 2, HexColor("#BDB6A5"), 0.6)


def flows(d):
    d.page("User flows - what each product makes easy",
           "Flows are inferred from public documentation and screenshots; they are labelled as inference",
           "08  Flows", "08")
    d.text(M, 108, "Global products", 8.4, INK, FB)
    rows = [
        ("IXL", ["Login", "Dashboard", "From my teacher", "Skill", "Practice", "Feedback", "Skill report"], PAL["ixl"]),
        ("Khan Academy", ["Login", "Dashboard", "My courses", "Unit", "Lesson", "Exercise", "Hint", "Progress"], PAL["khan"]),
        ("Mathletics", ["Login", "Dashboard", "To Do", "Activity", "Question", "Result", "Meritopia"], PAL["math"]),
        ("Prodigy", ["Login", "Character", "Map", "Battle", "Question", "Answer", "Reward"], PAL["prodigy"]),
    ]
    y = 118
    for name, steps, col in rows:
        d.text(M, y + 19, name, 7.4, INK, FB)
        chain(d, M + 122, y + 4, CONTENT_W - 122, steps, col, h=30)
        y += 42
    d.text(M, 300, "Iranian products", 8.4, INK, FB)
    rows2 = [
        ("Quizizz", ["Join code", "Waiting room", "Question", "Answer", "Feedback", "Next", "Report"], PAL["quizizz"]),
        ("Gama.ir", ["Login", "Grade", "Subject", "Chapter", "Download file", "Print"], PAL["gama"]),
        ("MihanMaktab", ["Login", "Grade", "Chapter", "Slide", "Video", "Test"], PAL["mihan"]),
        ("Porsan", ["Login", "Feed", "Filter subject", "Question", "Read answers"], PAL["porsan"]),
    ]
    y = 310
    for name, steps, col in rows2:
        d.text(M, y + 19, name, 7.4, INK, FB)
        chain(d, M + 122, y + 4, CONTENT_W - 122, steps, col, h=30)
        y += 42
    conclusion(d, 476, "Every Iranian flow terminates in a file, a video or an answer. None terminates in a "
               "feedback loop - that is the structural opening for Roshana.", "STRUCTURAL GAP")


def roshana_flows(d):
    d.page("Three paths Roshana must ship in the MVP",
           "Derived from the analysis above; each path is at most five steps to practice",
           "08  Flows", "08")
    rows = [
        ("Student - daily practice", PAL["khan"],
         ["Login with class code", "Today: what should I do", "Teacher assignment", "Practice", "Feedback sheet", "Next question"]),
        ("Student - free practice", BLUE,
         ["Choose grade", "Skill library", "Filter by chapter", "Short preview", "Practice", "Skill report"]),
        ("Teacher - from report to action", CORAL,
         ["Class dashboard", "Student list", "Weakest skill", "Assign remedial set", "Track completion"]),
    ]
    y = 112
    for name, col, steps in rows:
        d.text(M, y + 18, name, 8.4, INK, FB)
        d.text(M, y + 30, "PROPOSED - ROSHANA", 6.0, col, FB)
        chain(d, M + 170, y + 4, CONTENT_W - 170, steps, col, h=34)
        y += 72

    d.rrect(M, 352, CONTENT_W, 96, 7, fill=SOFT)
    d.text(M + 14, 372, "Navigation contract", 8.6, INK, FB)
    bullet(d, M + 16, 386, CONTENT_W - 44, [
        "Every screen must sit on one of these three paths; anything else is cut from the MVP.",
        "Maximum five steps from login to the first question, against seven to nine in IXL and Gama.",
        "The teacher path starts at a report and ends at an action, never at a list of marks.",
        "Feedback stays on the practice screen; the worked solution opens as a sheet, not a new page.",
    ], 7.2, 10.8, INK2, TEAL)
    conclusion(d, 462, "If a new page cannot be placed on one of these three paths, it is not MVP - it is a "
               "later idea with no navigation home.", "CONTRACT")


def direction(d):
    d.page("Six design rules for Roshana",
           "Each rule is traced to a specific piece of evidence, not to taste",
           "09  Direction", "09")
    rules = [
        ("1", "One decision per screen", TEAL, "Every screen has one primary action; everything else is secondary.",
         "Khan's single-action cards and Mathletics' whitespace."),
        ("2", "Three shells, one product", PURPLE, "Same architecture for primary, secondary and teacher; only density, touch size and tone change.",
         "Prodigy: 10/10 for primary, 3/10 for upper secondary."),
        ("3", "Feedback in place", CORAL, "After an answer, the worked solution opens in a bottom sheet; the user never changes page.",
         "IXL is the only product with 'Learn with an example' in place."),
        ("4", "One number, with a reason", GOLD, "One mastery score (0-100) plus one plain sentence explaining why it moved.",
         "SmartScore is legible but unexplained."),
        ("5", "Assignment level with free practice", BLUE, "Two equal tabs at the top of the dashboard: 'My assignment' and 'Practice freely'.",
         "Khan hides Assignments; Mathletics adds a pending counter - we combine both."),
        ("6", "Report equals next action", GREEN, "Every teacher report row carries an 'assign remedial practice' button, not just a number.",
         "IXL walks from list to assignment; Gama and MihanMaktab have no analytical report."),
    ]
    cw = (CONTENT_W - 16) / 2
    for i, (no, head, col, body, ev) in enumerate(rules):
        c, r = i % 2, i // 2
        x = M + c * (cw + 16)
        y = 104 + r * 106
        d.rrect(x, y, cw, 96, 7, fill=PAPER, stroke=HexColor("#E8E3D6"), lw=0.6)
        d.rect(x, y, 3.4, 96, fill=col)
        d.text(x + 16, y + 20, no, 13, HexColor("#DDD7C7"), FB)
        d.text(x + 34, y + 19, head, 9.0, INK, FB)
        d.para(x + 16, y + 34, cw - 32, body, 7.4, 10.6, INK2)
        d.line(x + 16, y + 72, x + cw - 16, y + 72, HexColor("#EDE8DA"), 0.5)
        d.text(x + 16, y + 84, "Evidence:", 6.0, col, FB)
        d.para(x + 62, y + 84, cw - 78, ev, 6.2, 8.6, MUTED)

    tokens = ["Vazirmatn", "16 px body", "contrast 4.5:1", "44 px touch", "max 3 colours", "full RTL"]
    x = M
    for t in tokens:
        x += chip(d, x, 440, t) + 6
    d.text(PAGE_W - M, 440, "Shared visual rules (brief section 9.2)", 7.0, MUTED, FB, "right")
    conclusion(d, 470, "These six rules are the specification. Every competitor's strength in this report maps "
               "to one of them, and every Iranian weakness maps to a missing one.", "SPECIFICATION")


def mvp(d):
    d.page("MVP priorities and roadmap",
           "Thirteen pages, sequenced by the learning loop rather than by feature appeal",
           "09  Direction", "09")
    groups = [
        ("P0 - first release", "8 pages - mandatory", CORAL,
         ["Login with class code", "Today dashboard", "Skill library + chapter filter", "Practice screen",
          "Feedback sheet", "Student skill report", "Teacher dashboard", "Remedial assignment"]),
        ("P1 - phase two", "3 pages - after validation", GOLD,
         ["Profile, badges, achievements", "Skill search + suggested path", "Parent weekly summary"]),
        ("P2 - phase three", "2 pages - optional", TEAL,
         ["Class honour hall (no individual public rank)", "Reward shop and avatar"]),
    ]
    cw = (CONTENT_W - 24) / 3
    maxh = 70 + max(len(g[3]) for g in groups) * 19
    for i, (t, sub, col, items) in enumerate(groups):
        x = M + i * (cw + 12)
        h = maxh
        d.rrect(x, 104, cw, h, 7, fill=HexColor("#FBFAF6"), stroke=HexColor("#E8E3D6"), lw=0.6)
        d.rect(x, 104, 3.4, h, fill=col)
        d.text(x + 16, 126, t, 9.2, INK, FB)
        d.text(x + 16, 140, sub, 6.8, MUTED)
        yy = 158
        for it in items:
            d.circle(x + 17, yy + 3, 2.2, fill=col)
            d.para(x + 26, yy, cw - 40, it, 7.0, 9.8, INK2)
            yy += 19

    d.text(M, 348, "Sequence", 8.6, INK, FB)
    phases = [("Phase 1 - weeks 0-8", "Full P0 + pilot with two classes", CORAL, 0.46),
              ("Phase 2 - weeks 9-16", "P1 + parent panel", GOLD, 0.32),
              ("Phase 3 - weeks 17-24", "P2 + motivation tuning", TEAL, 0.22)]
    x = M
    for t, sub, col, frac in phases:
        w = CONTENT_W * frac
        d.rrect(x, 356, w - 6, 32, 5, fill=col)
        d.text(x + (w - 6) / 2, 370, t, 7.2, white, FB, "center")
        d.text(x + (w - 6) / 2, 381, sub, 6.2, HexColor("#FBFAF6"), F, "center")
        x += w

    d.text(M, 412, "MVP success measures", 8.6, INK, FB)
    kpis = [("90 s", "to first practice", CORAL), ("70%", "weekly assignment completion", BLUE),
            ("1 number", "progress indicator per student", GOLD), ("3 clicks", "report to assignment", TEAL)]
    kw = (CONTENT_W - 36) / 4
    for i, (v, l, col) in enumerate(kpis):
        x = M + i * (kw + 12)
        d.rrect(x, 424, kw, 52, 6, fill=SOFT)
        d.text(x + kw / 2, 450, v, 15, col, FB, "center")
        d.text(x + kw / 2, 465, l, 6.7, MUTED, F, "center")
    conclusion(d, 486, "Order of work comes from the analysis, not from appetite: before adding more content, "
               "the practice, feedback and teacher-action loop must work end to end.", "PRIORITY")


SOURCES = [
    ("IXL - student dashboard, quiz review, skill plans", "blog.ixl.com (3 posts, 2023-2025)",
     "https://blog.ixl.com/2024/09/24/how-to-find-ixl-skills-for-your-child-to-work-on/"),
    ("Khan Academy - learner home, assignments, mobile keypad", "support.khanacademy.org",
     "https://support.khanacademy.org/hc/en-us/articles/360040168512"),
    ("Mathletics - student view and teacher console", "knowledgebase.mathletics.com",
     "https://knowledgebase.mathletics.com/"),
    ("Prodigy Math - game environment and keypad", "commonsensemedia.org / therocoveringtraditionalist.com",
     "https://www.commonsensemedia.org/app-reviews/prodigy-math-game"),
    ("Quizizz - question screen and authoring", "edutopia.org / askfilo.com",
     "https://www.edutopia.org/article/using-quizizz-engage-students"),
    ("Gama.ir - question library and exam sheet", "gama.ir + Aptoide listing",
     "https://gama.ir/"),
    ("Porsan - question feed and answers", "porsan.app / myket.ir",
     "https://porsan.app/"),
    ("MihanMaktab - course structure (no public UI screenshot)", "mihanmaktab.com",
     "https://mihanmaktab.com/"),
]


def sources(d):
    d.page("Sources, evidence quality and limitations",
           "Every image and number in this report has a dated, clickable source - access date 2025-10-31",
           "10  Sources", "10")
    y = 110
    for title, sub, url in SOURCES:
        d.rrect(M, y, CONTENT_W, 30, 5, fill=PAPER, stroke=HexColor("#EAE5D8"), lw=0.5)
        d.text(M + 12, y + 13, title, 7.2, INK, FB)
        d.text(M + 12, y + 24, sub, 6.2, MUTED)
        short = url.replace("https://", "")
        d.text(PAGE_W - M - 12, y + 18, short, 6.2, HexColor("#2F6FB4"), F, "right")
        d.link(PAGE_W - M - 12 - sw(short, 6.2), y + 9, sw(short, 6.2) + 6, 11, url)
        y += 33
    d.rrect(M, y + 4, CONTENT_W, 92, 6, fill=HexColor("#F7F5EF"))
    d.text(M + 14, y + 22, "Limitations", 8.0, INK, FB)
    bullet(d, M + 16, y + 34, CONTENT_W - 44, [
        "No authenticated access to any product; all flows are inferred from public pages, docs and videos (labelled INFERRED).",
        "Iranian products publish no analytics dashboards; their scores rest on observable UX, not measured data.",
        "MihanMaktab publishes no real interface screenshot - its page is schematic and never used as evidence.",
        "Scores are relative to Roshana's personas, not an absolute ranking of product quality.",
    ], 6.8, 10.2, INK2, CORAL)
    conclusion(d, y + 104, "If this document carries one message: Roshana should not build a bigger library, it "
               "should build the shortest path from a student's need to the right practice - and from there "
               "to a teacher's next action.", "FINAL NOTE")


def build(out=OUT):
    d = enlib.Deck(out)
    cover(d)
    method(d)
    summary(d)
    landscape(d)
    profiles(d)
    evidence_intro(d)
    for key in ORDER:
        imgs, notes = EVIDENCE[key]
        evidence_page(d, key, imgs, notes)
    colour_system(d)
    type_system(d)
    layout_patterns(d)
    dashboards(d)
    dashboard_wire(d)
    practice_anatomy(d)
    personas(d)
    criteria(d)
    matrix(d)
    ranking(d)
    for key in ORDER:
        product_page(d, key)
        product_good_bad(d, key)
    flows(d)
    roshana_flows(d)
    direction(d)
    mvp(d)
    sources(d)
    d.save()
    return d


if __name__ == "__main__":
    d = build()
    print("pages:", d.page_no, "->", OUT)
