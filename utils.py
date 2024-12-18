# pylint: enable=missing-class-docstring,missing-function-docstring
from dataclasses import dataclass
from itertools import batched, product
from math import sqrt
from pathlib import Path
from textwrap import dedent
from typing import Generator, Iterable, Self, overload


@dataclass(unsafe_hash=True)
class Point:
    """A point in a Grid or other 2D collection"""

    x: int
    y: int

    @staticmethod
    def parse(string: str):
        """Parses a string of "x,y" into a Point"""
        x, _, y = string.partition(",")
        return Point(int(x), int(y))

    @staticmethod
    def parse_many(string: str):
        """Parses a string of "x,y" lines into a list of Points"""
        return [Point.parse(line) for line in string.splitlines()]

    def __add__(self, other: Self):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int):
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other: int):
        return self * other

    def __str__(self):
        return f"{self.x},{self.y}"


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

    def index(self, point: Point) -> int:
        "Convert the Point to an index in Grid's internal list"
        return len(self) * point.y + point.x

    def point(self, index: int):
        """Convert the index to a Point in Grid"""
        return Point(index % len(self), index // len(self))

    def points(self):
        """Get all valid Points in Grid in order"""
        return (Point(x, y) for y, x in product(range(len(self)), repeat=2))

    @overload
    def neighbors(self, key: Point) -> Generator[Point]: ...
    @overload
    def neighbors(self, key: int) -> Generator[int]: ...

    def neighbors(self, key: Point | int) -> Generator[Point | int]:
        """Get all valid neighbors of a Point or index in Grid"""
        match key:
            case Point():
                for direction in STRAIGHTS:
                    if self.valid(key + direction):
                        yield key + direction
            case int():
                for point in self.neighbors(self.point(key)):
                    yield self.index(point)

    def valid(self, point: Point):
        """Check if a Point is in Grid"""
        return 0 <= point.x < len(self) and 0 <= point.y < len(self)

    def visualize(self, path: set[Point]):
        """Get a string representation, but with X replacing Points in the given path"""
        return "\n".join(
            "".join("X" if point in path else str(self[point]) for point in row)
            for row in batched(self.points(), len(self))
        )

    def __eq__(self, other: object):
        if isinstance(other, Grid):
            return self._items == other._items  # type: ignore
        return False

    def __getitem__(self, key: Point | int):
        match key:
            case Point():
                return self._items[self.index(key)]
            case int(index):
                return self._items[index]

    def __setitem__(self, key: Point | int, value: T):
        match key:
            case Point():
                self._items[self.index(key)] = value
            case int(index):
                self._items[index] = value

    def __len__(self):
        return int(sqrt(len(self._items)))

    def __str__(self):
        return self.visualize(set())


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
