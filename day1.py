from utils import get_input, parse_lines


def parse_rotations(string: str):
    return parse_lines(
        lambda line: int(line[1:]) * (-1 if line[0] == "L" else 1), string
    )


def zeros(list: list[int]):
    current = 50
    zeros = 0
    for n in list:
        current = (current + n) % 100
        if current == 0:
            zeros += 1
    return zeros


if __name__ == "__main__":
    print(zeros(parse_rotations(get_input(1))))
