from itertools import product
from pathlib import Path


def parse_grid(string: str):
    return [list(line) for line in string.splitlines()]


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
XMAS = ["X", "M", "A", "S"]


def search_xmas(grid: list[list[str]]):
    size = len(grid)

    return sum(
        # Check bounds
        0 <= x + 3 * dx < size and 0 <= y + 3 * dy < size
        # Check word match
        and [grid[x + i * dx][y + i * dy] for i in range(4)] == XMAS
        for dx, dy in DIRECTIONS
        for x, y in product(range(size), repeat=2)
    )


def search_x_mas(grid: list[list[str]]):
    raise NotImplementedError()


if __name__ == "__main__":
    grid = parse_grid(Path("resources/4.txt").read_text("utf8"))
    print(search_xmas(grid))
    # print(search_x_mas(grid))
