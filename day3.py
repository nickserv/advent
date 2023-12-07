import re
from pathlib import Path
from typing import Self


class Part:
    def __init__(self, number: int, line: int, start: int, end: int):
        self.number = number
        self.line = line
        self.start = start
        self.end = end

    @staticmethod
    def parse(string: str):
        divisor = string.index("\n") + 1
        return [
            Part(
                int(match.group()),
                match.start() // divisor,
                match.start() % divisor,
                match.end() % divisor,
            )
            for match in re.finditer("\\d+", string)
        ]

    def __repr__(self):
        return f"{self.line}:{self.start}-{self.end}={self.number}"


class Symbol:
    def __init__(
        self,
        value: str,
        line: int,
        character: int,
    ):
        self.value = value
        self.line = line
        self.character = character

    def __repr__(self):
        return f"{self.line}:{self.character}={self.value}"

    def adjacent(self: Self, part: Part):
        return (
            abs(self.line - part.line) <= 1
            and part.start - 2 < self.character <= part.end
        )

    def ratio(self, parts: list[Part]):
        neighbors = [part for part in parts if self.adjacent(part)]
        return neighbors[0].number * neighbors[1].number if len(neighbors) == 2 else 0

    @staticmethod
    def parse(string: str):
        return [
            Symbol(character, line_index, character_index)
            for line_index, line in enumerate(string.splitlines())
            for character_index, character in enumerate(line)
            if not character.isdigit() and character != "."
        ]


def sum_adjacent(parts: list[Part], symbols: list[Symbol]):
    return sum(
        part.number
        for part in parts
        if any(symbol.adjacent(part) for symbol in symbols)
    )


def sum_ratios(parts: list[Part], symbols: list[Symbol]):
    return sum(symbol.ratio(parts) for symbol in symbols if symbol.value == "*")


if __name__ == "__main__":
    string = Path("resources/3.txt").read_text("utf8")
    parts = Part.parse(string)
    symbols = Symbol.parse(string)
    print(sum_adjacent(parts, symbols))
    print(sum_ratios(parts, symbols))
