def parse_pattern(string: str):
    return [[char == "#" for char in line] for line in string.splitlines()]


def reflect(pattern: list[list[bool]]):
    return NotImplemented
