import unittest

from networkx import Graph

from day23 import largest_maximal_clique, parse_edges, password, triple_cliques
from utils import get_input

GRAPH = Graph(
    parse_edges(
        get_input(
            """
            kh-tc
            qp-kh
            de-cg
            ka-co
            yn-aq
            qp-ub
            cg-tb
            vc-aq
            tb-ka
            wh-tc
            yn-cg
            kh-ub
            ta-co
            de-co
            tc-td
            tb-wq
            wh-td
            ta-ka
            td-qp
            aq-cg
            wq-ub
            ub-vc
            de-ta
            wq-aq
            wq-vc
            wh-yn
            ka-de
            kh-ta
            co-tc
            wh-qp
            tb-vc
            td-yn
            """
        )
    )
)


class TestDay23(unittest.TestCase):
    def test_triple_cliques(self):
        self.assertCountEqual(
            [set(clique) for clique in triple_cliques(GRAPH)],
            [
                {"co", "de", "ta"},
                {"co", "ka", "ta"},
                {"de", "ka", "ta"},
                {"qp", "td", "wh"},
                {"tb", "vc", "wq"},
                {"tc", "td", "wh"},
                {"td", "wh", "yn"},
            ],
        )

    def largest_maximal_clique(self):
        self.assertCountEqual(largest_maximal_clique(GRAPH), ["co", "de", "ka", "ta"])

    def test_password(self):
        self.assertEqual(password(GRAPH), "co,de,ka,ta")
