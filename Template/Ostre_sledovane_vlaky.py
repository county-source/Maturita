#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROZBOR – Ostře sledované vlaky (Bohumil Hrabal)
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
OUTPUT_FILE = "/home/jakub/Maturita/moje-rozbory/Ostre_sledovane_vlaky_rozbor.pdf"

TITLE = "OSTŘE SLEDOVANÉ VLAKY"
AUTHOR_SUBTITLE = "Bohumil Hrabal"

AUTHOR_SECTION_TITLE = "AUTOR \u2013 BOHUMIL HRABAL (1914\u20131997)"
AUTHOR_KV = [
    ("N\u00e1rodnost:", "Nejv\u00fdznamn\u011bj\u0161\u00ed \u010desk\u00fd spisovatel 2. poloviny 20. stolet\u00ed, nejp\u0159ekl\u00e1dan\u011bj\u0161\u00ed \u010desk\u00fd autor"),
    ("P\u016fvod:", "Narozen v Brn\u011b-\u017didenic\u00edch, vyr\u016fstal v Nymburku (otec spr\u00e1vce pivovaru)"),
    ("Vzd\u011bl\u00e1n\u00ed:", "Pr\u00e1vnick\u00e1 fakulta UK v Praze \u2013 dokon\u010dil a\u017e po v\u00e1lce (1946). Studoval i filozofii a liter\u00e1rn\u00ed v\u011bdu"),
    ("Povol\u00e1n\u00ed:", "Za v\u00e1lky \u017eelezni\u010dn\u00ed d\u011bln\u00edk a v\u00fdprav\u010d\u00ed (inspirace pro OSV!). Pak d\u011bln\u00edk v ocel\u00e1rn\u00e1ch, bali\u010d star\u00e9ho pap\u00edru"),
    ("Tvorba:", "Od 1963 se v\u011bnoval pouze psan\u00ed. \u010clen Svazu \u010ds. spisovatel\u016f"),
    ("Normalizace:", "Po 1970 z\u00e1kaz publikov\u00e1n\u00ed \u2192 samizdatov\u00e9 a exilov\u00e9 vyd\u00e1v\u00e1n\u00ed. Od 1975 sm\u011bl op\u011bt (cenzurovan\u011b) vyd\u00e1vat"),
    ("Smrt:", "1997 p\u00e1d z okna nemocnice na Bulovce v Praze (p\u0159i krmen\u00ed holub\u016f). Ud\u011blena medaile Za z\u00e1sluhy"),
]
AUTHOR_WORKS = [
    "<b>P\u00e1bitel\u00e9</b> (1964) \u2013 pov\u00eddky, typick\u00fd hrabalovsk\u00fd humor a p\u00e1ben\u00ed",
    "<b>Post\u0159i\u017einy</b> (1976) \u2013 novela o \u017eivot\u011b v nymbursk\u00e9m pivovaru",
    "<b>Obsluhoval jsem anglick\u00e9ho kr\u00e1le</b> (1971, sam.) \u2013 rom\u00e1n, \u010d\u00ed\u0161n\u00edk Dit\u011b a jeho \u017eivotn\u00ed p\u0159\u00edb\u011bh",
    "<b>Slavnosti sn\u011b\u017eenek</b> (1978) \u2013 pov\u00eddkov\u00fd soubor, chatov\u00e1 oblast",
    "<b>P\u0159\u00edli\u0161 hlu\u010dn\u00e1 samota</b> (1976, sam.) \u2013 filosofick\u00e1 novela o bali\u010di star\u00e9ho pap\u00edru",
]

BASIC_INFO = [
    ("Lit. druh:", "Epika (pr\u00f3za)"),
    ("Lit. \u017e\u00e1nr:", "Tragikomick\u00e1 novela (kr\u00e1tk\u00fd rom\u00e1n)"),
    ("T\u00e9ma:", "Dosp\u00edv\u00e1n\u00ed mlad\u00e9ho mu\u017ee na pozad\u00ed v\u00e1lky; sou\u017eit\u00ed velk\u00fdch d\u011bjin s mal\u00fdmi lidsk\u00fdmi osudy"),
    ("\u010casoprostor:", "Mal\u00e1 \u017eelezni\u010dn\u00ed stanice (Kostomlaty) v Protektor\u00e1tu \u010cechy a Morava, \u00fanor 1945"),
    ("Vyd\u00e1no:", "1965. Zfilmov\u00e1no 1966 (re\u017eis\u00e9r Ji\u0159\u00ed Menzel) \u2013 Oscar za nejlep\u0161\u00ed cizojazyčn\u00fd film (1968)"),
]

COMPOSITION_KV = [
    ("Kompozice:", "6 kapitol, kombinace chronologick\u00e9ho a retrospektivn\u00edho postupu"),
    ("Vypr\u00e1v\u011b\u010d:", "Ich-forma \u2013 vypr\u00e1v\u00ed s\u00e1m Milo\u0161 Hrma (subjektivn\u00ed pohled, d\u016fv\u011brn\u00fd t\u00f3n)"),
    ("Promluvy:", "P\u0159\u00edm\u00e1 \u0159e\u010d, nevlastn\u00ed p\u0159\u00edm\u00e1 \u0159e\u010d, vnit\u0159n\u00ed monolog, dialog"),
]
COMPOSITION_BULLETS = [
    "<b>Proud v\u011bdom\u00ed</b> \u2013 dlouh\u00e1 souv\u011bt\u00ed, voln\u011b plynouc\u00ed my\u0161lenky (typick\u00fd Hrabal\u016fv styl)",
    "<b>Tragikomika</b> \u2013 sm\u00edch a trag\u00e9die se prol\u00ednaj\u00ed; banality vedle v\u00e1le\u010dn\u00fdch hr\u016fz",
    "<b>Retrospektivn\u00ed vsuvky</b> \u2013 Milo\u0161 vzpom\u00edn\u00e1 na rodinu, dal\u0161\u00ed \u010dlenov\u00e9 rodu (d\u011bda hypnotiz\u00e9r, str\u00fdc, otec)",
    "<b>Kontrast</b> \u2013 mal\u00fd sv\u011bt stanice vs. velk\u00e1 v\u00e1lka; intimn\u00ed probl\u00e9my vs. d\u011bjiny",
    "<b>Hovorov\u00fd jazyk</b> \u2013 n\u00e1dra\u017e\u00e1ck\u00fd slang, p\u0159irozen\u00e9 dialogy, m\u00edstn\u00ed kolorit",
]
TIP_TEXT = "Kl\u00ed\u010dov\u00e9 je pochopit kontrast: Milo\u0161\u016fv osobn\u00ed probl\u00e9m (sexu\u00e1ln\u00ed selh\u00e1n\u00ed, dosp\u00edv\u00e1n\u00ed) prob\u00edh\u00e1 na pozad\u00ed v\u00e1lky. Hrabal ukazuje, \u017ee i ve v\u00e1lce lid\u00e9 \u0159e\u0161\u00ed b\u011b\u017en\u00e9 lidsk\u00e9 starosti. Film z\u00edskal Oscara (1968, re\u017eis\u00e9r Ji\u0159\u00ed Menzel)."

MAIN_CHAR_1 = ("Milo\u0161 Hrma", "Mlad\u00fd (22 let), citliv\u00fd, naivn\u00ed v\u00fdprav\u010d\u00ed-elév. Trp\u00ed sebev\u011bdom\u00edm a <b>sexu\u00e1ln\u00edm selh\u00e1n\u00edm</b> s p\u0159\u00edtelkyn\u00ed M\u00e1\u0161ou \u2013 pokusí se o sebevra\u017edu (pod\u0159ez\u00e1n\u00ed \u017eil). B\u011bhem d\u011bje dozr\u00e1v\u00e1 v mu\u017ee (d\u00edky Viktorii). Nakonec hrdinsky vhod\u00ed bombu do n\u011bmeck\u00e9ho transportu, ale je zast\u0159elen.")
MAIN_CHAR_2 = ("Hubi\u010dka", "Sv\u00e9r\u00e1zn\u00fd v\u00fdprav\u010d\u00ed, zku\u0161en\u00fd sv\u016fdn\u00edk \u017een. Nen\u00e1vid\u00ed N\u011bmce. <b>Organizuje sabotá\u017e</b> proti n\u011bmeck\u00e9mu transportu. Potiskne \u00fa\u0159edn\u00edmi raz\u00edtky zadn\u00ed \u010d\u00e1st t\u011bla telegrafistky Zdeni\u010dky \u2013 absurdn\u00ed sc\u00e9na, kter\u00e1 je p\u0159edm\u011btem vy\u0161et\u0159ov\u00e1n\u00ed.")

SIDE_CHARACTERS = [
    ("P\u0159ednosta", "Vedouc\u00ed stanice \u2013 ambici\u00f3zn\u00ed, hodn\u00fd. Zbo\u017e\u0148uje holuby, p\u011bstuje je. Star\u00e1 se o hladk\u00fd chod stanice"),
    ("M\u00e1\u0161a", "Milo\u0161ova p\u0159\u00edtelkyn\u011b, pr\u016fvod\u010d\u00ed. Mil\u00e1 a trp\u011bliv\u00e1. Milo\u0161 s n\u00ed pro\u017e\u00edv\u00e1 sv\u016fj prvn\u00ed neúsp\u011bch"),
    ("Viktorie Freie", "Kr\u00e1sn\u00e1 Raku\u0161anka, spojka pro odboj. P\u0159inese v\u00fdbu\u0161ninu. Z Milo\u0161e se stane mu\u017e (kl\u00ed\u010dov\u00fd moment)"),
    ("Zdeni\u010dka Svat\u00e1", "Mlad\u00e1 telegrafistka. Nech\u00e1 se sv\u00e9st Hubi\u010dkou \u2013 potisknuta raz\u00edtky (komick\u00e1 sc\u00e9na)"),
    ("Zedn\u00ed\u010dek", "Kolaborant s N\u011bmci, \u010dlen rady. Vy\u0161et\u0159uje p\u0159\u00edpad Hubi\u010dky a Zdeni\u010dky"),
]

PLOT_BLOCKS = [
    ("N\u00e1vrat do slu\u017eby", "Mlad\u00fd v\u00fdprav\u010d\u00ed Milo\u0161 Hrma se vrac\u00ed na malou \u017eelezni\u010dn\u00ed stanici po pobytu v nemocnici \u2013 pokusil se o sebevra\u017edu pod\u0159ez\u00e1n\u00edm \u017eil. D\u016fvodem bylo sexu\u00e1ln\u00ed selh\u00e1n\u00ed s p\u0159\u00edtelkyn\u00ed M\u00e1\u0161ou. Na stanici pracuje s v\u00fdprav\u010d\u00edm Hubi\u010dkou a p\u0159ednostou."),
    ("Aféra s raz\u00edtky", "V\u00fdprav\u010d\u00ed Hubi\u010dka v noci potiskne \u00fa\u0159edn\u00edmi raz\u00edtky zadn\u00ed \u010d\u00e1st t\u011bla telegrafistky Zdeni\u010dky Svat\u00e9. P\u0159ij\u00ed\u017ed\u00ed rada Zedn\u00ed\u010dek, kolaborant s N\u011bmci, vyšet\u0159ovat p\u0159estupek. Hubi\u010dka je nakonec shled\u00e1n nevinn\u00fdm. Absurdn\u011b komick\u00e1 sc\u00e9na na pozad\u00ed v\u00e1lky."),
    ("Dozr\u00e1v\u00e1n\u00ed", "Milo\u0161e tr\u00e1p\u00ed jeho probl\u00e9m. Retrospektivn\u011b vzpom\u00edn\u00e1 na svou rodinu: d\u011bde\u010dek hypnotiz\u00e9r, kter\u00fd cht\u011bl zastavit n\u011bmeck\u00e9 tanky hypn\u00f3zou; otec na p\u0159ed\u010dasn\u00e9m d\u016fchodu. Stanicí proj\u00ed\u017ed\u011bj\u00ed n\u011bmeck\u00e9 vojensk\u00e9 transporty. Ve\u010der p\u0159ijde Viktorie Freie \u2013 kr\u00e1sn\u00e1 Raku\u0161anka, spojka odboje. Milo\u0161 s n\u00ed pro\u017eije prvn\u00ed \u00fasp\u011b\u0161n\u00fd milostn\u00fd z\u00e1\u017eitek."),
    ("Sabot\u00e1\u017e", "Hubi\u010dka sd\u011bl\u00ed Milo\u0161ovi pl\u00e1n: o p\u016flnoci projede transport n\u011bmeck\u00fdch zbran\u00ed, kter\u00fd cht\u011bj\u00ed zni\u010dit. Viktorie p\u0159inese revolver a \u010dasovanou v\u00fdbu\u0161ninu. Milo\u0161 se dobrovoln\u011b rozhodne, \u017ee bombu vhod\u00ed s\u00e1m."),
    ("Tragick\u00fd konec", 'Milo\u0161 vyleze na n\u00e1v\u011bstidlo a vhod\u00ed bombu do proj\u00ed\u017ed\u011bj\u00edc\u00edho vlaku. V posledn\u00ed chv\u00edli ho zpozoruje n\u011bmeck\u00fd voj\u00e1k \u2013 vz\u00e1jemn\u011b se zast\u0159el\u00ed. Oba spadnou do p\u0159\u00edkopu a um\u00edraj\u00ed. Milo\u0161 si uv\u011bdomuje <b>nesmyslnost jejich smrti</b> \u2013 mysl\u00ed na svou rodinu i na rodinu n\u011bmeck\u00e9ho voj\u00e1ka. Ale c\u00edt\u00ed klid z dobře vykonan\u00e9 pr\u00e1ce.'),
]

THEMES = [
    "<b>Dosp\u00edv\u00e1n\u00ed a p\u0159echod v mu\u017ee</b> \u2013 Milo\u0161\u016fv osobn\u00ed r\u016fst od chlapce k mu\u017ei (sexu\u00e1ln\u00ed i morální)",
    "<b>Nesmyslnost v\u00e1lky</b> \u2013 v\u00e1lka ni\u010d\u00ed osudy oby\u010dejn\u00fdch lid\u00ed, t\u00e9\u017e Milo\u0161\u016fv",
    "<b>Kontrast velk\u00fdch d\u011bjin a mal\u00fdch osud\u016f</b> \u2013 na pozad\u00ed sv\u011btov\u00e9 v\u00e1lky lid\u00e9 \u0159e\u0161\u00ed l\u00e1sku, sex, holuby",
    "<b>Tragikomika</b> \u2013 sm\u00edch a trag\u00e9die se neust\u00e1le prol\u00ednaj\u00ed (af\u00e9ra s raz\u00edtky vs. smrt)",
    "<b>Hrdinství oby\u010dejn\u00fdch lid\u00ed</b> \u2013 i slaboch jako Milo\u0161 dok\u00e1\u017ee vykonat hrdinský \u010din",
    "<b>Kritika v\u00e1lky a fa\u0161ismu</b> \u2013 n\u011bmeck\u00e1 okupace, kolaborace (Zedn\u00ed\u010dek), odboj",
]

CONTEXT_BULLETS = [
    "<b>2. vlna v\u00e1le\u010dn\u00e9 pr\u00f3zy</b> (60. l\u00e9ta 20. stolet\u00ed) \u2013 nov\u00fd pohled na v\u00e1lku bez patosu",
    "Autoři zachycuj\u00ed v\u00e1lku o\u010dima oby\u010dejn\u00fdch lid\u00ed, ne hrdin\u016f",
    "\u010cesk\u00e1 nov\u00e1 vlna \u2013 v kinematografii i v literatu\u0159e (Menzel, Forman, Chytilov\u00e1)",
    "Hrabal = p\u00e1bitel \u2013 vypr\u00e1v\u011b\u010d, kter\u00fd p\u0159ikra\u0161luje, fabuluje, plynouc\u00ed proud \u0159e\u010di",
]
CONTEXT_TABLE = [
    ("Ladislav Fuks", "Spalova\u010d mrtvol", "\u010cR \u2013 v\u00e1l. pr\u00f3za"),
    ("Josef \u0160kvoreck\u00fd", "Zbab\u011blci", "\u010cR \u2013 v\u00e1l. pr\u00f3za"),
    ("Ota Pavel", "Smrt kr\u00e1sn\u00fdch srnc\u016f", "\u010cR \u2013 v\u00e1l. pr\u00f3za"),
    ("Jan Otčen\u00e1\u0161ek", "Romeo, Julie a tma", "\u010cR \u2013 v\u00e1l. pr\u00f3za"),
    ("Arnošt Lustig", "Modlitba pro Kate\u0159inu H.", "\u010cR \u2013 v\u00e1l. pr\u00f3za"),
]

QUICK_REVIEW = [
    ("Autor", "Bohumil Hrabal (1914\u20131997), \u010desk\u00fd spisovatel"),
    ("\u017d\u00e1nr", "Tragikomick\u00e1 novela"),
    ("Sm\u011br", "2. vlna v\u00e1le\u010dn\u00e9 pr\u00f3zy, 60. l\u00e9ta"),
    ("Druh", "Epika (pr\u00f3za)"),
    ("Vypr\u00e1v\u011b\u010d", "Ich-forma (Milo\u0161 Hrma)"),
    ("Kde/kdy", "Mal\u00e1 \u017eel. stanice, Protektor\u00e1t, \u00fanor 1945"),
    ("T\u00e9ma", "Dosp\u00edv\u00e1n\u00ed na pozad\u00ed v\u00e1lky, nesmyslnost v\u00e1lky"),
    ("Postavy", "Milo\u0161 Hrma, Hubi\u010dka, M\u00e1\u0161a, Viktorie, Zdeni\u010dka"),
    ("Kl\u00ed\u010dov\u00e9", "Film \u2013 Oscar 1968 (re\u017eis\u00e9r Ji\u0159\u00ed Menzel)"),
    ("Jazyk", "Ich-forma, proud v\u011bdom\u00ed, tragikomika, hovorov\u00fd"),
    ("Kontext", "Fuks, \u0160kvoreck\u00fd, Ota Pavel, Lustig"),
]


# ============================================================
# ŠABLONA
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

story.append(KeepTogether([
    sec("ZÁKLADNÍ ÚDAJE O DÍLE", C_BLUE),
    sp(),
    kv(BASIC_INFO, C_BLUE_L, C_BLUE),
]))
story.append(sp(6))

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
    Table(char_rows, colWidths=[30*mm, W - 30*mm],
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

story.append(KeepTogether([
    sec("HLAVNÍ MYŠLENKY", C_GREEN),
    sp(),
    bl(THEMES, C_GREEN_L),
]))
story.append(sp(6))

ctx_rows = [[Paragraph("<b>Autor</b>", st_wh), Paragraph("<b>Dílo</b>", st_wh), Paragraph("<b>Kontext</b>", st_wh)]]
for a, d, c in CONTEXT_TABLE:
    ctx_rows.append([Paragraph(f"<b>{a}</b>", st_smallb), Paragraph(d, st_small), Paragraph(c, st_small)])
story.append(KeepTogether([
    sec("LITERÁRNÍ KONTEXT", C_ORANGE),
    sp(),
    bl(CONTEXT_BULLETS, C_ORANGE_L),
    sp(3),
    Table(ctx_rows, colWidths=[28*mm, W - 48*mm, 20*mm],
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
print(f"OK! \u2192 {OUTPUT_FILE}")
