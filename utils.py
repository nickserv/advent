# pylint: enable=missing-class-docstring,missing-function-docstring
from dataclasses import dataclass
from itertools import batched, product
from math import sqrt
from pathlib import Path
from textwrap import dedent
from typing import Iterable, Self


@dataclass(unsafe_hash=True)
class Point:
    """A point in a Grid or other 2D collection"""

    x: int
    y: int

    def __add__(self, other: Self):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int):
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other: int):
        return self * other


STRAIGHTS = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]
DIAGONALS = [Point(1, 1), Point(-1, 1), Point(1, -1), Point(-1, -1)]
DIRECTIONS = STRAIGHTS + DIAGONALS


class Grid[T]:
    """
    A square grid of items internally flattened as a list, with utilities for Point-
    based operations
    """

    _items: list[T]

    def __init__(self, items: Iterable[T]):
        self._items = list(items)

    def __eq__(self, other: object):
        if isinstance(other, Grid):
            return self._items == other._items  # type: ignore
        return False

    def __getitem__(self, point_or_index: Point | int):
        match point_or_index:
            case Point(x, y):
                return self._items[len(self) * y + x]
            case int(index):
                return self._items[index]

    def __len__(self):
        return int(sqrt(len(self._items)))

    def __str__(self):
        return self.visualize(set())

    def point(self, index: int):
        """Convert the index to a Point in Grid"""
        return Point(index % len(self), index // len(self))

    def points(self):
        """Get all valid Points in Grid in order"""
        return (Point(x, y) for y, x in product(range(len(self)), repeat=2))

    def valid(self, point: Point):
        """Check if a Point is in Grid"""
        return 0 <= point.x < len(self) and 0 <= point.y < len(self)

    def visualize(self, path: set[Point]):
        """Get a string representation, but with X replacing Points in the given path"""
        return "\n".join(
            "".join("X" if point in path else str(self[point]) for point in row)
            for row in batched(self.points(), len(self))
        )


class StringGrid(Grid[str]):
    """A Grid of characters from an ASCII art string"""

    def __init__(self, string: str):
        super().__init__(char for char in string if char != "\n")


def get_input(day_or_string: int | str):
    """Read an input from a file or inline string without extra whitespace"""
    match day_or_string:
        case int(day):
            return Path(f"resources/{day}.txt").read_text("utf8")
        case str(string):
            return dedent(string).strip()
