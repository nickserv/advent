import unittest

from day1 import parse_lists, similarity_score, total_distance


class Test(unittest.TestCase):
    SAMPLE = """
3   4
4   3
2   5
1   3
3   9
3   3
    """.strip()

    def test_total_distance(self):
        left, right = parse_lists(self.SAMPLE)
        self.assertEqual(total_distance(left, right), 11)

    def test_similarity_score(self):
        left, right = parse_lists(self.SAMPLE)
        self.assertEqual(similarity_score(left, right), 31)
