# -*- coding: utf-8 -*-
"""Minimal LTR report engine for the English edition (DejaVu + ReportLab)."""
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white
from PIL import Image

PAGE_W, PAGE_H = 841.89, 595.28
M = 34.0
CONTENT_W = PAGE_W - 2 * M

INK = HexColor("#16203A")
INK2 = HexColor("#2B3A5C")
PAPER = HexColor("#FFFFFF")
SOFT = HexColor("#F5F2EA")
LINE = HexColor("#DCD7C9")
MUTED = HexColor("#6E7583")
CORAL = HexColor("#E4572E")
TEAL = HexColor("#1B8A83")
GOLD = HexColor("#D9A03C")
PURPLE = HexColor("#6C4BB6")
BLUE = HexColor("#2F6FB4")
GREEN = HexColor("#3E8E5A")
PLUM = HexColor("#8E3B5E")
RED = HexColor("#C0392B")

REAL, SCHEMA, WIRE = TEAL, HexColor("#B5651D"), PURPLE

FD = "/usr/share/fonts/truetype/dejavu"
F = "DJ"
FB = "DJB"


def register():
    pdfmetrics.registerFont(TTFont(F, os.path.join(FD, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont(FB, os.path.join(FD, "DejaVuSans-Bold.ttf")))


def sw(s, size, bold=False):
    return pdfmetrics.stringWidth(s, FB if bold else F, size)


class Deck:
    def __init__(self, path):
        register()
        self.c = canvas.Canvas(path, pagesize=(PAGE_W, PAGE_H))
        self.c.setTitle("Roshana - Visual UX/UI Competitive Benchmark (English edition)")
        self.c.setAuthor("Roshana Product Design Research")
        self.c.setSubject("Visual UX/UI benchmark of 8 learning products against Roshana personas")
        self.page_no = 0
        self.chapter = ""
        self.chapter_no = ""

    # ---------------------------------------------------------------- basics
    def Y(self, y):
        return PAGE_H - y

    def text(self, x, y, s, size=9, color=INK, font=None, align="left"):
        c = self.c
        c.setFont(font or F, size)
        c.setFillColor(color)
        yp = self.Y(y)
        if align == "right":
            c.drawRightString(x, yp, s)
        elif align == "center":
            c.drawCentredString(x, yp, s)
        else:
            c.drawString(x, yp, s)
        return y

    def wrap(self, s, w, size=9, bold=False):
        font = FB if bold else F
        words = s.split(" ")
        lines, cur = [], ""
        for wd in words:
            trial = (cur + " " + wd).strip()
            if pdfmetrics.stringWidth(trial, font, size) <= w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = wd
        if cur:
            lines.append(cur)
        return lines

    def para(self, x, y, w, s, size=9, leading=None, color=INK2, bold=False,
             align="left", max_lines=None):
        leading = leading or size * 1.55
        lines = self.wrap(s, w, size, bold)
        if max_lines:
            lines = lines[:max_lines]
        yy = y
        for ln in lines:
            if align == "center":
                self.text(x + w / 2, yy, ln, size, color, FB if bold else F, "center")
            elif align == "right":
                self.text(x + w, yy, ln, size, color, FB if bold else F, "right")
            else:
                self.text(x, yy, ln, size, color, FB if bold else F)
            yy += leading
        return yy

    def fit_text(self, x, y, w, s, size=6.4, color=MUTED, font=None, align="left"):
        f = font or F
        if self.c.stringWidth(s, f, size) > w:
            while s and self.c.stringWidth(s + "\u2026", f, size) > w:
                s = s[:-1]
            s = s.rstrip(" /,.") + "\u2026"
        if align == "right":
            self.text(x, y, s, size, color, f, "right")
        else:
            self.text(x, y, s, size, color, f)
        return s

    def para_h(self, s, w, size=9, leading=None, bold=False):
        leading = leading or size * 1.55
        return len(self.wrap(s, w, size, bold)) * leading

    def rect(self, x, y, w, h, fill=None, stroke=None, lw=0.7):
        c = self.c
        c.saveState()
        if fill is not None:
            c.setFillColor(fill)
        if stroke is not None:
            c.setStrokeColor(stroke)
            c.setLineWidth(lw)
        c.rect(x, self.Y(y) - h, w, h,
               stroke=1 if stroke is not None else 0,
               fill=1 if fill is not None else 0)
        c.restoreState()

    def rrect(self, x, y, w, h, r=6, fill=None, stroke=None, lw=0.7):
        c = self.c
        c.saveState()
        if fill is not None:
            c.setFillColor(fill)
        if stroke is not None:
            c.setStrokeColor(stroke)
            c.setLineWidth(lw)
        c.roundRect(x, self.Y(y) - h, w, h, r,
                    stroke=1 if stroke is not None else 0,
                    fill=1 if fill is not None else 0)
        c.restoreState()

    def line(self, x1, y1, x2, y2, color=LINE, lw=0.7, dash=None):
        c = self.c
        c.saveState()
        c.setStrokeColor(color)
        c.setLineWidth(lw)
        if dash:
            c.setDash(dash)
        c.line(x1, self.Y(y1), x2, self.Y(y2))
        c.restoreState()

    def circle(self, x, y, r, fill=INK, stroke=None):
        c = self.c
        c.saveState()
        c.setFillColor(fill)
        if stroke is not None:
            c.setStrokeColor(stroke)
            c.setLineWidth(0.6)
        c.circle(x, self.Y(y), r, stroke=1 if stroke else 0, fill=1)
        c.restoreState()

    def image(self, path, x, y, w, h, border=True, contain=True):
        if path.lower().endswith(".webp"):
            path = _as_png(path)
        im = Image.open(path)
        iw, ih = im.size
        if contain:
            sc = min(w / iw, h / ih)
            dw, dh = iw * sc, ih * sc
            dx, dy = x + (w - dw) / 2, y + (h - dh) / 2
        else:
            dx, dy, dw, dh = x, y, w, h
        self.c.drawImage(path, dx, self.Y(dy) - dh, dw, dh, mask="auto")
        if border:
            self.rect(dx - 0.5, dy - 0.5, dw + 1, dh + 1, stroke=HexColor("#E4DFD2"), lw=0.5)
        return dx, dy, dw, dh

    # ---------------------------------------------------------------- pages
    def page(self, title=None, kicker=None, chapter=None, chapter_no=None, footer=True):
        if self.page_no:
            self.c.showPage()
        self.page_no += 1
        if chapter is not None:
            self.chapter = chapter
        if chapter_no is not None:
            self.chapter_no = chapter_no
        self.c.setFillColor(PAPER)
        self.c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        if title:
            self.text(PAGE_W - M, 24, self.chapter, 7.2, MUTED, F, "right")
            self.text(M, 24, "Roshana - Visual UX/UI Benchmark", 7.2, MUTED)
            self.text(M, 62, title, 19.5, INK, FB)
            if kicker:
                self.text(M, 80, kicker, 8.2, MUTED)
            self.line(M, 92, PAGE_W - M, 92, LINE, 0.8)
        if footer:
            self.line(M, 566, PAGE_W - M, 566, HexColor("#EDE8DA"), 0.6)
            self.text(M, 578, "Roshana  |  Visual UX/UI Competitive Benchmark  |  English edition  |  data collected 2025-10-31",
                      6.6, MUTED)
            self.text(PAGE_W - M, 578, "%02d" % self.page_no, 7.4, HexColor("#9AA0AC"), F, "right")

    def link(self, x, y, w, h, url):
        self.c.linkURL(url, (x, self.Y(y) - h, x + w, self.Y(y)), relative=0, thickness=0)

    def save(self):
        self.c.showPage()
        self.c.save()


# ---------------------------------------------------------------- components
def tag(d, x, y, kind, align="left"):
    """Evidence tag: REAL / SCHEMATIC / ROSHANA WIREFRAME."""
    conf = {"real": ("REAL PRODUCT SCREENSHOT", REAL, "actual UI"),
            "schematic": ("SCHEMATIC RECONSTRUCTION", SCHEMA, "re-drawn"),
            "wire": ("ROSHANA WIREFRAME", WIRE, "proposed")}
    en, col, _ = conf[kind]
    w = sw(en, 6.0, True) + 14
    x0 = x if align == "left" else x - w
    d.rrect(x0, y, w, 15, 3, fill=col)
    d.text(x0 + 7, y + 10.6, en, 6.0, white, FB)
    return w


def chip(d, x, y, label, col=INK2, size=6.6, pad=7, h=15):
    w = sw(label, size) + 2 * pad
    d.rrect(x, y, w, h, h / 2, fill=None, stroke=HexColor("#D9D3C4"), lw=0.6)
    d.text(x + pad, y + h / 2 + 2.3, label, size, col)
    return w


def bullet(d, x, y, w, items, size=7.4, leading=11.6, col=INK2, dot=TEAL, gap=3):
    yy = y
    for it in items:
        d.circle(x + 2.6, yy + 3.0, 2.2, fill=dot)
        yy = d.para(x + 11, yy, w - 11, it, size, leading, col) + gap
    return yy


def find(d, x, y, s, size, sub, col):
    """String with a coloured substring, LTR simple."""
    i = s.find(sub)
    if i < 0:
        d.text(x, y, s, size, INK2)
        return
    d.text(x, y, s[:i], size, INK2)
    x1 = x + sw(s[:i], size)
    d.text(x1, y, sub, size, col, FB)
    d.text(x1 + sw(sub, size, True), y, s[i + len(sub):], size, INK2)


def conclusion(d, y, body, tag_label="TAKEAWAY", color=CORAL, h=44):
    d.rrect(M, y, CONTENT_W, h, 6, fill=HexColor("#FBF1EC"))
    d.rect(M + CONTENT_W - 3.5, y + 8, 3.5, h - 16, fill=color)
    d.text(M + 12, y + 15, tag_label, 6.2, color, FB)
    d.para(M + 16, y + 28, CONTENT_W - 60, body, 7.6, 11.2, HexColor("#4A3B34"))


def _as_png(path):
    out = "/tmp/_en_" + os.path.basename(path).replace(".webp", ".png")
    if not os.path.exists(out):
        Image.open(path).convert("RGB").save(out, "PNG")
    return out


def bar(d, x, y, w, v, col, h=6, bg=HexColor("#EDE8DA")):
    d.rrect(x, y, w, h, h / 2, fill=bg)
    d.rrect(x, y, w * v, h, h / 2, fill=col)
