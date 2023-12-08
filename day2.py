from functools import reduce
from operator import mul


class Bag:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f"Bag(red={self.red}, green={self.green}, blue={self.blue})"

    @staticmethod
    def parse(string: str):
        bag = Bag()
        for segment in string.split(", "):
            count, _, color = segment.partition(" ")
            setattr(bag, color, int(count))
        return bag


COLORS = ["red", "green", "blue"]


def parse_game(line: str):
    return [Bag.parse(string) for string in line.strip().partition(": ")[2].split("; ")]


GOAL = Bag(red=12, green=13, blue=14)


def possible(game: list[Bag]):
    return all(
        getattr(bag, color) <= getattr(GOAL, color) for color in COLORS for bag in game
    )


def sum_possible(games: list[list[Bag]]):
    return sum(index + 1 for index, game in enumerate(games) if possible(game))


def power(game: list[Bag]) -> int:
    return reduce(mul, (max(getattr(bag, color) for bag in game) for color in COLORS))


def sum_powers(games: list[list[Bag]]):
    return sum(power(game) for game in games)


if __name__ == "__main__":
    with open("resources/2.txt", encoding="utf8") as file:
        games = [parse_game(line) for line in file.readlines()]
    print(sum_possible(games))
    print(sum_powers(games))
