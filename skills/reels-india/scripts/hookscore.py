#!/usr/bin/env python3
"""Score an English Reel hook for an Indian audience.

The bank's field shape follows Jakeschincariol/instagram-agent-skill
hooks.json (MIT). Formulas, examples, and this scoring code are original.
This is a house-rule gate. It does not predict views.

  python3 hookscore.py --hook "₹18,000 is what one missed SIP date cost me."
  python3 hookscore.py --hook "..." --on-screen "₹18,000 missed SIP"
  python3 hookscore.py hooks.txt
  python3 hookscore.py --json --hook "..."
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import langcheck

BANK_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "references", "hooks.json"
)

WEAK_OPENER_RE = re.compile(
    r"(?i)^\s*(hey\b|hi\b|hello\b|welcome\b|so\b|ok\b|okay\b|guys\b|in this (video|reel)|today i|i wanted to|have you ever)"
)
STAKES = {
    "stop", "never", "wrong", "mistake", "lost", "cost", "missed", "before",
    "only", "dont", "don't", "expires", "gone", "lock-in", "notice", "rent",
    "emi", "without", "instead",
}
ADDRESS = {
    "you", "your", "flatmate", "uncle", "manager", "mom", "mum", "parent",
    "parents", "friend", "colleague",
}
CITIES = {
    "bengaluru", "bangalore", "mumbai", "delhi", "pune", "hyderabad",
    "chennai", "kolkata", "gurugram", "gurgaon", "noida", "kota",
}
MARKERS = {
    "sip", "upi", "emi", "pf", "fd", "cibil", "salary", "rent", "chai",
    "swiggy", "metro", "hostel", "lakh", "crore", "ott", "bonus",
}


def clamp(n):
    return max(0.0, min(100.0, n))


def load_bank(path=BANK_PATH):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def match_formula(text, bank):
    by_id = {hook["id"]: hook for hook in bank["hooks"]}
    for hook_id in bank["classify_order"]:
        hook = by_id[hook_id]
        if re.search(hook["match"], text, re.IGNORECASE):
            return hook
    return None


def part_scores(text):
    tokens = [t.lower().strip(".,!?") for t in langcheck.words(text)]
    n = len(tokens)
    if WEAK_OPENER_RE.search(text):
        front = 0.0
    elif n and tokens[0] in {"the", "a", "an", "this", "it"}:
        front = 55.0
    else:
        front = 90.0

    spec = 20.0
    if "₹" in text or "lakh" in tokens or "crore" in tokens:
        spec += 35
    if any(ch.isdigit() for ch in text):
        spec += 25
    if any(t in CITIES for t in tokens):
        spec += 15
    if any(t in MARKERS for t in tokens):
        spec += 10
    spec = clamp(spec)

    if n <= 3:
        length = 45.0
    elif n <= 18:
        length = 100.0
    elif n <= 24:
        length = 60.0
    else:
        length = 25.0

    stakes = 85.0 if any(t in STAKES for t in tokens) else 40.0
    address = 85.0 if any(t in ADDRESS or t in CITIES for t in tokens) else 40.0
    return {
        "frontload": front,
        "specificity": spec,
        "length": length,
        "stakes": stakes,
        "address": address,
    }


def score_hook(text, on_screen=None, bank=None):
    bank = bank or load_bank()
    parts = part_scores(text)
    total = (
        0.24 * parts["frontload"]
        + 0.34 * parts["specificity"]
        + 0.16 * parts["length"]
        + 0.14 * parts["stakes"]
        + 0.12 * parts["address"]
    )
    found = langcheck.flags_for(text, [on_screen] if on_screen else None)
    penalties = {
        "dollar": 40,
        "401k": 40,
        "us_slang": 30,
        "hinglish": 50,
        "invented_stat": 25,
        "onscreen": 20,
    }
    for flag in found:
        total -= penalties[flag]
    if "dollar" in found or "401k" in found or "hinglish" in found or parts["frontload"] == 0:
        total = min(total, 39)
    total = clamp(total)
    if total >= 70:
        band = "STRONG"
    elif total >= 45:
        band = "OK"
    else:
        band = "WEAK"
    formula = match_formula(text, bank)
    weakest = min(parts, key=parts.get)
    dealbreakers = []
    if parts["frontload"] == 0:
        dealbreakers.append("Opens on a greeting or a preamble. Start on the point.")
    if "dollar" in found:
        dealbreakers.append("Dollar sign or the word dollar. Use ₹.")
    if "401k" in found:
        dealbreakers.append("US account (401k or Roth IRA). Use PF, SIP, or FD, and add the regulation-check line if it is a finance claim.")
    if "us_slang" in found:
        dealbreakers.append("US slang. Use plain Indian English.")
    if "hinglish" in found:
        dealbreakers.append("Hinglish or regional-language script. Keep the hook in English.")
    if "invented_stat" in found:
        dealbreakers.append("A percent or a study claim without [verify] on that line.")
    if "onscreen" in found:
        dealbreakers.append("On-screen line is over 7 words.")
    return {
        "hook": text,
        "score": round(total, 1),
        "band": band,
        "formula": formula["name"] if formula else None,
        "formula_id": formula["id"] if formula else None,
        "weakest": weakest.upper(),
        "parts": {k: round(v, 1) for k, v in parts.items()},
        "flags": found,
        "dealbreakers": dealbreakers,
        "on_screen": on_screen,
        "on_screen_words": langcheck.onscreen_word_count(on_screen) if on_screen else None,
        "house_rules": True,
        "predicts_views": False,
    }


def format_one(row):
    lines = [
        f"{row['score']:5.1f}  {row['band']:<6}  {row['hook']}",
        f"        formula: {row['formula'] or 'none'}",
        f"        weakest: {row['weakest']}",
    ]
    if row["on_screen"] is not None:
        lines.append(f"        on-screen ({row['on_screen_words']} words): {row['on_screen']}")
    for item in row["dealbreakers"]:
        lines.append(f"        dealbreaker: {item}")
    lines.append("        house rules, not a view prediction")
    return "\n".join(lines)


def read_hooks(path):
    if path == "-":
        return [line.strip() for line in sys.stdin if line.strip()]
    with open(path, encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Score English Reel hooks for Indian audiences.")
    parser.add_argument("file", nargs="?", help="Text file with one hook per line, or - for stdin.")
    parser.add_argument("--hook", help="Score a single spoken hook.")
    parser.add_argument("--on-screen", help="On-screen line for --hook. Hard cap is 7 words.")
    parser.add_argument("--json", action="store_true", help="Print JSON.")
    args = parser.parse_args(argv)

    if args.hook:
        rows = [score_hook(args.hook, args.on_screen)]
    elif args.file:
        rows = [score_hook(line) for line in read_hooks(args.file)]
        rows.sort(key=lambda row: row["score"], reverse=True)
    else:
        parser.print_help()
        return 2

    if args.json:
        payload = rows[0] if args.hook else rows
        json.dump(payload, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print("HOOK SCORE  (house rules, not a view predictor)")
        for row in rows:
            print(format_one(row))
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
