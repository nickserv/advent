import re
from typing import Generator, Iterable, Self

import numpy as np

from utils import get_input


class Machine:
    ax: np.uint
    ay: np.uint
    bx: np.uint
    by: np.uint
    x: np.uint
    y: np.uint

    def __init__(self, match: re.Match[str]):
        for key, value in match.groupdict().items():
            setattr(self, key, np.uint(value))

    @classmethod
    def parse(cls, string: str) -> Generator[Self]:
        for match in re.finditer(
            r"""
            Button\ A:\ X\+(?P<ax>\d+),\ Y\+(?P<ay>\d+)\n
            Button\ B:\ X\+(?P<bx>\d+),\ Y\+(?P<by>\d+)\n
            Prize:\ X=(?P<x>\d+),\ Y=(?P<y>\d+)
            """,
            string,
            re.X,
        ):
            yield cls(match)

    # Solve this system of equations:
    # ax * a + bx * b = x
    # ay * a + by * b = y
    def cost(self):
        coefficients = np.array([[self.ax, self.bx], [self.ay, self.by]])
        dependents = np.array([self.x, self.y])
        solution = np.linalg.solve(coefficients, dependents)
        if not all(np.isclose(solution, np.round(solution))):
            return np.uint(0)
        return np.sum(np.round(solution).astype(np.uint) * np.array([3, 1], np.uint))


def total_cost(machines: Iterable[Machine]):
    return sum(machine.cost() for machine in machines)


if __name__ == "__main__":
    machines = tuple(Machine.parse(get_input(13)))
    print(total_cost(machines))
