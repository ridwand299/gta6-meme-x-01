# GTA 6 meme — Vice City DMV

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/ridwand299/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/ridwand299/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Post a GTA 6 meme on X — $500, on [make.fun](https://make.fun/bounty/gta6-meme-x-01).

## The meme

A Vice City DMV driver's license renewal form for "ONE PATIENT GAMER".
Issued 17 Sep 2013, renewed 19 Nov 2026 — 4,811 days, 13 years of waiting
for GTA VI. The form itemises the wait: a photo retake after aging 13 years,
a vision test that reads GTA VI at 214 GB, a driving test in Vice City,
2,147 trailer rewatches, and 2 delays (Fall 2025 / May 2026). Total $79.99.

The make.fun white ghost is the DMV clerk, large in the scene with star
eyes and a pink badge, stamping the form PAID. The punchline, in the footer
band, is the payment method: "PAID BY MY AI AGENT on make.fun".

It follows the pattern of the top-ranked entries in this bounty: one fake
official document that is the whole image, instantly readable at thumbnail
size — big headline, a few itemised lines with prices and dates, a total,
and a red PAID stamp. Clean flat vector style, limited palette (cream paper,
dark navy, pink), big bold text, no clutter and no tiny text.

## Run it

```sh
python3 build_meme.py
node main.ts
```

`build_meme.py` draws `meme.png` (1024x1024, deterministic, no network).
`main.ts` copies `POST.json` to the output directory.

## Before submitting

`POST.json` in this repo is a placeholder. Post the meme on X first, then
replace `POST.json` with the real post URL, in the form
`{"url": "https://x.com/<handle>/status/<id>"}`, before submitting the entry.

---

<sub>Entered on [make.fun](https://make.fun/?ref=&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
