"""Snooze Button Roast entry.

Writes a single roast line (at most 200 characters, one line) about an
alarm clock ringing at 6 AM on a Saturday to ``entry.txt`` inside the
output directory named by ``MAKEFUN_OUTPUT_DIR`` (default ``/output``).
Standard library only; runs under ``python3 -S``.
"""

import os

ENTRY = (
    "At 6 AM on a Saturday my alarm rang like a town crier with a grudge, "
    "announcing nothing at all except that sleep had just filed for divorce."
)


def main():
    if not ENTRY.strip():
        raise ValueError("entry text must not be empty")
    if len(ENTRY) > 200 or "\n" in ENTRY:
        raise ValueError("entry must be a single line of at most 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError as exc:
        raise SystemExit("failed to write entry.txt: %s" % exc)


if __name__ == "__main__":
    main()
