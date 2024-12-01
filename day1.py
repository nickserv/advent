from collections import Counter
from pathlib import Path


def parse_lists(string: str) -> tuple[list[int], list[int]]:
    left, right = zip(*(map(int, line.split()) for line in string.splitlines()))
    return (left, right)


def total_distance(left: list[int], right: list[int]):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def similarity_score(left: list[int], right: list[int]):
    counter = Counter(right)
    return sum(number * counter[number] for number in left)


if __name__ == "__main__":
    left, right = parse_lists(Path("resources/1.txt").read_text("utf8"))
    print(total_distance(left, right))
    print(similarity_score(left, right))
