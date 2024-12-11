import unittest

from day5 import parse, sum_middle_numbers, sum_middle_numbers_fixed
from utils import get_input

UPDATES = parse(
    get_input(
        """
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47
        """
    )
)


class TestDay5(unittest.TestCase):
    def test_update_check_order(self):
        self.assertTrue(UPDATES[0].check_order())
        self.assertTrue(UPDATES[1].check_order())
        self.assertTrue(UPDATES[2].check_order())
        self.assertFalse(UPDATES[3].check_order())
        self.assertFalse(UPDATES[4].check_order())
        self.assertFalse(UPDATES[5].check_order())

    def test_update_sort(self):
        self.assertEqual(sorted(UPDATES[3]), [97, 75, 47, 61, 53])
        self.assertEqual(sorted(UPDATES[4]), [61, 29, 13])
        self.assertEqual(sorted(UPDATES[5]), [97, 75, 47, 29, 13])

    def test_sum_middle_numbers(self):
        self.assertEqual(sum_middle_numbers(UPDATES), 143)

    def test_sum_middle_numbers_fixed(self):
        self.assertEqual(sum_middle_numbers_fixed(UPDATES), 123)
