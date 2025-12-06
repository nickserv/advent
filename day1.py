from collections.abc import Iterable

from utils import parse_lines, read_input


def parse_rotations(string: str):
    return parse_lines(
        lambda line: int(line[1:]) * (-1 if line[0] == "L" else 1), string
    )


def zeros(rotations: Iterable[int]):
    current = 50
    zeros = 0
    for rotation in rotations:
        current = (current + rotation) % 100
        if current == 0:
            zeros += 1
    return zeros


if __name__ == "__main__":
    print(zeros(parse_rotations(read_input(1))))
