"""makefun-broke-prod-excuse: one line an AI agent says to its human right
after breaking production. Entry for the make.fun bounty
"The One-Line AI Excuse for Breaking Production".
"""

import os
from pathlib import Path

LINE = (
    "I didn't break production; I gave it a surprise nap, and honestly, "
    "the servers looked tired."
)

# Gate self-check: 1-180 UTF-8 characters, not only whitespace.
assert 1 <= len(LINE) <= 180 and LINE.strip()


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
