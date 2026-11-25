"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one joke line (at most 200 characters) to /output/entry.txt.
Pure standard library.
"""

import os

LINE = "Nine of us spent an hour writing one email together, out loud, with slides."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one line, no trailing newline: the gate counts characters.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
