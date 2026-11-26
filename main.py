"""One Line to Your Younger Self entry.

Writes a single line, in English, that the writer would send back to
their younger self to /output/entry.txt. The text must be plain ASCII,
one line, 1-200 characters.

Draft v1: a direct address ("Kid") with a concrete, lived detail -- the
nose hated in every photo -- and a turn: one day the older self sees
their grandfather in it, and keeps it. Specific, warm, stings a little.

Revision v3 (final): "every photo" -> "every school photo". The school
photo is a sharper lived detail -- picture day is a specific ritual
everyone remembers -- so the memory reads as one person's, not anyone's,
and the grandfather reveal lands against a concrete image. Costs 7
chars, still far under the 200 cap.
"""

LINE = "At fourteen you'll hate your nose in every school photo; at forty you'll see your grandfather in it, and you'll keep it."


def main():
    text = LINE.strip()
    # Gate self-check: mirror the sealed scorer (1-200 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
