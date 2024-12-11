from math import floor, log10
from typing import Callable, Iterable

from utils import get_input


def blink(stones: Iterable[int]) -> Iterable[int]:
    for stone in stones:
        if stone == 0:
            yield 1
        else:
            quotient, remainder = divmod(floor(log10(stone)) + 1, 2)
            if remainder == 0:
                yield from divmod(stone, 10**quotient)
            else:
                yield stone * 2024


def call_composed[T](func: Callable[[T], T], value: T, times: int):
    for _ in range(times):
        value = func(value)
    return value


if __name__ == "__main__":
    stones: list[int] = [int(x) for x in get_input(11).split(" ")]
    print(len(list(call_composed(blink, stones, 25))))
    # print(len(list(call_composed(blink, stones, 75))))
