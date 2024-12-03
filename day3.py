import re
from pathlib import Path


def parse_instructions(string: str):
    return [
        (
            (int(match[1]), int(match[2]))
            if match[0].startswith("mul")
            else match[0] == "do()"
        )
        for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", string)
    ]


def calculate(instructions: list[tuple[int, int] | bool], conditional: bool = False):
    result = 0
    scanning = True
    for instruction in instructions:
        if isinstance(instruction, tuple) and scanning:
            result += instruction[0] * instruction[1]
        elif isinstance(instruction, bool) and conditional:
            scanning = instruction
    return result


if __name__ == "__main__":
    instructions = parse_instructions(Path("resources/3.txt").read_text("utf8"))
    print(calculate(instructions))
    print(calculate(instructions, True))
