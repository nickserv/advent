import unittest

from day18 import Space
from utils import Point, get_input


class TestSpace(unittest.TestCase):
    def setUp(self):
        self.points = Point.parse_many(
            get_input(
                """
                5,4
                4,2
                4,5
                3,0
                2,1
                6,3
                2,4
                1,5
                0,6
                3,3
                2,6
                5,1
                1,2
                5,5
                2,5
                6,5
                1,4
                0,4
                6,4
                1,1
                6,1
                1,0
                0,5
                1,6
                2,0
                """
            )
        )

    def test_shortest_path(self):
        self.assertEqual(Space(7, self.points[:12]).shortest_path(), 22)

    def test_search(self):
        self.assertEqual(Space(7).search(self.points), Point(6, 1))
