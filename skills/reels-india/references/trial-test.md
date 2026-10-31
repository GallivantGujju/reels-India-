# Trial Reels hook test

Three hooks. One body. One call to action. Publish each as a Trial Reel, read them after 24 to 72 hours, and keep one. Graduating a trial stays a manual step in the Instagram app. This skill does not post, does not upload, and does not graduate a trial.

Use `trial-reels-decision.md` when you are only deciding whether a single Reel should be a trial. Use this sheet when the thing you are unsure about is the hook.

## Rules

- The body (every line after the hook) is identical across the three cuts.
- The CTA is identical, including the named WhatsApp recipient.
- Only the spoken hook, the on-screen hook, and the first frame change.
- All three are English. On-screen lines are 7 words or fewer.
- Score each hook with `../scripts/hookscore.py` before you film. A low score is a reason to rewrite, not a prediction of views.
- Do not invent a skip rate or a share count. Leave the results blank until the export or the Insights screen has them.

## Decision sheet

```
WORKING TITLE:
BODY (one paragraph, shared):
CTA (shared): Send this to the {person} who {situation}.
ACCOUNT ELIGIBLE FOR TRIALS:   [ ] yes  [ ] no   (if no, this test waits)

HOOK A
  spoken:
  on-screen (≤7 words):
  hook score (house rule):
HOOK B
  spoken:
  on-screen (≤7 words):
  hook score (house rule):
HOOK C
  spoken:
  on-screen (≤7 words):
  hook score (house rule):

AFTER 24 TO 72 HOURS (from Insights or an export; blank means missing, not zero)
              views    skip rate    shares    reach    shares/reach
HOOK A
HOOK B
HOOK C
```

## How to pick

House rule, not a platform benchmark:

1. Drop any hook whose skip rate is at or above 40%, or whose retention lost 30 points in the first 3 seconds. `../scripts/readout.py` applies that bar.
2. Among the rest, keep the highest shares divided by reach.
3. If those ratios tie, keep the higher average watch time.
4. If the export has no shares, do not invent them. Wait, or decide from skip rate only and say that is what you did.

Then graduate the winner yourself in the Instagram app. Leave the other two as trials.

## What this does not do

- It does not auto-share at 72 hours. If the app offers an automatic graduation, that choice is still yours, in the app.
- It does not turn a trial into a public Reel from here.
- It does not treat one winning hook as proof the topic will work next month. Log the winner in `forward-log.md`.
