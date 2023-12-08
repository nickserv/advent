from functools import reduce
from operator import mul
from typing import Iterator, Sequence


def parse_race(lines: Sequence[str]):
    return (int("".join(x for x in line if x.isdigit())) for line in lines)


def parse_races(lines: Sequence[str]) -> Iterator[tuple[int, int]]:
    return zip(*((int(x) for x in line.partition(": ")[2].split()) for line in lines))


def displacement(duration: int, time: int):
    return duration * (time - duration)


def solutions(time: int, distance: int):
    return sum(displacement(duration, time) > distance for duration in range(1, time))


def product_solutions(races: Iterator[tuple[int, int]]) -> int:
    return reduce(mul, (solutions(*race) for race in races))


if __name__ == "__main__":
    with open("resources/6.txt", encoding="utf8") as file:
        lines = file.readlines()
    print(product_solutions(parse_races(lines)))
    print(solutions(*parse_race(lines)))
