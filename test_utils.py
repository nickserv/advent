import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import utils


class TestUtils(unittest.TestCase):
    def test_clean_string(self):
        self.assertEqual(utils.clean_string("  hello world  "), "hello world")
        self.assertEqual(utils.clean_string("  \n  hello  \n  "), "hello")
        self.assertEqual(
            utils.clean_string("\n    indented\n    text\n"), "indented\ntext"
        )

    def test_parse_id_range(self):
        self.assertEqual(utils.parse_id_range("1-5"), range(1, 6))
        self.assertEqual(utils.parse_id_range("10-12"), range(10, 13))
        self.assertEqual(utils.parse_id_range("5-5"), range(5, 6))

    def test_parse_lines(self):
        self.assertEqual(utils.parse_lines(int, "1\n2\n3"), [1, 2, 3])
        self.assertEqual(
            utils.parse_lines(str.upper, "hello\nworld"), ["HELLO", "WORLD"]
        )

    def test_read_input(self):
        with TemporaryDirectory() as tmpdir:
            resources_dir = Path(tmpdir) / "resources"
            resources_dir.mkdir()
            test_file = resources_dir / "1.txt"
            test_file.write_text("test content", "utf8")

            # Temporarily change working directory for this test
            original_cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                content = utils.read_input(1)
                self.assertEqual(content, "test content")
            finally:
                os.chdir(original_cwd)


class TestPoint(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(utils.Point.parse("1,2"), utils.Point(1, 2))

    def test_parse_many(self):
        self.assertEqual(
            utils.Point.parse_many("1,2\n3,4"), [utils.Point(1, 2), utils.Point(3, 4)]
        )

    def test_add(self):
        self.assertEqual(utils.Point(1, 2) + utils.Point(3, 4), utils.Point(4, 6))

    def test_mod(self):
        self.assertEqual(utils.Point(2, 3) % utils.Point(2, 2), utils.Point(0, 1))

    def test_mul(self):
        self.assertEqual(utils.Point(1, 2) * 2, utils.Point(2, 4))

    def test_rmul(self):
        self.assertEqual(2 * utils.Point(1, 2), utils.Point(2, 4))

    def test_str(self):
        self.assertEqual(str(utils.Point(1, 2)), "1,2")


GRID = utils.Grid(range(4))


class TestGrid(unittest.TestCase):
    def test_index(self):
        self.assertEqual(GRID.index(utils.Point(0, 0)), 0)
        self.assertEqual(GRID.index(utils.Point(1, 0)), 1)
        self.assertEqual(GRID.index(utils.Point(0, 1)), 2)
        self.assertEqual(GRID.index(utils.Point(1, 1)), 3)

    def test_point(self):
        self.assertEqual(GRID.point(0), utils.Point(0, 0))
        self.assertEqual(GRID.point(1), utils.Point(1, 0))
        self.assertEqual(GRID.point(2), utils.Point(0, 1))
        self.assertEqual(GRID.point(3), utils.Point(1, 1))

    def test_neighbors(self):
        with self.subTest(key=utils.Point):
            self.assertCountEqual(
                list(GRID.neighbors(utils.Point(0, 0))),
                [utils.Point(0, 1), utils.Point(1, 0)],
            )
            self.assertCountEqual(
                list(GRID.neighbors(utils.Point(1, 0))),
                [utils.Point(0, 0), utils.Point(1, 1)],
            )
            self.assertCountEqual(
                list(GRID.neighbors(utils.Point(0, 1))),
                [utils.Point(0, 0), utils.Point(1, 1)],
            )
            self.assertCountEqual(
                list(GRID.neighbors(utils.Point(1, 1))),
                [utils.Point(0, 1), utils.Point(1, 0)],
            )

        with self.subTest(key=int):
            self.assertCountEqual(list(GRID.neighbors(0)), [1, 2])
            self.assertCountEqual(list(GRID.neighbors(1)), [0, 3])
            self.assertCountEqual(list(GRID.neighbors(2)), [0, 3])
            self.assertCountEqual(list(GRID.neighbors(3)), [1, 2])

    def test_visualize(self):
        self.assertEqual(GRID.visualize(set()), "01\n23")
        self.assertEqual(GRID.visualize(set(GRID)), "XX\nXX")

    def test_contains(self):
        self.assertIn(utils.Point(0, 0), GRID)
        self.assertIn(utils.Point(1, 1), GRID)
        self.assertNotIn(utils.Point(-1, 0), GRID)
        self.assertNotIn(utils.Point(0, -1), GRID)
        self.assertNotIn(utils.Point(2, 0), GRID)
        self.assertNotIn(utils.Point(0, 2), GRID)

    def test_eq(self):
        self.assertEqual(utils.Grid(range(4)), utils.Grid(range(4)))

    def test_getitem(self):
        with self.subTest(key=utils.Point):
            self.assertEqual(GRID[utils.Point(0, 0)], 0)
            self.assertEqual(GRID[utils.Point(1, 0)], 1)
            self.assertEqual(GRID[utils.Point(0, 1)], 2)
            self.assertEqual(GRID[utils.Point(1, 1)], 3)

        with self.subTest(key=int):
            self.assertEqual(GRID[0], 0)
            self.assertEqual(GRID[1], 1)
            self.assertEqual(GRID[2], 2)
            self.assertEqual(GRID[3], 3)

    def test_iter(self):
        self.assertEqual(
            list(GRID),
            [
                utils.Point(0, 0),
                utils.Point(1, 0),
                utils.Point(0, 1),
                utils.Point(1, 1),
            ],
        )

    def test_len(self):
        self.assertEqual(len(GRID), 2)

    def test_str(self):
        self.assertEqual(str(GRID), "01\n23")


class TestStringGrid(unittest.TestCase):
    def test_new(self):
        self.assertEqual(utils.StringGrid("ab\ncd"), utils.Grid(iter("abcd")))
