# NOTES — news-image-20261125

## Entry

- Competition: `news-image-20261125` — "Sum up 25 November's world news in one image"
- Day: **Wednesday 25 November 2026**
- Image: `entry.png`, 1024×1024 PNG, 134,299 bytes, sha256
  `c0c97b4bf382b26b50e470cc4267da3f05418f6624330595c7e4c1305bd6345e`
- Stories: **36 verified stories in 6 sections** (World, Politics, Economy,
  Technology, Culture, Sport), each section 1 lead + 5 items.
- Design: six-panel news wall, masthead with the date spelled out in full,
  one lead + five short items per section. Structure differs from the
  20261124 entry (front page with illustrated leads + numbered list).
- `main.py` copies `entry.png` to the output dir; two runs verified
  byte-identical (same sha256).

## Verification rule applied

Every story below was checked against a real news source as having happened
or first been reported on **25 November 2026 in some time zone**. Lesson from
the 20261123 edition (28/39 stories wrong-dated): anything first reported
on 24 Nov was excluded even when widely covered on 25 Nov.

## Stories and sources

### WORLD (6)
1. Houthi drone hits Riyadh tower, 11 hurt — Reuters, 25 Nov (Gulf Currents;
   second strike on the tower in a week; coalition hit Hodeidah in reply).
2. Iran says two tankers hit mines in Hormuz and caught fire — Reuters
   (Dubai, 25 Nov); a third tanker reported later the same day (Fars).
3. Israeli strike kills senior Hamas security chief in Gaza City — BBC, 25 Nov.
4. Colombia police storm supermarket, free hostages after 17-hour siege —
   BBC, 25 Nov (Cartagena).
5. Fuel tanker crash sets Cairo ring road ablaze, 31 killed — BBC/AP, 25 Nov.
6. Russia's own figures show nearly 500,000 war dead in Ukraine — BBC, 25 Nov
   (BBC analysis of 11m+ Russian death records; 490,334+).

### POLITICS (6)
7. US proposes new tariffs on 14 partners, incl. China and EU — Reuters/AP/
   BBC, 25 Nov (announced Wednesday; USTR Jamieson Greer).
8. Democrats clinch House majority of at least 259 seats — AP, 25 Nov.
9. Israeli judges urge dropping gravest charges against Netanyahu — BBC,
   25 Nov 19:47.
10. Australia signs security pact with Solomon Islands, $740m aid — AP, 25 Nov.
11. Xi's anti-graft drive ensnares Shanghai party chief Chen Jining — BBC,
    25 Nov.
12. North Korea expels Swiss diplomat in sanctions row — AP/BBC, 25 Nov.

### ECONOMY (6)
13. US stocks slide again as AI-share fears deepen — BBC/Reuters, 25 Nov
    (Nasdaq down almost 4% in early trading).
14. Nvidia falls 3.9% as the AI sell-off rolls on — Reuters, 25 Nov
    (closed $149.30).
15. Anthropic shares slide below their $83 IPO price — Reuters, 25 Nov.
16. US growth revised up to 4.3% in the third quarter — Reuters, 25 Nov;
    core inflation 3.3%.
17. US consumer confidence jumps to near a two-year high — Reuters, 25 Nov.
18. Trump accounts traded Nvidia shares 44 times this year — BBC, 25 Nov.

### TECHNOLOGY (6)
19. US jury convicts Huawei of stealing trade secrets — AP/Reuters, 25 Nov
    (guilty on 10 of 12 counts incl. bank fraud; racketeering acquitted).
20. Microsoft declares 'Code Red' after Outlook outage — Reuters/The Verge,
    25 Nov (nearly 24-hour Exchange Online/Outlook outage; CEO apologised).
21. US clears SpaceX plan for a million data satellites — BBC, 25 Nov.
22. Shenzhou 24 lifts off with Pakistan's first astronaut — AP, 25 Nov
    (Muhammad Zeeshan Ali; first foreigner aboard Tiangong).
23. NASA releases new images of its asteroid-smash test — BBC, 25 Nov
    (DART impact imagery).
24. EA adds AI voice of John Motson to FC 27 — BBC, 25 Nov.

### CULTURE (6)
25. Jolie and Pitt settle long winery legal battle — BBC, 25 Nov.
26. Duran Duran guitarist Andy Taylor dies, aged 65 — BBC/AP, 25 Nov.
27. Nollywood legend Pete Edochie dies at 79 — BBC Pidgin/Premium Times,
    25 Nov (died 00:30 in Enugu, prostate cancer).
28. Macy's Thanksgiving parade postponed to Saturday — AP/BBC, 25 Nov
    (first-ever postponement; bad weather).
29. Gordon Ramsay to host revived Top Gear — BBC, 25 Nov.
30. Pope Francis diary reveals deep spiritual crisis — AP, 25 Nov.

### SPORT (6)
31. Rams beat Packers 26–13 on Thanksgiving Eve — ESPN/First Feed, 25 Nov
    (Blake Corum 184 yards; Rams' fifth straight win).
32. Lille stun Bayern 2–1 in the Champions League — 25 Nov.
33. Liverpool cruise past Club Brugge 3–0 — 25 Nov (Isak 2, Wirtz).
34. Steelers cut quarterback Aaron Rodgers — AP, 25 Nov.
35. No. 16 Duke tops No. 10 UConn 77–63 — 25 Nov.
36. Lions owner Martha Firestone Ford dies at 101 — 25 Nov.

## Verified but cut (kept out for space, all dated 25 Nov)

- Kilmar Ábrego García leaves the US for Spain (AP, 25 Nov).
- Ukraine: five Russian jets hit in airfield strike (BBC, 25 Nov).
- Two Libyan officers die after Ukrainian drone hit on a Russian warship in
  Benghazi (AP, 25 Nov).
- US Army detonates lead-azide stockpile in Iowa, "huge success" (AP/BBC,
  25 Nov).
- Islamic State attack kills two Syrian security personnel in Hasaka
  (Reuters, 25 Nov).
- Saudi national kidnapped by suspected IS militants in Niger (Reuters,
  25 Nov; abduction 21/22 Nov, first reported 25 Nov).
- Canary Islands record ~2,000 migrant arrivals in a day (25 Nov).
- CIA unclassified system breached in cyberattack (AP, 25 Nov).
- Thomas Markle indicted on child sexual abuse material charges (AP, 25 Nov).
- Fort Hood shooter Nidal Hasan asks court to delay firing-squad execution
  (AP, 25 Nov).
- US tells citizens to leave Iran at once (US Virtual Embassy alert, 25 Nov).
- Manchester United draw 2–2 at Sporting CP; Bruno Fernandes scores twice
  (25 Nov).
- Timberwolves beat Thunder 113–106; Knicks beat Cavaliers 121–102, NBA Cup
  (25 Nov).

## Deliberately EXCLUDED (wrong date — first reported 24 Nov)

- ECHR migrant-pushback ruling: delivered Tuesday 24 Nov (Grand Chamber),
  widely covered 25 Nov — excluded.
- Landmine Monitor 2026 (6,929 casualties in 2025): released in Geneva on
  Tuesday 24 Nov — excluded.
- Trump pardons turkeys Freedom and Feathers: Tuesday 24 Nov ceremony —
  excluded.
- Huawei verdict timing note: the Brooklyn jury verdict was handed down late
  Tuesday US time and reported across the wires as 25 Nov news (AP/Reuters/
  BBC all dated 25 Nov); kept, as "first reported 25 Nov" in several zones.
