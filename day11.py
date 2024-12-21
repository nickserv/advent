from collections.abc import Callable, Iterable
from functools import cache
from itertools import chain
from math import floor, log10

from utils import get_input


@cache
def change(stone: int) -> Iterable[int]:
    if stone == 0:
        return (1,)
    quotient, remainder = divmod(floor(log10(stone)) + 1, 2)
    if remainder == 0:
        return divmod(stone, 10**quotient)
    return (stone * 2024,)


def blink(stones: Iterable[int]):
    return chain.from_iterable(change(stone) for stone in stones)


def call_composed[T](func: Callable[[T], T], value: T, times: int):
    for _ in range(times):
        value = func(value)
    return value


if __name__ == "__main__":
    stones: list[int] = [int(x) for x in get_input(11).split(" ")]
    print(len(list(call_composed(blink, stones, 25))))
    # print(len(list(call_composed(blink, stones, 75))))
