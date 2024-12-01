import unittest

from day5 import lookup, lookup_many, parse

seeds, maps = parse(
    """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
)


class Test(unittest.TestCase):
    def test_lookup(self):
        self.assertEqual(lookup(maps[0], 79), 81)
        self.assertEqual(lookup(maps[0], 14), 14)
        self.assertEqual(lookup(maps[0], 55), 57)
        self.assertEqual(lookup(maps[0], 13), 13)

    def test_locations(self):
        self.assertEqual(lookup_many(maps, 79), 82)
        self.assertEqual(lookup_many(maps, 14), 43)
        self.assertEqual(lookup_many(maps, 55), 86)
        self.assertEqual(lookup_many(maps, 13), 35)
