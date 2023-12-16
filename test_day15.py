import unittest

from day15 import custom_hash, powers, total_power

STEPS = [
    "rn=1",
    "cm-",
    "qp=3",
    "cm=2",
    "qp-",
    "pc=4",
    "ot=9",
    "ab=5",
    "pc-",
    "pc=6",
    "ot=7",
]


class Test(unittest.TestCase):
    def test_custom_hash(self):
        self.assertEqual(custom_hash("HASH"), 52)
        self.assertEqual(custom_hash(STEPS[0]), 30)
        self.assertEqual(custom_hash(STEPS[1]), 253)
        self.assertEqual(custom_hash(STEPS[2]), 97)
        self.assertEqual(custom_hash(STEPS[3]), 47)
        self.assertEqual(custom_hash(STEPS[4]), 14)
        self.assertEqual(custom_hash(STEPS[5]), 180)
        self.assertEqual(custom_hash(STEPS[6]), 9)
        self.assertEqual(custom_hash(STEPS[7]), 197)
        self.assertEqual(custom_hash(STEPS[8]), 48)
        self.assertEqual(custom_hash(STEPS[9]), 214)
        self.assertEqual(custom_hash(STEPS[10]), 231)
        self.assertEqual(custom_hash(STEPS), 1320)

    def test_powers(self):
        for index, box in enumerate(powers(STEPS)):
            match index:
                case 0:
                    expected = {"rn": 1, "cm": 2}
                case 3:
                    expected = {"ot": 7, "ab": 5, "pc": 6}
                case _:
                    expected = {}
            self.assertEqual(box, expected)

    def test_total_power(self):
        self.assertEqual(total_power(STEPS), 145)
