import unittest

from day13 import Machine, total_cost
from utils import get_input

MACHINES = tuple(
    Machine.parse(
        get_input(
            """
            Button A: X+94, Y+34
            Button B: X+22, Y+67
            Prize: X=8400, Y=5400

            Button A: X+26, Y+66
            Button B: X+67, Y+21
            Prize: X=12748, Y=12176

            Button A: X+17, Y+86
            Button B: X+84, Y+37
            Prize: X=7870, Y=6450

            Button A: X+69, Y+23
            Button B: X+27, Y+71
            Prize: X=18641, Y=10279
            """
        )
    )
)


class TestMachine(unittest.TestCase):
    def test_cost(self):
        self.assertEqual(MACHINES[0].cost(), 280)
        self.assertEqual(MACHINES[1].cost(), 0)
        self.assertEqual(MACHINES[2].cost(), 200)
        self.assertEqual(MACHINES[3].cost(), 0)


class TestDay13(unittest.TestCase):
    def test_total_cost(self):
        self.assertEqual(total_cost(MACHINES), 480)
