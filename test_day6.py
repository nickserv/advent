import unittest

from day6 import parse_worksheet, solve_worksheet
from utils import clean_string

WORKSHEET = parse_worksheet(
    clean_string(
        """
        123 328  51 64
         45 64  387 23
          6 98  215 314
        *   +   *   +
        """
    )
)


class TestDay5(unittest.TestCase):
    def test_solve_worksheet(self):
        self.assertEqual(solve_worksheet(WORKSHEET), 4277556)
