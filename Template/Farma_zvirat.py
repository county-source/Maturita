#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROZBOR – Farma zvířat (George Orwell)
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
# FONTY
# ============================================================
fd = "/usr/share/fonts/TTF/"
pdfmetrics.registerFont(TTFont('DJ', os.path.join(fd, 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DJB', os.path.join(fd, 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DJI', os.path.join(fd, 'DejaVuSans-Oblique.ttf')))

# ============================================================
# BARVY
# ============================================================
C_HEADER = HexColor('#212121')
C_GOLD = HexColor('#e2e2e2')

C_INDIGO = HexColor('#283593');    C_INDIGO_L = HexColor('#e8eaf6')
C_BLUE = HexColor('#1565c0');      C_BLUE_L = HexColor('#e3f2fd')
C_TEAL = HexColor('#00897b');      C_TEAL_L = HexColor('#e0f2f1')
C_PURPLE = HexColor('#7b1fa2');    C_PURPLE_L = HexColor('#f3e5f5')
C_RED = HexColor('#c62828');       C_RED_L = HexColor('#ffebee')
C_GREEN = HexColor('#2e7d32');     C_GREEN_L = HexColor('#e8f5e9')
C_ORANGE = HexColor('#e65100');    C_ORANGE_L = HexColor('#fff3e0')
C_DARK = HexColor('#212121');      C_DARK_L = HexColor('#f5f5f5')

C_GRAY = HexColor('#e0e0e0')
C_TIP_BG = HexColor('#fffde7');    C_TIP_BD = HexColor('#fbc02d')

# ============================================================
# ROZMĚRY
# ============================================================
PAGE_W, PAGE_H = A4
MARGIN = 12*mm
W = PAGE_W - 2*MARGIN

# ============================================================
# DATA
# ============================================================
OUTPUT_FILE = "/home/jakub/Maturita/moje-rozbory/Farma_zvirat_rozbor.pdf"

TITLE = "FARMA ZVÍŘAT"
AUTHOR_SUBTITLE = "George Orwell"

AUTHOR_SECTION_TITLE = "AUTOR – GEORGE ORWELL (1903–1950)"
AUTHOR_KV = [
    ("Národnost:", "Britský spisovatel, novinář a esejista"),
    ("Původ:", "Narozen v Mótihári (Britská Indie) jako Eric Arthur Blair. Otec úředník koloniální správy"),
    ("Vzdělání:", "Stipendium na Etonu (prestižní škola). Po škole nešel na univerzitu – vstoupil k policii v Barmě"),
    ("Kariéra:", "1922–1927 koloniální policie v Barmě → znechucení imperialismem. Pak žil v bídě v Paříži a Londýně, psal reportáže"),
    ("Šp. válka:", "1936 bojoval ve Španělské občanské válce proti fašismu. Zraněn střelou do krku. Zážitky → Hold Katalánsku"),
    ("Pseudonym:", "George Orwell – zvolil si ho 1933 (řeka Orwell v Anglii). Vlastní jméno: Eric Arthur Blair"),
    ("Smrt:", "1950 zemřel na tuberkulózu v Londýně, ve věku 46 let"),
]
AUTHOR_WORKS = [
    "<b>Na dně v Paříži a Londýně</b> (1933) – reportáž o životě v bídě",
    "<b>Hold Katalánsku</b> (1938) – zážitky z občanské války ve Španělsku",
    "<b>1984</b> (1949) – antiutopický román, totální kontrola, Velký Bratr",
    "<b>Barmské dny</b> (1934) – román o koloniální Barmě",
]

BASIC_INFO = [
    ("Lit. druh:", "Epika (próza)"),
    ("Lit. žánr:", "Alegorická bajka / antiutopický román (satirická novela)"),
    ("Téma:", "Kritika totalitarismu – revoluce, která zradí vlastní ideály; zvířata svrhnou farmáře, ale prasata se stanou horšími tyrani"),
    ("Časoprostor:", "Panská farma (Manor Farm) v Anglii, 30.–40. léta 20. století (alegoricky dějiny SSSR 1917–1943)"),
    ("Vydáno:", "1945 (psáno za 2. SV, obtížně hledal vydavatele – SSSR byl spojenec)"),
]

COMPOSITION_KV = [
    ("Kompozice:", "10 kapitol, chronologický postup, rámcové prvky (farma na začátku i na konci)"),
    ("Vyprávěč:", "Er-forma – vševědoucí vnější vypravěč, nezúčastněný pozorovatel"),
    ("Promluvy:", "Přímá řeč (projevy prasat, hesla), nepřímá řeč, popisy"),
]
COMPOSITION_BULLETS = [
    "<b>Alegorie (jinotaj)</b> – každé zvíře = reálná postava/skupina z dějin SSSR",
    "<b>Bajka</b> – zvířata jednají jako lidé, text má poučný charakter",
    "<b>Satira a ironie</b> – postupné zrazování revolučních ideálů, měnění přikázání",
    "<b>Gradace</b> – prasata se postupně stávají lidmi (šaty, alkohol, chůze po dvou)",
    "<b>Kontrast</b> – počáteční nadšení z revoluce vs. výsledný teror; heslo „všichni rovni“ vs. realita",
]
TIP_TEXT = "Farma zvířat je alegorií dějin SSSR – každé zvíře odpovídá konkrétní historické postavě nebo skupině. Na zkoušce vysvětli paralely: Napoleon = Stalin, Kuliš = Trockij, Major = Lenin/Marx, psi = tajná policie, ovce = nevzdělaný lid."

MAIN_CHAR_1 = ("Napoleon", "Kanec – hlavní záporná postava. Chytrý, lstivý, málomluvný, mocichtivý. Postupně přebírá veškerou moc, vyžene Kuliše, vychovává psy jako svou tajnou policii. <b>Alegorie Stalina</b> – buduje kult osobnosti, mění pravidla ve svůj prospěch, stává se diktátorem.")
MAIN_CHAR_2 = ("Kuliš", "Kanec – inteligentní, nadšený, plný nápadů (větrný mlýn, vzdělávání). Chce skutečně zlepšit život na farmě. Napoleon ho poštve psy a vyžene. Poté je obviňován ze všech problémů farmy. <b>Alegorie Trockého</b> – revolucionář, který prohrál boj o moc se Stalinem.")

SIDE_CHARACTERS = [
    ("Major", "Starý kanec, respektovaný. Před smrtí vyzve ke vzpouře proti lidem. Alegorie Lenina a Marxe"),
    ("Pištík", "Vepř – Napoleonův propagandista. Manipuluje, překrucuje fakta, přepisuje přikázání. Alegorie sovětské propagandy"),
    ("Boxer", "Tažný kůň – nejpracovitější, oddaný, heslo „Budu pracovat ještě víc!“ Nakonec prodán na jatka. Alegorie prostého pracujícího lidu"),
    ("Molina", "Klisna – marnivá, chce stuhy a cukr. Odejde k lidem. Alegorie buržoazie, která utekla ze SSSR"),
    ("Benjamín", "Osel – cynický, chytrý, ale pasivní. Vše vidí, nic nedělá. Alegorie intelektuálů / autora (Orwell)"),
    ("Ovce", "Tupě opakují hesla „Čtyři nohy dobré, dvě špatné!“. Alegorie manipulované masy"),
    ("Psi", "Napoleonovi bodyguardi. Vychováni od štěňat k poslušnosti. Alegorie tajné policie (NKVD)"),
    ("Pan Jones", "Původní majitel farmy. Opilec, zanedbává zvířata. Alegorie cara Mikuláše II."),
]

PLOT_BLOCKS = [
    ("Vzpoura", "Na Panské farmě starý kanec Major přednese projev o útlaku lidmi a naučí zvířata píseň Zvířata Anglie. Po jeho smrti zvířata vyženou opilého pana Jonese. Farmu přejmenují na Zvířecí farmu. Prasata sepíší 7 přikázání animalismu – hlavní: „Všechna zvířata jsou si rovna.“"),
    ("Budování", "Prasata se ujímají vedení (umí číst a psát). Napoleon a Kuliš se přou o směřování farmy. Kuliš navrhuje stavbu větrného mlýna. Zvířata tvrdě pracují, věří ve společné dobro. Jones se pokusí farmu dobýt zpět – zvířata ho odrazí (Bitva u kravína)."),
    ("Převrat", "Napoleon poštve vycvičené psy na Kuliše a vyžene ho z farmy. Stává se jediným vůdcem. Přikáže stavbu mlýna (Kulišův nápad si přivlastní). Pištík přesvědčuje zvířata, že Kuliš byl od začátku zrádce. Začínají čistky – „zrádci“ jsou popraveni psy. Přikázání se tajně mění."),
    ("Úpadek", "Prasata se stěhují do domu, spí v postelích, pijí alkohol – vše zakázáno, ale přikázání jsou přepsána (např. „nesmí spát v posteli s povlečením“). Boxer se nadře k smrti – Napoleon ho prodá řezníkovi a za peníze koupí whisky. Pištík tvrdí, že Boxer zemřel v nemocnici."),
    ("Závěr", "Prasata chodí po dvou nohách, nosí šaty, obchodují s lidmi. Na farmě visí jediné přikázání: „Všechna zvířata jsou si rovna, ale některá jsou si rovnější.“ Napoleon pozve farmáře na hostinu, hrají poker. Zvířata se dívají oknem a <b>nedokážou rozeznat prasata od lidí</b>."),
]

THEMES = [
    "<b>Zrada revoluce</b> – revoluce požírá vlastní děti; ideály se zvrhnou v novou tyranii",
    "<b>Kritika totalitarismu</b> – konkrétně stalinismu, ale obecně každé diktatury",
    "<b>Propaganda a manipulace</b> – Pištík mění dějiny, přepisuje pravidla, dav tomu věří",
    "<b>Moc korumpuje</b> – „Absolutní moc korumpuje absolutně“ – prasata se stávají tím, proti čemu bojovala",
    "<b>Pasivita mas</b> – ovce tupě opakují hesla, Boxer slepě pracuje, Benjamín nic nedělá",
    "<b>Alegorie SSSR</b> – celý příběh mapuje dějiny od revoluce 1917 po Teheránskou konferenci 1943",
]

CONTEXT_BULLETS = [
    "<b>Antiutopická literatura</b> (dystopie) – 1. polovina 20. století",
    "Reakce na vzestup totalitních režimů (fašismus, stalinismus) ve 20.–40. letech",
    "Varování před zneužitím moci, propagandy a ideologie",
    "Orwell = jeden z nejvýznamnějších autorů politické satiry 20. století",
]
CONTEXT_TABLE = [
    ("G. Orwell", "1984", "Anglie – dystopie"),
    ("A. Huxley", "Konec civilizace", "Anglie – dystopie"),
    ("R. Bradbury", "451 stupňů Fahrenheita", "USA – dystopie"),
    ("W. Golding", "Pán much", "Anglie – alegorie"),
    ("J. Hašek", "Osudy dobrého vojáka Švejka", "ČR – satira"),
]

QUICK_REVIEW = [
    ("Autor", "George Orwell (1903–1950), britský spisovatel, vl. jm. Eric A. Blair"),
    ("Žánr", "Alegorická bajka / antiutopická novela"),
    ("Směr", "Antiutopická literatura, pol. satira (1. pol. 20. stol.)"),
    ("Druh", "Epika (próza)"),
    ("Vyprávěč", "Er-forma (vševědoucí)"),
    ("Kde/kdy", "Panská farma, Anglie, 30.–40. léta (alegoricky SSSR 1917–1943)"),
    ("Téma", "Zrada revoluce, totalitarismus, propaganda"),
    ("Postavy", "Napoleon (Stalin), Kuliš (Trockij), Major (Lenin), Boxer, Pištík"),
    ("Citát", "„Všechna zvířata jsou si rovna, ale některá jsou si rovnější.“"),
    ("Jazyk", "Er-forma, alegorie, satira, ironie, gradace, bajka"),
    ("Kontext", "Orwell (1984), Huxley, Bradbury, Golding"),
]


# ============================================================
# ŠABLONA – generuje PDF z dat výše
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

def sec(text, color):
    t = Table([[Paragraph(text, st_sec)]], colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

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

story.append(make_header())
story.append(sp(6))

# AUTOR
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

# ZÁKLADNÍ ÚDAJE
story.append(KeepTogether([
    sec("ZÁKLADNÍ ÚDAJE O DÍLE", C_BLUE),
    sp(),
    kv(BASIC_INFO, C_BLUE_L, C_BLUE),
]))
story.append(sp(6))

# KOMPOZICE A JAZYK
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

# POSTAVY
char_elements = [
    sec("POSTAVY", C_PURPLE),
    sp(),
    cbox(MAIN_CHAR_1[0], MAIN_CHAR_1[1], C_PURPLE, C_PURPLE_L),
    sp(3),
    cbox(MAIN_CHAR_2[0], MAIN_CHAR_2[1], C_PURPLE, C_PURPLE_L),
    sp(3),
]
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

# DĚJ
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

# HLAVNÍ MYŠLENKY
story.append(KeepTogether([
    sec("HLAVNÍ MYŠLENKY", C_GREEN),
    sp(),
    bl(THEMES, C_GREEN_L),
]))
story.append(sp(6))

# LITERÁRNÍ KONTEXT
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

# RYCHLÝ PŘEHLED
qr_rows = [[
    Paragraph("<b>?</b>", S('QH1', fontName='DJB', fontSize=8, textColor=white, leading=11)),
    Paragraph("<b>Odpověď</b>", S('QH2', fontName='DJB', fontSize=8, textColor=white, leading=11)),
]]
for q, a in QUICK_REVIEW:
    qr_rows.append([Paragraph(q, st_body), Paragraph(a, st_body)])
story.append(KeepTogether([
    sec("RYCHLÝ PŘEHLED", C_DARK),
    sp(),
    Table(qr_rows, colWidths=[24*mm, W - 24*mm],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,0), C_DARK),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_DARK_L, white]),
            ('TOPPADDING', (0,0), (-1,-1), 3.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LINEBELOW', (0,0), (-1,-1), 0.3, C_GRAY),
            ('LINEBEFORE', (1,0), (1,-1), 0.3, C_GRAY),
            ('BOX', (0,0), (-1,-1), 1.5, C_DARK),
        ]),
    ),
]))

# ============================================================
# BUILD
# ============================================================
doc.build(story)
print(f"OK! → {OUTPUT_FILE}")
