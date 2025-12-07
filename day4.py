from collections.abc import Generator

from utils import DIRECTIONS, Grid, Point, overload, read_input


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

    def removable(self) -> Generator[Point]:
        accessible = list(self.accessible())
        if accessible:
            for point in accessible:
                self[point] = False
                yield point
            yield from self.removable()


if __name__ == "__main__":
    grid = PaperGrid(read_input(4))
    print(len(list(grid.accessible())))
    print(len(list(grid.removable())))
