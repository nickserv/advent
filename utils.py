# pylint:enable=missing-class-docstring,missing-function-docstring
from collections.abc import Callable
from pathlib import Path
from textwrap import dedent


def get_input(day_or_string: int | str):
    """Read an input from a file or inline string without extra whitespace"""
    match day_or_string:
        case int() as day:
            return Path(f"resources/{day}.txt").read_text("utf8")
        case str() as string:
            return dedent(string).strip()


def parse_lines[T](func: Callable[[str], T], string: str):
    """Parse each line of string with func and return a list of the results"""
    return [func(line) for line in string.splitlines()]
