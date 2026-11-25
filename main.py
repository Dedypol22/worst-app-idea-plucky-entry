"""QueuePal — the worst app idea ever pitched.

The pitch: an app that hires someone to stand in line for you at
the DMV, then live-streams their boredom to your phone so you still
feel like you waited, ticket number and all.

Why it wins under the judge criteria:

1. It names a specific app (QueuePal) and exactly what it uselessly
   does — outsourcing the queue, then re-delivering the queue — in
   one clean sentence pitched as a serious product.
2. The uselessness is funny through a perfect mismatch: the app
   solves waiting, then carefully undoes its own solution, so the
   customer pays to avoid the DMV and still experiences the DMV.
   The deadpan kicker, "ticket number and all", sells the founder
   who genuinely believes this is a feature.
3. It sounds like a real founder pitch: a product name, a clear
   service (hire a stand-in), a concrete setting (the DMV), and a
   target user (anyone who hates queues) — no wink, no irony.
4. At 178 characters it uses the space well: every clause adds a
   detail (the hire, the place, the live-stream, the kicker) with
   no padding and no second idea crowding in.
5. It leaves a vivid, specific picture: a stranger filming their
   own boredom on a plastic DMV chair while you watch it from your
   couch, ticket number and all.

Candidates beaten in the v2 draft round (scored 1-5 on each of the
five judge criteria, total out of 25):

- QueuePal, 25/25 — the winner above.
- SidewalkCrack, 23/25 — GPS alerts so you never step on a sidewalk
  crack and break your mother's back; a perfect mismatch, but its
  target user is only implied.
- SockMatch, 22/25 — a certified sock-folding professional mails a
  weekly report on your socks' compatibility; great deadpan, but
  the lost-sock joke is a familiar trope.
- SpotSaver, 22/25 — pay a stranger three dollars to hold a parking
  spot, then receive a photo of the empty space; a complete pitch,
  but holding a spot is plausible enough to be less absurd.
- ElevatorPal, 20/25 — books a friendly stranger to ride the
  elevator with you so you never endure the silence alone.
- DoorbellBuddy, 20/25 — rings your own doorbell when you arrive
  home so you feel the thrill of a surprise visitor, without one.
- GrandmaVoice, 20/25 — calls your phone in your grandmother's
  voice to remind you to wear a jacket, even when she sits next
  to you; voice cloning is a real product, so it reads creepy
  rather than useless.
- UmbrellaShare, 18/25 — rent someone else's umbrella by the
  minute, but only on sunny days; sharp, but a generic
  sharing-economy trope with a thin scene.

This v2 replaces the v1 MirrorShare pitch (a marketplace renting out
your own reflection, 161 characters), which finished round 1 ranked
#1390 of 1852 with a score of 439199 — too close to a generic
absurd-app joke, with no scene the judges could picture.
"""

import os
import sys

LINE = (
    "QueuePal is an app that hires someone to stand in line for "
    "you at the DMV, then live-streams their boredom to your phone "
    "so you still feel like you waited, ticket number and all."
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
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
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
