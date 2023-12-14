import numpy as np


class Maze:

    def __init__(self, tiles: np.array):
        self._tiles = tiles
        self._current_y, self._current_x = self._start_index()
        self._last_direction = None

    def solve(self) -> int:
        pass

    def _start_index(self):
        return np.argwhere(self._tiles == 'S')[0]


def load_data(filename: str) -> Maze:
    with open(filename, 'r') as file:
        data = []
        for line in file:
            data.append([tile for tile in line.strip()])
    return Maze(np.array(data))


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
