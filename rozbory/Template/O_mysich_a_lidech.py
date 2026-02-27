#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROZBOR - O mysich a lidech (John Steinbeck)
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
# ROZMERY
# ============================================================
PAGE_W, PAGE_H = A4
MARGIN = 12*mm
W = PAGE_W - 2*MARGIN

# ============================================================
# DATA
# ============================================================
OUTPUT_FILE = "/home/jakub/Maturita/rozbory/moje-rozbory/O_mysich_a_lidech_rozbor.pdf"

TITLE = "O MY\u0160\u00cdCH A LIDECH"
AUTHOR_SUBTITLE = "John Steinbeck"

AUTHOR_SECTION_TITLE = "AUTOR \u2013 JOHN STEINBECK (1902\u20131968)"
AUTHOR_KV = [
    ("N\u00e1rodnost:", "Americk\u00fd spisovatel, novin\u00e1\u0159, dramatik. Nositel Nobelovy ceny za literaturu (1962)"),
    ("P\u016fvod:", "Narozen v Salinasu, Kalifornie. Poch\u00e1zel z chud\u0161\u00edch pom\u011br\u016f, otec \u00fa\u0159edn\u00edk, matka u\u010ditelka"),
    ("Vzd\u011bl\u00e1n\u00ed:", "Studoval historii, anglickou literaturu a biologii na Stanfordu \u2013 \u0161kolu nedokon\u010dil"),
    ("Povol\u00e1n\u00ed:", "Pracoval na farm\u00e1ch, ran\u010d\u00edch, v cukrovarech \u2013 poznal \u017eivot d\u011bln\u00edk\u016f (inspirace pro d\u00edlo)"),
    ("Styl:", "Realismus \u2013 zobrazuje \u017eivot chud\u00fdch lid\u00ed, hospod\u00e1\u0159skou krizi, konflikt dobra a zla"),
    ("Ocen\u011bn\u00ed:", "Nobelova cena za literaturu 1962, Pulitzerova cena za Hrozny hn\u011bvu"),
    ("Smrt:", "Zem\u0159el 1968 v New Yorku. V z\u00e1v\u011bru \u017eivota kontroverze kv\u016fli podpo\u0159e vietnamsk\u00e9 v\u00e1lky"),
]
AUTHOR_WORKS = [
    "<b>Hrozny hn\u011bvu</b> (1939) \u2013 rom\u00e1n o rodin\u011b Joadov\u00fdch za hospod\u00e1\u0159sk\u00e9 krize, Pulitzerova cena",
    "<b>Na v\u00fdchod od r\u00e1je</b> (1952) \u2013 rodinn\u00e1 s\u00e1ga, biblick\u00e9 motivy (Kain a \u00c1bel)",
    "<b>Pl\u00e1\u0148 Tortilla</b> (1935) \u2013 humoristick\u00fd rom\u00e1n o mexick\u00fdch Ameri\u010danech v Kalifornii",
    "<b>Ryz\u00e1\u010dek</b> (1933) \u2013 rom\u00e1n o chlapci a jeho pony",
    "<b>Toulky s Charleym</b> (1962) \u2013 cestopis po Americe se psem Charleym",
]

BASIC_INFO = [
    ("Lit. druh:", "Epika (pr\u00f3za)"),
    ("Lit. \u017e\u00e1nr:", "Novela s prvky alegorie a bal\u00e1dy (pochmurn\u00fd d\u011bj, tragick\u00fd z\u00e1v\u011br)"),
    ("T\u00e9ma:", "P\u0159\u00e1telstv\u00ed, osamocenost, americk\u00fd sen chud\u00fdch d\u011bln\u00edk\u016f \u2013 a jeho nedosa\u017eitelnost"),
    ("\u010casoprostor:", "Kalifornie (Salinaské \u00fadol\u00ed), 30. l\u00e9ta 20. stolet\u00ed \u2013 doba hospod\u00e1\u0159sk\u00e9 krize v USA"),
    ("Vyd\u00e1no:", "1937. Zfilmov\u00e1no 1939 a 1992. Jedno z nejzn\u00e1m\u011bj\u0161\u00edch Steinbeckov\u00fdch d\u011bl"),
]

COMPOSITION_KV = [
    ("Kompozice:", "6 kapitol, chronologick\u00fd postup. D\u011bj se odehr\u00e1v\u00e1 b\u011bhem n\u011bkolika dn\u016f"),
    ("Vypr\u00e1v\u011b\u010d:", "Er-forma \u2013 v\u0161ev\u011bdouc\u00ed vypr\u00e1v\u011b\u010d, objektivn\u00ed pozorovatel"),
    ("Promluvy:", "P\u0159\u00edm\u00e1 \u0159e\u010d (dialogy d\u011bln\u00edk\u016f), nespisovn\u00fd jazyk, slang"),
]
COMPOSITION_BULLETS = [
    "<b>Realismus</b> \u2013 v\u011brn\u00fd obraz \u017eivota sez\u00f3nn\u00edch d\u011bln\u00edk\u016f za hospod\u00e1\u0159sk\u00e9 krize",
    "<b>Symbolika</b> \u2013 my\u0161i a kr\u00e1l\u00edci = k\u0159ehkost sn\u016f; \u0159eka na za\u010d\u00e1tku i konci = kruhov\u00e1 kompozice",
    "<b>Kontrast</b> \u2013 sny (farma, kr\u00e1l\u00edci) vs. drsn\u00e1 realita; fyzick\u00e1 s\u00edla Lennieho vs. jeho du\u0161evn\u00ed prostota",
    "<b>Dramati\u010dnost</b> \u2013 d\u011bj sp\u011bje k nevyhnuteln\u00e9 trag\u00e9dii, nap\u011bt\u00ed graduje",
    "<b>Nespisovn\u00fd jazyk</b> \u2013 hovorov\u00e1 angli\u010dtina d\u011bln\u00edk\u016f, autentick\u00e9 dialogy",
]
TIP_TEXT = "Kl\u00ed\u010dov\u00fd je z\u00e1v\u011br: George zast\u0159el\u00ed Lennieho z l\u00e1sky \u2013 aby ho u\u0161et\u0159il lyn\u010dov\u00e1n\u00ed. Je to akt milosrdenstv\u00ed, ne vra\u017eda. N\u00e1zev je z b\u00e1sn\u011b Roberta Burnse: i ty nejl\u00e9pe p\u0159ipraven\u00e9 pl\u00e1ny my\u0161\u00ed a lid\u00ed se \u010dasto zhat\u00ed."

MAIN_CHAR_1 = ("George Milton", "Mal\u00fd, chytr\u00fd, <b>ob\u011btav\u00fd</b>. Star\u00e1 se o Lennieho jako o vlastn\u00edho bratra. Tou\u017e\u00ed po vlastn\u00ed farm\u011b a klidn\u00e9m \u017eivot\u011b. \u010casto se na Lennieho zlob\u00ed, ale ve skute\u010dnosti ho m\u00e1 velmi r\u00e1d. Na konci se rozhodne Lennieho zast\u0159elit, aby ho u\u0161et\u0159il hor\u0161\u00edho osudu.")
MAIN_CHAR_2 = ("Lennie Small", "Obrovsk\u00fd, fyzicky siln\u00fd, ale <b>du\u0161evn\u011b zaostal\u00fd</b>. Dobr\u00e1ck\u00fd, naivn\u00ed, pracovit\u00fd. R\u00e1d hlad\u00ed m\u011bkk\u00e9 v\u011bci (my\u0161i, \u0161t\u011b\u0148ata, vlasy) \u2013 ale svou silou je zab\u00edj\u00ed. Sn\u00ed o vlastn\u00edch kr\u00e1l\u00edc\u00edch. Nechtěn\u011b zab\u00edj\u00ed Curleyovu \u017eenu.")

SIDE_CHARACTERS = [
    ("Curley", "\u0160\u00e9f\u016fv syn \u2013 agresivn\u00ed, \u017e\u00e1rliv\u00fd, namy\u0161len\u00fd. Vyvol\u00e1v\u00e1 konflikty, Lennie mu rozdrt\u00ed ruku"),
    ("Curleyova \u017eena", "Kr\u00e1sn\u00e1, osam\u011bl\u00e1, vyz\u00fdvav\u00e1. Nen\u00e1vid\u00ed sv\u016fj \u017eivot. Lennie j\u00ed omylem zlom\u00ed vaz"),
    ("Slim", "Respektovan\u00fd p\u0159edák. Moudr\u00fd, spravedliv\u00fd. Pochop\u00ed George\u016fv \u010din na konci"),
    ("Candy", "Star\u00fd d\u011bln\u00edk s amputovanou rukou. Chce se p\u0159ipojit ke George\u016fvu snu o farm\u011b"),
    ("Crooks", "\u010cerno\u0161sk\u00fd \u010deled\u00edn. \u017dije odděleně, ob\u011b\u0165 rasismu. Inteligentní, ale zatrpkl\u00fd"),
]

PLOT_BLOCKS = [
    ("P\u0159\u00edchod na ran\u010d", "George a Lennie, dva putuj\u00edc\u00ed d\u011bln\u00edci, sm\u011b\u0159uj\u00ed na ran\u010d v Salinaském \u00fadol\u00ed, kde maj\u00ed domluvenou pr\u00e1ci. Lennie m\u00e1 po kaps\u00e1ch mrtvou myš \u2013 r\u00e1d hlad\u00ed m\u011bkk\u00e9 v\u011bci, ale svou silou je zab\u00edj\u00ed. George mu sl\u00edbil, \u017ee a\u017e vyd\u011blaj\u00ed dostatek pen\u011bz, koup\u00ed si vlastn\u00ed farmu a Lennie se bude starat o kr\u00e1l\u00edky."),
    ("Sezn\u00e1men\u00ed s ran\u010dem", "Na ran\u010di potkaj\u00ed nepříjemn\u00e9ho \u0161\u00e9fova syna Curleyho, jeho kr\u00e1snou ale osam\u011blou \u017eenu, moudr\u00e9ho předáka Slima, star\u00e9ho Candyho a \u010derno\u0161sk\u00e9ho \u010deled\u00edna Crookse. George zak\u00e1\u017ee Lenniemu mluvit \u2013 aby si nikdo nev\u0161iml jeho du\u0161evn\u00edho handicapu."),
    ("Rozdrcen\u00e1 ruka", "Agresivn\u00ed Curley se do Lennieho pust\u00ed. Lennie mu v sebeobraně sev\u0159e p\u011bst a svou obrovskou silou mu <b>rozdrt\u00ed ruku</b>. Candy se nab\u00eddne, \u017ee přidá sv\u00e9 \u00faspory ke George\u016fvu snu o farm\u011b \u2013 na chv\u00edli se zd\u00e1, \u017ee sen se m\u016f\u017ee splnit."),
    ("Smrt \u0161t\u011bn\u011bte a Curleyovy \u017eeny", "Lennie dostane od Slima \u0161t\u011bn\u011b, ale svou silou ho zab\u00edj\u00ed. Pak za n\u00edm p\u0159ijde Curleyova \u017eena. Nab\u00eddne mu, aby j\u00ed pohladil vlasy. Lennie hlad\u00ed p\u0159\u00edli\u0161 silně, Curleyova \u017eena za\u010dne k\u0159i\u010det. Lennie se lekne, zacpe j\u00ed pusu a <b>omylem j\u00ed zlom\u00ed vaz</b>. Ut\u00edká pry\u010d."),
    ("Tragick\u00fd z\u00e1v\u011br", "Kdy\u017e ostatn\u00ed najdou mrtvou Curleyovu \u017eenu, cel\u00fd ran\u010d se vyd\u00e1 Lennieho hledat. Curley chce pomstu. Jen George v\u00ed, kam se Lennie schoval (u \u0159eky, kde příb\u011bh za\u010dal). George p\u0159ijde za Lenniem, vypr\u00e1v\u00ed mu o farm\u011b a kr\u00e1l\u00edc\u00edch a <b>zast\u0159el\u00ed ho</b> \u2013 akt milosrdenstv\u00ed, aby ho ušet\u0159il lyn\u010dov\u00e1n\u00ed."),
]

THEMES = [
    "<b>P\u0159\u00e1telstv\u00ed a oddanost</b> \u2013 George a Lennie \u2013 jeden bez druh\u00e9ho nem\u016f\u017ee existovat",
    "<b>Nedosa\u017eiteln\u00fd americk\u00fd sen</b> \u2013 vlastn\u00ed farma a kr\u00e1l\u00edci z\u016fstanou navždy snem",
    "<b>Osamělost</b> \u2013 ka\u017ed\u00e1 postava je n\u011bjak osaměl\u00e1 (Curleyova \u017eena, Crooks, Candy)",
    "<b>S\u00edla a k\u0159ehkost</b> \u2013 Lennieho obrovská s\u00edla vs. k\u0159ehkost my\u0161\u00ed, \u0161t\u011b\u0148at, lid\u00ed",
    "<b>Rasismus a vyk\u00e1z\u00e1n\u00ed</b> \u2013 Crooks \u017eije oddělený, na okraji spole\u010dnosti",
    "<b>Milosrdenstv\u00ed vs. n\u00e1sil\u00ed</b> \u2013 George\u016fv \u010din na konci \u2013 vra\u017eda nebo akt l\u00e1sky?",
]

CONTEXT_BULLETS = [
    "<b>Americk\u00e1 meziv\u00e1le\u010dn\u00e1 literatura</b> \u2013 30. l\u00e9ta 20. stolet\u00ed, hospod\u00e1\u0159sk\u00e1 krize (Velk\u00e1 deprese)",
    "Realismus \u2013 autenti\u010dt\u00ed hrdinov\u00e9, drsn\u00fd jazyk, \u017e\u00e1dn\u00e1 idealizace",
    "Ztracen\u00e1 generace \u2013 auto\u0159i poznamenaní 1. svět. v\u00e1lkou, ztr\u00e1ta ide\u00e1l\u016f",
    "Steinbeck = hlas chud\u00fdch \u2013 zobrazuje \u017eivot farm\u00e1\u0159\u016f a d\u011bln\u00edk\u016f v Kalifornii",
]
CONTEXT_TABLE = [
    ("E. Hemingway", "Sta\u0159ec a mo\u0159e", "USA \u2013 realismus"),
    ("E. M. Remarque", "Na z\u00e1p. front\u011b klid", "N\u011bm. \u2013 v\u00e1l. pr\u00f3za"),
    ("F. S. Fitzgerald", "Velk\u00fd Gatsby", "USA \u2013 ztr. gen."),
    ("W. Faulkner", "Hluk a v\u0159ava", "USA \u2013 realismus"),
    ("R. Rolland", "Petr a Lucie", "FR \u2013 v\u00e1l. pr\u00f3za"),
]

QUICK_REVIEW = [
    ("Autor", "John Steinbeck (1902\u20131968), americk\u00fd spisovatel, Nobel 1962"),
    ("\u017d\u00e1nr", "Novela (prvky alegorie a bal\u00e1dy)"),
    ("Sm\u011br", "Realismus, meziv\u00e1le\u010dn\u00e1 literatura, 30. l\u00e9ta"),
    ("Druh", "Epika (pr\u00f3za)"),
    ("Vypr\u00e1v\u011b\u010d", "Er-forma (v\u0161ev\u011bdouc\u00ed)"),
    ("Kde/kdy", "Kalifornie, Salinaské \u00fadol\u00ed, 30. l\u00e9ta \u2013 hosp. krize"),
    ("T\u00e9ma", "P\u0159\u00e1telstv\u00ed, americk\u00fd sen, osamělost, milosrdenstv\u00ed"),
    ("Postavy", "George, Lennie, Curley, Curleyova \u017eena, Slim, Candy"),
    ("Pointa", "George zast\u0159el\u00ed Lennieho z l\u00e1sky (akt milosrdenstv\u00ed)"),
    ("Jazyk", "Er-forma, nespisovn\u00fd, dialogy, symbolika, kontrast"),
    ("Kontext", "Hemingway, Remarque, Fitzgerald, Faulkner"),
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
