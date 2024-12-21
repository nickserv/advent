import re
from collections.abc import Generator, Iterable
from dataclasses import dataclass
from typing import Self

import numpy as np

from utils import get_input


@dataclass(kw_only=True)
class Machine:
    ax: np.uint
    ay: np.uint
    bx: np.uint
    by: np.uint
    x: np.uint
    y: np.uint

    @classmethod
    def parse_many(cls, string: str) -> Generator[Self]:
        for match in re.finditer(
            r"""
            Button\ A:\ X\+(?P<ax>\d+),\ Y\+(?P<ay>\d+)\n
            Button\ B:\ X\+(?P<bx>\d+),\ Y\+(?P<by>\d+)\n
            Prize:\ X=(?P<x>\d+),\ Y=(?P<y>\d+)
            """,
            string,
            re.X,
        ):
            yield cls(
                **{key: np.uint(value) for key, value in match.groupdict().items()}
            )

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
    machines = tuple(Machine.parse_many(get_input(13)))
    print(total_cost(machines))
