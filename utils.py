from itertools import product
from pathlib import Path
from textwrap import dedent
from typing import Iterable, Iterator, cast


def get_input(day_or_string: int | str):
    match day_or_string:
        case int(day):
            return Path(f"resources/{day}.txt").read_text("utf8")
        case str(string):
            return dedent(string).strip()


def pairs[T](iterable: Iterable[T]):
    return cast(Iterator[tuple[T, T]], product(iterable, repeat=2))
