#!/usr/bin/env python3
"""One-line AI excuse for a missed deadline.

Writes the excuse to /output/entry.txt: one line, 69 characters, UTF-8.
Falls back to ./output/entry.txt when /output is not writable, and
refuses to write an entry outside the 1-200 character gate.
"""

import os
import sys

LINE = "The deadline was in my context window, but a grocery list evicted it."

OUTPUT_PATHS = ("/output/entry.txt", "output/entry.txt")


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        print(f"entry is {len(LINE)} chars, outside the 1-200 gate", file=sys.stderr)
        raise SystemExit(1)
    last_error = None
    for path in OUTPUT_PATHS:
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(LINE)
            return
        except OSError as exc:
            last_error = exc
    print(f"could not write entry: {last_error}", file=sys.stderr)
    raise SystemExit(1)


if __name__ == "__main__":
    main()
