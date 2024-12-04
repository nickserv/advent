from itertools import product
from pathlib import Path

import numpy as np


def parse_grid(string: str):
    return [list(line) for line in string.splitlines()]


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
XMAS = np.array(list("XMAS"))


def search_xmas(grid: list[list[str]]):
    matrix = np.array(grid)
    size = matrix.shape[0]

    return sum(
        # Check bounds
        0 <= x + 3 * dx < size and 0 <= y + 3 * dy < size
        # Check word match
        and np.array_equal(matrix[x + np.arange(4) * dx, y + np.arange(4) * dy], XMAS)
        for dx, dy in DIRECTIONS
        for x, y in product(range(size), repeat=2)
    )


def search_x_mas(grid: list[list[str]]):
    raise NotImplementedError()


if __name__ == "__main__":
    grid = parse_grid(Path("resources/4.txt").read_text("utf8"))
    print(search_xmas(grid))
    # print(search_x_mas(grid))
