import unittest

from day3 import calculate, calculate_conditional

INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
INPUT_COND = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


class TestDay2(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(INPUT), 161)

    def test_calculate_conditional(self):
        self.assertEqual(calculate_conditional(INPUT_COND), 48)
