from itertools import combinations
from pathlib import Path
from typing import Self


class Galaxy:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other: object):
        if not isinstance(other, Galaxy):
            return NotImplemented
        return self.row == other.row and self.col == other.col

    def __repr__(self):
        return f"Galaxy({self.row}, {self.col})"

    def __sub__(self, other: Self):
        return abs(self.row - other.row) + abs(self.col - other.col)


def parse(string: str):
    return [
        Galaxy(*divmod(index, string.index("\n") + 1))
        for index, char in enumerate(string)
        if char == "#"
    ]


def expand(galaxies: list[Galaxy], size: int = 2):
    rows = {galaxy.row for galaxy in galaxies}
    empty_rows = {row for row in range(max(rows)) if not row in rows}
    cols = {galaxy.col for galaxy in galaxies}
    empty_cols = {col for col in range(max(cols)) if not col in cols}
    return [
        Galaxy(
            galaxy.row + (size - 1) * sum(1 for row in empty_rows if galaxy.row > row),
            galaxy.col + (size - 1) * sum(1 for row in empty_cols if galaxy.col > row),
        )
        for galaxy in galaxies
    ]


def sum_diffs(galaxies: list[Galaxy]):
    return sum(x - y for x, y in combinations(galaxies, 2))


if __name__ == "__main__":
    galaxies = parse(Path("resources/11.txt").read_text("utf8"))
    print(sum_diffs(expand(galaxies)))
    print(sum_diffs(expand(galaxies, 1000000)))
