from functools import cmp_to_key

from utils import get_input

type Rule = tuple[int, int]
type Update = list[int]


def parse_rule(string: str) -> Rule:
    x, _, y = string.partition("|")
    return (int(x), int(y))


def parse_update(string: str) -> Update:
    return [int(x) for x in string.split(",")]


def parse(string: str):
    top, _, bottom = string.partition("\n\n")
    rules = {parse_rule(rule) for rule in top.splitlines()}
    updates = [parse_update(update) for update in bottom.splitlines()]
    return rules, updates


def check_update_order(update: Update, rules: set[Rule]):
    return all(
        not (rule[0] in update and rule[1] in update)
        or update.index(rule[0]) < update.index(rule[1])
        for rule in rules
    )


def fix_update_order(update: Update, rules: set[Rule]) -> Update:
    def cmp(x: int, y: int):
        if (x, y) in rules:
            return -1
        if (y, x) in rules:
            return 1
        return NotImplemented

    return sorted(update, key=cmp_to_key(cmp))


def sum_middle_numbers(updates: list[Update], rules: set[Rule]):
    return sum(
        update[len(update) // 2]
        for update in updates
        if check_update_order(update, rules)
    )


def sum_middle_numbers_fixed(updates: list[Update], rules: set[Rule]):
    return sum(
        fix_update_order(update, rules)[len(update) // 2]
        for update in updates
        if not check_update_order(update, rules)
    )


if __name__ == "__main__":
    rules, updates = parse(get_input(5))
    print(sum_middle_numbers(updates, rules))
    print(sum_middle_numbers_fixed(updates, rules))
