from typing import Generator

from utils import DIRECTIONS, Point, StringGrid, get_input


class WordSearch(StringGrid):
    def __extract(self, point: Point, direction: Point):
        i = 0
        result = ""

        # Check bounds
        while self.valid(current := point + i * direction):
            result += self[current]
            i += 1

        return result

    def search_xmas(self):
        return (
            point
            for direction in DIRECTIONS
            for point in self.points()
            if self.__extract(point, direction).startswith("XMAS")
        )

    def search_x_mas(self) -> Generator[Point]:
        raise NotImplementedError()


if __name__ == "__main__":
    word_search = WordSearch(get_input(4))
    print(len(list(word_search.search_xmas())))
    # print(len(list(word_search.search_x_mas())))
