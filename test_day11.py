# pylint-dev/pylint#9574
# pylint:disable=unsubscriptable-object
import unittest

from networkx import DiGraph

from day11 import parse_adjacency_dict, paths
from utils import clean_string

GRAPH: DiGraph[str] = DiGraph(parse_adjacency_dict(clean_string("""
    aaa: you hhh
    you: bbb ccc
    bbb: ddd eee
    ccc: ddd eee fff
    ddd: ggg
    eee: out
    fff: out
    ggg: out
    hhh: ccc fff iii
    iii: out
""")))


class TestDay11(unittest.TestCase):
    def test_paths(self):
        self.assertEqual(paths(GRAPH), 5)
