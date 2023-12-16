from functools import reduce
from pathlib import Path


def custom_hash(steps: str | list[str]):
    if isinstance(steps, str):
        return reduce(lambda current, char: (current + ord(char)) * 17 % 256, steps, 0)
    return sum(map(custom_hash, steps))


def powers(steps: list[str]):
    lens_boxes: list[dict[str, int]] = [{} for _ in range(256)]
    for step in steps:
        if "=" in step:
            label, _, focal_length = step.partition("=")
            lens_boxes[custom_hash(label)][label] = int(focal_length)
        elif step.endswith("-"):
            label = step[:-1]
            lens_boxes[custom_hash(label)].pop(label, None)
        else:
            raise ValueError(f"invalid step for power(): '{step}'")
    return lens_boxes


def total_power(steps: list[str]):
    return sum(
        (index + 1) * (slot + 1) * power
        for index, box in enumerate(powers(steps))
        for slot, power in enumerate(box.values())
    )


if __name__ == "__main__":
    steps = Path("resources/15.txt").read_text("utf8").rstrip().split(",")
    print(custom_hash(steps))
    print(total_power(steps))
