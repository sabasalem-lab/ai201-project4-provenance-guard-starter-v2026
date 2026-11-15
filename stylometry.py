"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────
def sentence_length_spread(text: str) -> float:
    """
    Coefficient of variation of sentence length (stdev / mean word count).
    Higher = lumpier = more human-ish. 0.0 for fewer than two sentences,
    since one sentence has no spread to measure.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = sum(lengths) / len(lengths)
    if mean == 0:
        return 0.0
    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    """Unique words / total words. Higher = more varied vocabulary = more human-ish."""
    w = words(text)
    if not w:
        return 0.0
    return len(set(w)) / len(w)


def punctuation_density(text: str) -> float:
    """
    Varied punctuation (commas, semicolons, colons, dashes, question and
    exclamation marks, parentheses) per word. Full stops excluded — every
    writer uses those. Higher = more varied punctuation = more human-ish.
    """
    w = words(text)
    if not w:
        return 0.0
    marks = len(re.findall(r"[,;:—\-?!()]", text))
    return marks / len(w)


def style_signal(text: str) -> float:
    """
    0–1, higher = more likely AI, same direction as detector.model_signal.

    All three measures point human-ish when high, so each is scaled to 0–1
    and flipped (1 - x). Equal thirds — no measure dominates by scale.

    Scaling caps, from eyeballing real text: spread rarely exceeds ~0.8,
    punctuation density rarely exceeds ~0.3. TTR is already 0–1.
    """
    spread_h = min(sentence_length_spread(text) / 0.8, 1.0)
    ttr_h = type_token_ratio(text)
    punct_h = min(punctuation_density(text) / 0.3, 1.0)
    human_ish = (spread_h + ttr_h + punct_h) / 3
    return round(1.0 - human_ish, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
