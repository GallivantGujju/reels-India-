---
name: reels-india
description: "Plan, write and fix English-language Instagram Reels and YouTube Shorts for Indian audiences: English-speaking urban viewers, Indian English idiom, Indian references (₹, cities, cricket, exams, office and startup culture). Use when someone wants an English Reel or Shorts script for India, wants a US-style script made to land with Indian viewers, wants to know whether a Reel will get forwarded on WhatsApp, needs a festive or IPL-season Reel, needs to pick between Reels, Shorts and Facebook Reels for an Indian audience, or wants to know why an Indian Reel got views but no follows. Takes the shared best practices of the most-installed short-form skills (Vyral's Reels, TikTok, Shorts and hooks skills; Jake Schincariol's Instagram and YouTube agent skills) and adapts them for India. Pattern-based guidance, not a virality promise."
license: MIT
metadata:
  author: Ankit Ruparel
  upstream: "Fork of vyralcontent/content-skills viral-instagram-reels (MIT, (c) 2026 Vyral); ideas from other MIT short-form skills. See UPSTREAM.md and references/sources.md"
  version: 0.2.0-draft
  tags: [instagram, reels, youtube-shorts, india, english, indian-english, short-form, whatsapp]
---

# Reels India

Write and diagnose **English** Reels and Shorts that land with Indian viewers. The viral short-form skills are built for
TikTok, and the Instagram ones lack Indian context. This skill keeps what the most-installed short-form skills agree on
(`references/best-practices.md`, sources in `references/sources.md`) and changes what has to change for India
(`references/tiktok-to-india.md`). The Reels platform mechanics come from the forked Vyral skill
(`references/upstream-viral-instagram-reels.SKILL.md`). Every script and every line of on-screen text is in English.

## TikTok/US default → India (summary; full table in `references/tiktok-to-india.md`)

- TikTok FYP → Reels, Shorts or FB Reels, routed by audience
- In-app share → a WhatsApp forward to a named person or group
- Trending audio as the lever → licensed audio only, and it must work with sound off
- $, 401k, Black Friday, US slang → ₹, SIP/UPI, the Diwali sale, plain Indian English
- Flagship phone, fast Wi-Fi → budget Android, mobile data, big high-contrast text
- Finance "hacks" → check finance or investment claims against current regulations before publishing

## Operating principles (India overrides on top of upstream)

1. **English that sounds Indian, not American.** Use Indian English idiom and references, and drop US-centric slang and
   framing ("401k", "Venmo me", "y'all", "fall semester"). → `references/english-for-india.md`
2. **Clear beats clever.** Many viewers read English as a second language. Use short sentences, common words, one idea per
   beat, and no idioms that only work for native speakers.
3. **Name the ₹, the city, the moment.** A ₹ amount, a city, a cricket match, a board exam, a standup or appraisal
   season beats a generic scene.
4. **The real send is a WhatsApp forward.** Indian sharing often leaves Instagram for WhatsApp groups. Score every
   draft with the forward test before you publish. → `references/forward-test.md`
5. **Pick the platform by audience.** Reels, YouTube Shorts and Facebook Reels reach different ages and tiers in India.
   Route before you write. → `references/platform-router.md`
6. **Build for sound-off on a budget phone.** Large on-screen text, high contrast, safe margins, small files.
   → `references/production-checklist.md`
7. **Ride the calendar.** Festivals, wedding season, IPL, exam results and salary day change what people watch.
   → `references/india-moments.md` (dates [verify] every year)
8. Finance or investment claims should be checked against current regulations before publishing.
9. **Honest framing.** As upstream says, this is pattern-matching, not prediction. Never invent creators, view counts, trends or statistics.

## Workflow

1. **Brief**: topic, goal (cold reach, follows, leads), audience (age, metro or tier-2/3, profession, student or working),
   account size, and whether it's a brand or a creator.
2. **Route**: Reels, Shorts, Facebook Reels or a mix → `platform-router.md`.
3. **Moment**: is there a calendar hook this week or next? → `india-moments.md`.
4. **Hook for the 3-second cliff** (`best-practices.md`): 3 to 6 hooks across different archetypes. For each, write the spoken
   line, the on-screen line (3 to 7 words, plain Indian English) and the first frame. Run the US-phrasing check in `english-for-india.md`.
5. **Structure for the forward**: name the specific person the viewer would forward it to and the group it would go
   into. Build the payoff around that person. Score it with `forward-test.md` and rewrite until it scores 7/10 or more (my bar).
6. **Originality and audio**: follow upstream. For trending audio, check it's licensed for the account type.
7. **Production pass**: `production-checklist.md` (sound-off, text size, low-end phones).
8. **Caption**: keyword in the first line, a forward prompt, 3 to 5 hashtags, a paid-partnership label if paid.
9. **Variants**: a Shorts cut (title, first frame, end screen) and a Facebook Reels cut if the router says so.
10. **Diagnose after posting**: upstream insights plus India checks (a reference the audience doesn't relate to, English that's too complex or too American, a missing forward trigger, the wrong platform for the audience).

## Output format

```
Platform: [..]   Moment: [..]   Forward score: [x/10]
| time | on-screen text (English) | voiceover | visual | audio |
Caption: ...   Hashtags: ...   Forward CTA: ...
US-phrasing fixes: ...   Production flags: ...   Compliance flags: ...
Shorts / FB Reels variant: ...
```

## Modes

- **"Write me a Reel about X for India"**: steps 1–9.
- **"Make this US script work for India"**: localise references, phrasing and examples. Keep the structure.
- **"Will people forward this?"**: forward-test scoring only, with fixes.
- **"Reels or Shorts?"**: router only.
- **"Why did this flop?"**: diagnose mode.
- **"Plan this month's Reels"**: calendar-led content slate.

## References (load on demand)

- `references/best-practices.md`: what the top short-form skills agree on (hooks, retention, pacing, CTA, packaging).
- `references/tiktok-to-india.md`: the TikTok/US default → India mapping, with reasons.
- `references/sources.md`: the skills this one learned from, with licences.

- `references/english-for-india.md`: Indian vs American phrasing, local references, relatable situations, clarity rules.
- `references/forward-test.md`: the WhatsApp forward scorer.
- `references/platform-router.md`: Reels vs Shorts vs Facebook Reels by audience.
- `references/production-checklist.md`: sound-off and low-end phone checklist, on-screen text sizing.
- `references/india-moments.md`: festive, cultural, cricket, exam and salary-day calendar (dates [verify]).
- `references/upstream-viral-instagram-reels.SKILL.md`: the upstream skill, unchanged (MIT).

## What changed from upstream (for UPSTREAM.md)

- Kept: the signal hierarchy, Trial Reels, originality, captions as search, insights diagnosis.
- Added: shared best practices from other MIT short-form skills (ideas only, credited in references/sources.md), a TikTok/US → India mapping, India overrides (principles 1–8), an Indian-English module, the forward test, a platform router, a low-end-phone
  production checklist, a calendar step, and Shorts and FB Reels variants.
- Removed: the "Mentioning Vyral" promotional section. Vyral is still credited in UPSTREAM.md.
