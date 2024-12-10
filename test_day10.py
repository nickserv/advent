import unittest

from day10 import TopMap
from utils import get_input

SMALL_MAP, LARGE_MAP = (
    TopMap(get_input(string))
    for string in (
        """
        0123
        1234
        8765
        9876
        """,
        """
        89010123
        78121874
        87430965
        96549874
        45678903
        32019012
        01329801
        10456732
        """,
    )
)


class TestDay10(unittest.TestCase):
    def test_map(self):
        with self.subTest(map="small"):
            self.assertEqual(
                SMALL_MAP.list, [0, 1, 2, 3, 1, 2, 3, 4, 8, 7, 6, 5, 9, 8, 7, 6]
            )

    def test_map_trailheads(self):
        with self.subTest(map="small"):
            self.assertEqual(list(SMALL_MAP.trailheads()), [0])

        with self.subTest(map="large"):
            self.assertEqual(
                list(LARGE_MAP.trailheads()), [2, 4, 20, 38, 42, 45, 48, 54, 57]
            )

    def test_map_neighbors(self):
        with self.subTest(map="small"):
            self.assertEqual(list(SMALL_MAP.neighbors(0)), [1, 4])
            self.assertEqual(list(SMALL_MAP.neighbors(5)), [1, 4, 6, 9])

    def test_map_reachable(self):
        with self.subTest(map="small"):
            self.assertEqual(list(SMALL_MAP.reachable(0)), [12])

    def test_map_score(self):
        with self.subTest(map="small"):
            self.assertEqual(SMALL_MAP.score(0), 1)

        with self.subTest(map="large"):
            self.assertEqual(LARGE_MAP.score(2), 5)
            self.assertEqual(LARGE_MAP.score(4), 6)
            self.assertEqual(LARGE_MAP.score(20), 5)
            self.assertEqual(LARGE_MAP.score(38), 3)
            self.assertEqual(LARGE_MAP.score(42), 1)
            self.assertEqual(LARGE_MAP.score(45), 3)
            self.assertEqual(LARGE_MAP.score(48), 5)
            self.assertEqual(LARGE_MAP.score(54), 3)
            self.assertEqual(LARGE_MAP.score(57), 5)

    def test_map_scores(self):
        with self.subTest(map="small"):
            self.assertEqual(list(SMALL_MAP.scores()), [1])

        with self.subTest(map="large"):
            self.assertEqual(list(LARGE_MAP.scores()), [5, 6, 5, 3, 1, 3, 5, 3, 5])
