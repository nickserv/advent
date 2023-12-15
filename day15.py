from functools import reduce
from pathlib import Path


def custom_hash(string: str) -> int:
    substrings = string.split(",")
    if len(substrings) == 1:
        return reduce(lambda current, char: (current + ord(char)) * 17 % 256, string, 0)
    return sum(custom_hash(substring) for substring in substrings)


if __name__ == "__main__":
    print(custom_hash(Path("resources/15.txt").read_text("utf8").rstrip()))
