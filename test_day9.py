import unittest

from day9 import extrapolate, extrapolate_all, parse

HISTORIES = [
    parse(line)
    for line in """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
    """.strip().splitlines()
]


class Test(unittest.TestCase):
    def test_extrapolate(self):
        self.assertEqual(extrapolate(HISTORIES[0]), 18)
        self.assertEqual(extrapolate(HISTORIES[1]), 28)
        self.assertEqual(extrapolate(HISTORIES[2]), 68)

    def test_extrapolate_all(self):
        self.assertEqual(extrapolate_all(HISTORIES), 114)
