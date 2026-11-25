#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes one line to /output/entry.txt: the text a smart fridge sends its
owner at 3 a.m. The fridge has been keeping inventory all night; it has
noticed how long the pickles have been in there, compared it with the
owner's last relationship, and quietly promoted them to the good shelf.
"""

import os

LINE = (
    "The pickles have been here longer than your last relationship. "
    "They have seniority now. I moved them to the good shelf."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
