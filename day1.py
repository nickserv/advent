from collections import Counter
from pathlib import Path


def parse_lists(string: str) -> tuple[list[int], list[int]]:
    return tuple(zip(*(map(int, line.split()) for line in string.splitlines())))


def total_distance(left: list[int], right: list[int]):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def similarity_score(left: list[int], right: list[int]):
    counter = Counter(right)
    return sum(number * counter[number] for number in left)


if __name__ == "__main__":
    lists = parse_lists(Path("resources/1.txt").read_text("utf8"))
    print(total_distance(*lists))
    print(similarity_score(*lists))
