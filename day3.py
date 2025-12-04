from functools import reduce
from itertools import combinations
from collections.abc import Iterable
from utils import get_input
from utils import parse_lines


def parse_bank(string: str):
    return list(map(int, string))


def digits_to_int(digits: Iterable[int]):
    return reduce(lambda x, y: x * 10 + y, digits)


def joltage(bank: Iterable[int], r: int):
    return max(map(digits_to_int, combinations(bank, r)))


def total_joltage(banks: Iterable[Iterable[int]], r: int):
    return sum(joltage(bank, r) for bank in banks)


if __name__ == "__main__":
    banks = parse_lines(parse_bank, get_input(3))
    print(total_joltage(banks, 2))
    print(total_joltage(banks, 12))
