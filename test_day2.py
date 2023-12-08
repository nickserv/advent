import unittest

from day2 import parse_game, possible, power, sum_possible, sum_powers

GAMES = [
    parse_game(line)
    for line in """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """.strip().splitlines()
]


class Test(unittest.TestCase):
    def test_possible(self):
        self.assertTrue(possible(GAMES[0]))
        self.assertTrue(possible(GAMES[1]))
        self.assertFalse(possible(GAMES[2]))
        self.assertFalse(possible(GAMES[3]))
        self.assertTrue(possible(GAMES[4]))

    def test_sum_possible(self):
        self.assertEqual(sum_possible(GAMES), 8)

    def test_power(self):
        self.assertEqual(power(GAMES[0]), 48)
        self.assertEqual(power(GAMES[1]), 12)
        self.assertEqual(power(GAMES[2]), 1560)
        self.assertEqual(power(GAMES[3]), 630)
        self.assertEqual(power(GAMES[4]), 36)

    def test_sum_powers(self):
        self.assertEqual(sum_powers(GAMES), 2286)
