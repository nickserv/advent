from collections.abc import Generator, Iterable
from dataclasses import dataclass
from itertools import batched, product
from math import sqrt
from typing import Self, overload

from utils import get_input, parse_lines


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
        return parse_lines(Point.parse, string)

    def __add__(self, other: Self):
        return Point(self.x + other.x, self.y + other.y)

    def __mod__(self, other: Self):
        return Point(self.x % other.x, self.y % other.y)

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
    A grid of items internally flattened as a list, with utilities for Point-based
    operations
    """

    _items: list[T]
    _width: int

    @staticmethod
    def format_value(value: T):
        """Converts a contained value to a string (preferably a single character)"""
        return str(value)

    def __init__(self, items: Iterable[T]):
        self._items = list(items)
        self._width = int(sqrt(len(self._items)))

    def index(self, point: Point) -> int:
        "Convert the Point to an index in Grid's internal list"
        return self._width * point.y + point.x

    def point(self, index: int):
        """Convert the index to a Point in Grid"""
        return Point(index % self._width, index // self._width)

    @overload
    def neighbors(self, key: Point) -> Generator[Point]: ...
    @overload
    def neighbors(self, key: int) -> Generator[int]: ...

    def neighbors(self, key: Point | int) -> Generator[Point | int]:
        """Get all valid neighbors of a Point or index in Grid"""
        match key:
            case Point():
                for direction in DIRECTIONS:
                    if key + direction in self:
                        yield key + direction
            case int():
                for point in self.neighbors(self.point(key)):
                    yield self.index(point)

    def visualize(self, path: set[Point]):
        """Get a string representation, but with X replacing Points in the given path"""
        return "\n".join(
            "".join(
                "X" if point in path else self.format_value(self[point])
                for point in row
            )
            for row in batched(self, self._width)
        )

    def __contains__(self, key: Point | int):
        match key:
            case Point(x, y):
                return 0 <= x < self._width and 0 <= y < len(self._items) // self._width
            case index:
                return 0 <= index < len(self._items)

    def __eq__(self, other: object):
        if isinstance(other, Grid):
            return self._items == other._items  # type:ignore[reportUnknownMemberType]
        return False

    def __getitem__(self, key: Point | int):
        match key:
            case Point():
                return self._items[self.index(key)]
            case int() as index:
                return self._items[index]

    def __setitem__(self, key: Point | int, value: T):
        match key:
            case Point():
                self._items[self.index(key)] = value
            case int() as index:
                self._items[index] = value

    def __iter__(self):
        return (
            Point(x, y)
            for y, x in product(
                range(len(self._items) // self._width), range(self._width)
            )
        )

    def __len__(self):
        return self._width

    def __str__(self):
        return self.visualize(set())


class PaperGrid(Grid[bool]):
    @staticmethod
    def format_value(value: bool):
        return "@" if value else "."

    def __init__(self, string: str):
        super().__init__(char == "@" for char in string if char != "\n")

    def accessible(self) -> Generator[Point]:
        for point in self:
            if (
                self[point]
                and sum(self[neighbor] for neighbor in self.neighbors(point)) < 4
            ):
                yield point

    def removable(self) -> Generator[Point]:
        accessible = list(self.accessible())
        if accessible:
            for point in accessible:
                self[point] = False
                yield point
            yield from self.removable()


if __name__ == "__main__":
    grid = PaperGrid(get_input(4))
    print(len(list(grid.accessible())))
    print(len(list(grid.removable())))
