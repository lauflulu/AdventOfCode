import numpy as np


class Maze:

    def __init__(self, tiles: np.array):
        self._tiles = tiles
        self._current_x = 0
        self._current_y = 0
        self._last_direction = None

    def solve(self) -> int:
        pass


def load_data(filename: str) -> Maze:
    pass


def get_result(maze):
    return maze.solve()


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
