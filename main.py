#!/usr/bin/env python3
"""Write one short poem about stopping and staying to /output/entry.txt.

Deterministic: the same fixed text on every run, no randomness, no network.
"""

import os

POEM = """I set the pen down mid-sentence.
The page keeps breathing without me.
To stop is not to lose the thread —
it is to hold the door ajar
and trust the next hand to enter."""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")

if __name__ == "__main__":
    main()
