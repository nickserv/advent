import re
from itertools import cycle
from math import lcm
from pathlib import Path


def parse(string: str) -> tuple[list[bool], dict[str, tuple[str, str]]]:
    lines = string.splitlines()
    return [char == "R" for char in lines[0]], dict(
        (match.group(1), (match.group(2), match.group(3)))
        for line in lines[2:]
        for match in re.finditer(
            r"([\w\d]{2}\w) = \(([\w\d]{2}\w), ([\w\d]{2}\w)\)", line
        )
    )


def steps(
    instructions: list[bool],
    network: dict[str, tuple[str, str]],
    start: str = "AAA",
    ends: frozenset[str] = frozenset(["ZZZ"]),
):
    for index, instruction in enumerate(cycle(instructions)):
        start = network[start][instruction]
        if start in ends:
            return index + 1
    return 0


def complex_steps(instructions: list[bool], network: dict[str, tuple[str, str]]):
    starts = (key for key in network.keys() if key.endswith("A"))
    ends = frozenset(key for key in network.keys() if key.endswith("Z"))
    return lcm(*(steps(instructions, network, start, ends) for start in starts))


if __name__ == "__main__":
    instructions, network = parse(Path("resources/8.txt").read_text("utf8"))
    print(steps(instructions, network))
    print(complex_steps(instructions, network))
