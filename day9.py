from functools import reduce
from itertools import pairwise


def parse(string: str):
    return [int(char) for char in string.split()]


def diffs(history: list[int]):
    diffs = [history]
    while any(diffs[-1]):
        diffs.append([next - previous for previous, next in pairwise(diffs[-1])])
    return diffs


def extrapolate(history: list[int], reverse: bool = False):
    return reduce(
        lambda total, diff: diff[0] - total if reverse else diff[-1] + total,
        reversed(diffs(history)),
        0,
    )


def extrapolate_all(histories: list[list[int]], reverse: bool = False):
    return sum(extrapolate(history, reverse) for history in histories)


if __name__ == "__main__":
    with open("resources/9.txt", encoding="utf8") as file:
        histories = [parse(line) for line in file.readlines()]
    for reverse in False, True:
        print(extrapolate_all(histories, reverse))
