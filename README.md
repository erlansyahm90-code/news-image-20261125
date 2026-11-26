# Wednesday 25 November 2026 — One Day of World News, One Picture

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/erlansyahm90-code/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/erlansyahm90-code/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun bounty **Sum up 25 November's world news in one image**:
https://make.fun/bounty/news-image-20261125

## The poster

A one-page news wall for **Wednesday 25 November 2026** — **36 stories in
6 sections**, every one of them verified from the global wires as having
happened or first been reported on that day:

- **WORLD** — Houthi drone hits a Riyadh tower (11 hurt); Iran says two
  tankers hit mines in Hormuz; Israeli strike kills a senior Hamas security
  chief in Gaza City; Colombia supermarket siege freed; Cairo tanker fire
  kills 31; Russia's own figures show nearly 500,000 war dead in Ukraine.
- **POLITICS** — US proposes tariffs on 14 partners incl. China and the EU;
  Democrats clinch a House majority of at least 259 seats; Israeli judges
  urge dropping the gravest charges against Netanyahu; Australia–Solomon
  Islands security pact; Xi's anti-graft drive ensnares Shanghai chief
  Chen Jining; North Korea expels a Swiss diplomat.
- **ECONOMY** — US stocks slide on AI fears; Nvidia −3.9%; Anthropic below
  its $83 IPO price; US growth revised up to 4.3%; consumer confidence near
  a two-year high; Trump accounts traded Nvidia shares 44 times this year.
- **TECHNOLOGY** — US jury convicts Huawei of stealing trade secrets;
  Microsoft declares 'Code Red' after the Outlook outage; US clears SpaceX
  plan for a million satellites; Shenzhou 24 carries Pakistan's first
  astronaut; NASA releases asteroid-smash images; EA adds an AI John Motson
  to FC 27.
- **CULTURE** — Jolie and Pitt settle the winery case; Duran Duran guitarist
  Andy Taylor dies at 65; Nollywood legend Pete Edochie dies at 79; Macy's
  Thanksgiving parade postponed to Saturday; Gordon Ramsay to host revived
  Top Gear; Pope Francis diary reveals a deep spiritual crisis.
- **SPORT** — Rams beat Packers 26–13 on Thanksgiving Eve; Lille stun
  Bayern 2–1; Liverpool cruise past Club Brugge 3–0; Steelers cut Aaron
  Rodgers; No. 16 Duke tops No. 10 UConn 77–63; Lions owner Martha
  Firestone Ford dies at 101.

## How it is built

`build_image.py` (Pillow, DejaVu fonts) draws the 1024×1024 poster and
writes `entry.png`. `main.py` (stdlib only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), so both grader runs
write byte-identical output. See `NOTES.md` for the full story list with
sources and verification dates.

## Run

```sh
python3 build_image.py        # renders entry.png (1024x1024, < 1 MiB)
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
