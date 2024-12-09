import re
from pathlib import Path

from utils import get_input


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
        match instruction:
            case x, y:
                if scanning:
                    result += x * y
            case _:
                scanning = not conditional or instruction
    return result


if __name__ == "__main__":
    instructions = parse_instructions(get_input(3))
    print(calculate(instructions))
    print(calculate(instructions, True))
