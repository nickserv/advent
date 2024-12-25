from collections.abc import Collection
from itertools import product
from typing import cast

from utils import get_input

type Block = tuple[int, int, int, int, int]


def parse(string: str):
    is_lock = string.startswith("#")
    rows = string.splitlines()[1:-1]
    blocks = cast(
        Block, tuple(sum(row[column] == "#" for row in rows) for column in range(0, 5))
    )
    return is_lock, blocks


def is_fitting(lock: Block, key: Block):
    return all(s <= 5 for s in (l + k for l, k in zip(lock, key)))


def count_fitting(blocks: Collection[tuple[bool, Block]]):
    locks = (block[1] for block in blocks if block[0])
    keys = (block[1] for block in blocks if not block[0])
    return sum(is_fitting(lock, key) for lock, key in product(locks, keys))


if __name__ == "__main__":
    print(count_fitting([parse(block) for block in get_input(25).split("\n\n")]))
