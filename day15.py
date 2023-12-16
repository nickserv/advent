from functools import reduce
from pathlib import Path


def custom_hash(steps: str | list[str]):
    if isinstance(steps, str):
        return reduce(lambda current, char: (current + ord(char)) * 17 % 256, steps, 0)
    return sum(map(custom_hash, steps))


if __name__ == "__main__":
    print(custom_hash(Path("resources/15.txt").read_text("utf8").rstrip().split(",")))
