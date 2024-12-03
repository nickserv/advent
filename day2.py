from pathlib import Path
from typing import Callable


def parse_lists(string: str):
    return [[int(x) for x in line.split()] for line in string.strip().split("\n")]


def safe(list2: list[int]):
    direction = list2[1] > list2[0]
    zipped = list(zip(list2, list2[1:]))
    return all(x < y if direction else x > y for x, y in zipped) and all(
        x != y and abs(x - y) <= 3 for x, y in zipped
    )


def safe_tolerant(list2: list[int]):
    return any(safe(list2[:index] + list2[index + 1 :]) for index in range(len(list2)))


def count(lists2: list[list[int]], safe_func: Callable[[list[int]], bool] = safe):
    return sum(safe_func(list2) for list2 in lists2)


if __name__ == "__main__":
    lists = parse_lists(Path("resources/2.txt").read_text("utf8"))
    print(count(lists))
    print(count(lists, safe_tolerant))
