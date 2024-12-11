from functools import total_ordering
from itertools import pairwise
from typing import Sequence

from utils import get_input


class Rule(tuple[int, int]):
    @staticmethod
    def parse(string: str):
        x, _, y = string.partition("|")
        return Rule((int(x), int(y)))


_rules: set[Rule]


@total_ordering
class Page(int):
    def __lt__(self, other: int):
        return Rule((self, other)) in _rules


class Update(list[Page]):
    @staticmethod
    def parse(string: str):
        return Update([Page(int(x)) for x in string.split(",")])

    def check_order(self):
        return all(page < next_page for page, next_page in pairwise(self))


def parse(string: str):
    top, _, bottom = string.partition("\n\n")
    # A global is basically the only convenient way to make rules available to all instances, and
    # composability isn't a concern since the implementation and test files only have one set of
    # rules each.
    global _rules  # pylint: disable=global-statement
    _rules = {Rule.parse(line) for line in top.splitlines()}
    return [Update.parse(line) for line in bottom.splitlines()]


def middle[T](items: Sequence[T]):
    return items[len(items) // 2]


def sum_middle_numbers(updates: list[Update]) -> int:
    return sum(middle(update) for update in updates if update.check_order())


def sum_middle_numbers_fixed(updates: list[Update]) -> int:
    return sum(middle(sorted(update)) for update in updates if not update.check_order())


if __name__ == "__main__":
    updates = parse(get_input(5))
    print(sum_middle_numbers(updates))
    print(sum_middle_numbers_fixed(updates))
