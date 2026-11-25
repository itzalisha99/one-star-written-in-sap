#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review from a houseplant about the human
who owns it to /output/entry.txt.
"""

import os

ENTRY = (
    "One star. She mists my leaves twice a day and never waters my roots, "
    "so I am damp on the outside and dying on the inside."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8, 1-279 chars, not whitespace-only."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > 279:
        raise ValueError(f"entry is {len(text)} chars, over the 279 limit")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
