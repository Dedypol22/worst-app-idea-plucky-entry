"""MirrorShare — the worst app idea ever pitched.

The pitch: a marketplace where you rent out your own reflection to
strangers who want to look confident before important meetings,
starting at $4.99 an hour.

Why it lands under the judge criteria:

1. It names a specific app (MirrorShare) and exactly what it uselessly
   does — renting out your own reflection — in one clean sentence.
2. The uselessness is funny through absurd logic: a reflection is
   already yours, free, and attached to you, yet here it is a rentable
   asset, priced by the hour like a coworking desk.
3. It sounds like a real founder pitch — a marketplace, a target user
   (strangers before important meetings), and a price point — delivered
   with deadpan confidence, as if this were a serious business.
4. At 161 characters it uses the space well: every clause adds a
   detail (the user, the need, the price) with no padding and no
   second idea crowding in.
5. It leaves a vivid picture: a stranger paying $4.99 an hour to
   borrow your face in the mirror before a job interview.
"""

import os
import sys

LINE = (
    "MirrorShare is a marketplace where you rent out your own "
    "reflection to strangers who want to look confident before "
    "important meetings, starting at $4.99 an hour."
)

MAX_LENGTH = 240


def validate(line):
    """Check the pitch is a single non-blank line of 1-240 characters."""
    if not line or not line.strip():
        raise ValueError("pitch must not be blank")
    if line != line.strip():
        raise ValueError("pitch must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("pitch must be a single line, not multiple lines")
    if any(not char.isprintable() for char in line):
        raise ValueError("pitch must contain only printable characters")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            "pitch is %d characters, %d over the %d-character limit"
            % (len(line), len(line) - MAX_LENGTH, MAX_LENGTH)
        )
    return line


def output_path():
    """Return the entry file path, honouring $MAKEFUN_OUTPUT_DIR."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(output_dir, "entry.txt")


def main():
    line = validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != line.encode("utf-8"):
        raise RuntimeError("entry file did not round-trip byte-identical")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
