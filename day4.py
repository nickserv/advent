from typing import Self


class Card:
    winning: set[int]
    have: set[int]

    def __init__(self, string: str):
        winning, _, have = string.partition(": ")[2].partition(" | ")
        self.winning = {int(number) for number in winning.split()}
        self.have = {int(number) for number in have.split()}

    def points(self):
        matches = len(self.winning & self.have)
        return matches if matches < 2 else 2 ** (matches - 1)

    @classmethod
    def sum(cls, cards: list[Self]):
        return sum(card.points() for card in cards)


if __name__ == "__main__":
    with open("resources/4.txt", encoding="utf8") as file:
        print(Card.sum([Card(line) for line in file.readlines()]))
