from itertools import cycle

from utils import STRAIGHTS, StringGrid, get_input


class Lab(StringGrid):
    def path(self):
        it = cycle(STRAIGHTS)
        direction = next(it)
        point = self.start()
        path = {point}

        while point + direction in self:
            if self[point + direction] == "#":
                direction = next(it)
            else:
                point += direction
                path.add(point)

        return path

    def start(self):
        return self.point(self._items.index("^"))


if __name__ == "__main__":
    lab = Lab(get_input(6))
    print(len(lab.path()))
