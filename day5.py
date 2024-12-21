from collections.abc import Sequence
from itertools import pairwise

from utils import get_input, parse_lines

type Rule = tuple[int, int]


def parse_rule(string: str) -> Rule:
    x, _, y = string.partition("|")
    return int(x), int(y)


_rules: set[Rule]


class Page(int):
    def __lt__(self, other: int):
        return (self, other) in _rules


type Update = list[Page]


def parse_update(string: str) -> Update:
    return [Page(x) for x in string.split(",")]


def check_order(update: Update):
    return all(page < next_page for page, next_page in pairwise(update))


def parse(string: str):
    top, _, bottom = string.partition("\n\n")
    # A global is basically the only convenient way to make rules available to all
    # instances, and composability isn't a concern since the implementation and test
    # files only have one set of rules each.
    global _rules  # pylint: disable=global-statement
    _rules = set(parse_lines(parse_rule, top))
    return parse_lines(parse_update, bottom)


def middle[T](items: Sequence[T]):
    return items[len(items) // 2]


def sum_middle_numbers(updates: list[Update]) -> int:
    return sum(middle(update) for update in updates if check_order(update))


def sum_middle_numbers_fixed(updates: list[Update]) -> int:
    return sum(middle(sorted(update)) for update in updates if not check_order(update))


if __name__ == "__main__":
    updates = parse(get_input(5))
    print(sum_middle_numbers(updates))
    print(sum_middle_numbers_fixed(updates))
