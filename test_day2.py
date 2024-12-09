import unittest

from day2 import count, parse_lists, safe, safe_tolerant
from utils import get_input

LISTS = parse_lists(
    get_input(
        """
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
        """
    )
)


class TestDay2(unittest.TestCase):
    def test_safe(self):
        self.assertTrue(safe(LISTS[0]))
        self.assertFalse(safe(LISTS[1]))
        self.assertFalse(safe(LISTS[2]))
        self.assertFalse(safe(LISTS[3]))
        self.assertFalse(safe(LISTS[4]))
        self.assertTrue(safe(LISTS[5]))

    def test_count(self):
        self.assertEqual(count(LISTS), 2)

    def test_count_tolerant(self):
        self.assertEqual(count(LISTS, safe_tolerant), 4)
