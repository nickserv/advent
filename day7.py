from itertools import chain
from math import floor, log10
from operator import add, mul
from typing import Callable, Generator

from utils import get_input

type Equation = tuple[int, list[int]]


def parse_equation(string: str) -> Equation:
    test, _, numbers = string.partition(": ")
    return int(test), [int(number) for number in numbers.split(" ")]


def parse_equations(string: str):
    return [parse_equation(line) for line in string.splitlines()]


type BinaryOperation = Callable[[int, int], int]


def results(numbers: list[int], *operations: BinaryOperation) -> Generator[int]:
    *initial, last = numbers
    if initial:
        yield from chain(
            operation(result, last)
            for result in results(initial, *operations)
            for operation in operations
        )
    else:
        yield last


def total(equations: list[Equation], *operations: BinaryOperation):
    return sum(
        test for test, numbers in equations if test in results(numbers, *operations)
    )


def concat(x: int, y: int):
    order: int = 10 ** (floor(log10(y)) + 1)
    return x * order + y


if __name__ == "__main__":
    equations = parse_equations(get_input(7))
    print(total(equations, add, mul))
    print(total(equations, add, mul, concat))
