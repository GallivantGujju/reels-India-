# Changelog

## 1.0.0

- Shipped the 12 Vyral Reels files the forked skill points at, plus the caption, pinned-comment, bait-check, and CTA templates from Vyral's captions skill. MIT, credited in NOTICE.md and UPSTREAM.md, lightly adapted for English scripts aimed at Indian audiences. Pointers to files that are not in this repo were removed.
- Set the skill version to 1.0.0. The merged v0.1 skill had been marked 0.2.0-draft.
- Cited the TikTok ban (India Today, 8 September 2025, IT Minister Ashwini Vaishnaw), the Reels ad safe zone (14% top, 35% bottom, 6% each side, labelled an ad spec), and the Cursor install path `.cursor/skills/reels-india/SKILL.md`.
- Left 2027 festival, exam, sale, and cricket dates marked [verify].
- Labelled the 7/10 forward-test bar a house rule and added `references/forward-log.md` to compare it with shares divided by reach.
- Added an India-English hook bank (`references/hooks.json`) and `scripts/hookscore.py`. The JSON field shape follows Jake Schincariol's MIT hook bank. The formulas and the scorer are original.
- Added a Trial Reels hook test: three hooks, the same body, the same CTA, and a decision sheet. Graduating a trial stays a manual step in the Instagram app.
- Added `audience.md` and `stories.md`. The skill asks for a true story instead of inventing one.
- Expanded evals to 24 pass cases plus flag fixtures, and added `scripts/run_evals.py` (dollar, 401k, US slang, on-screen length, Hinglish, the regulation-check line, invented stats).
- Added `scripts/readout.py` for an Instagram insights JSON or CSV and a YouTube Studio retention CSV. It names one leak. Sample fixtures are synthetic. No API, no OAuth, no posting.
- Added a GitHub Action that fails when a skill or reference path is missing and runs the deterministic checks.

## 0.1.0

- First merged skill: English Reels and Shorts for Indian audiences, forked from Vyral's viral-instagram-reels, with the India modules (phrasing, forward test, platform router, production checklist, calendar) and 7 eval cases. The version field in that skill file read 0.2.0-draft.
