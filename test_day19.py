import unittest

from day19 import count_possible, count_ways, count_ways_sum, parse
from utils import get_input


class TestDay19(unittest.TestCase):
    def setUp(self):
        self.patterns, self.designs = parse(
            get_input(
                # cspell:disable
                """
                r, wr, b, g, bwu, rb, gb, br

                brwrr
                bggr
                gbbr
                rrbgbr
                ubwu
                bwurrg
                brgr
                bbrgwb
                """
                # cspell:enable
            )
        )

    def test_count_ways(self):
        self.assertEqual(count_ways(self.patterns, self.designs[0]), 2)
        self.assertEqual(count_ways(self.patterns, self.designs[1]), 1)
        self.assertEqual(count_ways(self.patterns, self.designs[2]), 4)
        self.assertEqual(count_ways(self.patterns, self.designs[3]), 6)
        self.assertEqual(count_ways(self.patterns, self.designs[4]), 0)
        self.assertEqual(count_ways(self.patterns, self.designs[5]), 1)
        self.assertEqual(count_ways(self.patterns, self.designs[6]), 2)
        self.assertEqual(count_ways(self.patterns, self.designs[7]), 0)

    def test_count_possible(self):
        self.assertEqual(count_possible(self.patterns, self.designs), 6)

    def test_count_ways_sum(self):
        self.assertEqual(count_ways_sum(self.patterns, self.designs), 16)
