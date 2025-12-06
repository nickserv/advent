# pylint:enable=missing-class-docstring,missing-function-docstring
from collections.abc import Callable
from pathlib import Path
from textwrap import dedent


def clean_string(string: str):
    """Clean extra whitespace from an inline input string"""
    return dedent(string).strip()


def parse_lines[T](func: Callable[[str], T], string: str):
    """Parse each line of string with func and return a list of the results"""
    return [func(line) for line in string.splitlines()]


def read_input(day: int):
    """Read an input from a file"""
    return Path(f"resources/{day}.txt").read_text("utf8")
