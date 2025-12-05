import unittest

from day4 import PaperGrid
from utils import get_input

GRID = PaperGrid(
    get_input(
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
