#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROZBOR - Kulicka (Guy de Maupassant)
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
# ROZM\u011aRY
# ============================================================
PAGE_W, PAGE_H = A4
MARGIN = 12*mm
W = PAGE_W - 2*MARGIN

# ============================================================
# DATA
# ============================================================
OUTPUT_FILE = "/home/jakub/Maturita/moje-rozbory/Kulicka_rozbor.pdf"

TITLE = "KULI\u010cKA"
AUTHOR_SUBTITLE = "Guy de Maupassant"

AUTHOR_SECTION_TITLE = "AUTOR \u2013 GUY DE MAUPASSANT (1850\u20131893)"
AUTHOR_KV = [
    ("N\u00e1rodnost:", "Francouzsk\u00fd spisovatel, novin\u00e1\u0159 a dramatik"),
    ("P\u016fvod:", "Narozen na z\u00e1mku Miromesnil v Normandii. Poch\u00e1zel ze z\u00e1mo\u017en\u00e9 rodiny, rodi\u010de se rozvedli"),
    ("Vzd\u011bl\u00e1n\u00ed:", "Studoval pr\u00e1va v Pa\u0159\u00ed\u017ei, studia p\u0159eru\u0161il prusko-francouzskou v\u00e1lkou (1870\u20131871)"),
    ("Mentor:", "Gustave Flaubert \u2013 p\u0159\u00edtel rodiny, u\u010dil Maupassanta ps\u00e1t. Nov\u00fdm se stal a\u017e po 10 letech tr\u00e9ninku"),
    ("Kari\u00e9ra:", "\u00da\u0159edn\u00edk na ministerstvu, od 1880 (po \u00fasp\u011bchu Kuli\u010dky) se v\u011bnoval jen ps\u00e1n\u00ed"),
    ("Styl:", "Mistr kr\u00e1tk\u00e9 pov\u00eddky \u2013 napsal jich p\u0159es 300. Realismus, p\u0159esn\u00fd popis, psychologie postav"),
    ("Smrt:", "Trp\u011bl syfilidou, psychick\u00fdmi poruchami. Pokus o sebevra\u017edu 1892. Zem\u0159el 1893 v \u00fastavu v Pa\u0159\u00ed\u017ei"),
]
AUTHOR_WORKS = [
    "<b>Mil\u00e1\u010dek</b> (1885) \u2013 rom\u00e1n o karieristovi, kter\u00fd vyu\u017e\u00edv\u00e1 \u017eeny k spole\u010densk\u00e9mu vzestupu",
    "<b>Petre\u010dek</b> (1883) \u2013 rom\u00e1n, \u0159e\u0161\u00ed podstatu otcovstv\u00ed a d\u011bdicov\u00ed",
    "<b>Sl\u00e1va a b\u00edda kurtiz\u00e1n</b> \u2013 pov\u00eddkov\u00fd soubor, pov\u00eddky ze spole\u010dnosti",
    "<b>Horla</b> (1887) \u2013 hororov\u00e1 pov\u00eddka, t\u00e9ma \u0161\u00edlenstv\u00ed a paranoia",
]

BASIC_INFO = [
    ("Lit. druh:", "Epika (pr\u00f3za)"),
    ("Lit. \u017e\u00e1nr:", "Nov\u00e9la (kr\u00e1tk\u00e1 pov\u00eddka s pointou)"),
    ("T\u00e9ma:", "Pokrytectv\u00ed m\u011b\u0161\u0165\u00e1ck\u00e9 spole\u010dnosti \u2013 lid\u00e9 pohrdaj\u00ed prostitutkou, ale sami jsou mor\u00e1ln\u011b hor\u0161\u00ed"),
    ("\u010casoprostor:", "Normandie (Rouen \u2192 Le Havre), zima 1870\u20131871, prusko-francouzsk\u00e1 v\u00e1lka"),
    ("Vyd\u00e1no:", "1880 \u2013 prvn\u00ed velk\u00fd \u00fasp\u011bch Maupassanta, sou\u010d\u00e1st sb\u00edrky Me\u0161danick\u00e9 ve\u010dery"),
]

COMPOSITION_KV = [
    ("Kompozice:", "Chronologick\u00e1, line\u00e1rn\u00ed d\u011bj \u2013 cesta dostavn\u00edkem z Rouenu do Le Havru"),
    ("Vypr\u00e1v\u011b\u010d:", "Er-forma \u2013 v\u0161ev\u011bdouc\u00ed vypr\u00e1v\u011b\u010d, objektivn\u00ed pozorovatel, ironick\u00fd t\u00f3n"),
    ("Promluvy:", "P\u0159\u00edm\u00e1 \u0159e\u010d (dialogy cestuj\u00edc\u00edch), pop\u0159\u00edpad\u011b vnit\u0159n\u00ed popisy"),
]
COMPOSITION_BULLETS = [
    "<b>Realismus</b> \u2013 p\u0159esn\u00fd, detailn\u00ed popis postav, prost\u0159ed\u00ed a situac\u00ed",
    "<b>Ironie a satira</b> \u2013 vypr\u00e1v\u011b\u010d ironicky komentuje pokrytectv\u00ed m\u011b\u0161\u0165\u00e1k\u016f",
    "<b>Kontrast</b> \u2013 prostitu\u010dka je mor\u00e1ln\u011b nadřazen\u00e1 (ob\u011btavost) vs. m\u011b\u0161\u0165\u00e1ci (pokrytci)",
    "<b>Symbolika</b> \u2013 dostavn\u00edk jako mikrokosmos spole\u010dnosti, j\u00eddlo jako symbol solidarity/v\u010d\u011b\u010dnosti",
    "<b>Pointa</b> \u2013 z\u00e1v\u011bre\u010dn\u00e1 sc\u00e9na vyhrocuje pokrytectv\u00ed \u2013 Kuli\u010dka pl\u00e1\u010de, ostatn\u00ed j\u00ed pohrdaj\u00ed",
]
TIP_TEXT = "D\u016fle\u017eit\u00e9 je pochopit kontrast: Kuli\u010dka je prostitutka, ale z\u00e1rove\u0148 nejslu\u0161n\u011bj\u0161\u00ed a nejob\u011btav\u011bj\u0161\u00ed postava. M\u011b\u0161\u0165\u00e1ci, kte\u0159\u00ed j\u00ed pohrdaj\u00ed, jsou pokrytci \u2013 vyu\u017eij\u00ed ji a pak se od n\u00ed odvrátí. Maupassant tím kritizuje celou spole\u010dnost."

MAIN_CHAR_1 = ("Kuli\u010dka", "Al\u017eb\u011bta Roussetov\u00e1, p\u0159ezd\u00edvan\u00e1 Kuli\u010dka \u2013 prostitutka, ale <b>nejob\u011btav\u011bj\u0161\u00ed a nejslu\u0161n\u011bj\u0161\u00ed</b> postava. Baculat\u00e1, p\u0159\u00edv\u011btiv\u00e1, vlastenka (nen\u00e1vid\u00ed Prusy). Sd\u00edl\u00ed j\u00eddlo s cestuj\u00edc\u00edmi, ob\u011btuje se kdy\u017e je ti\u0161\u00ed k prusk\u00e9mu d\u016fstojn\u00edkovi. Nakonec je ostatn\u00edmi ponížena a opu\u0161t\u011bna.")
MAIN_CHAR_2 = ("Prusk\u00fd d\u016fstojn\u00edk", "Bezejmenn\u00fd prusk\u00fd d\u016fstojn\u00edk, kter\u00fd zadr\u017euje dostavn\u00edk v hostinci a <b>po\u017eaduje noc s Kuli\u010dkou</b>. Dokud mu nevyhov\u00ed, nikdo nesm\u00ed pokra\u010dovat v cest\u011b. Zosobn\u011bn\u00ed okupantsk\u00e9 moci a ponížen\u00ed.")

SIDE_CHARACTERS = [
    ("Pan Loiseau", "Obchodn\u00edk s v\u00ednem. Lakomc, vulg\u00e1rn\u00ed, ale praktick\u00fd. Tlac\u00ed Kuli\u010dku k ustoupen\u00ed"),
    ("Man\u017eel\u00e9 Carr\u00e9-Lamadonovi", "Fabrikant s man\u017eelkou \u2013 vy\u0161\u0161\u00ed spole\u010dnost. P\u0159etvá\u0159ka, pokrytectv\u00ed ve vy\u0161\u0161\u00ed form\u011b"),
    ("Hrab\u011b a hrab\u011bnka de Br\u00e9ville", "\u0160lechta \u2013 zdánliv\u011b u\u0161lechtil\u00ed, ale sou\u010dinní s n\u00e1tlakem na Kuli\u010dku"),
    ("Cornudet", "Demokrat, liberál. Jediný, kdo se nepodílí na nátlaku na Kuličku. Tichý pozorovatel"),
    ("Jepti\u0161ky", "Dv\u011b \u0159eholn\u00ed sestry, tiché, zbo\u017en\u00e9. P\u0159esto podpo\u0159\u00ed n\u00e1tlak argumenty o ob\u011bti"),
]

PLOT_BLOCKS = [
    ("Odjezd z Rouenu", "Za prusko-francouzsk\u00e9 v\u00e1lky z obsazen\u00e9ho Rouenu vyr\u00e1\u017e\u00ed dostavn\u00edk do Le Havru. Cestuje v n\u011bm deset lid\u00ed: t\u0159i p\u00e1ry m\u011b\u0161\u0165\u00e1k\u016f (obchodn\u00edk, fabrikant, \u0161lechtic se sv\u00fdmi man\u017eelkami), demokrat Cornudet, dv\u011b jepti\u0161ky a prostitutka Kuli\u010dka. M\u011b\u0161\u0165\u00e1ci j\u00ed pohrdaj\u00ed."),
    ("Sd\u00edlen\u00ed j\u00eddla", "B\u011bhem cesty v\u0161ichni vyhladov\u00ed \u2013 nikdo si nevzal j\u00eddlo. Jedině Kuli\u010dka m\u00e1 pln\u00fd ko\u0161 z\u00e1sob. Velkorys\u011b sd\u00edl\u00ed sv\u00e9 j\u00eddlo se v\u0161emi. M\u011b\u0161\u0165\u00e1ci zprvu v\u00e1haj\u00ed, ale hlad je p\u0159em\u016f\u017ee. Na chv\u00edli jsou ke Kuli\u010dce vlídní a p\u0159\u00e1tel\u0161t\u00ed."),
    ("Zadr\u017een\u00ed v hostinci", "Dostavn\u00edk se zastav\u00ed v hostinci v Tôtes. Prusk\u00fd d\u016fstojn\u00edk zadr\u017euje v\u0161echny cestuj\u00edc\u00ed a po\u017eaduje, aby s n\u00edm Kuli\u010dka str\u00e1vila noc. Kuli\u010dka odm\u00edt\u00e1 \u2013 z vlastenectv\u00ed (nechce se poddat Prusovi). Skupina nem\u016f\u017ee pokra\u010dovat d\u00e1l."),
    ("N\u00e1tlak", "M\u011b\u0161\u0165\u00e1ci se zprvu tv\u00e1\u0159\u00ed zhnusen\u011b, ale postupn\u011b na Kuli\u010dku naléhaj\u00ed, aby se d\u016fstojn\u00edkovi podvolila a v\u0161ichni mohli jet d\u00e1l. Argumentuj\u00ed historick\u00fdmi p\u0159\u00edklady hrdinsk\u00e9 ob\u011bti. I jepti\u0161ky podpo\u0159\u00ed n\u00e1tlak pomoc\u00ed n\u00e1bo\u017eensk\u00fdch argument\u016f. Kuli\u010dka nakonec ustoup\u00ed."),
    ("Ponížen\u00ed", 'Po noci s d\u016fstojn\u00edkem je dostavn\u00edk propuštěn. M\u011b\u0161\u0165\u00e1ci se ale od Kuli\u010dky ihned odvrac\u00ed \u2013 op\u011bt j\u00ed pohrdaj\u00ed, ned\u00edvaj\u00ed se na ni. Ka\u017ed\u00fd m\u00e1 jídlo, jen Kuli\u010dka nem\u00e1 nic. Nikdo se s n\u00ed nepod\u011bl\u00ed. Kuli\u010dka <b>ti\u0161e pl\u00e1\u010de</b>, zatímco Cornudet si pohvizduje Marseillaisu.'),
]

THEMES = [
    "<b>Pokrytectv\u00ed m\u011b\u0161\u0165\u00e1ck\u00e9 spole\u010dnosti</b> \u2013 m\u011b\u0161\u0165\u00e1ci pohrdaj\u00ed Kuli\u010dkou, ale sami jsou mor\u00e1ln\u011b zka\u017een\u00ed",
    "<b>Kontrast skutečn\u00e9 a zdánliv\u00e9 mravnosti</b> \u2013 prostitutka je ob\u011btav\u011bj\u0161\u00ed ne\u017e zbo\u017en\u00e1 \u0161lechta",
    "<b>Vyu\u017e\u00edv\u00e1n\u00ed slabších</b> \u2013 cestuj\u00edc\u00ed Kuli\u010dku vyu\u017eij\u00ed (jídlo, ob\u011b\u0165) a pak zahodí",
    "<b>Vlastenectv\u00ed</b> \u2013 Kuli\u010dka odm\u00edt\u00e1 Prusa z vlastenectv\u00ed, m\u011b\u0161\u0165\u00e1ci vlastenectv\u00ed p\u0159edstíraj\u00ed",
    "<b>Kritika v\u00e1lky</b> \u2013 v\u00e1lka obnažuje pravou pova\u0159u lid\u00ed, ni\u010d\u00ed lidskou d\u016fstojnost",
]

CONTEXT_BULLETS = [
    "<b>Realismus / naturalismus</b> \u2013 2. polovina 19. stolet\u00ed, Francie",
    "P\u0159esn\u00fd, objektivn\u00ed popis reality, psychologie postav, \u017e\u00e1dn\u00e1 idealizace",
    "Maupassant \u2013 \u017e\u00e1k Gustava Flauberta, mistr kr\u00e1tk\u00e9 povídky (300+ pov\u00eddek)",
    "Prusko-francouzsk\u00e1 v\u00e1lka (1870\u20131871) jako pozad\u00ed \u2013 Francie poražena, okupov\u00e1na",
]
CONTEXT_TABLE = [
    ("G. Flaubert", "Pan\u00ed Bovaryov\u00e1", "FR \u2013 realismus"),
    ("\u00c9. Zola", "Naná / Germinál", "FR \u2013 naturalismus"),
    ("Stendhal", "\u010cerven\u00fd a \u010dern\u00fd", "FR \u2013 realismus"),
    ("H. de Balzac", "Otec Goriot", "FR \u2013 realismus"),
    ("L. N. Tolstoj", "Anna Karenina", "RU \u2013 realismus"),
]

QUICK_REVIEW = [
    ("Autor", "Guy de Maupassant (1850\u20131893), francouzsk\u00fd spisovatel"),
    ("\u017d\u00e1nr", "Nov\u00e9la (kr\u00e1tk\u00e1 pov\u00eddka s pointou)"),
    ("Sm\u011br", "Realismus / naturalismus (2. pol. 19. stol.)"),
    ("Druh", "Epika (pr\u00f3za)"),
    ("Vypr\u00e1v\u011b\u010d", "Er-forma (v\u0161ev\u011bdouc\u00ed, ironick\u00fd)"),
    ("Kde/kdy", "Normandie, prusko-fr. v\u00e1lka, 1870\u20131871"),
    ("T\u00e9ma", "Pokrytectv\u00ed m\u011b\u0161\u0165\u00e1k\u016f, ob\u011b\u0165 Kuli\u010dky"),
    ("Postavy", "Kuli\u010dka, Loiseau, Carr\u00e9-Lamadonovi, Br\u00e9villovi"),
    ("Pointa", "Kuli\u010dka pl\u00e1\u010de, nikdo se nepod\u011bl\u00ed \u2013 nevd\u011b\u010dnost"),
    ("Jazyk", "Er-forma, ironie, satira, kontrast, realismus"),
    ("Kontext", "Flaubert, Zola, Balzac, Tolstoj"),
]


# ============================================================
# SABLONA
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
# SESTAVENI DOKUMENTU
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
    Paragraph("<b>Dal\u0161\u00ed d\u00edla:</b>", S('DA', fontName='DJB', textColor=C_INDIGO)),
    sp(2),
    bl(AUTHOR_WORKS, C_INDIGO_L),
]))
story.append(sp(6))

story.append(KeepTogether([
    sec("Z\u00c1KLADN\u00cd \u00daDAJE O D\u00cdLE", C_BLUE),
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

story.append(sec("D\u011aJ", C_RED))
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
    sec("HLAVN\u00cd MY\u0160LENKY", C_GREEN),
    sp(),
    bl(THEMES, C_GREEN_L),
]))
story.append(sp(6))

ctx_rows = [[Paragraph("<b>Autor</b>", st_wh), Paragraph("<b>D\u00edlo</b>", st_wh), Paragraph("<b>Kontext</b>", st_wh)]]
for a, d, c in CONTEXT_TABLE:
    ctx_rows.append([Paragraph(f"<b>{a}</b>", st_smallb), Paragraph(d, st_small), Paragraph(c, st_small)])
story.append(KeepTogether([
    sec("LITER\u00c1RN\u00cd KONTEXT", C_ORANGE),
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
    Paragraph("<b>Odpov\u011b\u010f</b>", S('QH2', fontName='DJB', fontSize=8, textColor=white, leading=11)),
]]
for q, a in QUICK_REVIEW:
    qr_rows.append([Paragraph(q, st_body), Paragraph(a, st_body)])
story.append(KeepTogether([
    sec("RYCHL\u00dd P\u0158EHLED", C_DARK),
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
