from typing import Sequence

DIGITS = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)


def find_digits(line: str, indexes: range, parse: bool = False):
    for index in indexes:
        if line[index].isdigit():
            return int(line[index])
        if parse:
            for digit_index, digit in enumerate(DIGITS):
                if line[index:].startswith(digit):
                    return digit_index + 1
    return 0


def calibration_value(line: str, parse: bool = False):
    first = find_digits(line, range(len(line)), parse)
    last = find_digits(line, range(len(line) - 1, -1, -1), parse)
    return first * 10 + last


def calibration_value_sum(lines: Sequence[str], parse: bool = False):
    return sum(calibration_value(line, parse) for line in lines)


if __name__ == "__main__":
    with open("resources/1.txt", encoding="utf8") as file:
        lines = file.readlines()
    for parse in False, True:
        print(calibration_value_sum(lines, parse))
