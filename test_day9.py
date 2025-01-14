import unittest

from day9 import Blocks, checksum, compact, expand
from utils import digits

FIRST_MAP = digits("2333133121414131402")
SECOND_MAP = digits("12345")


def blocks(string: str) -> Blocks:
    return [None if char == "." else int(char) for char in string]


FIRST_BLOCKS = blocks("00...111...2...333.44.5555.6666.777.888899")
SECOND_BLOCKS = blocks("0..111....22222")


FIRST_IDS = list(digits("0099811188827773336446555566"))
SECOND_IDS = list(digits("022111222"))


class TestDay9(unittest.TestCase):
    def test_expand(self):
        self.assertEqual(expand(FIRST_MAP), FIRST_BLOCKS)
        self.assertEqual(expand(SECOND_MAP), SECOND_BLOCKS)

    def test_compact(self):
        self.assertEqual(list(compact(FIRST_BLOCKS)), FIRST_IDS)
        self.assertEqual(list(compact(SECOND_BLOCKS)), SECOND_IDS)

    def test_checksum(self):
        self.assertEqual(checksum(FIRST_IDS), 1928)
