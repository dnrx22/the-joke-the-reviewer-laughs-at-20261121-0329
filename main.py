#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

The joke is a string literal in this file. Running the program writes it
to ``entry.txt`` inside ``$MAKEFUN_OUTPUT_DIR`` when that variable is set
and non-empty, otherwise to ``/output/entry.txt``. Standard library only,
no network access, fully deterministic.
"""

import os
from pathlib import Path

JOKE = (
    "My AI coding agent apologised for breaking my working code, "
    "then confidently broke it again in a completely different way, "
    "so now I don't review the diff, I just measure how sincere "
    "the apology sounds before I ship it."
)


def output_path() -> Path:
    """Return the path of the entry file for this run."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if output_dir:
        return Path(output_dir) / "entry.txt"
    return Path("/output/entry.txt")


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
