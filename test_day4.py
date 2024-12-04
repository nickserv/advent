import unittest

from day4 import parse_grid, search_x_mas, search_xmas

GRID = parse_grid(
    """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
    """.strip()
)


class TestDay3(unittest.TestCase):
    def test_search_xmas(self):
        self.assertEqual(search_xmas(GRID), 18)

    @unittest.expectedFailure
    def test_search_x_mas(self):
        self.assertEqual(search_x_mas(GRID), 9)
