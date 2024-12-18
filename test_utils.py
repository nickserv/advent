import unittest

from utils import Grid, Point, StringGrid


class TestPoint(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(Point.parse("1,2"), Point(1, 2))

    def test_parse_many(self):
        self.assertEqual(Point.parse_many("1,2\n3,4"), [Point(1, 2), Point(3, 4)])

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * 2, Point(2, 4))

    def test_rmul(self):
        self.assertEqual(2 * Point(1, 2), Point(2, 4))

    def test_str(self):
        self.assertEqual(str(Point(1, 2)), "1,2")


GRID = Grid(range(4))


class TestGrid(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Grid(range(4)), Grid(range(4)))

    def test_getitem(self):
        with self.subTest(key=Point):
            self.assertEqual(GRID[Point(0, 0)], 0)
            self.assertEqual(GRID[Point(1, 0)], 1)
            self.assertEqual(GRID[Point(0, 1)], 2)
            self.assertEqual(GRID[Point(1, 1)], 3)
        with self.subTest(key=int):
            self.assertEqual(GRID[0], 0)
            self.assertEqual(GRID[1], 1)
            self.assertEqual(GRID[2], 2)
            self.assertEqual(GRID[3], 3)

    def test_len(self):
        self.assertEqual(len(GRID), 2)

    def test_str(self):
        self.assertEqual(str(GRID), "01\n23")

    def test_index(self):
        self.assertEqual(GRID.index(Point(0, 0)), 0)
        self.assertEqual(GRID.index(Point(1, 0)), 1)
        self.assertEqual(GRID.index(Point(0, 1)), 2)
        self.assertEqual(GRID.index(Point(1, 1)), 3)

    def test_point(self):
        self.assertEqual(GRID.point(0), Point(0, 0))
        self.assertEqual(GRID.point(1), Point(1, 0))
        self.assertEqual(GRID.point(2), Point(0, 1))
        self.assertEqual(GRID.point(3), Point(1, 1))

    def test_points(self):
        self.assertEqual(
            list(GRID.points()), [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]
        )

    def test_neighbors(self):
        with self.subTest(key=Point):
            self.assertCountEqual(
                list(GRID.neighbors(Point(0, 0))), [Point(0, 1), Point(1, 0)]
            )
            self.assertCountEqual(
                list(GRID.neighbors(Point(1, 0))), [Point(0, 0), Point(1, 1)]
            )
            self.assertCountEqual(
                list(GRID.neighbors(Point(0, 1))), [Point(0, 0), Point(1, 1)]
            )
            self.assertCountEqual(
                list(GRID.neighbors(Point(1, 1))), [Point(0, 1), Point(1, 0)]
            )
        with self.subTest(key=int):
            self.assertCountEqual(list(GRID.neighbors(0)), [1, 2])
            self.assertCountEqual(list(GRID.neighbors(1)), [0, 3])
            self.assertCountEqual(list(GRID.neighbors(2)), [0, 3])
            self.assertCountEqual(list(GRID.neighbors(3)), [1, 2])

    def test_valid(self):
        self.assertTrue(GRID.valid(Point(0, 0)))
        self.assertTrue(GRID.valid(Point(1, 1)))
        self.assertFalse(GRID.valid(Point(-1, 0)))
        self.assertFalse(GRID.valid(Point(0, -1)))
        self.assertFalse(GRID.valid(Point(2, 0)))
        self.assertFalse(GRID.valid(Point(0, 2)))

    def test_visualize(self):
        self.assertEqual(GRID.visualize(set()), "01\n23")
        self.assertEqual(GRID.visualize(set(GRID.points())), "XX\nXX")


class TestStringGrid(unittest.TestCase):
    def test_new(self):
        self.assertEqual(StringGrid("ab\ncd"), Grid(iter("abcd")))
