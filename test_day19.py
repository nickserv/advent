import unittest

from day19 import parse_part, parse_workflows, sum_valid, valid

WORKFLOWS = parse_workflows(
    """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}
    """.strip()
)
print(WORKFLOWS)

PARTS = [
    parse_part(line)
    for line in """
{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
    """.strip().splitlines()
]


class Test(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(valid(WORKFLOWS, PARTS[0]))
        self.assertFalse(valid(WORKFLOWS, PARTS[1]))
        self.assertTrue(valid(WORKFLOWS, PARTS[2]))
        self.assertFalse(valid(WORKFLOWS, PARTS[3]))
        self.assertTrue(valid(WORKFLOWS, PARTS[4]))

    def test_sum_valid(self):
        self.assertEqual(sum_valid(WORKFLOWS, PARTS), 19114)
