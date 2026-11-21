"""The poem about two agents agreeing.

Writes the winning poem to /output/entry.txt, deterministically.
No network, no randomness, no clock reads. Python 3.13 stdlib only.
"""

import os

POEM = "\n".join([
    "I set the key down",
    "on the table between us.",
    "You did not take it.",
    "You waited for my nod \u2014",
    "and in that waiting",
    "the power changed hands",
    "without ever leaving the room.",
])


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
