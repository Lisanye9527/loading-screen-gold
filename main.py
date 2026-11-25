"""Entry for make.fun bounty "Loading Screen Gold: A Tip in 200 Characters".

Writes one line of text -- a loading-screen tip for stressed developers
and AI coding agents -- to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output``
when the variable is unset, matching the grader container).

The line is a constant, so the program is deterministic: every run
writes exactly the same bytes. Before writing, the program checks the
line against the bounty gate (UTF-8 text of 1 to 200 characters, not
only white space, a single line) and fails loudly if it ever drifts
out of bounds.

Run it from the repository root, for example:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

TIP = (
    "Tip: This loading screen is the AI re-reading all 40,000 lines "
    "of your codebase, so it can change the wrong file with total "
    "confidence \u2014 then explain, in detail, why it was the right one."
)

MAX_CHARS = 200


def main() -> int:
    line = TIP
    if not line.strip():
        print("error: the tip is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: the tip must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: the tip is {len(line)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(line, encoding="utf-8")
    written = dest.read_text(encoding="utf-8")
    if written != line:
        print("error: written text differs from the tip", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(line)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
