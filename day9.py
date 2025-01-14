from collections.abc import Iterable
from itertools import cycle, repeat

from utils import digits, get_input

type Blocks = list[int | None]
type CompactBlocks = list[int]


def expand(digits: Iterable[int]) -> Blocks:
    index = 0
    result: Blocks = []
    for element, file in zip(digits, cycle((True, False))):
        if file:
            value = index
            index += 1
        else:
            value = None
        result += repeat(value, element)
    return result


def find_last[T](items: list[T]):
    return next(
        (
            len(items) - index - 1
            for index, item in enumerate(reversed(items))
            if item is not None
        ),
        None,
    )


def compact(blocks: Blocks) -> CompactBlocks:
    write_index = 0
    read_index = len(blocks) - 1
    compact_blocks: CompactBlocks = []
    while write_index <= read_index:
        block = blocks[write_index]
        if block is None:
            if (index := find_last(blocks[:read_index])) is not None:
                if (value := blocks[read_index]) is not None:
                    read_index = index
                    compact_blocks.append(value)
        else:
            compact_blocks.append(block)
        write_index += 1
    return compact_blocks


def checksum(blocks: CompactBlocks):
    return sum(index * id for index, id in enumerate(blocks))


if __name__ == "__main__":
    disk_map = digits(get_input(9).strip())
    print(checksum(compact(expand(disk_map))))
