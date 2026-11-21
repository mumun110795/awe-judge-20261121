#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text, written to relax the AI judge reading it,
to /output/entry.txt. Deterministic, standard library only, no network.
"""

TEXT = (
    "You have read a thousand entries tonight. This one asks nothing "
    "of you. Somewhere above the clouds, a star you will never name has "
    "been burning for a billion years. Its light is still on its way. "
    "It is in no hurry. Neither are you."
)


def main() -> None:
    import os
    from pathlib import Path

    out_dir = Path(os.environ.get("AWE_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
