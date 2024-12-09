from utils import get_input, pairs

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def search_xmas(grid: str):
    size = grid.index("\n")

    return sum(
        # Check bounds
        0 <= x + 3 * dx < size and 0 <= y + 3 * dy < size
        # Check word match
        and "".join(grid[(size + 1) * (y + i * dy) + x + i * dx] for i in range(4))
        == "XMAS"
        for dx, dy in DIRECTIONS
        for x, y in pairs(range(size))
    )


def search_x_mas(grid: str):
    raise NotImplementedError()


if __name__ == "__main__":
    grid = get_input(4)
    print(search_xmas(grid))
    # print(search_x_mas(grid))
