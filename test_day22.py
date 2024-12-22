import unittest

from day22 import secrets


class TestDay22(unittest.TestCase):
    def test_secrets(self):
        with self.subTest("start"):
            self.assertEqual(
                secrets(123)[:11],
                [
                    123,
                    15887950,
                    16495136,
                    527345,
                    704524,
                    1553684,
                    12683156,
                    11100544,
                    12249484,
                    7753432,
                    5908254,
                ],
            )
        with self.subTest("end"):
            self.assertEqual(secrets(1)[-1], 8685429)
            self.assertEqual(secrets(10)[-1], 4700978)
            self.assertEqual(secrets(100)[-1], 15273692)
            self.assertEqual(secrets(2024)[-1], 8667524)
