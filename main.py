"""Haunted sign entry: write one funny line to /output/entry.txt."""

import os

SETUP = "DO NOT ENTER. The ghost in aisle 3 has rebooted the server 47 times"
TURN = "and it still will not stop beeping."


def build_sign():
    return SETUP + " " + TURN


SIGN = build_sign()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SIGN)


if __name__ == "__main__":
    main()
