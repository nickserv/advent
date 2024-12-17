from itertools import pairwise
from typing import Callable

from utils import get_input


def parse_lists(string: str):
    return [[int(x) for x in line.split()] for line in string.splitlines()]


def safe(list2: list[int]):
    direction = list2[1] > list2[0]
    return all(x < y if direction else x > y for x, y in pairwise(list2)) and all(
        x != y and abs(x - y) <= 3 for x, y in pairwise(list2)
    )


def safe_tolerant(list2: list[int]):
    return any(safe(list2[:index] + list2[index + 1 :]) for index in range(len(list2)))


def count(lists2: list[list[int]], safe_func: Callable[[list[int]], bool] = safe):
    return sum(safe_func(list2) for list2 in lists2)


if __name__ == "__main__":
    lists = parse_lists(get_input(2))
    print(count(lists))
    print(count(lists, safe_tolerant))
