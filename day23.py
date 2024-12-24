# pylint-dev/pylint#9574
# pylint:disable=unsubscriptable-object
from __future__ import annotations

from networkx import Graph, enumerate_all_cliques, find_cliques

from utils import get_input


def triple_cliques(graph: Graph[str]):
    for clique in enumerate_all_cliques(graph):
        if len(clique) == 3 and any(s.startswith("t") for s in clique):
            yield clique


def largest_maximal_clique(graph: Graph[str]):
    return max(find_cliques(graph), key=len)


def password(graph: Graph[str]):
    return ",".join(sorted(largest_maximal_clique(graph)))


def parse_edge(string: str):
    first, _, second = string.partition("-")
    return first, second


def parse_edges(string: str):
    return (parse_edge(line) for line in string.splitlines())


if __name__ == "__main__":
    graph = Graph(parse_edges(get_input(23)))
    print(len(list(triple_cliques(graph))))
    print(",".join(sorted(largest_maximal_clique(graph))))
