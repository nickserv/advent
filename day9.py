from collections.abc import Iterable
from itertools import combinations, starmap

from utils import Point, parse_lines, read_input


def area(a: Point, b: Point):
    x, y = a - b + Point(1, 1)
    return abs(x * y)


def max_area(points: Iterable[Point]):
    return max(starmap(area, combinations(points, 2)))


if __name__ == "__main__":
    points = parse_lines(Point.parse, read_input(9))
    print(max_area(points))
