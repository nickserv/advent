import unittest

from day4 import PaperGrid
from utils import clean_string

GRID = PaperGrid(
    clean_string(
        """
        ..@@.@@@@.
        @@@.@.@.@@
        @@@@@.@.@@
        @.@@@@..@.
        @@.@@@@.@@
        .@@@@@@@.@
        .@.@.@.@@@
        @.@@@.@@@@
        .@@@@@@@@.
        @.@.@@@.@.
        """
    )
)


class TestPaperGrid(unittest.TestCase):
    def test_accessible(self):
        self.assertEqual(len(list(GRID.accessible())), 13)

    def test_removable(self):
        self.assertEqual(len(list(GRID.removable())), 43)
