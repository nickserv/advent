import unittest

from day8 import complex_steps, parse, steps


class Test(unittest.TestCase):
    def test_steps(self):
        instructions, network = parse(
            """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
            """.strip()
        )
        self.assertEqual(steps(instructions, network), 2)
        instructions, network = parse(
            """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
            """.strip()
        )
        self.assertEqual(steps(instructions, network), 6)

    def test_complex_steps(self):
        instructions, network = parse(
            """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
            """.strip()
        )
        self.assertEqual(complex_steps(instructions, network), 6)
