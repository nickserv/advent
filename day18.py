from collections import deque
from collections.abc import Iterable

from utils import Grid, Point, get_input


class Space(Grid[bool]):
    def __init__(
        self,
        size: int,
        points: Iterable[Point] = iter(
            ()
        ),  # type:ignore[reportCallInDefaultInitializer]
    ):
        super().__init__([False] * size**2)
        for point in points:
            self[point] = True

    def shortest_path(self):
        origin = Point(0, 0)
        destination = Point(len(self) - 1, len(self) - 1)
        visited = {origin}
        queue = deque([origin])
        dist = {origin: 0}
        while queue:
            current = queue.popleft()
            for neighbor in self.neighbors(current):
                if (
                    not self[neighbor]
                    and neighbor not in visited
                    and neighbor not in dist
                ):
                    visited.add(neighbor)
                    queue.append(neighbor)
                    dist[neighbor] = dist[current] + 1
        return dist[destination]

    def search(self, points: list[Point]):
        for point in points:
            self[point] = True
            try:
                self.shortest_path()
            except KeyError:
                return point
        return None


if __name__ == "__main__":
    points = Point.parse_many(get_input(18))
    print(Space(71, points[:1024]).shortest_path())
    print(Space(71).search(points))
