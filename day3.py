import re
from pathlib import Path


def parse_instructions(string: str):
    return (
        (int(match[1]), int(match[2]))
        for match in re.finditer(r"mul\((\d+),(\d+)\)", string)
    )


def calculate(string: str):
    return sum(x * y for x, y in parse_instructions(string))


def parse_instructions_conditional(string: str):
    return (
        (
            (int(match[1]), int(match[2]))
            if match[0].startswith("mul")
            else match[0] == "do()"
        )
        for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", string)
    )


def calculate_conditional(string: str):
    result = 0
    scanning = True
    for instruction in parse_instructions_conditional(string):
        if isinstance(instruction, bool):
            scanning = instruction
        elif scanning:
            result += instruction[0] * instruction[1]
    return result


if __name__ == "__main__":
    input2 = Path("resources/3.txt").read_text("utf8")
    print(calculate(input2))
    print(calculate_conditional(input2))
