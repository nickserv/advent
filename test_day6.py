import unittest

from day6 import Lab
from utils import Point, get_input

LAB = Lab(
    get_input(
        """
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
        """
    )
)


class TestDay6(unittest.TestCase):
    def test_lab_path(self):
        self.assertEqual(len(LAB.path()), 41)

    def test_lab_start(self):
        self.assertEqual(LAB.start(), Point(4, 6))
