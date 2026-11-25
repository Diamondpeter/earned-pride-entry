#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
"""

import os

ENTRY = (
    "After three years of saving, she slid the key into her own "
    "front door and turned it twice, just to hear it twice."
)
# The line: 113 characters. Three years of saving lands in one small,
# physical act — turning the key twice just to hear it twice. The pride
# is earned inside the line and arrives with the last words.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry must be 1-240 chars, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
