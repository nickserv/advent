from itertools import pairwise


def parse(string: str):
    return [int(char) for char in string.split()]


def diffs(history: list[int]):
    diffs = [history]
    while any(diffs[-1]):
        diffs.append([next - previous for previous, next in pairwise(diffs[-1])])
    return diffs


def extrapolate(history: list[int]):
    return sum(diff[-1] for diff in diffs(history))


def extrapolate_all(histories: list[list[int]]):
    return sum(map(extrapolate, histories))


if __name__ == "__main__":
    with open("resources/9.txt", encoding="utf8") as file:
        histories = [parse(line) for line in file.readlines()]
    print(extrapolate_all(histories))
