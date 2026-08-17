import unittest

from day9 import max_area
from utils import Point, clean_string, parse_lines

POINTS = parse_lines(
    Point.parse,
    clean_string("""
        7,1
        11,1
        11,7
        9,7
        9,5
        2,5
        2,3
        7,3
    """),
)


class TestDay9(unittest.TestCase):
    def test_max_area(self):
        self.assertEqual(max_area(POINTS), 50)
