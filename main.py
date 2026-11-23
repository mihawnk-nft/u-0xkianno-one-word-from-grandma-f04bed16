"""One Word From Grandma — entry program (pure stdlib).

Writes exactly one word to /output/entry.txt: the word a grandma
would text about AI.

The word is ROBUT — grandma's typo for ROBOT. Warm, a little
baffled, funny in one word, tied to robots/machines, and a fresh
twist on the obvious pick.
"""

import os

WORD = "ROBUT"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
