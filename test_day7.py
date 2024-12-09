import unittest
from operator import add, mul
from typing import cast

from day7 import concat, parse_equations, results, total
from utils import get_input

EQUATIONS = parse_equations(
    get_input(
        """
        190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20
        """
    )
)
TESTS, NUMBERS = cast(tuple[list[int], list[list[int]]], zip(*EQUATIONS))


class TestDay7(unittest.TestCase):
    def test_results(self):
        self.assertEqual(list(results(NUMBERS[0], add, mul)), [29, 190])
        self.assertEqual(
            list(results(NUMBERS[1], add, mul)), [148, 3_267, 3_267, 87_480]
        )
        self.assertEqual(
            list(results(NUMBERS[8], add, mul)),
            [53, 660, 292, 5_440, 102, 1_640, 1_076, 21_120],
        )

    def test_valid(self):
        self.assertIn(TESTS[0], results(NUMBERS[0], add, mul))
        self.assertIn(TESTS[1], results(NUMBERS[1], add, mul))
        self.assertNotIn(TESTS[2], results(NUMBERS[2], add, mul))
        self.assertNotIn(TESTS[3], results(NUMBERS[3], add, mul))
        self.assertNotIn(TESTS[4], results(NUMBERS[4], add, mul))
        self.assertNotIn(TESTS[5], results(NUMBERS[5], add, mul))
        self.assertNotIn(TESTS[6], results(NUMBERS[6], add, mul))
        self.assertNotIn(TESTS[7], results(NUMBERS[7], add, mul))
        self.assertIn(TESTS[8], results(NUMBERS[8], add, mul))

    def test_total(self):
        self.assertEqual(total(EQUATIONS, add, mul), 3_749)

    def test_concat(self):
        self.assertEqual(concat(12, 345), 12_345)
