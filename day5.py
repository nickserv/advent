from pathlib import Path


def parse_rule(string: str):
    x, _, y = string.partition("|")
    return (int(x), int(y))


def parse_update(string: str):
    return [int(x) for x in string.split(",")]


def parse(string: str):
    top, _, bottom = string.partition("\n\n")
    rules = [parse_rule(rule) for rule in top.splitlines()]
    updates = [parse_update(update) for update in bottom.splitlines()]
    return rules, updates


def check_update_order(update: list[int], rules: list[tuple[int, int]]):
    return all(
        not (rule[0] in update and rule[1] in update)
        or update.index(rule[0]) < update.index(rule[1])
        for rule in rules
    )


def sum_middle_numbers(updates: list[list[int]], rules: list[tuple[int, int]]):
    return sum(
        update[len(update) // 2]
        for update in updates
        if check_update_order(update, rules)
    )


if __name__ == "__main__":
    rules, updates = parse(Path("resources/5.txt").read_text("utf8"))
    print(sum_middle_numbers(updates, rules))
