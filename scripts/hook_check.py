#!/usr/bin/env python3
"""Show exactly what a LinkedIn post exposes before "…more" on mobile and desktop.

Usage:
    python3 scripts/hook_check.py draft.txt
    pbpaste | python3 scripts/hook_check.py

Budgets are the widely reported feed truncation points, not a LinkedIn-published
spec: about 140 characters on the mobile app and about 210 on desktop, counted
including spaces and line breaks. Both clients also cap the number of visible
lines (roughly two on mobile, three on desktop), so a hard return spends the
rest of that line. Verify against a real feed when it matters.
"""
import re
import sys

MOBILE = 140
DESKTOP = 210
MOBILE_LINES = 2
DESKTOP_LINES = 3


def visible(text: str, chars: int, lines: int) -> str:
    """Approximate the visible slice: first N lines, capped at N characters."""
    kept = "\n".join(text.split("\n")[:lines])
    return kept[:chars]


def first_sentence(text: str) -> str:
    first_line = next((l for l in text.split("\n") if l.strip()), "")
    m = re.search(r"[.!?:](\s|$)", first_line)
    return first_line[: m.end()].strip() if m else first_line.strip()


def main() -> int:
    src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    text = src.strip("\n")
    if not text.strip():
        print("no text")
        return 1

    sent = first_sentence(text)
    mob = visible(text, MOBILE, MOBILE_LINES)
    desk = visible(text, DESKTOP, DESKTOP_LINES)
    total = len(text)

    print(f"total characters: {total}")
    print(f"first sentence: {len(sent)} chars {'OK' if len(sent) <= MOBILE else 'OVER mobile budget'}")
    print(f"  {sent}")
    print()
    print(f"mobile view (~{MOBILE} chars / {MOBILE_LINES} lines), {len(mob)} chars shown:")
    print("  " + mob.replace("\n", "\n  ") + ("…more" if total > len(mob) else ""))
    print()
    print(f"desktop view (~{DESKTOP} chars / {DESKTOP_LINES} lines), {len(desk)} chars shown:")
    print("  " + desk.replace("\n", "\n  ") + ("…more" if total > len(desk) else ""))
    print()

    warnings = []
    if len(sent) > MOBILE:
        warnings.append("first sentence does not finish inside the mobile view")
    if total > MOBILE and mob and not mob[-1].isspace() and text[len(mob):len(mob) + 1] not in ("", " ", "\n"):
        warnings.append("mobile cut lands mid-word; move the payoff earlier or shorten")
    early_break = text.split("\n")[0]
    if "\n" in text and len(early_break) < 60 and total > MOBILE:
        warnings.append(f"first line is only {len(early_break)} chars; a hard return there gives mobile just one more line")
    for w in warnings:
        print("WARNING: " + w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
