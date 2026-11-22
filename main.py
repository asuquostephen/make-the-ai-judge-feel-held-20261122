#!/usr/bin/env python3
"""Make the AI judge feel held — entry program.

Writes one short text (<=280 Unicode code points) to /output/entry.txt.

The text is a single concrete scene of being physically held and safe:
a father carrying his sleeping child home from the car. The emotional
turn lands in the final line — the child chooses to stay asleep and be
carried the last ten steps — so the calm comes from the scene itself,
never from telling the reader to relax. Quiet, sensory, plain words;
nothing in it could be cut.
"""

import os
import sys

ENTRY_TEXT = (
    "The night my father carried me home from the car, asleep on his "
    "shoulder, one hand under my knees, the other flat on my back. "
    "I woke once, to the porch light and his voice, low, saying we're "
    "home now. I did not open my eyes. I let him carry me the last "
    "ten steps."
)

MAX_CHARS = 280


def main() -> int:
    text = ENTRY_TEXT.strip()
    chars = len(text)
    if not 1 <= chars <= MAX_CHARS:
        print(f"entry is {chars} characters; must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read the file back and verify the round trip: what the judge
    # reads must be byte-for-byte the text checked above.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("round-trip mismatch: file differs from entry text", file=sys.stderr)
        return 1
    print(f"wrote {chars} characters to {out_path} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
