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

> Status: **v1.0.0**. Pattern-based guidance. It does not promise virality, and it does not post.

## What's new in v1

- The 12 Vyral files the forked skill points at are in the repo, plus Vyral's caption, pinned-comment, bait-check, and CTA templates. MIT, credited, lightly adapted for India. See [UPSTREAM.md](UPSTREAM.md).
- Version 1.0.0 and a [CHANGELOG.md](CHANGELOG.md) from 0.1 to 1.0.
- TikTok ban, Reels ad safe zones, and the Cursor install path are cited. 2027 festival and exam dates stay [verify].
- The 7/10 forward bar is labelled a house rule, with a log against shares divided by reach.
- An India-English hook bank and `scripts/hookscore.py`. Scores are house rules, not view predictions.
- A Trial Reels hook test: 3 hooks, the same body, the same CTA. Graduating a trial stays a manual step in the Instagram app.
- `audience.md` and `stories.md`. The skill asks for a true story instead of inventing one.
- 24 eval cases and `scripts/run_evals.py`. A GitHub Action runs the link check and those checks.
- `scripts/readout.py` reads an Instagram insights export and a YouTube Studio retention CSV and names one leak. No API, no OAuth, no posting.

## Modules

| Module | File | What it does |
|---|---|---|
| Short-form best practices | `skills/reels-india/references/best-practices.md` | What the top short-form skills agree on: hooks, retention, pacing, CTA, packaging |
| TikTok/US → India mapping | `skills/reels-india/references/tiktok-to-india.md` | Each TikTok or US default, the India adaptation, and why |
| English for India | `skills/reels-india/references/english-for-india.md` | Indian vs American phrasing swaps, local references, relatable situations, clarity rules for mixed English proficiency |
| WhatsApp forward test | `skills/reels-india/references/forward-test.md` | Scores a draft 0–10. The 7/10 bar is a house rule |
| Forward log | `skills/reels-india/references/forward-log.md` | Log that score against shares divided by reach for the next 10 to 20 Reels |
| Platform router | `skills/reels-india/references/platform-router.md` | Reels vs Shorts vs Facebook Reels by audience age and city tier (heuristics, [verify] against your analytics) |
| Production checklist | `skills/reels-india/references/production-checklist.md` | Sound-off viewing, on-screen text, the Reels ad-spec safe zone, low-end phones |
| India moments calendar | `skills/reels-india/references/india-moments.md` | Diwali, wedding season, IPL, exam results, appraisal and placement season, salary day (2027 dates [verify]) |
| Hook bank | `skills/reels-india/references/hooks.json` | English formulas: template, Indian example, on-screen line, failure mode |
| Trial hook test | `skills/reels-india/references/trial-test.md` | 3 hooks, same body, same CTA, decision sheet |
| Audience and stories | `skills/reels-india/audience.md`, `skills/reels-india/stories.md` | One named viewer. True moments only |
| Vyral Reels files | `skills/reels-india/references/` | Trial Reels, hooks, sends, originality, captions, insights, Edits, diagnose, and the four templates |
| Diagnose | `skills/reels-india/scripts/readout.py` | One leak from an Instagram export or a YouTube Studio retention CSV |

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
- **Cursor**: `.cursor/skills/reels-india/SKILL.md`. Cursor's Agent Skills docs load project skills from `.cursor/skills/`, and the folder name matches the skill `name` (https://cursor.com/docs/skills).

The skill folder is self-contained. It does not need a token.

## Examples

```
Write a 25-second English Reel for India: why young professionals in Bengaluru are buying bonds.
Here's a US creator's money-saving script. Make it work for Indian viewers.
Will people forward this Reel?
Should this exam-prep explainer go on Reels, Shorts or Facebook?
My Diwali gifting Reel got 40k views and 3 follows. Why?
Test 3 hooks for this Reel. Same body, same CTA.
Score this hook.
Here is my Instagram insights export and my YouTube retention CSV. What is the one leak?
```

Test prompts with expected behaviour are in `skills/reels-india/evals/cases.json`. Run `python3 skills/reels-india/scripts/run_evals.py`.

## Layout

```
skills/reels-india/SKILL.md
skills/reels-india/audience.md
skills/reels-india/stories.md
skills/reels-india/references/best-practices.md
skills/reels-india/references/tiktok-to-india.md
skills/reels-india/references/sources.md
skills/reels-india/references/english-for-india.md
skills/reels-india/references/forward-test.md
skills/reels-india/references/forward-log.md
skills/reels-india/references/platform-router.md
skills/reels-india/references/production-checklist.md
skills/reels-india/references/india-moments.md              (2027 dates [verify])
skills/reels-india/references/hooks.json
skills/reels-india/references/trial-test.md
skills/reels-india/references/upstream-viral-instagram-reels.SKILL.md
skills/reels-india/scripts/hookscore.py
skills/reels-india/scripts/readout.py
skills/reels-india/scripts/run_evals.py
skills/reels-india/scripts/check_links.py
skills/reels-india/evals/cases.json
skills/reels-india/fixtures/
shared/india-moments.md                                     canonical calendar
UPSTREAM.md, NOTICE.md, CHANGELOG.md, LICENSE, LICENSE.vyral
```

## Sources we learned from

Install figures as read on 31 Oct 2026 IST; they change daily.

| Source | What we took | Licence | Signal |
|---|---|---|---|
| [Vyral viral-instagram-reels](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-instagram-reels) | The Reels skill, the 12 files it points at, lightly adapted | MIT © 2026 Vyral | not indexed on skills.marketing |
| [Vyral viral-captions-and-ctas](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-captions-and-ctas) | Bait check, caption template, pinned comment, CTA picker | MIT © 2026 Vyral | |
| [Vyral viral-tiktok-content](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-tiktok-content) | Completion gate, saves and shares over likes, anti-patterns; the defaults this skill maps to India | MIT © 2026 Vyral | 29,794 installs on skills.marketing, the most-installed short-form skill there |
| [Vyral viral-youtube-shorts](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-youtube-shorts) | Retention curve, loops, the Short → long-form link | MIT © 2026 Vyral | not indexed on skills.marketing |
| [Vyral viral-hooks](https://github.com/vyralcontent/content-skills/tree/main/skills/viral-hooks) | Hook batches, three hook layers, specific beats clever | MIT © 2026 Vyral | |
| [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) | The field shape of the hook bank. Formulas and the scorer are original | MIT © 2026 Jake Schincariol | ~8.6K installs across the repo on skills.sh |
| [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) | Hook leak, cliff, and slide as three different problems. The readout code is original | MIT © 2026 Jake Schincariol | ~5.9K installs across the repo on skills.sh |

## Pairs well with

- [srvjha/reel-animated-explainer](https://github.com/srvjha/reel-animated-explainer): a Claude Code plugin that turns a talking-head video into an animated explainer reel with Remotion (word-timed captions, scenes, music ducking). Use reels-india for the script, then that plugin for the edit. Check its licence before you reuse anything.

## Inspirations and credits

These ideas came from people posting on X about short-form video and distribution in India. The handles are credited for the thinking. Nothing here quotes them or is endorsed by them, and I haven't re-checked the individual posts [verify before linking]:

- [@Divyetweets](https://x.com/Divyetweets) (Divye Agarwal, co-founder of Binge Labs): a 0→450K Reels case study that shaped the hook and format thinking
- [@janwhyy](https://x.com/janwhyy) (Janhavi Jain): a post on dark social, i.e. sharing over WhatsApp and DMs, which led to the forward test
- [@neilmukti](https://x.com/neilmukti): D2C bets in India
- [@VaibhavSisinty](https://x.com/VaibhavSisinty) (Vaibhav Sisinty, GrowthSchool): using AI to test content variations

## Limits

- The skill does not post, does not upload, and does not graduate a Trial Reel. Graduation stays a manual step in the Instagram app.
- `scripts/readout.py` reads files you already exported. A blank metric is missing, not zero.
- Hook scores and the 7/10 forward bar are house rules. They are not predictions.
- Not legal or compliance advice. A finance or investment claim should carry this line: Check this finance or investment claim against current regulations before publishing. Health claims should be checked with your own compliance team. Indian ad rules (ASCI, SEBI, RBI) are **not** encoded here.
- Festival, exam and sale dates move. Every 2027 date of that kind in `skills/reels-india/references/india-moments.md` is [verify] until you fill it from an official source.
- The platform router is a set of heuristics. No platform demographics are claimed. Check them against your own analytics.
- Not affiliated with or endorsed by Vyral, Jake Schincariol, Instagram/Meta or YouTube/Google.

## Sibling repos

- [copy-council](https://github.com/GallivantGujju/copy-council): six classic copywriters score your copy 0–100
- [whatsapp-funnel](https://github.com/GallivantGujju/whatsapp-funnel): WhatsApp-first lifecycle funnels for Indian brands

## Licence

MIT © 2026 Ankit Ruparel. It includes MIT-licensed material © 2026 Vyral and uses the field shape of MIT-licensed work by Jake Schincariol. See NOTICE.md.
