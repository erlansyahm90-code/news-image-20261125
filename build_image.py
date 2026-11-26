#!/usr/bin/env python3
"""Draw the one-page world-news poster for Wednesday 25 November 2026.

A six-panel news wall: a masthead with the date spelled out in full, then
six coloured section panels (World, Politics, Economy, Technology, Culture,
Sport), each with one lead story and five short items. 36 verified stories
in total. Output is a 1024x1024 PNG.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

SIZE = 1024
PAPER = (251, 248, 241)
INK = (22, 22, 22)
SOFT_INK = (74, 74, 74)
RULE = (178, 34, 34)
PANEL_LINE = (198, 192, 180)
WHITE = (255, 255, 255)

MASTHEAD_TOP = 26
GRID_TOP = 156
GRID_LEFT = 26
GRID_GAP = 14
PANEL_W = 479
PANEL_H = 266
FOOTER_Y = 992

# (section name, accent colour, lead title, lead subline, [5 item titles])
SECTIONS = [
    (
        "WORLD",
        (139, 30, 30),
        "Houthi drone hits Riyadh tower \u2014 11 hurt",
        "Second strike on the skyscraper in a week; coalition hits Hodeidah",
        [
            "Iran says two tankers hit mines in Hormuz and caught fire",
            "Israeli strike kills senior Hamas security chief in Gaza City",
            "Colombia police storm supermarket, free hostages after siege",
            "Fuel tanker crash sets Cairo ring road ablaze \u2014 31 killed",
            "Russia's own figures show nearly 500,000 war dead in Ukraine",
        ],
    ),
    (
        "POLITICS",
        (31, 58, 95),
        "US proposes new tariffs on 14 partners, incl. China and EU",
        "White House targets 'excess factory capacity' abroad",
        [
            "Democrats clinch House majority of at least 259 seats",
            "Israeli judges urge dropping gravest charges against Netanyahu",
            "Australia signs security pact with Solomon Islands, $740m aid",
            "Xi's anti-graft drive ensnares Shanghai party chief Chen Jining",
            "North Korea expels Swiss diplomat in sanctions row",
        ],
    ),
    (
        "ECONOMY",
        (30, 91, 62),
        "US stocks slide again as AI-share fears deepen",
        "Wall Street recoups most early losses by the close",
        [
            "Nvidia falls 3.9% as the AI sell-off rolls on",
            "Anthropic shares slide below their $83 IPO price",
            "US growth revised up to 4.3% in the third quarter",
            "US consumer confidence jumps to near a two-year high",
            "Trump accounts traded Nvidia shares 44 times this year",
        ],
    ),
    (
        "TECHNOLOGY",
        (74, 44, 107),
        "US jury convicts Huawei of stealing trade secrets",
        "Guilty on 10 of 12 counts, incl. bank fraud; racketeering cleared",
        [
            "Microsoft declares 'Code Red' after Outlook outage",
            "US clears SpaceX plan for a million data satellites",
            "Shenzhou 24 lifts off with Pakistan's first astronaut",
            "NASA releases new images of its asteroid-smash test",
            "EA adds AI voice of John Motson to FC 27",
        ],
    ),
    (
        "CULTURE",
        (138, 90, 0),
        "Jolie and Pitt settle long winery legal battle",
        "Eight-year fight over the French vineyard they bought in 2008 ends",
        [
            "Duran Duran guitarist Andy Taylor dies, aged 65",
            "Nollywood legend Pete Edochie dies at 79",
            "Macy's Thanksgiving parade postponed to Saturday",
            "Gordon Ramsay to host revived Top Gear",
            "Pope Francis diary reveals deep spiritual crisis",
        ],
    ),
    (
        "SPORT",
        (15, 92, 92),
        "Rams beat Packers 26\u201313 on Thanksgiving Eve",
        "Blake Corum runs for 184 yards as Rams win a fifth straight",
        [
            "Lille stun Bayern 2\u20131 in the Champions League",
            "Liverpool cruise past Club Brugge 3\u20130",
            "Steelers cut quarterback Aaron Rodgers",
            "No. 16 Duke tops No. 10 UConn 77\u201363",
            "Lions owner Martha Firestone Ford dies at 101",
        ],
    ),
]


def load_font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


FONTS = {
    "kicker": load_font("DejaVuSans-Bold.ttf", 14),
    "date": load_font("DejaVuSerif-Bold.ttf", 46),
    "subtitle": load_font("DejaVuSans.ttf", 15),
    "bignum": load_font("DejaVuSerif-Bold.ttf", 44),
    "bignum_cap": load_font("DejaVuSans-Bold.ttf", 12),
    "head": load_font("DejaVuSans-Bold.ttf", 16),
    "head_count": load_font("DejaVuSans.ttf", 13),
    "lead": load_font("DejaVuSans-Bold.ttf", 16),
    "lead_sub": load_font("DejaVuSans.ttf", 12),
    "item": load_font("DejaVuSans.ttf", 13),
    "footer": load_font("DejaVuSans.ttf", 12),
}


def wrap(draw, text, font, max_width, max_lines=None):
    """Greedy word wrap; returns a list of lines (truncated at max_lines)."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
            if max_lines and len(lines) == max_lines:
                break
    if current and (not max_lines or len(lines) < max_lines):
        lines.append(current)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
    if max_lines and len(lines) == max_lines and current and lines[-1] != current:
        # Last line overflowed: mark it with an ellipsis.
        last = lines[-1]
        while last and draw.textlength(last + "\u2026", font=font) > max_width:
            last = last.rsplit(" ", 1)[0] if " " in last else last[:-1]
        lines[-1] = last + "\u2026"
    return lines


def draw_masthead(draw):
    draw.text((GRID_LEFT, MASTHEAD_TOP), "T H E   W O R L D   I N   O N E   P A G E",
              font=FONTS["kicker"], fill=RULE)
    draw.text((GRID_LEFT, MASTHEAD_TOP + 22), "Wednesday 25 November 2026",
              font=FONTS["date"], fill=INK)
    draw.text((GRID_LEFT, MASTHEAD_TOP + 84),
              "36 verified stories  \u00b7  6 sections  \u00b7  One day, one page",
              font=FONTS["subtitle"], fill=SOFT_INK)
    # Right-hand badge: story count.
    num = "36"
    num_w = draw.textlength(num, font=FONTS["bignum"])
    draw.text((SIZE - GRID_LEFT - num_w, MASTHEAD_TOP + 6), num,
              font=FONTS["bignum"], fill=RULE)
    cap = "STORIES"
    cap_w = draw.textlength(cap, font=FONTS["bignum_cap"])
    draw.text((SIZE - GRID_LEFT - cap_w, MASTHEAD_TOP + 56), cap,
              font=FONTS["bignum_cap"], fill=SOFT_INK)
    draw.rectangle((GRID_LEFT, GRID_TOP - 16, SIZE - GRID_LEFT, GRID_TOP - 13),
                   fill=RULE)


def draw_panel(draw, x, y, section):
    name, accent, lead_title, lead_sub, items = section
    # Panel frame and header bar.
    draw.rectangle((x, y, x + PANEL_W, y + PANEL_H), outline=PANEL_LINE, width=1)
    draw.rectangle((x, y, x + PANEL_W, y + 30), fill=accent)
    draw.text((x + 14, y + 7), name, font=FONTS["head"], fill=WHITE)
    count = "6 stories"
    cw = draw.textlength(count, font=FONTS["head_count"])
    draw.text((x + PANEL_W - 14 - cw, y + 8), count,
              font=FONTS["head_count"], fill=WHITE)

    body_x = x + 14
    body_w = PANEL_W - 28
    cy = y + 30 + 9

    # Lead story: bold title (max 2 lines) + one grey subline.
    for i, line in enumerate(wrap(draw, lead_title, FONTS["lead"], body_w, 2)):
        draw.text((body_x, cy + i * 20), line, font=FONTS["lead"], fill=INK)
    cy += 40
    for line in wrap(draw, lead_sub, FONTS["lead_sub"], body_w, 1):
        draw.text((body_x, cy), line, font=FONTS["lead_sub"], fill=SOFT_INK)
    cy += 15 + 9
    draw.line((body_x, cy, x + PANEL_W - 14, cy), fill=PANEL_LINE, width=1)
    cy += 10

    # Five compact items with accent square bullets.
    for title in items:
        lines = wrap(draw, title, FONTS["item"], body_w - 16, 2)
        draw.rectangle((body_x, cy + 4, body_x + 7, cy + 11), fill=accent)
        for i, line in enumerate(lines):
            draw.text((body_x + 16, cy + i * 16), line,
                      font=FONTS["item"], fill=INK)
        cy += 31


def build():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(img)
    # Thin outer frame.
    draw.rectangle((8, 8, SIZE - 9, SIZE - 9), outline=INK, width=2)
    draw_masthead(draw)
    for idx, section in enumerate(SECTIONS):
        col = idx % 2
        row = idx // 2
        x = GRID_LEFT + col * (PANEL_W + GRID_GAP)
        y = GRID_TOP + row * (PANEL_H + GRID_GAP)
        draw_panel(draw, x, y, section)
    draw.text((SIZE // 2, FOOTER_Y),
              "Every story happened or was first reported on Wednesday 25 November 2026  \u00b7  Sources: Reuters \u00b7 AP \u00b7 BBC",
              font=FONTS["footer"], fill=SOFT_INK, anchor="ma")
    return img


def main():
    img = build()
    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
