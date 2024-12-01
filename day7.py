from collections import Counter
from enum import Enum

HandType = Enum(
    "HandType",
    "FIVE_OF_A_KIND FOUR_OF_A_KIND FULL_HOUSE THREE_OF_A_KIND TWO_PAIR ONE_PAIR HIGH_CARD",
)


class Hand:
    def __init__(self, cards: str, bid: int = 0):
        self.cards = cards
        self.bid = bid

    def rank(self) -> int:
        return NotImplemented

    # FIXME types should reflect if every card in input has a HandType
    def type(self):
        match sorted(Counter(self.cards).values()):
            case [5]:
                return HandType.FIVE_OF_A_KIND
            case [1, 4]:
                return HandType.FOUR_OF_A_KIND
            case [2, 3]:
                return HandType.FULL_HOUSE
            case [1, 1, 3]:
                return HandType.THREE_OF_A_KIND
            case [1, 2, 2]:
                return HandType.TWO_PAIR
            case [1, 1, 1, 2]:
                return HandType.ONE_PAIR
            case [1, 1, 1, 1, 1]:
                return HandType.HIGH_CARD

    @staticmethod
    def parse(string: str):
        cards, bid = string.split()
        return Hand(cards, int(bid))
