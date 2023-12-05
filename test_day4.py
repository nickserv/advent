import unittest


from day4 import Card


CARDS = [
    Card(line)
    for line in """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip().splitlines()
]


class Test(unittest.TestCase):
    def test_init(self):
        self.assertEqual(CARDS[0].winning, {41, 48, 83, 86, 17})
        self.assertEqual(CARDS[0].have, {83, 86, 6, 31, 17, 9, 48, 53})

    def test_points(self):
        self.assertEqual(CARDS[0].points(), 8)
        self.assertEqual(CARDS[1].points(), 2)
        self.assertEqual(CARDS[2].points(), 2)
        self.assertEqual(CARDS[3].points(), 1)
        self.assertEqual(CARDS[4].points(), 0)
        self.assertEqual(CARDS[5].points(), 0)

    def test_sum(self):
        self.assertEqual(Card.sum(CARDS), 13)
