from itertools import cycle, repeat
from typing import Generator, Iterable, Optional

from colorama import Style

from utils import get_input

type Blocks = list[Optional[int]]
type CompactBlocks = list[int]
type Ints = Generator[int]


def ints(string: str) -> Ints:
    return (int(char) for char in string)


def expand(ints: Iterable[int]) -> Blocks:
    index = 0
    result: Blocks = []
    for element, file in zip(ints, cycle((True, False))):
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


def format_block(block: Optional[int], highlight: bool):
    return "".join(
        (
            Style.BRIGHT if highlight else "",
            "." if block is None else str(block),
            Style.RESET_ALL,
        )
    )


def format_blocks(blocks: Blocks, write_index: int, read_index: int):
    return "".join(
        format_block(block, index in (write_index, read_index))
        for index, block in enumerate(blocks)
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
                    print(
                        format_blocks(
                            [
                                *compact_blocks[:(write_index)],
                                *blocks[(write_index):read_index],
                                blocks[read_index],
                                *([None] * (len(blocks) - read_index - 1)),
                            ],
                            (write_index),
                            read_index,
                        )
                    )
                    read_index = index
                    compact_blocks.append(value)
        else:
            compact_blocks.append(block)
        write_index += 1
    return compact_blocks


def checksum(blocks: CompactBlocks):
    return sum(index * id for index, id in enumerate(blocks))


if __name__ == "__main__":
    disk_map = ints(get_input(9).strip())
    print(checksum(compact(expand(disk_map))))
