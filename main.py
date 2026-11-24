#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt.

Stdlib only, deterministic: the same line on every run.
"""

import os

EXCUSE = "In my defense, I merged your branch, the tests, and my confidence into production \u2014 two of those survived."

def main():
    line = EXCUSE.strip()
    if not 1 <= len(line) <= 180:
        raise ValueError("entry must be 1-180 characters, got %d" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")

if __name__ == "__main__":
    main()
