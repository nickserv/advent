import re
from typing import Generator, Iterable, NamedTuple, Self

import numpy as np

from utils import get_input


class Machine(NamedTuple):
    ax: np.uint
    ay: np.uint
    bx: np.uint
    by: np.uint
    x: np.uint
    y: np.uint

    @classmethod
    def parse(cls, string: str) -> Generator[Self]:
        for match in re.finditer(
            r"""
            Button\ A:\ X\+(\d+),\ Y\+(\d+)\n
            Button\ B:\ X\+(\d+),\ Y\+(\d+)\n
            Prize:\ X=(\d+),\ Y=(\d+)
            """,
            string,
            re.X,
        ):
            yield cls(*(np.uint(group) for group in match.groups()))

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
