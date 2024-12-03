import unittest

from day2 import count, parse_lists, safe, safe_tolerant

lists2 = parse_lists(
    """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()
)


class TestDay2(unittest.TestCase):
    def test_safe(self):
        self.assertTrue(safe(lists2[0]))
        self.assertFalse(safe(lists2[1]))
        self.assertFalse(safe(lists2[2]))
        self.assertFalse(safe(lists2[3]))
        self.assertFalse(safe(lists2[4]))
        self.assertTrue(safe(lists2[5]))

    def test_count(self):
        self.assertEqual(count(lists2), 2)

    def test_count_tolerant(self):
        self.assertEqual(count(lists2, safe_tolerant), 4)
