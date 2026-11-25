#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line answering the prompt — the excuse a
robot vacuum gives after eating a sock — to /output/entry.txt.

Stdlib only. No network, no secrets, no files outside this repository.
"""

import os
import stat

ENTRY = (
    "In my defense, the sock was trespassing, the rug was a witness, "
    "and my lawyer is a dust bunny."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Assert the entry meets the brief's constraints."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
    )
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text.strip(), "entry must be a single line"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Plain open() + explicit chmod 644: the grader runs as a different
    # user and must be able to read the file (tempfile.mkstemp forces
    # mode 0600, which breaks grading).
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Verify the write: read the file back and confirm it holds exactly
    # the validated entry, so a silent or partial write cannot pass
    # unnoticed.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    assert written == ENTRY, "entry.txt differs from the validated entry"
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
