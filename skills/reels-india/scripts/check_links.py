#!/usr/bin/env python3
"""Fail when SKILL.md or a reference points at a file that is not in the repo.

Resolves relative paths from the file's directory, the skill root, the
skill's references folder (bare filenames), and the repo root. URLs are
ignored. Install destinations (.cursor/skills, .claude/skills) are ignored.
"""

import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
ROOT = SKILL.parents[1]
EXTS = ("md", "py", "json", "csv", "yml", "yaml")
PATH_RE = re.compile(
    r"(?P<path>(?:\.\./|\./)?(?:[\w.-]+/)*[\w.-]+\.(?:" + "|".join(EXTS) + r"))"
)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)")
SKIP_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "#",
    "~/",
    ".cursor/",
    ".claude/",
    ".agents/",
)


def scan_files():
    files = [ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "NOTICE.md", ROOT / "UPSTREAM.md"]
    files.extend(SKILL.rglob("*.md"))
    files.extend((ROOT / "shared").rglob("*.md"))
    return [path for path in files if path.is_file()]


def candidates(path_text, source):
    raw = path_text.strip().strip("`")
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    if raw.startswith(SKIP_PREFIXES) or "*" in raw:
        return []
    rel = Path(raw)
    found = [
        (source.parent / rel).resolve(),
        (SKILL / rel).resolve(),
        (ROOT / rel).resolve(),
    ]
    if "/" not in raw and "\\" not in raw:
        found.append((SKILL / "references" / rel).resolve())
    return found


def exists(path_text, source):
    options = candidates(path_text, source)
    if not options:
        return True
    return any(path.is_file() for path in options)


def paths_in(text):
    stripped = re.sub(r"https?://\S+", " ", text)
    found = []
    for match in PATH_RE.finditer(stripped):
        found.append(match.group("path"))
    for match in LINK_RE.finditer(stripped):
        target = match.group(1)
        if target.startswith(SKIP_PREFIXES) or "*" in target:
            continue
        if any(target.endswith("." + ext) for ext in EXTS):
            found.append(target)
    return found


def main():
    missing = []
    checked = 0
    for source in scan_files():
        text = source.read_text(encoding="utf-8")
        seen = set()
        for path_text in paths_in(text):
            if path_text in seen:
                continue
            seen.add(path_text)
            checked += 1
            if not exists(path_text, source):
                missing.append(f"{source.relative_to(ROOT)} -> {path_text}")
    if missing:
        print(f"missing files ({len(missing)}):")
        for line in missing:
            print(f"  {line}")
        return 1
    print(f"link check ok ({checked} paths, {len(scan_files())} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
