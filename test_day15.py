import unittest

from day15 import custom_hash


class Test(unittest.TestCase):
    def test_custom_hash(self):
        self.assertEqual(custom_hash("HASH"), 52)
        self.assertEqual(custom_hash("rn=1"), 30)
        self.assertEqual(custom_hash("cm-"), 253)
        self.assertEqual(custom_hash("qp=3"), 97)
        self.assertEqual(custom_hash("cm=2"), 47)
        self.assertEqual(custom_hash("qp-"), 14)
        self.assertEqual(custom_hash("pc=4"), 180)
        self.assertEqual(custom_hash("ot=9"), 9)
        self.assertEqual(custom_hash("ab=5"), 197)
        self.assertEqual(custom_hash("pc-"), 48)
        self.assertEqual(custom_hash("pc=6"), 214)
        self.assertEqual(custom_hash("ot=7"), 231)
        self.assertEqual(
            custom_hash(
                [
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
            ),
            1320,
        )
