import unittest

from day14 import Point, Space
from utils import get_input

CLAMP = (11, 7)
SPACE = Space(
    get_input(
        """
        p=0,4 v=3,-3
        p=6,3 v=-1,-3
        p=10,3 v=-1,2
        p=2,0 v=2,-1
        p=0,0 v=1,3
        p=3,0 v=-2,-2
        p=7,6 v=-1,-3
        p=3,0 v=-1,-2
        p=9,3 v=2,3
        p=7,3 v=-1,2
        p=2,4 v=2,-3
        p=9,5 v=-3,-3
        """
    ),
    *CLAMP
)


class TestRobot(unittest.TestCase):
    def test_move(self):
        robot = SPACE.robots[10]
        self.assertEqual(robot.position, Point(2, 4, *CLAMP))
        robot.move()
        self.assertEqual(robot.position, Point(4, 1, *CLAMP))
        robot.move()
        self.assertEqual(robot.position, Point(6, 5, *CLAMP))
        robot.move()
        self.assertEqual(robot.position, Point(8, 2, *CLAMP))
        robot.move()
        self.assertEqual(robot.position, Point(10, 6, *CLAMP))
        robot.move()
        self.assertEqual(robot.position, Point(1, 3, *CLAMP))


class TestSpace(unittest.TestCase):
    def test_safety(self):
        SPACE.move(100)
        self.assertEqual(SPACE.safety(), 12)
