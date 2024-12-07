from enum import Enum, auto
from pathlib import Path
from typing import NamedTuple, SupportsIndex


class Direction(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

    def next(self):
        directions = list(Direction)
        return directions[(directions.index(self) + 1) % len(directions)]


class Point(NamedTuple):
    x: int
    y: int

    def next(self, direction: Direction):
        match direction:
            case Direction.UP:
                return Point(self.x, self.y - 1)
            case Direction.RIGHT:
                return Point(self.x + 1, self.y)
            case Direction.DOWN:
                return Point(self.x, self.y + 1)
            case Direction.LEFT:
                return Point(self.x - 1, self.y)

    def valid(self, size: int):
        return 0 <= self.x < size and 0 <= self.y < size


class Lab(str):
    size: int

    def __new__(cls, string: str):
        obj = super().__new__(cls, string)
        obj.size = string.index("\n")
        return obj

    def __getitem__(self, index: Point | SupportsIndex | slice):
        if not isinstance(index, Point):
            return super().__getitem__(index)
        new_index = self.size * index.y + index.x + index.y
        return super().__getitem__(new_index)

    def path(self):
        direction = Direction.UP
        point = self.start()
        path = {point}

        while point.next(direction).valid(self.size):
            if self[point.next(direction)] == "#":
                direction = direction.next()
            point = point.next(direction)
            path.add(point)

        return path

    def point(self, index: int):
        index -= self.count("\n", 0, index)
        return Point(index % self.size, index // self.size)

    def start(self):
        return self.point(self.index("^"))

    def visualize(self, path: set[Point]):
        points = [[Point(x, y) for x in range(self.size)] for y in range(self.size)]
        return "\n".join(
            "".join("X" if point in path else self[point] for point in row)
            for row in points
        )


if __name__ == "__main__":
    lab = Lab(Path("resources/6.txt").read_text("utf8").strip())
    print(len(lab.path()))
