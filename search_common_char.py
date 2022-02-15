import operator
from typing import Counter


def count_chars(strings: str) -> tuple[str, int]:
    l: list[tuple[str, int]] = [
        (char, strings.count(char)) for char in chars.lower() if not char.isspace()
    ]
    return max(l, key=operator.itemgetter(1))


def count_chars_v2(strings: str) -> tuple[str, int]:
    strings = strings.lower()
    d: dict[str, int] = Counter()
    for char in strings:
        if not char.isspace():
            d[char] += 1
    max_key: str = max(d, key=d.get)
    return max_key, d[max_key]


if __name__ == "__main__":
    chars = "This is a pen. This is an apple. Applepen"
    print(count_chars_v2(chars))
