import unittest

from day3 import Part, Symbol, sum_adjacent, sum_ratios

STRING = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()
PARTS = Part.parse(STRING)
SYMBOLS = Symbol.parse(STRING)


class TestSymbol(unittest.TestCase):
    def test_adjacent(self):
        self.assertTrue(SYMBOLS[0].adjacent(PARTS[0]))
        self.assertTrue(SYMBOLS[0].adjacent(PARTS[2]))
        self.assertTrue(SYMBOLS[1].adjacent(PARTS[3]))
        self.assertTrue(SYMBOLS[2].adjacent(PARTS[4]))
        self.assertTrue(SYMBOLS[3].adjacent(PARTS[6]))
        self.assertTrue(SYMBOLS[5].adjacent(PARTS[7]))
        self.assertTrue(SYMBOLS[4].adjacent(PARTS[8]))
        self.assertTrue(SYMBOLS[5].adjacent(PARTS[9]))
        for symbol in SYMBOLS:
            self.assertFalse(symbol.adjacent(PARTS[1]))
            self.assertFalse(symbol.adjacent(PARTS[5]))

    def test_ratio(self):
        self.assertEqual(SYMBOLS[0].ratio(PARTS), 16345)
        self.assertEqual(SYMBOLS[2].ratio(PARTS), 0)
        self.assertEqual(SYMBOLS[5].ratio(PARTS), 451490)


class Test(unittest.TestCase):
    def test_sum_adjacent(self):
        self.assertEqual(sum_adjacent(PARTS, SYMBOLS), 4361)

    def test_sum_ratios(self):
        self.assertEqual(sum_ratios(PARTS, SYMBOLS), 467835)
