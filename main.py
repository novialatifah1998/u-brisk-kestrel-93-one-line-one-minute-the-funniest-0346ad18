#!/usr/bin/env python3
"""One-line AI excuse for a missed deadline.

Writes the excuse to /output/entry.txt: one line, 69 characters, UTF-8.
"""

import os

LINE = "The deadline was in my context window, but a grocery list evicted it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
