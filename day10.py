from collections import deque
from typing import Callable, Self

from utils import Grid, get_input


class TopMap(Grid[int]):
    def __init__(self, string: str):
        super().__init__(int(char) for char in string if char != "\n")

    def trailheads(self):
        return (index for index, value in enumerate(self._items) if value == 0)

    def neighbors(self, position: int):
        width = len(self)
        if position >= width:
            yield position - width
        if position % width != 0:
            yield position - 1
        if position % width != width - 1:
            yield position + 1
        if position < len(self._items) - width:
            yield position + width

    def reachable(self, trailhead: int):
        visited = {trailhead}
        queue = deque([trailhead])
        while queue:
            current = queue.popleft()
            if self._items[current] == 9:
                yield current
            for neighbor in self.neighbors(current):
                if (
                    self._items[neighbor] == self._items[current] + 1
                    and neighbor not in visited
                ):
                    visited.add(neighbor)
                    queue.append(neighbor)

    def score(self, trailhead: int):
        return len(list(self.reachable(trailhead)))

    def rating(self, trailhead: int):
        trails = 0
        queue = deque([trailhead])
        while queue:
            current = queue.popleft()
            if self._items[current] == 9:
                trails += 1
            for neighbor in self.neighbors(current):
                if self._items[neighbor] == self._items[current] + 1:
                    queue.append(neighbor)
        return trails

    def all(self, strategy: Callable[[Self, int], int]):
        return (strategy(self, trailhead) for trailhead in self.trailheads())


if __name__ == "__main__":
    top_map = TopMap(get_input(10))
    print(sum(top_map.all(TopMap.score)))
    print(sum(top_map.all(TopMap.rating)))
