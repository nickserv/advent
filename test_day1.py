import unittest

from day1 import parse_rotations, zeros
from utils import get_input

LIST = parse_rotations(
    get_input(
        """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
        """
    )
)


class TestDay1(unittest.TestCase):
    def test_zeros(self):
        self.assertEqual(zeros(LIST), 3)
