"""One Line, One Chill — make.fun entry.

Writes one original single-sentence horror line to /output/entry.txt.
Deterministic: the same text on every run. No network, no input files,
no secrets, nothing read from outside this repository.
"""

import os

LINE = (
    "The dentist found a second set of teeth growing behind mine, "
    "and when I asked what they were chewing, he said, \"You.\""
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
