import unittest

from day11 import blink, call_composed


class TestDay11(unittest.TestCase):
    def test_blink(self):
        self.assertEqual(
            list(blink((0, 1, 10, 99, 999))), [1, 2024, 1, 0, 9, 9, 2021976]
        )

    def test_blink_composed(self):
        self.assertEqual(len(list(call_composed(blink, (125, 17), 25))), 55312)
