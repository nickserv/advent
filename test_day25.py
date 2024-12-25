import unittest

from day25 import count_fitting, is_fitting, parse
from utils import get_input

BLOCK_PAIRS = [
    parse(block)
    for block in get_input(
        """
        #####
        .####
        .####
        .####
        .#.#.
        .#...
        .....

        #####
        ##.##
        .#.##
        ...##
        ...#.
        ...#.
        .....

        .....
        #....
        #....
        #...#
        #.#.#
        #.###
        #####

        .....
        .....
        #.#..
        ###..
        ###.#
        ###.#
        #####

        .....
        .....
        .....
        #....
        #.#..
        #.#.#
        #####
        """
    ).split("\n\n")
]


class TestDay25(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(BLOCK_PAIRS[0], (True, (0, 5, 3, 4, 3)))
        self.assertEqual(BLOCK_PAIRS[1], (True, (1, 2, 0, 5, 3)))
        self.assertEqual(BLOCK_PAIRS[2], (False, (5, 0, 2, 1, 3)))
        self.assertEqual(BLOCK_PAIRS[3], (False, (4, 3, 4, 0, 2)))
        self.assertEqual(BLOCK_PAIRS[4], (False, (3, 0, 2, 0, 1)))

    def test_is_fitting(self):
        blocks = [block for _, block in BLOCK_PAIRS]
        self.assertFalse(is_fitting(blocks[0], blocks[2]))
        self.assertFalse(is_fitting(blocks[0], blocks[3]))
        self.assertTrue(is_fitting(blocks[0], blocks[4]))
        self.assertFalse(is_fitting(blocks[1], blocks[2]))
        self.assertTrue(is_fitting(blocks[1], blocks[3]))
        self.assertTrue(is_fitting(blocks[1], blocks[4]))

    def test_count_fitting(self):
        self.assertEqual(count_fitting(BLOCK_PAIRS), 3)
