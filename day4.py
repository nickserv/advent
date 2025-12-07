from collections.abc import Generator

from utils import Grid, Point, read_input


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
                and sum(
                    self[neighbor] for neighbor in self.neighbors(point, diagonal=True)
                )
                < 4
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
    grid = PaperGrid(read_input(4))
    print(len(list(grid.accessible())))
    print(len(list(grid.removable())))
