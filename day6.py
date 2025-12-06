from functools import reduce
from operator import add, mul

from day5 import read_input
from utils import Callable, parse_lines

type Operator = Callable[[int, int], int]
type Worksheet = list[tuple[Operator, tuple[int, ...]]]


def solve_worksheet(worksheet: Worksheet):
    return sum(reduce(operator, numbers) for operator, numbers in worksheet)


def parse_operator(operator: str) -> Operator:
    match operator:
        case "+":
            return add
        case "*":
            return mul
        case _:
            raise ValueError(f"Unsupported operator: {operator!r}")


def parse_worksheet(string: str) -> Worksheet:
    *numbers, operators = parse_lines(lambda line: line.split(), string)
    return list(
        zip(
            map(parse_operator, operators),
            zip(*((int(number) for number in row) for row in numbers)),
        )
    )


if __name__ == "__main__":
    worksheet = parse_worksheet(read_input(6))
    print(solve_worksheet(worksheet))
