import unittest

from day1 import parse_lists, similarity_score, total_distance
from utils import get_input

LISTS = parse_lists(
    get_input(
        """
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """
    )
)


class TestDay1(unittest.TestCase):
    def test_total_distance(self):
        self.assertEqual(total_distance(*LISTS), 11)

    def test_similarity_score(self):
        self.assertEqual(similarity_score(*LISTS), 31)
