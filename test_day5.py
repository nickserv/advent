import unittest

from day5 import count_fresh, parse_ids
from utils import clean_string

ID_RANGES, IDS = parse_ids(
    clean_string(
        """
        3-5
        10-14
        16-20
        12-18

        1
        5
        8
        11
        17
        32
        """
    )
)


class TestDay5(unittest.TestCase):
    def test_count_fresh(self):
        self.assertEqual(count_fresh(ID_RANGES, IDS), 3)
