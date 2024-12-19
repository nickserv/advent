from collections import Counter

from utils import get_input, parse_lines


def parse_lists(string: str) -> tuple[list[int], list[int]]:
    return tuple(zip(*parse_lines(lambda line: (int(c) for c in line.split()), string)))


def total_distance(left: list[int], right: list[int]):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def similarity_score(left: list[int], right: list[int]):
    counter = Counter(right)
    return sum(number * counter[number] for number in left)


if __name__ == "__main__":
    lists = parse_lists(get_input(1))
    print(total_distance(*lists))
    print(similarity_score(*lists))
