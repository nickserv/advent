from itertools import batched, chain

from utils import get_input


def parse_id_range(id_range: str):
    left, right = id_range.split("-")
    return range(int(left), int(right) + 1)


def parse_id_ranges(id_ranges: str):
    return [parse_id_range(id_range) for id_range in id_ranges.split(",")]


def is_valid_id(id_int: int, advanced: bool = False):
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


def invalid_ids(id_ranges: list[range], advanced: bool = False):
    return set(
        id for id in chain.from_iterable(id_ranges) if not is_valid_id(id, advanced)
    )


if __name__ == "__main__":
    id_ranges = parse_id_ranges(get_input(2))
    print(sum(invalid_ids(id_ranges)))
    print(sum(invalid_ids(id_ranges, True)))
