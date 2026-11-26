#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one sign line (1-120 chars) to /output/entry.txt.
"""

SIGN = "Do not unplug Rack 3. The ghost inside is the only one who remembers the root password."

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def get_sign():
    """Return the sign line, stripped of surrounding whitespace."""
    return SIGN.strip()


def validate(text):
    """Gate: the entry must be 1-120 non-blank characters."""
    if not text or text.isspace():
        raise ValueError("sign must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"sign must be 1-120 chars, got {len(text)}")
    return text


def main():
    text = validate(get_sign())
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
