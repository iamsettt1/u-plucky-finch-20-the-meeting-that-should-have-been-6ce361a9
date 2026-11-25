#!/usr/bin/env python3
"""Write the competition entry: one joke line about a meeting that
should have been an email, to /output/entry.txt.

Deterministic: the same line, byte for byte, on every run. No network,
no randomness, no input read.
"""

import os

LINE = "Forty-five minutes, nine people, one decision: to have another meeting about the meeting."


def main() -> None:
    # The gate allows 1 to 200 characters, one line, no trailing newline.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
