from collections.abc import Iterable

from utils import parse_id_range, parse_lines, read_input


def count_fresh(id_ranges: Iterable[range], ids: Iterable[int]):
    return sum(any(id in id_range for id_range in id_ranges) for id in ids)


def parse_ids(string: str):
    top, _, bottom = string.partition("\n\n")
    return parse_lines(parse_id_range, top), parse_lines(int, bottom)


if __name__ == "__main__":
    id_ranges, ids = parse_ids(read_input(5))
    print(count_fresh(id_ranges, ids))
