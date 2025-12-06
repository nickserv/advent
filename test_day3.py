import unittest

from day3 import joltage, parse_banks, total_joltage
from utils import clean_string

BANKS = parse_banks(
    clean_string(
        """
        987654321111111
        811111111111119
        234234234234278
        818181911112111
        """
    )
)


class TestDay3(unittest.TestCase):
    def test_joltage(self):
        self.assertEqual(joltage(BANKS[0], 2), 98)
        self.assertEqual(joltage(BANKS[1], 2), 89)
        self.assertEqual(joltage(BANKS[2], 2), 78)
        self.assertEqual(joltage(BANKS[3], 2), 92)
        self.assertEqual(joltage(BANKS[0], 12), 987654321111)
        self.assertEqual(joltage(BANKS[1], 12), 811111111119)
        self.assertEqual(joltage(BANKS[2], 12), 434234234278)
        self.assertEqual(joltage(BANKS[3], 12), 888911112111)

    def test_total_joltage(self):
        self.assertEqual(total_joltage(BANKS, 2), 357)
        self.assertEqual(total_joltage(BANKS, 12), 3121910778619)
