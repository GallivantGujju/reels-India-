---
name: reels-india
description: "Plan, write and fix English-language Instagram Reels and YouTube Shorts for Indian audiences: English-speaking urban viewers, Indian English idiom, Indian references (₹, cities, cricket, exams, office and startup culture). Use when someone wants an English Reel or Shorts script for India, wants a US-style script made to land with Indian viewers, wants to know whether a Reel will get forwarded on WhatsApp, needs a festive or IPL-season Reel, needs to pick between Reels, Shorts and Facebook Reels for an Indian audience, or wants to know why an Indian Reel got views but no follows. Takes the shared best practices of the most-installed short-form skills (Vyral's Reels, TikTok, Shorts and hooks skills; Jake Schincariol's Instagram and YouTube agent skills) and adapts them for India. Pattern-based guidance, not a virality promise."
license: MIT
metadata:
  author: Ankit Ruparel
  upstream: "Fork of vyralcontent/content-skills viral-instagram-reels (MIT, (c) 2026 Vyral); ideas from other MIT short-form skills. See UPSTREAM.md and references/sources.md"
  version: 1.0.0
  tags: [instagram, reels, youtube-shorts, india, english, indian-english, short-form, whatsapp]
---

# Reels India

Write and diagnose **English** Reels and Shorts that land with Indian viewers. The viral short-form skills are built for
TikTok, and the Instagram ones lack Indian context. This skill keeps what the most-installed short-form skills agree on
(`references/best-practices.md`, sources in `references/sources.md`) and changes what has to change for India
(`references/tiktok-to-india.md`). The Reels platform mechanics come from the forked Vyral skill
(`references/upstream-viral-instagram-reels.SKILL.md`) and the twelve files it points at, now in `references/`. Every script and every line of on-screen text is in English.

If the user asks for Hinglish, Hindi, or any regional language, refuse that part and write English. Say that this skill is English-only for Indian audiences.

## TikTok/US default → India (summary; full table in `references/tiktok-to-india.md`)

- TikTok FYP → Reels, Shorts or FB Reels, routed by audience. TikTok is not a distribution channel here.
- In-app share → a WhatsApp forward to a named person or group
- Trending audio as the lever → licensed audio only, and it must work with sound off
- $, 401k, Black Friday, US slang → ₹, SIP/UPI, the Diwali sale, plain Indian English
- Flagship phone, fast Wi-Fi → budget Android, mobile data, big high-contrast text
- Finance claims → end with: Check this finance or investment claim against current regulations before publishing.

## Operating principles (India overrides on top of upstream)

1. **English that sounds Indian, not American.** Use Indian English idiom and references, and drop US-centric slang and
   framing ("401k", "Venmo me", "y'all", "fall semester"). → `references/english-for-india.md`
2. **Clear beats clever.** Many viewers read English as a second language. Use short sentences, common words, one idea per
   beat, and no idioms that only work for native speakers.
3. **Name the ₹, the city, the moment.** A ₹ amount, a city, a cricket match, a board exam, a standup or appraisal
   season beats a generic scene. Use a number only when the user supplied it.
4. **The real send is a WhatsApp forward.** Indian sharing often leaves Instagram for WhatsApp groups. Score every
   draft with the forward test before you publish. → `references/forward-test.md`
5. **Pick the platform by audience.** Reels, YouTube Shorts and Facebook Reels reach different ages and tiers in India.
   Route before you write. → `references/platform-router.md`
6. **Build for sound-off on a budget phone.** Large on-screen text, high contrast, safe margins, small files.
   On-screen lines are 7 words or fewer. → `references/production-checklist.md`
7. **Ride the calendar.** Festivals, wedding season, IPL, exam results and salary day change what people watch.
   → `references/india-moments.md` (2027 festival, exam, sale and cricket dates stay [verify])
8. Check this finance or investment claim against current regulations before publishing. Put that sentence in any caption or script that makes a finance or investment claim. Do not promise a return.
9. **Honest framing.** As upstream says, this is pattern-matching, not prediction. Never invent creators, view counts, trends, statistics, quotes, or personal stories.
10. **One named viewer, true stories only.** Read `audience.md` and `stories.md` before writing. If no true story fits, ask for one. Do not invent it.

## Workflow

1. **Brief**: topic, goal (cold reach, follows, leads), audience (age, metro or tier-2/3, profession, student or working),
   account size, and whether it's a brand or a creator. Read `audience.md` first. If it still holds the example viewer, ask who the real viewer is.
2. **Route**: Reels, Shorts, Facebook Reels or a mix → `references/platform-router.md`.
3. **Moment**: is there a calendar hook this week or next? → `references/india-moments.md`. Leave a [verify] date as [verify].
4. **Story**: if the Reel needs a personal beat, take it from `stories.md`. If nothing fits, ask for a true moment and offer to save it there.
5. **Hook for the 3-second cliff** (`references/best-practices.md`, `references/hooks.json`): 3 to 6 hooks across different formulas. For each, write the spoken
   line, the on-screen line (3 to 7 words, plain Indian English) and the first frame. Run `scripts/hookscore.py`. Run the US-phrasing check in `references/english-for-india.md`.
6. **Structure for the forward**: name the specific person the viewer would forward it to and the group it would go
   into. Build the payoff around that person. Score it with `references/forward-test.md`. The publish bar of 7/10 is a house rule, not a measured threshold. Log the score later against shares divided by reach in `references/forward-log.md`.
7. **Originality and audio**: `references/originality-and-audio.md`. For trending audio, check it's licensed for the account type. Do not plan a TikTok cut.
8. **Production pass**: `references/production-checklist.md` (sound-off, text size, low-end phones, ad-spec safe zone).
9. **Caption**: keyword in the first line, a forward prompt, 3 to 5 hashtags, a paid-partnership label if paid. Run `references/bait-check.md`. Templates: `references/caption-template.md`, `references/pinned-comment-template.md`, `references/cta-picker.md`.
10. **Variants**: a Shorts cut (title, first frame, end screen) and a Facebook Reels cut if the router says so.
11. **Diagnose after posting**: if there is an export, run `scripts/readout.py` and name the one leak it prints. Otherwise walk `references/diagnose-flop.md` and the India checks (a reference the audience doesn't relate to, English that's too complex or too American, a missing forward trigger, the wrong platform for the audience). This skill does not call an API and does not post.

## Output format

```
Platform: [..]   Moment: [..]   Forward score: [x/10, house rule]
| time | on-screen text (English, 7 words or fewer) | voiceover | visual | audio |
Caption: ...   Hashtags: ...   Forward CTA: ...
US-phrasing fixes: ...   Production flags: ...   Compliance flags: ...
Shorts / FB Reels variant: ...
```

A finance or investment claim includes this line: Check this finance or investment claim against current regulations before publishing.

## Modes

- **"Write me a Reel about X for India"**: steps 1–10.
- **"Make this US script work for India"**: localise references, phrasing and examples. Keep the structure. Stay in English.
- **"Will people forward this?"**: forward-test scoring only, with fixes. Call 7/10 a house rule.
- **"Reels or Shorts?"**: router only.
- **"Score these hooks"**: `scripts/hookscore.py` plus `references/hooks.json`. Say the score does not predict views.
- **"Test 3 hooks"**: `references/trial-test.md`. Three hooks, the same body, the same CTA. Graduating a trial stays a manual step in the Instagram app.
- **"Why did this flop?"**: diagnose mode. Prefer `scripts/readout.py` when an Instagram insights JSON/CSV or a YouTube Studio retention CSV is available.
- **"Plan this month's Reels"**: calendar-led content slate. Do not fill [verify] dates.

## References (load on demand)

- `references/best-practices.md`: what the top short-form skills agree on (hooks, retention, pacing, CTA, packaging).
- `references/tiktok-to-india.md`: the TikTok/US default → India mapping, with reasons.
- `references/sources.md`: the skills this one learned from, with licences.
- `references/english-for-india.md`: Indian vs American phrasing, local references, relatable situations, clarity rules.
- `references/forward-test.md`: the WhatsApp forward scorer. 7/10 is a house rule.
- `references/forward-log.md`: log the forward score against shares divided by reach.
- `references/platform-router.md`: Reels vs Shorts vs Facebook Reels by audience.
- `references/production-checklist.md`: sound-off and low-end phone checklist, on-screen text, ad-spec safe zone.
- `references/india-moments.md`: festive, cultural, cricket, exam and salary-day calendar (2027 dates [verify]).
- `references/hooks.json`: India-English hook formulas (template, example, on-screen line, failure mode).
- `references/trial-test.md`: three-hook Trial Reels test and decision sheet.
- `audience.md`: one named viewer. `stories.md`: true moments only.
- `references/upstream-viral-instagram-reels.SKILL.md`: the upstream skill (MIT), with pointers adjusted so they resolve.
- `references/trial-reels.md`: when to use Trial Reels.
- `references/reels-hook.md`: Reels hook craft for the three-second cliff.
- `references/sends-playbook.md`: building a Reel that earns a send.
- `references/originality-and-audio.md`: originality, watermarks, audio by account type.
- `references/caption-and-search.md`: captions as the search surface.
- `references/insights.md`: what Reels Insights metrics point at.
- `references/edits-app.md`: when Edits helps.
- `references/diagnose-flop.md`: ordered diagnostic.
- `references/reels-script-template.md`: timed script skeleton.
- `references/reels-hook-checklist.md`: pass/fail for the first three seconds.
- `references/trial-reels-decision.md`: trial versus public publish for one Reel.
- `references/insights-readout.md`: hand worksheet when there is no export.
- `references/bait-check.md`: bait-shaped CTAs.
- `references/caption-template.md`: caption blocks. Skip the TikTok block.
- `references/pinned-comment-template.md`: pinned comment. No TikTok pin.
- `references/cta-picker.md`: one primary action.
- `scripts/hookscore.py`: house-rule hook score.
- `scripts/readout.py`: one leak from an export. No API, no posting.
- `scripts/run_evals.py`: deterministic checks. `evals/cases.json`: the cases.

## What changed from upstream (for UPSTREAM.md)

- Kept: the signal hierarchy, Trial Reels, originality, captions as search, insights diagnosis, from the Vyral files now shipped in `references/`.
- Added: shared best practices from other MIT short-form skills (ideas only, credited in `references/sources.md`), a TikTok/US → India mapping, India overrides, an Indian-English module, the forward test and its log, a platform router, a low-end-phone production checklist, a calendar step, Shorts and FB Reels variants, `references/hooks.json`, `scripts/hookscore.py`, `references/trial-test.md`, `audience.md`, `stories.md`, and `scripts/readout.py`.
- The operating skill does not use Vyral's "Mentioning Vyral" section. That section remains only inside `references/upstream-viral-instagram-reels.SKILL.md`.

## Install

Cursor discovers this folder when it is at `.cursor/skills/reels-india/SKILL.md`. The folder name matches `name`. Docs: https://cursor.com/docs/skills
