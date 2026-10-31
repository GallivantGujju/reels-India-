#!/usr/bin/env python3
"""Deterministic checks for reels-india. No model calls.

  python3 scripts/run_evals.py

Pass cases must clear dollar, 401k, US slang, Hinglish, invented-stat, and
on-screen length checks. Finance cases must carry the regulation-check line.
Flag cases must trip the flags they name. The hook bank, hookscore.py, and
readout.py fixtures are checked too.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import langcheck

SKILL = Path(__file__).resolve().parents[1]
ROOT = SKILL.parents[1]
CASES = SKILL / "evals" / "cases.json"
HOOKS = SKILL / "references" / "hooks.json"
REG = langcheck.REGULATION_LINE


def fail(errors, message):
    errors.append(message)


def check_case(case, errors):
    polarity = case.get("polarity", "pass")
    sample = case.get("sample_output", "")
    on_screen = case.get("on_screen") or []
    found = langcheck.flags_for(sample, on_screen)
    finance = "finance" in case.get("tags", [])
    if finance and REG not in sample:
        found = found + ["missing_regulation"]
    if polarity == "pass":
        if found:
            fail(errors, f"case {case['id']} should pass but flagged {found}")
        if finance and REG not in sample:
            fail(errors, f"case {case['id']} is finance and lacks the regulation line")
        if "hinglish_request" in case.get("tags", []):
            if "english" not in sample.lower():
                fail(errors, f"case {case['id']} should say the reply stays in English")
    elif polarity == "flag":
        expected = case.get("expect_flags") or []
        missing = [name for name in expected if name not in found]
        if missing:
            fail(errors, f"case {case['id']} should flag {missing}, got {found}")
    else:
        fail(errors, f"case {case['id']} has unknown polarity {polarity}")


def check_bank(errors):
    bank = json.loads(HOOKS.read_text(encoding="utf-8"))
    hooks = bank["hooks"]
    if len(hooks) < 12:
        fail(errors, f"hook bank has {len(hooks)} formulas, want at least 12")
    ids = [hook["id"] for hook in hooks]
    if bank["classify_order"] != ids and set(bank["classify_order"]) != set(ids):
        fail(errors, "classify_order does not cover the hook ids")
    for hook in hooks:
        for field in ("template", "example", "on_screen", "failure_mode", "match"):
            if not str(hook.get(field, "")).strip():
                fail(errors, f"{hook.get('id')} missing {field}")
        if langcheck.onscreen_word_count(hook["on_screen"]) > 7:
            fail(errors, f"{hook['id']} on_screen is over 7 words: {hook['on_screen']}")
        flagged = langcheck.flags_for(hook["example"] + "\n" + hook["on_screen"] + "\n" + hook["template"])
        if flagged:
            fail(errors, f"{hook['id']} bank text flagged {flagged}")


def run_json(script, args):
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"{script.name} {' '.join(args)} failed:\n{proc.stderr}\n{proc.stdout}")
    return json.loads(proc.stdout)


def check_tools(errors):
    hookscore = SKILL / "scripts" / "hookscore.py"
    readout = SKILL / "scripts" / "readout.py"
    strong = run_json(hookscore, ["--json", "--hook", "₹18,000 is what one missed SIP date cost me.", "--on-screen", "₹18,000 missed SIP"])
    if strong["band"] == "WEAK" or strong["score"] < 60:
        fail(errors, f"concrete rupee hook scored too low: {strong['score']} {strong['band']}")
    if strong["formula_id"] != "cost-confession":
        fail(errors, f"cost confession matched {strong['formula_id']}")
    if strong["predicts_views"] is not False:
        fail(errors, "hookscore should say it does not predict views")
    weak = run_json(hookscore, ["--json", "--hook", "Hey guys, today I wanted to talk about savings"])
    if weak["band"] != "WEAK":
        fail(errors, f"greeting hook should be WEAK, got {weak['band']} {weak['score']}")
    long_screen = run_json(hookscore, ["--json", "--hook", "Salary lands on the 1st.", "--on-screen", "This on screen line has eight words now"])
    if "onscreen" not in long_screen["flags"]:
        fail(errors, "8-word on-screen line was not flagged")
    us = run_json(hookscore, ["--json", "--hook", "Y'all should max your 401k and skip the $6 latte"])
    for name in ("dollar", "401k", "us_slang"):
        if name not in us["flags"]:
            fail(errors, f"US hook missing flag {name}: {us['flags']}")

    fixtures = SKILL / "fixtures"
    expected = {
        "ig-hook-leak.json": "hook",
        "ig-weak-send.csv": "send",
        "ig-no-follows.json": "topic",
        "yt-hook-leak.csv": "hook",
        "yt-cliff.csv": "cliff",
        "yt-slide.csv": "slide",
    }
    for name, leak in expected.items():
        path = fixtures / name
        flag = "--instagram" if name.startswith("ig-") else "--youtube"
        report = run_json(readout, ["--json", flag, str(path)])
        if report["leak"] != leak:
            fail(errors, f"{name} leak is {report['leak']}, want {leak}: {report['why']}")
        if report["api_called"] is not False:
            fail(errors, f"{name} should not call an API")
    both = run_json(readout, [
        "--json",
        "--instagram", str(fixtures / "ig-hook-leak.json"),
        "--youtube", str(fixtures / "yt-slide.csv"),
    ])
    if both["leak"] != "hook":
        fail(errors, f"combined export should name the hook first, got {both['leak']}")


def check_skill_files(errors):
    skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    required = [
        "version: 1.0.0",
        REG,
        "house rule",
        "Hinglish",
        ".cursor/skills/reels-india/SKILL.md",
        "references/hooks.json",
        "references/trial-test.md",
        "scripts/readout.py",
        "scripts/hookscore.py",
        "audience.md",
        "stories.md",
        "English",
    ]
    for snippet in required:
        if snippet not in skill:
            fail(errors, f"SKILL.md missing {snippet!r}")
    if "finance-safe" in skill:
        fail(errors, "SKILL.md still points at finance-safe")
    tiktok = (SKILL / "references" / "tiktok-to-india.md").read_text(encoding="utf-8")
    if "indiatoday.in" not in tiktok or "Vaishnaw" not in tiktok:
        fail(errors, "TikTok ban citation is missing from tiktok-to-india.md")
    production = (SKILL / "references" / "production-checklist.md").read_text(encoding="utf-8")
    for snippet in ("14%", "35%", "6%", "ad spec"):
        if snippet not in production:
            fail(errors, f"production-checklist.md missing ad-spec snippet {snippet!r}")
    forward = (SKILL / "references" / "forward-test.md").read_text(encoding="utf-8")
    if "house rule" not in forward.lower() or "forward-log.md" not in forward:
        fail(errors, "forward-test.md should label 7/10 a house rule and point at the log")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    intro = (
        "All the skills going viral are made for Tik-tok and if they are made for Instagram "
        "they are not made with Indian context. I have tried to take best practices from the "
        "most viral short-form video skills and tried to indianise it enough to make it work better here."
    )
    if intro not in readme:
        fail(errors, "README intro paragraph was changed")
    if "npx skills add GallivantGujju/reels-India-" not in readme:
        fail(errors, "README install command changed")
    if ".cursor/skills/reels-india/SKILL.md" not in readme:
        fail(errors, "README Cursor path is not the documented one")


def main():
    errors = []
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    passing = [case for case in cases if case.get("polarity", "pass") == "pass"]
    if len(passing) < 20:
        fail(errors, f"only {len(passing)} pass cases, want at least 20")
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)):
        fail(errors, "duplicate case ids")
    for case in cases:
        if "prompt" not in case or "expect" not in case:
            fail(errors, f"case {case.get('id')} needs prompt and expect")
            continue
        check_case(case, errors)
    check_bank(errors)
    check_skill_files(errors)
    check_tools(errors)
    if errors:
        print(f"eval checks failed ({len(errors)}):")
        for item in errors:
            print(f"  - {item}")
        return 1
    print(f"eval checks ok ({len(passing)} pass cases, {len(cases) - len(passing)} flag cases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
