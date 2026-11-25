"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one joke line (at most 200 characters) to /output/entry.txt.
Pure standard library.
"""

import os

# The turn lands on the last beat: the meeting did not replace the email,
# it became the email's drafting session — nine people, out loud, with slides.
LINE = "Nine of us spent an hour writing one email together \u2014 out loud, with slides."

MAX_CHARS = 200


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1-200 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write atomically, exactly one line, no trailing newline:
    # the gate counts every character in the file.
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
