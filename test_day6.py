import unittest

from day6 import Direction, Lab, Point
from utils import get_input

ORIGIN = Point(0, 0)
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
    def test_direction_next(self):
        self.assertEqual(Direction.UP.next(), Direction.RIGHT)
        self.assertEqual(Direction.RIGHT.next(), Direction.DOWN)
        self.assertEqual(Direction.DOWN.next(), Direction.LEFT)
        self.assertEqual(Direction.LEFT.next(), Direction.UP)

    def test_point_next(self):
        self.assertEqual(ORIGIN.next(Direction.UP), Point(0, -1))
        self.assertEqual(ORIGIN.next(Direction.RIGHT), Point(1, 0))
        self.assertEqual(ORIGIN.next(Direction.DOWN), Point(0, 1))
        self.assertEqual(ORIGIN.next(Direction.LEFT), Point(-1, 0))

    def test_point_valid(self):
        self.assertTrue(Point(0, 0).valid(2))
        self.assertTrue(Point(1, 1).valid(2))
        self.assertFalse(Point(-1, 0).valid(2))
        self.assertFalse(Point(0, -1).valid(2))
        self.assertFalse(Point(2, 0).valid(2))
        self.assertFalse(Point(0, 2).valid(2))

    def test_lab_new(self):
        self.assertIsInstance(LAB, str)
        self.assertEqual(LAB.size, 10)

    def test_lab_getitem(self):
        self.assertEqual(LAB[0], ".")
        self.assertEqual(LAB[Point(0, 0)], ".")
        self.assertEqual(LAB[Point(4, 6)], "^")
        self.assertEqual(LAB[Point(2, 3)], "#")

    def test_lab_path(self):
        self.assertEqual(len(LAB.path()), 41)

    def test_lab_point(self):
        self.assertEqual(LAB.point(0), Point(0, 0))
        self.assertEqual(LAB.point(12), Point(1, 1))

    def test_lab_start(self):
        self.assertEqual(LAB.start(), Point(4, 6))

    def test_lab_visualize(self):
        self.assertEqual(LAB.visualize(set()), LAB)
