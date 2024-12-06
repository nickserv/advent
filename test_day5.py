import unittest

from day5 import (
    check_update_order,
    fix_update_order,
    parse,
    sum_middle_numbers,
    sum_middle_numbers_fixed,
)

RULES, UPDATES = parse(
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
    """.strip()
)


class TestDay5(unittest.TestCase):
    def test_check_update_order(self):
        self.assertTrue(check_update_order(UPDATES[0], RULES))
        self.assertTrue(check_update_order(UPDATES[1], RULES))
        self.assertTrue(check_update_order(UPDATES[2], RULES))
        self.assertFalse(check_update_order(UPDATES[3], RULES))
        self.assertFalse(check_update_order(UPDATES[4], RULES))
        self.assertFalse(check_update_order(UPDATES[5], RULES))

    def test_fix_update_order(self):
        self.assertEqual(fix_update_order(UPDATES[3], RULES), [97, 75, 47, 61, 53])
        self.assertEqual(fix_update_order(UPDATES[4], RULES), [61, 29, 13])
        self.assertEqual(fix_update_order(UPDATES[5], RULES), [97, 75, 47, 29, 13])

    def test_sum_middle_numbers(self):
        self.assertEqual(sum_middle_numbers(UPDATES, RULES), 143)

    def test_sum_middle_numbers_fixed(self):
        self.assertEqual(sum_middle_numbers_fixed(UPDATES, RULES), 123)
