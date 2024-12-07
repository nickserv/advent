from itertools import chain
from math import floor, log10
from operator import add, mul
from pathlib import Path
from typing import Callable, Iterable


def parse_equation(string: str):
    test, _, numbers = string.partition(": ")
    return int(test), [int(number) for number in numbers.split(" ")]


def parse_equations(string: str):
    return [parse_equation(line) for line in string.splitlines()]


type BinaryOperation = Callable[[int, int], int]


def results(numbers: list[int], *operations: BinaryOperation) -> Iterable[int]:
    *initial, last = numbers
    return (
        chain(
            operation(result, last)
            for result in results(initial, *operations)
            for operation in operations
        )
        if initial
        else (last,)
    )


def total(equations: list[tuple[int, list[int]]], *operations: BinaryOperation):
    return sum(
        test for test, numbers in equations if test in results(numbers, *operations)
    )


def concat(x: int, y: int):
    order: int = 10 ** (floor(log10(y)) + 1)
    return x * order + y


if __name__ == "__main__":
    equations = parse_equations(Path("resources/7.txt").read_text())
    print(total(equations, add, mul))
    print(total(equations, add, mul, concat))
