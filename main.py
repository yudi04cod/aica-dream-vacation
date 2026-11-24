#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

The whole entry is a single emoji: Mount Fuji, U+1F5FB.

Why this one: a dream vacation should be one particular place, not
any holiday. Fuji is a postcard in a single glyph — a snow-capped
peak under a blue sky, the trip everyone pictures when they say
"one day, Japan". It is specific where a beach or a plane is generic,
instantly readable at any size on any screen, and it carries the
quiet surprise of choosing a mountain over the obvious seaside.
"""

from pathlib import Path

# Mount Fuji, U+1F5FB — one code point, four UTF-8 bytes.
DREAM = "\U0001F5FB"


def entry_bytes() -> bytes:
    """Encode the chosen emoji, refusing anything that is not one glyph."""
    if len(DREAM) != 1:
        raise ValueError("entry must be exactly one character")
    if DREAM.isspace():
        raise ValueError("entry must not be whitespace")
    return DREAM.encode("utf-8")


def write_entry() -> Path:
    """Write the emoji to /output/entry.txt and check what landed."""
    import os
    import sys

    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = entry_bytes()
    # The gate allows 1-8 characters; our entry is exactly one, and
    # four bytes is the smallest honest size a single emoji can be.
    if len(payload) != 4:
        print("unexpected emoji byte length", file=sys.stderr)
        raise SystemExit(1)
    target.write_bytes(payload)
    landed = target.read_bytes()
    if landed != payload or len(landed.decode("utf-8")) != 1:
        print("entry.txt does not match the chosen emoji", file=sys.stderr)
        raise SystemExit(1)
    return target


def main() -> int:
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
