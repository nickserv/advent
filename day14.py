def parse_rock(string: str):
    match string:
        case "O":
            return True
        case "#":
            return False
        case ".":
            return None
        case _:
            raise ValueError(string)


def parse_platform(string: str):
    return list(
        zip(*([parse_rock(char) for char in line] for line in string.splitlines()))
    )


def shift(rocks: list[bool], shift: int):
    indexes = [index for index, rock in enumerate(rocks) if rock is False]
    return rocks[shift:] + rocks[:shift]


INPUT = parse_platform(
    """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
    """.strip()
)

print(INPUT)
# print(sorted(INPUT[0], reverse=True))
