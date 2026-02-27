#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ŠABLONA – Literární rozbor cheat sheet (maturita)
==================================================
Tento skript generuje 3stránkové PDF rozbory literárních děl.
Stačí vyplnit DATA sekci dole a spustit.

Výstup: A4 PDF, DejaVu fonty, 8barevná paleta, ReportLab.
Struktura: Header → Autor → Základní údaje → Kompozice a jazyk → TIP →
           Postavy (2 hlavní boxy + tabulka) → Děj (bloky) →
           Hlavní myšlenky → Literární kontext + tabulka → Rychlý přehled
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ============================================================
# FONTY – DejaVu (podpora češtiny)
# ============================================================
fd = "/usr/share/fonts/TTF/"
pdfmetrics.registerFont(TTFont('DJ', os.path.join(fd, 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DJB', os.path.join(fd, 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DJI', os.path.join(fd, 'DejaVuSans-Oblique.ttf')))

# ============================================================
# BARVY – 8 sekcí, každá má tmavou + světlou variantu
# ============================================================
C_HEADER = HexColor('#212121')       # Hlavička dokumentu (tmavě šedá/černá)
C_GOLD = HexColor('#e2e2e2')         # Podtitulek v hlavičce

C_INDIGO = HexColor('#283593');    C_INDIGO_L = HexColor('#e8eaf6')   # AUTOR
C_BLUE = HexColor('#1565c0');      C_BLUE_L = HexColor('#e3f2fd')     # ZÁKLADNÍ ÚDAJE
C_TEAL = HexColor('#00897b');      C_TEAL_L = HexColor('#e0f2f1')     # KOMPOZICE A JAZYK
C_PURPLE = HexColor('#7b1fa2');    C_PURPLE_L = HexColor('#f3e5f5')   # POSTAVY
C_RED = HexColor('#c62828');       C_RED_L = HexColor('#ffebee')      # DĚJ
C_GREEN = HexColor('#2e7d32');     C_GREEN_L = HexColor('#e8f5e9')    # HLAVNÍ MYŠLENKY
C_ORANGE = HexColor('#e65100');    C_ORANGE_L = HexColor('#fff3e0')   # LITERÁRNÍ KONTEXT
C_DARK = HexColor('#212121');      C_DARK_L = HexColor('#f5f5f5')     # RYCHLÝ PŘEHLED

C_GRAY = HexColor('#e0e0e0')          # Oddělovací čáry v tabulkách
C_TIP_BG = HexColor('#fffde7');    C_TIP_BD = HexColor('#fbc02d')     # TIP box

# ============================================================
# ROZMĚRY
# ============================================================
PAGE_W, PAGE_H = A4
MARGIN = 12*mm
W = PAGE_W - 2*MARGIN

# ============================================================
# ████████████████████████████████████████████████████████████
# ████  DATA – ZDE VYPLŇ OBSAH PRO KONKRÉTNÍ DÍLO  ██████████
# ████████████████████████████████████████████████████████████
# ============================================================

# --- Výstupní soubor ---
OUTPUT_FILE = "/home/jakub/Maturita/moje-rozbory/XX_Nazev_rozbor.pdf"

# --- Hlavička ---
TITLE = "NÁZEV DÍLA"           # velký nadpis
AUTHOR_SUBTITLE = "Jméno Autora"  # kurzívou pod nadpisem

# --- Sekce AUTOR ---
AUTHOR_SECTION_TITLE = "AUTOR – JMÉNO AUTORA (rok–rok)"
AUTHOR_KV = [
    # (klíč, hodnota) – podporuje <b>tučné</b> v hodnotě
    ("Národnost:", "..."),
    ("Vzdělání:", "..."),
    ("Kariéra:", "..."),
    ("Osobní:", "..."),
    ("Smrt:", "..."),
    ("Zajímavost:", "..."),
]
AUTHOR_WORKS = [
    # bullet pointy s dalšími díly, <b>tučné</b> pro kategorie
    "<b>Dramata:</b> ...",
    "<b>Romány:</b> ...",
    "<b>Povídky:</b> ...",
]

# --- Sekce ZÁKLADNÍ ÚDAJE ---
BASIC_INFO = [
    ("Lit. druh:", "Epika / Drama / Lyrika"),
    ("Lit. žánr:", "..."),
    ("Téma:", "..."),
    ("Časoprostor:", "..."),
    ("Vydáno:", "rok, okolnosti"),
]

# --- Sekce KOMPOZICE A JAZYK ---
COMPOSITION_KV = [
    ("Kompozice:", "..."),
    ("Vyprávěč:", "ich-forma / er-forma / ..."),
    ("Promluvy:", "přímá řeč, dialogy, ..."),
]
COMPOSITION_BULLETS = [
    # odrážky pod KV tabulkou
    "<b>Jazyk</b> – ...",
    "<b>Kontrast</b> – ...",
    "<b>Gradace</b> – ...",
]
TIP_TEXT = "Tip pro ústní zkoušku – klíčová informace k zapamatování."

# --- Sekce POSTAVY ---
# 2 hlavní postavy (velké boxy)
MAIN_CHAR_1 = ("Jméno 1", "Popis hlavní postavy s <b>tučnými</b> klíčovými slovy.")
MAIN_CHAR_2 = ("Jméno 2", "Popis druhé hlavní postavy.")
# Vedlejší postavy (tabulka)
SIDE_CHARACTERS = [
    # (jméno, popis)
    ("Postava A", "Krátký popis"),
    ("Postava B", "Krátký popis"),
    ("Postava C", "Krátký popis"),
    ("Postava D", "Krátký popis"),
]

# --- Sekce DĚJ ---
PLOT_BLOCKS = [
    # (nadpis bloku, text děje) – 4–5 bloků
    ("Úvod / Expozice", "Co se děje na začátku..."),
    ("Zápletka", "Hlavní konflikt..."),
    ("Vyvrcholení", "Klimax příběhu..."),
    ("Závěr", "Rozuzlení..."),
]

# --- Sekce HLAVNÍ MYŠLENKY ---
THEMES = [
    "<b>Hlavní téma</b> – vysvětlení",
    "<b>Další téma</b> – vysvětlení",
    "<b>Další téma</b> – vysvětlení",
]

# --- Sekce LITERÁRNÍ KONTEXT ---
CONTEXT_BULLETS = [
    "<b>Směr/období</b> (doplnit)",
    "Zařazení autora...",
    "Další kontext...",
]
CONTEXT_TABLE = [
    # (autor, dílo, kontext/země)
    ("Autor 1", "Dílo 1", "Země/směr"),
    ("Autor 2", "Dílo 2", "Země/směr"),
    ("Autor 3", "Dílo 3", "Země/směr"),
]

# --- Sekce RYCHLÝ PŘEHLED ---
QUICK_REVIEW = [
    # (otázka, odpověď)
    ("Autor", "Jméno (rok–rok), národnost"),
    ("Žánr", "..."),
    ("Směr", "..."),
    ("Druh", "Epika / Drama / Lyrika"),
    ("Vyprávěč", "ich-forma / er-forma / drama"),
    ("Kde/kdy", "místo, čas"),
    ("Téma", "..."),
    ("Postavy", "výčet klíčových postav"),
    ("Klíčové", "nejdůležitější fakt k zapamatování"),
    ("Jazyk", "..."),
    ("Kontext", "autoři stejného směru/období"),
]


# ============================================================
# ████████████████████████████████████████████████████████████
# ████  ŠABLONA – NEMĚNIT (generuje PDF z dat výše)  ████████
# ████████████████████████████████████████████████████████████
# ============================================================

doc = SimpleDocTemplate(
    OUTPUT_FILE, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=MARGIN, bottomMargin=MARGIN,
)

def S(name, **kw):
    d = dict(fontName='DJ', fontSize=8, textColor=black, leading=11, spaceBefore=0, spaceAfter=0)
    d.update(kw)
    return ParagraphStyle(name, **d)

st_title = S('T', fontName='DJB', fontSize=22, textColor=white, alignment=TA_CENTER, leading=26)
st_author = S('A', fontName='DJI', fontSize=11, textColor=C_GOLD, alignment=TA_CENTER, leading=14)
st_sec = S('Sec', fontName='DJB', fontSize=10.5, textColor=white, leading=13)
st_body = S('B')
st_key = S('K', fontName='DJB', fontSize=8, textColor=HexColor('#1a1a2e'), leading=11)
st_small = S('Sm', fontSize=7.5, leading=10)
st_smallb = S('SmB', fontName='DJB', fontSize=7.5, leading=10)
st_tip = S('Tip', fontName='DJI', fontSize=7.5, textColor=HexColor('#b33600'), leading=10)
st_wh = S('WH', fontName='DJB', fontSize=7.5, textColor=white, leading=10)
st_plot_b = S('PB', fontSize=7.5, alignment=TA_JUSTIFY, leading=10.5)

story = []
sp = lambda h=4: Spacer(1, h)

# --- Helper: hlavička dokumentu ---
def make_header():
    t = Table([
        [Paragraph(TITLE, st_title)],
        [Paragraph(AUTHOR_SUBTITLE, st_author)],
    ], colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_HEADER),
        ('TOPPADDING', (0,0), (-1,0), 12),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 10),
    ]))
    return t

# --- Helper: barevný nadpis sekce ---
def sec(text, color):
    t = Table([[Paragraph(text, st_sec)]], colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

# --- Helper: klíč-hodnota tabulka ---
def kv(pairs, bg, border, kw=36*mm):
    rows = [[Paragraph(f"<b>{k}</b>", st_key), Paragraph(v, st_body)] for k, v in pairs]
    t = Table(rows, colWidths=[kw, W - kw])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (0,-1), 8),
        ('LEFTPADDING', (1,0), (1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-2), 0.5, C_GRAY),
        ('BOX', (0,0), (-1,-1), 1.2, border),
    ]))
    return t

# --- Helper: bullet list ---
def bl(items, bg, mark="\u2022"):
    rows = [[Paragraph(f"{mark} {i}", st_body)] for i in items]
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

# --- Helper: TIP box ---
def tipbox(text):
    t = Table([[Paragraph(f"<b>TIP:</b> {text}", st_tip)]], colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_TIP_BG),
        ('BOX', (0,0), (-1,-1), 1, C_TIP_BD),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

# --- Helper: character box (hlavní postava) ---
def cbox(name, desc, col, bg):
    t = Table([[
        Paragraph(f"<b>{name}</b>", S(f'c{id(name)}', fontName='DJB', fontSize=8.5, textColor=col, leading=11)),
        Paragraph(desc, st_body),
    ]], colWidths=[28*mm, W - 28*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (1,0), (1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 0.7, col),
    ]))
    return t


# ============================================================
# SESTAVENÍ DOKUMENTU
# ============================================================

# ---- HLAVIČKA ----
story.append(make_header())
story.append(sp(6))

# ---- AUTOR ----
story.append(KeepTogether([
    sec(AUTHOR_SECTION_TITLE, C_INDIGO),
    sp(),
    kv(AUTHOR_KV, C_INDIGO_L, C_INDIGO),
]))
story.append(sp(3))
story.append(KeepTogether([
    Paragraph("<b>Další díla:</b>", S('DA', fontName='DJB', textColor=C_INDIGO)),
    sp(2),
    bl(AUTHOR_WORKS, C_INDIGO_L),
]))
story.append(sp(6))

# ---- ZÁKLADNÍ ÚDAJE ----
story.append(KeepTogether([
    sec("ZÁKLADNÍ ÚDAJE O DÍLE", C_BLUE),
    sp(),
    kv(BASIC_INFO, C_BLUE_L, C_BLUE),
]))
story.append(sp(6))

# ---- KOMPOZICE A JAZYK ----
story.append(KeepTogether([
    sec("KOMPOZICE A JAZYK", C_TEAL),
    sp(),
    kv(COMPOSITION_KV, C_TEAL_L, C_TEAL),
    sp(3),
    bl(COMPOSITION_BULLETS, C_TEAL_L),
    sp(3),
    tipbox(TIP_TEXT),
]))
story.append(sp(6))

# ---- POSTAVY ----
char_elements = [
    sec("POSTAVY", C_PURPLE),
    sp(),
    cbox(MAIN_CHAR_1[0], MAIN_CHAR_1[1], C_PURPLE, C_PURPLE_L),
    sp(3),
    cbox(MAIN_CHAR_2[0], MAIN_CHAR_2[1], C_PURPLE, C_PURPLE_L),
    sp(3),
]
# Tabulka vedlejších postav
char_rows = [[Paragraph("<b>Postava</b>", st_wh), Paragraph("<b>Popis</b>", st_wh)]]
for name, desc in SIDE_CHARACTERS:
    char_rows.append([Paragraph(f"<b>{name}</b>", st_smallb), Paragraph(desc, st_small)])
char_elements.append(
    Table(char_rows, colWidths=[25*mm, W - 25*mm],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,0), C_PURPLE),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, C_PURPLE_L]),
            ('TOPPADDING', (0,0), (-1,-1), 2.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LINEBELOW', (0,1), (-1,-2), 0.3, C_GRAY),
            ('BOX', (0,0), (-1,-1), 1, C_PURPLE),
        ]),
    )
)
story.append(KeepTogether(char_elements))
story.append(sp(6))

# ---- DĚJ ----
story.append(sec("DĚJ", C_RED))
story.append(sp())
for title, text in PLOT_BLOCKS:
    story.append(KeepTogether([
        Table(
            [[
                Paragraph(f"<b>{title}</b>", S(f'p{id(title)}', fontName='DJB', fontSize=8, textColor=C_RED, leading=11)),
                Paragraph(text, st_plot_b),
            ]],
            colWidths=[28*mm, W - 28*mm],
            style=TableStyle([
                ('BACKGROUND', (0,0), (0,-1), C_RED_L),
                ('BACKGROUND', (1,0), (1,-1), HexColor('#fffafa')),
                ('TOPPADDING', (0,0), (-1,-1), 4),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('RIGHTPADDING', (1,0), (1,-1), 6),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('BOX', (0,0), (-1,-1), 0.5, C_RED),
            ]),
        ),
        sp(2),
    ]))
story.append(sp(4))

# ---- HLAVNÍ MYŠLENKY ----
story.append(KeepTogether([
    sec("HLAVNÍ MYŠLENKY", C_GREEN),
    sp(),
    bl(THEMES, C_GREEN_L),
]))
story.append(sp(6))

# ---- LITERÁRNÍ KONTEXT ----
ctx_rows = [[Paragraph("<b>Autor</b>", st_wh), Paragraph("<b>Dílo</b>", st_wh), Paragraph("<b>Kontext</b>", st_wh)]]
for a, d, c in CONTEXT_TABLE:
    ctx_rows.append([Paragraph(f"<b>{a}</b>", st_smallb), Paragraph(d, st_small), Paragraph(c, st_small)])
story.append(KeepTogether([
    sec("LITERÁRNÍ KONTEXT", C_ORANGE),
    sp(),
    bl(CONTEXT_BULLETS, C_ORANGE_L),
    sp(3),
    Table(ctx_rows, colWidths=[25*mm, W - 45*mm, 20*mm],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,0), C_ORANGE),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, C_ORANGE_L]),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BOX', (0,0), (-1,-1), 1, C_ORANGE),
            ('LINEBELOW', (0,1), (-1,-2), 0.3, C_GRAY),
        ]),
    ),
]))
story.append(sp(6))

# ---- RYCHLÝ PŘEHLED ----
qr_rows = [[
    Paragraph("<b>?</b>", S('QH1', fontName='DJB', fontSize=8, textColor=white, leading=11)),
    Paragraph("<b>Odpověď</b>", S('QH2', fontName='DJB', fontSize=8, textColor=white, leading=11)),
]]
for q, a in QUICK_REVIEW:
    qr_rows.append([Paragraph(q, st_body), Paragraph(a, st_body)])
story.append(KeepTogether([
    sec("RYCHLÝ PŘEHLED", C_DARK),
    sp(),
    Table(qr_rows, colWidths=[22*mm, W - 22*mm],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,0), C_DARK),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_DARK_L, white]),
            ('TOPPADDING', (0,0), (-1,-1), 3.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LINEBELOW', (0,1), (-1,-2), 0.3, C_GRAY),
            ('BOX', (0,0), (-1,-1), 1.5, C_DARK),
        ]),
    ),
]))

# ============================================================
# BUILD
# ============================================================
doc.build(story)
print(f"OK! → {OUTPUT_FILE}")