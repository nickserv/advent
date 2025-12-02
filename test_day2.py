import unittest

from day2 import invalid_ids, parse_id_ranges

ID_RANGES = parse_id_ranges(
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
)


class TestDay1(unittest.TestCase):
    def test_invalid_ids(self):
        self.assertEqual(sum(invalid_ids(ID_RANGES)), 1227775554)

    def test_invalid_ids_advanced(self):
        self.assertEqual(sum(invalid_ids(ID_RANGES, True)), 4174379265)
