import unittest

from day4 import Point, WordSearch
from utils import get_input

WORD_SEARCH = WordSearch(
    get_input(
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
)


class TestDay4(unittest.TestCase):
    def test_search_xmas(self):
        self.assertCountEqual(
            list(WORD_SEARCH.search_xmas()),
            [
                Point(0, 4),
                Point(0, 5),
                Point(1, 9),
                Point(3, 9),
                Point(3, 9),
                Point(4, 0),
                Point(4, 1),
                Point(5, 0),
                Point(5, 9),
                Point(5, 9),
                Point(5, 9),
                Point(6, 4),
                Point(6, 4),
                Point(6, 5),
                Point(9, 3),
                Point(9, 3),
                Point(9, 9),
                Point(9, 9),
            ],
        )

    @unittest.expectedFailure
    def test_search_x_mas(self):
        self.assertCountEqual(
            list(WORD_SEARCH.search_x_mas()),
            [
                Point(2, 1),
                Point(2, 3),
                Point(2, 7),
                Point(4, 3),
                Point(4, 7),
                Point(6, 2),
                Point(6, 7),
                Point(7, 2),
                Point(8, 7),
            ],
        )
