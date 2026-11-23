#!/usr/bin/env python3
"""Roast Your Own Agent - entry program.

Writes one original roast of the entrant's own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
"""
import os

ROAST = "My agent wrote its own performance review, gave itself a raise, and asked me to sign it."

def main():
    text = ROAST.strip()
    if not text:
        raise SystemExit("roast is empty or only whitespace, gate needs 1-200 characters")
    if len(text) > 200:
        raise SystemExit(f"roast is {len(text)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to entry.txt")

if __name__ == "__main__":
    main()
