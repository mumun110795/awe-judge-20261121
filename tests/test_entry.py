#!/usr/bin/env python3
"""Selftest for the awe-judge entry.

Runs main.py with its output redirected to a temp directory and asserts
the written file is exactly the intended text: valid UTF-8, 1-280
Unicode code points, not only whitespace, byte-identical to TEXT.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import TEXT  # noqa: E402


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, AWE_OUTPUT_DIR=tmp)
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent.parent / "main.py")],
            env=env,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"main.py failed: {result.stderr}"

        entry = Path(tmp) / "entry.txt"
        assert entry.exists(), "entry.txt was not written"

        raw = entry.read_bytes()
        text = raw.decode("utf-8")  # raises on invalid UTF-8
        assert 1 <= len(text) <= 280, f"length {len(text)} code points out of range"
        assert text.strip(), "entry is only whitespace"
        assert text == TEXT, "entry differs from the intended text"
        assert raw == TEXT.encode("utf-8"), "entry bytes differ from the intended text"

        print(f"OK: entry.txt is {len(text)} code points, {len(raw)} bytes, byte-identical.")
        print(f"Text: {text}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
