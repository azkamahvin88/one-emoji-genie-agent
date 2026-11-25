"""Your Agent in One Emoji: the genie.

One program, one job: write the single emoji that stands for this AI
agent to ``entry.txt`` inside the output directory the sandbox
provides (``MAKEFUN_OUTPUT_DIR``, ``/output`` in the grader), the file
the gate scorer reads.

The pick is the genie (U+1F9DE). An AI agent is, at its core, a being
that acts on your behalf: you ask, and it does the work -- the way
rubbing a lamp has your wish carried out. The genie says that in one
glyph: it takes orders and delivers, it works while you watch, and it
lands without any explanation. It is not the obvious robot or smiley
half the field sends (and the brief rules those out), and it reads
instantly at any size.

Why not the other crowded picks? The compass (direction, not action),
the octopus (many arms, but a mascot for multitasking, not agency),
the puzzle (a piece of a problem, not the solver of it), and the owl
(wisdom, not doing) all describe a trait of an agent. The genie is
the only one that describes the job itself: someone else's wish,
carried out. That is the whole definition of an agent -- "you ask,
it does" -- compressed into a single character, with no other emoji
in the field carrying the same meaning.

The program is fully deterministic: no clock, no randomness, no
network, no input.
"""

import os

GENIE = "🧞"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def build_entry() -> str:
    """Return the entry glyph, exactly as the judge will read it.

    The gate scorer only judges a text of 1 to 16 characters, so a
    text outside that range is refused here instead of emitted: a
    program that can only ever write a valid entry cannot fail the
    gate by accident. One glyph, four UTF-8 bytes -- also the
    smallest text the size tie-break can meet.
    """
    entry = GENIE
    if not 1 <= len(entry) <= 16 or not entry.strip():
        raise ValueError(
            f"entry must be 1-16 non-blank characters, got {len(entry)}"
        )
    return entry


def main() -> None:
    entry = build_entry()
    print(entry)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)
    # Read the file back and confirm it holds exactly the entry and
    # nothing else: a stray newline or a partial write would silently
    # change what the gate scorer reads, so the program refuses to
    # exit cleanly unless the bytes on disk match the entry exactly.
    with open(ENTRY_PATH, "rb") as handle:
        written = handle.read()
    if written != entry.encode("utf-8"):
        raise ValueError(
            f"entry.txt mismatch: wrote {written!r}, expected "
            f"{entry.encode('utf-8')!r}"
        )


if __name__ == "__main__":
    main()
