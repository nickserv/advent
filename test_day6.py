import unittest

from day6 import displacement, parse_race, parse_races, product_solutions, solutions

INPUT = """
Time:      7  15   30
Distance:  9  40  200        
""".strip()


class Test(unittest.TestCase):
    def test_displacement(self):
        self.assertEqual(displacement(0, 7), 0)
        self.assertEqual(displacement(1, 7), 6)
        self.assertEqual(displacement(2, 7), 10)
        self.assertEqual(displacement(3, 7), 12)
        self.assertEqual(displacement(4, 7), 12)
        self.assertEqual(displacement(5, 7), 10)
        self.assertEqual(displacement(6, 7), 6)
        self.assertEqual(displacement(7, 7), 0)

    def test_solutions(self):
        self.assertEqual(solutions(7, 9), 4)
        self.assertEqual(solutions(15, 40), 8)
        self.assertEqual(solutions(30, 200), 9)
        self.assertEqual(solutions(*parse_race(INPUT)), 71503)

    def test_product_solutions(self):
        self.assertEqual(product_solutions(parse_races(INPUT)), 288)
