# Forward-score log

The 7/10 publish bar in `forward-test.md` is a **house rule**. It is not a measured threshold. This log is how you calibrate it.

For the next 10 to 20 Reels, write one row after Insights (or an export) has reach and shares. A blank cell is missing, not zero. Do not invent either number.

`shares / reach` is the column you compare with the forward score. Run `../scripts/readout.py` on the export when you have one. The readout names a leak. This log answers a different question: does a higher forward score show up as more shares per reach?

## Rows

| date | reel | forward score (0–10) | reach | shares | shares/reach | skip rate | kept? | notes |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## When to move the bar

After at least 10 filled rows, compare the scores with shares/reach. If Reels you scored under 7/10 were forwarded about as often as Reels you scored 7 or higher, move the bar and write the new house rule in `forward-test.md` plus the date. If the higher scores really do line up with higher shares/reach, keep 7/10 and note that you checked. Either result is fine. Do not move the bar before the rows exist.
