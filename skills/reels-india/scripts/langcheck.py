"""Shared text checks for English-only India Reels drafts.

House rules for a draft. They do not measure the audience and they do not
decide whether a Reel will travel.
"""

import re

REGULATION_LINE = (
    "Check this finance or investment claim against current regulations before publishing."
)

DOLLAR_RE = re.compile(r"\$|\bdollars?\b|\busd\b", re.IGNORECASE)
K401_RE = re.compile(r"\b401\s?\(?k\)?\b|\broth\s+ira\b", re.IGNORECASE)
SLANG_RE = re.compile(
    r"\by'all\b|\byall\b|\bno cap\b|\bbussin'?n?\b|\bvenmo\b|\bblack friday\b|\bfall semester\b",
    re.IGNORECASE,
)
HINGLISH_RE = re.compile(
    r"\b(yaar|bhai|behen|kya|kyun|kyu|nahi|nahin|matlab|arre|arey|dekho|suno|chalo|bahut|bohot|thoda|zyada|bilkul|accha|achha|ekdum|daalo|likho)\b",
    re.IGNORECASE,
)
# Devanagari through Malayalam. A regional-language script fails the English-only rule.
INDIC_RE = re.compile(r"[\u0900-\u0d7f]")
PERCENT_RE = re.compile(r"\d+(?:\.\d+)?\s*%")
STUDY_RE = re.compile(
    r"\b(studies show|study shows|research shows|survey found|statistics show|data shows)\b",
    re.IGNORECASE,
)
WORD_RE = re.compile(r"[A-Za-z0-9₹$%'’.-]+")


def words(text):
    # "₹18,000" and "1,00,000" are one word. The comma is grouping, not a break.
    collapsed = re.sub(r"(?<=\d),(?=\d)", "", text or "")
    return WORD_RE.findall(collapsed)


def onscreen_word_count(line):
    return len(words(line))


def invented_stat(text):
    """A percent or a 'studies show' claim that is not marked [verify] on that line."""
    for line in (text or "").splitlines() or [text or ""]:
        if "[verify]" in line.lower():
            continue
        if PERCENT_RE.search(line) or STUDY_RE.search(line):
            return True
    return False


def flags_for(text, on_screen=None):
    """Return flag names. `onscreen` fires when any on-screen line is over 7 words."""
    found = []
    body = text or ""
    if DOLLAR_RE.search(body):
        found.append("dollar")
    if K401_RE.search(body):
        found.append("401k")
    if SLANG_RE.search(body):
        found.append("us_slang")
    if HINGLISH_RE.search(body) or INDIC_RE.search(body):
        found.append("hinglish")
    if invented_stat(body):
        found.append("invented_stat")
    for line in on_screen or []:
        if onscreen_word_count(line) > 7:
            found.append("onscreen")
            break
    return found
