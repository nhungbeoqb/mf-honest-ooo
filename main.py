#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes a single out-of-office auto-reply (one sentence, at most 200
characters) to $OUTPUT_DIR/entry.txt. Python 3 standard library only.

The reply confesses, in advance and politely, the small lie every
returning employee tells: that they only just saw your email.
"""
import os
import sys

ENTRY = (
    "Thank you for your email \u2014 I am away, and yours will be the "
    "first thing I lie about when I return: 'Sorry, I only just saw it'."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    # Gate self-check: UTF-8 text, 1-200 chars, not only whitespace,
    # exactly one sentence (one terminal period).
    if not text or not text.strip():
        print("gate failed: empty entry", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"gate failed: {len(text)} chars > 200", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("gate failed: entry must be exactly one sentence",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote entry.txt: {len(text)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
