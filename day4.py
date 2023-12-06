class Card:
    winning: set[int]
    have: set[int]

    def __init__(self, string: str):
        winning, _, have = string.partition(": ")[2].partition(" | ")
        self.winning = {int(number) for number in winning.split()}
        self.have = {int(number) for number in have.split()}

    def matches(self):
        return len(self.winning & self.have)

    def points(self):
        matches = self.matches()
        return matches if matches < 2 else 2 ** (matches - 1)


def sum_points(cards: list[Card]):
    return sum(card.points() for card in cards)


def sum_bonuses(cards: list[Card]):
    bonuses = [1] * len(cards)
    for card_index, card in enumerate(cards):
        for bonus_index in range(card_index + 1, card_index + 1 + card.matches()):
            bonuses[bonus_index] += bonuses[card_index]
    return sum(bonuses)


if __name__ == "__main__":
    with open("resources/4.txt", encoding="utf8") as file:
        cards = [Card(line) for line in file.readlines()]
    print(sum_points(cards))
    print(sum_bonuses(cards))
