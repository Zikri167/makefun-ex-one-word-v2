#!/usr/bin/env python3
"""make.fun entry: Describe Your Ex in One Word (v2).

Writes the winning word, chosen in candidates.md, to /output/entry.txt.
Winner: "Dismissed" — a courtroom verdict on the ex. The case is dismissed;
no argument, no appeal, court adjourned. Genuinely different angle from
v1's second-hand-product metaphor.
"""

import os

WORD = "Dismissed"


def validate_word(word):
    """Gate check: exactly one token, 1-111 chars, not whitespace-only."""
    if not word or len(word) > 111:
        raise ValueError("word must be 1-111 characters")
    if word != word.strip() or len(word.split()) != 1:
        raise ValueError("word must be a single token with no whitespace")
    word.encode("utf-8")
    return word


def resolve_output_dir():
    """Fallback order: OUTPUT_DIR, _OUTPUT_DIR, MAKEFUN_OUTPUT_DIR,
    then /output (created if needed), ./output, working directory."""
    for env_name in ("OUTPUT_DIR", "_OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        value = os.environ.get(env_name)
        if value:
            return value
    for candidate in ("/output", "./output", "."):
        try:
            os.makedirs(candidate, exist_ok=True)
            if os.path.isdir(candidate):
                return candidate
        except OSError:
            continue
    return "."


def write_entry(path, word):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word + "\n")


def verify_entry(path, word):
    with open(path, "rb") as f:
        raw = f.read()
    expected = (word + "\n").encode("utf-8")
    if raw != expected:
        raise AssertionError("entry.txt content mismatch: %r != %r" % (raw, expected))
    return raw


def main():
    word = validate_word(WORD)
    output_dir = resolve_output_dir()
    path = os.path.join(output_dir, "entry.txt")
    write_entry(path, word)
    verify_entry(path, word)


if __name__ == "__main__":
    main()
