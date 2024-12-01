import unittest

from day13 import parse_pattern, reflect


class Test(unittest.TestCase):
    def test_reflect(self):
        pattern = parse_pattern(
            """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
            """.strip()
        )
        self.assertEqual(reflect(pattern), 5)

        pattern = parse_pattern(
            """
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
            """.strip()
        )
        self.assertEqual(reflect(pattern), 400)
