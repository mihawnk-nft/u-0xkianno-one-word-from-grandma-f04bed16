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

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 30
# characters, not only white space. Fail loudly instead of writing
# an entry the gate would refuse.
assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
assert WORD.strip(), "word must not be only white space"
assert WORD == WORD.strip(), "word must not carry surrounding space"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
