"""Funniest Forecast for a City That Isn't — entry 1.

Writes a single-line weather forecast for the invented city of
Natterford to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib
only, no network.
"""

import os

ENTRY = (
    "In Natterford, sunshine is expected, but the sun is running "
    "twenty minutes late and has sent a cloud to apologise."
)


def main() -> None:
    # Gate (kit competition.yaml): entry.txt must be UTF-8 text of
    # 1 to 120 characters, not only white space.
    if not 1 <= len(ENTRY) <= 120 or not ENTRY.strip():
        raise ValueError(
            f"entry must be 1-120 non-blank characters, got {len(ENTRY)}"
        )
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
