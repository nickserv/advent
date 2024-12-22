import unittest
from itertools import islice

from day22 import iter_secrets, last


class TestDay22(unittest.TestCase):
    def test_iter_secrets(self):
        self.assertEqual(
            list(islice(iter_secrets(123), 10)),
            [
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

    def test_last_secret(self):
        self.assertEqual(last(iter_secrets(1)), 8685429)
        self.assertEqual(last(iter_secrets(10)), 4700978)
        self.assertEqual(last(iter_secrets(100)), 15273692)
        self.assertEqual(last(iter_secrets(2024)), 8667524)
