from dataclasses import dataclass
from pathlib import Path


@dataclass
class Entry:
    destination_range_start: int
    source_range_start: int
    range_length: int


def parse(string: str):
    return (
        [int(number) for number in string.partition("\n")[0][7:].split()],
        [
            [
                Entry(*(int(number) for number in line.split()))
                for line in section.splitlines()[1:]
            ]
            for section in string.split("\n\n")[1:]
        ],
    )


def lookup(map: list[Entry], seed: int):
    return seed


def lookup_many(maps: list[list[Entry]], seed: int):
    return seed


if __name__ == "__main__":
    seeds, maps = parse(Path("resources/5.txt").read_text("utf8"))
    print(min(lookup_many(maps, seed) for seed in seeds))
