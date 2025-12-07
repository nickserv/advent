from collections.abc import Iterable
from itertools import batched, chain

from utils import parse_id_range, read_input


def is_valid_id(id_int: int, *, advanced: bool = False):
    id_string = str(id_int)
    halfway = len(id_string) // 2
    if advanced:
        return not any(
            len(set(batched(id_string, batch_length))) == 1
            for batch_length in range(1, halfway + 1)
        )
    if len(id_string) % 1:
        return True
    left, right = id_string[:halfway], id_string[halfway:]
    return left != right


def invalid_ids(id_ranges: Iterable[range], *, advanced: bool = False):
    return set(
        id
        for id in chain.from_iterable(id_ranges)
        if not is_valid_id(id, advanced=advanced)
    )


def parse_id_ranges(string: str):
    return list(map(parse_id_range, string.split(",")))


if __name__ == "__main__":
    id_ranges = parse_id_ranges(read_input(2))
    print(sum(invalid_ids(id_ranges)))
    print(sum(invalid_ids(id_ranges, advanced=True)))
