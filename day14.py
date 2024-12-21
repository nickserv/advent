import operator
import re
from dataclasses import dataclass
from functools import reduce

from PIL import Image

from utils import Point, get_input, parse_lines


@dataclass
class ClampedPoint(Point):
    clamp: Point

    @staticmethod
    def parse_clamped(string: str, clamp: Point):
        point = Point.parse(string)
        return ClampedPoint(point.x, point.y, clamp)

    def __add__(self, other: Point):
        other = self.__class__(other.x, other.y, self.clamp)
        point = super().__add__(other) % self.clamp
        return ClampedPoint(point.x, point.y, self.clamp)

    def __mul__(self, other: int):
        point = super().__mul__(other) % self.clamp
        return ClampedPoint(point.x, point.y, self.clamp)


class Robot:  # pylint:disable=too-few-public-methods
    position: ClampedPoint

    def __init__(self, string: str, clamp: Point):
        match = re.fullmatch(r"p=(\d+,\d+) v=(-?\d+,-?\d+)", string)
        if not match:
            raise ValueError(repr(string))
        self.position = ClampedPoint.parse_clamped(match[1], clamp)
        self.__velocity = Point.parse(match[2])

    def move(self):
        self.position += self.__velocity


class Space:
    def __init__(self, string: str, clamp: Point):
        self.robots = tuple(parse_lines(lambda line: Robot(line, clamp), string))
        self.clamp = clamp

    def __str__(self):
        grid = [["." for _ in range(self.clamp.x)] for _ in range(self.clamp.y)]
        for robot in self.robots:
            grid[robot.position.y][robot.position.x] = "#"
        return "\n".join("".join(row) for row in grid)

    def image(self):
        grid = [[False for _ in range(self.clamp.x)] for _ in range(self.clamp.y)]
        for robot in self.robots:
            grid[robot.position.y][robot.position.x] = True
        data = [255 if item else 0 for row in grid for item in row]
        image = Image.new("L", (self.clamp.x, self.clamp.y))
        image.putdata(data)  # type:ignore
        return image

    def move(self, times: int = 1):
        for _ in range(times):
            for robot in self.robots:
                robot.move()

    def safety(self) -> int:
        counts = [0, 0, 0, 0]
        for robot in self.robots:
            if robot.position.x > self.clamp.x // 2:
                if robot.position.y > self.clamp.y // 2:
                    counts[0] += 1
                elif robot.position.y < self.clamp.y // 2:
                    counts[3] += 1
            elif robot.position.x < self.clamp.x // 2:
                if robot.position.y > self.clamp.y // 2:
                    counts[1] += 1
                elif robot.position.y < self.clamp.y // 2:
                    counts[2] += 1
        return reduce(operator.mul, counts)


if __name__ == "__main__":
    space = Space(get_input(14), Point(101, 103))
    space.move(100)
    print(space.safety())

    space = Space(get_input(14), Point(101, 103))
    for i in range(1, 10_000):  # The answer is below 10,000
        space.move()
        space.image().save(f"output/{i}.png")
