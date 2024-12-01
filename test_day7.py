import unittest

from day7 import Hand, HandType

hands = [
    Hand.parse(line)
    for line in """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().splitlines()
]


class HandTest(unittest.TestCase):
    def test_type(self):
        self.assertEqual(Hand("AAAAA").type(), HandType.FIVE_OF_A_KIND)
        self.assertEqual(Hand("AA8AA").type(), HandType.FOUR_OF_A_KIND)
        self.assertEqual(Hand("23332").type(), HandType.FULL_HOUSE)
        self.assertEqual(Hand("TTT98").type(), HandType.THREE_OF_A_KIND)
        self.assertEqual(Hand("23432").type(), HandType.TWO_PAIR)
        self.assertEqual(Hand("A23A4").type(), HandType.ONE_PAIR)
        self.assertEqual(Hand("23456").type(), HandType.HIGH_CARD)

        self.assertEqual(Hand("33332").type(), HandType.FOUR_OF_A_KIND)
        self.assertEqual(Hand("2AAAA").type(), HandType.FOUR_OF_A_KIND)
        self.assertEqual(Hand("77888").type(), HandType.FULL_HOUSE)
        self.assertEqual(Hand("77788").type(), HandType.FULL_HOUSE)
