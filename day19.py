from utils import get_input

cache = {"": 1}


def count_ways(patterns: list[str], design: str) -> int:
    if design in cache:
        return cache[design]
    cache[design] = sum(
        count_ways(patterns, design[len(pattern) :])
        for pattern in patterns
        if design.startswith(pattern)
    )
    return cache[design]


def count_possible(patterns: list[str], designs: list[str]) -> int:
    return sum(bool(count_ways(patterns, design)) for design in designs)


def count_ways_sum(patterns: list[str], designs: list[str]):
    return sum(count_ways(patterns, design) for design in designs)


def parse(string: str):
    top, _, bottom = string.partition("\n\n")
    return top.split(", "), bottom.splitlines()


if __name__ == "__main__":
    patterns, designs = parse(get_input(19))
    print(count_possible(patterns, designs))
    print(count_ways_sum(patterns, designs))
