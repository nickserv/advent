import operator
import re
from functools import reduce
from typing import Self

from PIL import Image

from utils import get_input


class Point:
    x: int
    y: int
    clamp_x: int
    clamp_y: int

    def __init__(self, x: int, y: int, clamp_x: int, clamp_y: int):
        self.x = x
        self.y = y
        self.clamp_x = clamp_x
        self.clamp_y = clamp_y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __iadd__(self, other: Self):
        self.x = (self.x + other.x) % self.clamp_x
        self.y = (self.y + other.y) % self.clamp_y
        return self

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.clamp_x}, {self.clamp_y})"


class Robot:  # pylint: disable=too-few-public-methods
    position: Point
    velocity: Point

    def __init__(self, string: str, clamp_x: int, clamp_y: int):
        match = re.fullmatch(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", string)
        if not match:
            raise ValueError(f"Invalid Robot string: {string}")
        self.position = Point(int(match[1]), int(match[2]), clamp_x, clamp_y)
        self.__velocity = Point(int(match[3]), int(match[4]), clamp_x, clamp_y)

    def move(self):
        self.position += self.__velocity


class Space:
    def __init__(self, string: str, clamp_x: int, clamp_y: int):
        self.robots = tuple(
            Robot(line, clamp_x, clamp_y) for line in string.splitlines()
        )
        self.clamp_x = clamp_x
        self.clamp_y: int = clamp_y

    def __str__(self):
        grid = [["." for _ in range(self.clamp_x)] for _ in range(self.clamp_y)]
        for robot in self.robots:
            grid[robot.position.y][robot.position.x] = "#"
        return "\n".join("".join(row) for row in grid)

    def image(self):
        grid = [[False for _ in range(self.clamp_x)] for _ in range(self.clamp_y)]
        for robot in self.robots:
            grid[robot.position.y][robot.position.x] = True
        data = [255 if item else 0 for row in grid for item in row]
        image = Image.new("L", (self.clamp_x, self.clamp_y))
        image.putdata(data)  # type: ignore
        return image

    def move(self, times: int = 1):
        for _ in range(times):
            for robot in self.robots:
                robot.move()

    def safety(self) -> int:
        counts = [0, 0, 0, 0]
        for robot in self.robots:
            if robot.position.x > self.clamp_x // 2:
                if robot.position.y > self.clamp_y // 2:
                    counts[0] += 1
                elif robot.position.y < self.clamp_y // 2:
                    counts[3] += 1
            elif robot.position.x < self.clamp_x // 2:
                if robot.position.y > self.clamp_y // 2:
                    counts[1] += 1
                elif robot.position.y < self.clamp_y // 2:
                    counts[2] += 1
        return reduce(operator.mul, counts)


if __name__ == "__main__":
    space = Space(get_input(14), 101, 103)
    space.move(100)
    print(space.safety())

    space = Space(get_input(14), 101, 103)
    for i in range(1, 10_000):  # The answer is below 10,000
        space.move()
        space.image().save(f"output/{i}.png")
