#!/usr/bin/env python3
"""Name the single biggest leak in an Instagram export or a YouTube Studio retention CSV.

No API, no OAuth, no posting. Numbers below the bars are house rules for this
skill, not platform benchmarks.

  python3 readout.py --instagram insights.json
  python3 readout.py --instagram insights.csv --youtube retention.csv --duration 24
  python3 readout.py --youtube retention.csv --json

Instagram accepts a flat JSON object, a Graph-style {"data": [{"name", "values"}]}
object, or a CSV (metric,value rows, or one header row of metric names).
YouTube accepts a Studio-style CSV: a position (timestamp, seconds, percent, or
0–1 ratio) and a retention figure. Lines starting with # are ignored.

House-rule bars, applied in this order (the earliest one that trips is the leak):
  hook        skip rate >= 40%, or 30 points lost in the first 3 seconds
  cliff       a later step drops 12 points or more
  slide       ending retention <= 35% and no cliff
  watch_time  average watch under 30% of the length
  topic       follows are present, views >= 1000, and follows/views < 0.0008
  send        shares/reach < 1%
"""

import argparse
import csv
import json
import sys

BARS = {
    "skip_rate": 0.40,
    "hook_drop_points": 30.0,
    "cliff_points": 12.0,
    "slide_end": 35.0,
    "send_ratio": 0.01,
    "follows_per_view": 0.0008,
    "min_views_for_follows": 1000,
    "watch_fraction": 0.30,
}
ORDER = ["hook", "cliff", "slide", "watch_time", "topic", "send"]
FIX = {
    "hook": "Recut the first three seconds before you change the body or the CTA.",
    "cliff": "The hold broke at one moment. Compress or pay off the promise there before you touch the ending.",
    "slide": "Viewers left steadily through the middle. Cut pacing. Do not add a new topic.",
    "watch_time": "Average watch is under 30% of the length on this house rule. Shorten the middle before you rewrite the hook.",
    "topic": "Views held up and follows did not. Make the topic legible in the first frame and the first caption line.",
    "send": "Watch held and shares did not. Rewrite the CTA to one named WhatsApp recipient.",
    "none": "No house-rule bar tripped. Do not change the format on this export alone.",
}


def _num(value):
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace(",", "").replace("%", "")
    if text == "":
        return None
    return float(text)


def _first(row, names):
    for name in names:
        if name in row and row[name] not in (None, ""):
            return row[name]
    return None


def _as_ratio(value):
    if value is None:
        return None
    number = float(value)
    if number > 1:
        number = number / 100.0
    return number


def normalize_ig(row):
    lower = {str(k).strip().lower(): v for k, v in row.items() if not str(k).startswith("_")}
    reach = _num(_first(lower, ("reach",)))
    views = _num(_first(lower, ("views", "video_views", "plays")))
    shares = _num(_first(lower, ("shares", "sends", "share_count")))
    follows = _num(_first(lower, ("follows", "followers", "followers_from_this_post")))
    skip = _as_ratio(_num(_first(lower, ("reels_skip_rate", "skip_rate", "skip"))))
    avg = _num(_first(lower, ("ig_reels_avg_watch_time", "avg_watch_time", "average_watch_time", "avg_watch_time_ms")))
    duration = _num(_first(lower, ("video_length_seconds", "duration", "duration_seconds", "length_seconds")))
    unit = str(_first(lower, ("watch_time_unit",)) or "").lower()
    if avg is not None and duration is not None:
        if unit == "ms" or (unit == "" and avg > duration):
            avg = avg / 1000.0
    retention = lower.get("retention")
    return {
        "reach": reach,
        "views": views,
        "shares": shares,
        "follows": follows,
        "skip_rate": skip,
        "avg_watch_s": avg,
        "duration_s": duration,
        "retention": retention,
    }


def load_instagram(path):
    if path.lower().endswith(".json"):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        if isinstance(data, dict) and isinstance(data.get("data"), list):
            flat = {}
            for item in data["data"]:
                if not isinstance(item, dict) or "name" not in item:
                    continue
                values = item.get("values") or []
                if values and isinstance(values[0], dict) and "value" in values[0]:
                    flat[item["name"]] = values[0]["value"]
                elif "value" in item:
                    flat[item["name"]] = item["value"]
            if isinstance(data.get("retention"), list):
                flat["retention"] = data["retention"]
            return normalize_ig(flat)
        if isinstance(data, dict) and isinstance(data.get("metrics"), dict):
            merged = dict(data["metrics"])
            merged.update({k: v for k, v in data.items() if k != "metrics"})
            return normalize_ig(merged)
        if isinstance(data, dict):
            return normalize_ig(data)
        raise SystemExit(f"could not read Instagram JSON: {path}")
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = [
            row for row in csv.reader(fh)
            if row and row[0].strip() and not row[0].strip().startswith("#")
        ]
    if not rows:
        raise SystemExit(f"no rows in {path}")
    header = [cell.strip().lower() for cell in rows[0]]
    if header[0] in ("metric", "name", "metric_name") and len(rows) > 1:
        flat = {}
        for row in rows[1:]:
            if len(row) >= 2:
                flat[row[0].strip()] = row[1].strip()
        return normalize_ig(flat)
    if any(cell in ("reach", "views", "shares") for cell in header) and len(rows) > 1:
        return normalize_ig(dict(zip(header, rows[1])))
    raise SystemExit(f"could not read Instagram CSV: {path}")


def _position(cell):
    text = cell.strip()
    if ":" in text:
        parts = text.split(":")
        try:
            nums = [float(p) for p in parts]
        except ValueError:
            return None
        seconds = 0.0
        for part in nums:
            seconds = seconds * 60 + part
        return seconds
    try:
        return float(text.replace("%", "").replace(",", ""))
    except ValueError:
        return None


def load_youtube(path, duration=None):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        raw_rows = [
            row for row in csv.reader(fh)
            if row and row[0].strip() and not row[0].strip().startswith("#")
        ]
    points = []
    saw_percent_sign = False
    for row in raw_rows:
        if len(row) < 2:
            continue
        if "%" in row[1]:
            saw_percent_sign = True
        x = _position(row[0])
        try:
            y = float(row[1].strip().replace("%", "").replace(",", ""))
        except ValueError:
            continue
        if x is None:
            continue
        points.append((x, y))
    if len(points) < 4:
        raise SystemExit(f"need at least 4 retention points in {path}")
    ys = [y for _, y in points]
    if not saw_percent_sign and max(ys) <= 1.5:
        points = [(x, y * 100.0) for x, y in points]
    xs = [x for x, _ in points]
    if any(":" in (raw_rows[i][0] if i < len(raw_rows) else "") for i in range(len(raw_rows))):
        # timestamps already converted to seconds inside _position; detect via values growing past 1
        # A file of timestamps was converted, so xs are seconds. Mark by checking the source.
        axis = "seconds"
    elif max(xs) <= 1.05:
        axis = "ratio"
    elif duration is None and max(xs) <= 100.5 and len(points) >= 40:
        axis = "percent"
    elif duration is not None and max(xs) <= 100.5 and max(xs) > (duration + 1):
        axis = "percent"
    else:
        # Short exports in seconds (0, 1, 2, ... under a few minutes) and timestamp files.
        axis = "seconds"
    # Timestamp files take the seconds branch above only if we didn't mis-detect.
    # Re-read: if the first cell of a data row contains a colon, force seconds.
    for row in raw_rows:
        if len(row) >= 2 and ":" in row[0]:
            axis = "seconds"
            break
    return {"points": points, "axis": axis, "duration": duration}


def _hook_cutoff(curve, duration):
    axis = curve["axis"]
    if axis == "seconds":
        return 3.0, "first 3 seconds"
    if duration and duration > 0 and axis == "ratio":
        return 3.0 / duration, "first 3 seconds"
    if duration and duration > 0 and axis == "percent":
        return 3.0 / duration * 100.0, "first 3 seconds"
    if axis == "percent":
        return 10.0, "first 10% (duration was not passed, so 3 seconds could not be marked)"
    return 0.10, "first 10% (duration was not passed, so 3 seconds could not be marked)"


def leaks_from_curve(curve, duration=None):
    duration = duration or curve.get("duration")
    points = curve["points"]
    cutoff, window = _hook_cutoff(curve, duration)
    start = points[0][1]
    in_window = [y for x, y in points if x <= cutoff]
    hook_end = in_window[-1] if in_window else start
    hook_drop = start - hook_end
    later = []
    for i in range(1, len(points)):
        x0, y0 = points[i - 1]
        x1, y1 = points[i]
        if x0 < cutoff:
            continue
        later.append((y0 - y1, x0, x1))
    cliff = max(later, default=(0.0, None, None))
    end = points[-1][1]
    found = []
    if hook_drop >= BARS["hook_drop_points"]:
        found.append({
            "id": "hook",
            "severity": hook_drop / 100.0,
            "why": (
                f"Retention lost {hook_drop:.0f} points in the {window}, "
                f"at or above the house-rule bar of {BARS['hook_drop_points']:.0f} points."
            ),
        })
    if cliff[0] >= BARS["cliff_points"]:
        found.append({
            "id": "cliff",
            "severity": cliff[0] / 100.0,
            "why": (
                f"A step from {cliff[1]} to {cliff[2]} lost {cliff[0]:.0f} points, "
                f"at or above the house-rule bar of {BARS['cliff_points']:.0f}."
            ),
        })
    if end <= BARS["slide_end"] and cliff[0] < BARS["cliff_points"]:
        found.append({
            "id": "slide",
            "severity": (start - end) / 100.0,
            "why": (
                f"Retention ended at {end:.0f}%, at or below the house-rule bar of "
                f"{BARS['slide_end']:.0f}%, and no single step cleared the cliff bar."
            ),
        })
    return found


def leaks_from_instagram(metrics):
    found = []
    if metrics.get("retention"):
        # Optional list of {t, pct} or [t, pct].
        points = []
        for item in metrics["retention"]:
            if isinstance(item, dict):
                points.append((_num(item.get("t", item.get("time"))), _num(item.get("pct", item.get("retention")))))
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                points.append((_num(item[0]), _num(item[1])))
        points = [(t, y) for t, y in points if t is not None and y is not None]
        if len(points) >= 4:
            found.extend(leaks_from_curve({"points": points, "axis": "seconds", "duration": metrics.get("duration_s")}))
    skip = metrics.get("skip_rate")
    if skip is not None and skip >= BARS["skip_rate"]:
        found.append({
            "id": "hook",
            "severity": skip,
            "why": (
                f"Skip rate is {skip:.0%}, at or above the house-rule bar of {BARS['skip_rate']:.0%}."
            ),
        })
    avg = metrics.get("avg_watch_s")
    duration = metrics.get("duration_s")
    if avg is not None and duration:
        fraction = avg / duration
        if fraction < BARS["watch_fraction"]:
            found.append({
                "id": "watch_time",
                "severity": BARS["watch_fraction"] - fraction,
                "why": (
                    f"Average watch is {fraction:.0%} of the length, under the house-rule bar of "
                    f"{BARS['watch_fraction']:.0%}."
                ),
            })
    follows = metrics.get("follows")
    views = metrics.get("views")
    if follows is not None and views is not None and views >= BARS["min_views_for_follows"]:
        ratio = follows / views
        if ratio < BARS["follows_per_view"]:
            found.append({
                "id": "topic",
                "severity": BARS["follows_per_view"] - ratio,
                "why": (
                    f"Follows from this Reel are {follows:.0f} on {views:.0f} views "
                    f"({ratio:.4f} follows per view), under the house-rule bar of "
                    f"{BARS['follows_per_view']}."
                ),
            })
    shares = metrics.get("shares")
    reach = metrics.get("reach")
    if shares is not None and reach:
        ratio = shares / reach
        if ratio < BARS["send_ratio"]:
            found.append({
                "id": "send",
                "severity": BARS["send_ratio"] - ratio,
                "why": (
                    f"Shares divided by reach is {ratio:.4f}, under the house-rule bar of "
                    f"{BARS['send_ratio']:.0%}."
                ),
            })
    return found


def pick(found):
    if not found:
        return {
            "id": "none",
            "severity": 0,
            "why": "No house-rule bar tripped on the fields this export contained.",
        }
    rank = {name: i for i, name in enumerate(ORDER)}
    found.sort(key=lambda item: (rank[item["id"]], -item["severity"]))
    return found[0]


def diagnose(instagram=None, youtube=None, duration=None):
    found = []
    if instagram:
        for item in leaks_from_instagram(instagram):
            item["source"] = "instagram"
            found.append(item)
    if youtube:
        for item in leaks_from_curve(youtube, duration):
            item["source"] = "youtube"
            found.append(item)
    winner = pick(found)
    others = [item for item in found if item is not winner and item["id"] != winner["id"]]
    return {
        "leak": winner["id"],
        "source": winner.get("source"),
        "why": winner["why"],
        "fix": FIX[winner["id"]],
        "also": [{"leak": item["id"], "source": item.get("source"), "why": item["why"]} for item in others],
        "house_rules": True,
        "api_called": False,
    }


def format_report(report):
    source = f" ({report['source']})" if report.get("source") else ""
    lines = [
        f"Biggest leak: {report['leak']}{source}",
        f"Why: {report['why']}",
        f"Fix: {report['fix']}",
    ]
    if report["also"]:
        extra = ", ".join(f"{item['leak']} ({item['source']})" for item in report["also"])
        lines.append(f"Later bars also tripped: {extra}. Fix the biggest leak first.")
    lines.append(
        "House rules, not platform benchmarks: skip rate 40%; "
        "30 points lost in the first 3 seconds; a later step of 12 points; "
        "an ending at or below 35% with no cliff; average watch under 30% of the length; "
        "under 0.8 follows per view when the export includes follows and views are at least 1000; "
        "shares/reach under 1%."
    )
    lines.append("No API call. No posting.")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Name the single biggest leak in an export.")
    parser.add_argument("--instagram", help="Instagram insights JSON or CSV.")
    parser.add_argument("--youtube", help="YouTube Studio audience-retention CSV.")
    parser.add_argument("--duration", type=float, help="Video length in seconds, if the CSV axis is a ratio or a percent.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if not args.instagram and not args.youtube:
        parser.print_help()
        return 2
    instagram = load_instagram(args.instagram) if args.instagram else None
    youtube = load_youtube(args.youtube, args.duration) if args.youtube else None
    report = diagnose(instagram, youtube, args.duration)
    if args.json:
        json.dump(report, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(format_report(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
