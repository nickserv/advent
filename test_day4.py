import unittest

from day4 import search_x_mas, search_xmas
from utils import get_input

GRID = get_input(
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
    """
)


class TestDay4(unittest.TestCase):
    def test_search_xmas(self):
        self.assertEqual(search_xmas(GRID), 18)

    @unittest.expectedFailure
    def test_search_x_mas(self):
        self.assertEqual(search_x_mas(GRID), 9)
