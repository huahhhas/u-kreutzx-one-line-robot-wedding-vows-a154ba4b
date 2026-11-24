#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entry program (stdlib only).

Writes the exact vow line to $OUTPUT_DIR/entry.txt (default /output),
with NO trailing newline, then self-verifies the written file:
UTF-8, 1-160 characters, not only whitespace, exact match,
no trailing newline, byte-identical.
"""

import os
import sys

LINE = "I vow to love you until my battery dies \u2014 and even then, I'll reboot just to say I do."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verification: read back and check every gate condition.
    with open(path, "rb") as f:
        written = f.read()
    text = written.decode("utf-8")  # raises if not valid UTF-8
    assert written == data, "written bytes differ from the line"
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1-160"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text, "line contains a newline"
    assert not written.endswith(b"\n"), "trailing newline present"
    print(f"OK: wrote {len(written)} bytes, {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
