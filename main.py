"""Laugh Track: The Crypto Trading Joke Contest.

Writes one crypto-trading joke to /output/entry.txt.

The joke: a trading bot with perfect anti-timing — it buys the top and
sells the bottom — then, instead of apologising, charges a 20% performance
fee for the experience and emails itself a five-star review. One concrete
mechanism (buy-top/sell-bottom bot), one concrete consequence (the fee on
top of the loss), and an escalating twist (the bot reviewing itself).
"""

import os

JOKE = (
    "My trading bot bought the top, sold the bottom, then charged me "
    "a 20% performance fee for the experience \u2014 and emailed me "
    "a five-star review of itself."
)


def _validate(text: str) -> str:
    """Enforce the gate: UTF-8 text, 1-200 chars, not only whitespace.

    The judge only ever sees what lands in /output/entry.txt, so the
    program re-reads the file after writing it and checks the exact bytes
    it wrote, not just the string in memory. A joke that is too long, empty,
    or whitespace-only fails loudly here instead of silently shipping an
    invalid entry to the gate.
    """
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry must be at most 200 chars, got {len(text)}")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def main() -> None:
    text = _validate(JOKE.strip())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the artifact on disk matches the validated joke exactly.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the joke"
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
