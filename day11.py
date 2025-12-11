# pylint-dev/pylint#9574
# pylint:disable=unsubscriptable-object
from networkx import DiGraph, all_simple_paths

from utils import parse_lines, read_input


def paths(graph: DiGraph[str]):
    return len(list(all_simple_paths(graph, "you", "out")))


def parse_adjacency(string: str):
    origin, _, rest = string.partition(":")
    return origin, tuple(rest.split())


def parse_adjacency_dict(string: str):
    return dict(parse_lines(parse_adjacency, string))


if __name__ == "__main__":
    graph: DiGraph[str] = DiGraph(parse_adjacency_dict(read_input(11)))
    print(paths(graph))
