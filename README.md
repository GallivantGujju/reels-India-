# reels-India-

All the skills going viral are made for Tik-tok and if they are made for Instagram they are not made with Indian context. I have tried to take best practices from the most viral short-form video skills and tried to indianise it enough to make it work better here.

An agent skill for writing, planning and fixing **English-language Instagram Reels and YouTube Shorts for Indian audiences**.
It keeps what the most-installed short-form skills agree on (hooks, retention, pacing, CTA, packaging) and changes what
has to change for India: Indian English instead of US idiom, ₹ and city specifics, cricket, exams, office and startup
culture, CTAs built for the WhatsApp forward, and production for sound-off viewing on budget phones. It works in
Claude Code, Cursor and other agents that support SKILL.md skills.

The base is a fork of Vyral's [`viral-instagram-reels`](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-instagram-reels) (MIT).
Ideas also come from Vyral's TikTok, Shorts and hooks skills and from Jake Schincariol's Instagram and YouTube agent skills
(all MIT). See [Sources we learned from](#sources-we-learned-from) and [UPSTREAM.md](UPSTREAM.md).

> Status: **v0.2 draft**. It's pattern-based guidance and doesn't promise virality.

## Modules

| Module | File | What it does |
|---|---|---|
| Short-form best practices | `references/best-practices.md` | What the top short-form skills agree on: hooks, retention, pacing, CTA, packaging |
| TikTok/US → India mapping | `references/tiktok-to-india.md` | Each TikTok or US default, the India adaptation, and why |
| English for India | `references/english-for-india.md` | Indian vs American phrasing swaps, local references, relatable situations, clarity rules for mixed English proficiency |
| WhatsApp forward test | `references/forward-test.md` | Scores a draft 0–10 on "would someone forward this to a group?" and rewrites the weak parts |
| Platform router | `references/platform-router.md` | Reels vs Shorts vs Facebook Reels by audience age and city tier (heuristics, [verify]) |
| Production checklist | `references/production-checklist.md` | Sound-off viewing, on-screen text size and contrast, safe zones, low-end phones, slow data |
| India moments calendar | `references/india-moments.md` | Diwali, wedding season, IPL, exam results, appraisal and placement season, salary day (dates [verify]) |
| Diagnose | `SKILL.md` | Why a Reel got views but no follows: relatability, English that's too complex or too American, no forward trigger, wrong platform |
| Compliance hand-off | → copy-council `finance-safe` | Finance and health claims go there first |

## Install

Repository: https://github.com/GallivantGujju/reels-India-

With the skills CLI:

```
npx skills add GallivantGujju/reels-India-
```

Or clone the repo:

```
git clone https://github.com/GallivantGujju/reels-India-.git
```

Manually, copy the `skills/reels-india/` folder to:

- **Claude Code**: `~/.claude/skills/reels-india/` (all projects) or `.claude/skills/reels-india/` (one project)
- **Cursor**: `.cursor/skills/reels-india/` in your project [verify against current Cursor docs]

The skill folder is self-contained.

## Examples

```
Write a 25-second English Reel for India: why young professionals in Bengaluru are buying bonds.
Here's a US creator's money-saving script. Make it work for Indian viewers.
Will people forward this Reel?
Should this exam-prep explainer go on Reels, Shorts or Facebook?
My Diwali gifting Reel got 40k views and 3 follows. Why?
```

Test prompts with expected behaviour are in `skills/reels-india/evals/cases.json`.

## Layout

```
skills/reels-india/SKILL.md
skills/reels-india/references/best-practices.md
skills/reels-india/references/tiktok-to-india.md
skills/reels-india/references/sources.md
skills/reels-india/references/english-for-india.md
skills/reels-india/references/forward-test.md
skills/reels-india/references/platform-router.md
skills/reels-india/references/production-checklist.md
skills/reels-india/references/india-moments.md              (dates [verify])
skills/reels-india/references/upstream-viral-instagram-reels.SKILL.md   upstream, unchanged
skills/reels-india/evals/cases.json
shared/india-moments.md                                     canonical calendar
UPSTREAM.md, NOTICE.md, LICENSE, LICENSE.vyral
```

## Sources we learned from

Install figures as read on 31 Oct 2026 IST; they change daily.

| Source | What we took | Licence | Signal |
|---|---|---|---|
| [Vyral viral-instagram-reels](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-instagram-reels) | Forked: Reels mechanics (sends per reach, Trial Reels, originality, captions as search) | MIT © 2026 Vyral | not indexed on skills.marketing |
| [Vyral viral-tiktok-content](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-tiktok-content) | Completion gate, saves and shares over likes, anti-patterns; the defaults this skill maps to India | MIT © 2026 Vyral | 29,794 installs on skills.marketing, the most-installed short-form skill there |
| [Vyral viral-youtube-shorts](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-youtube-shorts) | Retention curve, loops, the Short → long-form link | MIT © 2026 Vyral | not indexed on skills.marketing |
| [Vyral viral-hooks](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-hooks) | Hook batches, three hook layers, specific beats clever | MIT © 2026 Vyral | |
| [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) | Scored hooks, the hook/stake/body/payoff/loop shape, separate on-screen script, safe zone | MIT © 2026 Jake Schincariol | ~8.6K installs across the repo on skills.sh |
| [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) | Shorts that stand alone with a new first line; retention diagnosis | MIT © 2026 Jake Schincariol | ~5.9K installs across the repo on skills.sh |

Only the Vyral Reels file is included as text, shipped unchanged under its licence. Everything else is ideas, rewritten.

## Pairs well with

- [srvjha/reel-animated-explainer](https://github.com/srvjha/reel-animated-explainer): a Claude Code plugin that turns a talking-head video into an animated explainer reel with Remotion (word-timed captions, scenes, music ducking). Use reels-india for the script, then that plugin for the edit. Check its licence before you reuse anything.

## Inspirations and credits

These ideas came from people posting on X about short-form video and distribution in India. The handles are credited for the thinking. Nothing here quotes them or is endorsed by them, and I haven't re-checked the individual posts [verify before linking]:

- [@Divyetweets](https://x.com/Divyetweets) (Divye Agarwal, co-founder of Binge Labs): a 0→450K Reels case study that shaped the hook and format thinking
- [@janwhyy](https://x.com/janwhyy) (Janhavi Jain): a post on dark social, i.e. sharing over WhatsApp and DMs, which led to the forward test
- [@neilmukti](https://x.com/neilmukti): D2C bets in India
- [@VaibhavSisinty](https://x.com/VaibhavSisinty) (Vaibhav Sisinty, GrowthSchool): using AI to test content variations

## Sibling repos

- [copy-council](https://github.com/GallivantGujju/copy-council): six classic copywriters score your copy 0–100, plus a `finance-safe` check
- [whatsapp-funnel](https://github.com/GallivantGujju/whatsapp-funnel): WhatsApp-first lifecycle funnels for Indian brands

## Disclaimer and [verify] notes

- Not legal or compliance advice. For finance or health claims, run the copy through copy-council's `finance-safe` skill and your own compliance team. Indian ad rules (ASCI, SEBI, RBI) are **not** encoded here.
- Festival, exam and sale dates move every year. Every date in `india-moments.md` is [verify] until you fill it from an official source.
- The platform router and production checklist are heuristics. No platform demographics are claimed. Check them against your own analytics.
- The forward-test publish bar (7/10) is a working rule, not a measured threshold.
- Not affiliated with or endorsed by Vyral, Jake Schincariol, Instagram/Meta or YouTube/Google.

## Licence

MIT © 2026 Ankit Ruparel. It includes MIT-licensed material © 2026 Vyral and draws on MIT-licensed work by Jake Schincariol. See NOTICE.md.
