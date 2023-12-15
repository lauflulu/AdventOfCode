import numpy as np


class Maze:

    def __init__(self, tiles: np.array):
        self._tiles = tiles
        self._current_y, self._current_x = self._start_index()
        self._last_direction = None

    def count_loop_tiles(self) -> int:
        c = 0
        self.move()
        while not all((self._current_y, self._current_x) == self._start_index()):
            c += 1
            self.move()
        return c

    def move(self):
        for _y, _x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if self._last_direction == (-_y, -_x):
                continue
            if not 0 <= self._current_y + _y < self._tiles.shape[0]:
                continue
            if not 0 <= self._current_x + _x < self._tiles.shape[1]:
                continue
            if (_y == 1 and self._current_tile() in ['|', 'F', '7', 'S']
                    and self._tiles[self._current_y + _y, self._current_x] in ['|', 'J', 'L', 'S']):
                self._current_y += _y
                self._last_direction = (_y, 0)
                return
            if (_x == 1 and self._current_tile() in ['-', 'F', 'L', 'S']
                    and self._tiles[self._current_y, self._current_x + _x] in ['-', 'J', '7', 'S']):
                self._current_x += _x
                self._last_direction = (0, _x)
                return
            if (_y == -1 and self._current_tile() in ['|', 'L', 'J', 'S']
                    and self._tiles[self._current_y + _y, self._current_x] in ['|', '7', 'F', 'S']):
                self._current_y += _y
                self._last_direction = (_y, 0)
                return
            if (_x == -1 and self._current_tile() in ['-', 'J', '7', 'S']
                    and self._tiles[self._current_y, self._current_x + _x] in ['-', 'F', 'L', 'S']):
                self._current_x += _x
                self._last_direction = (0, _x)
                return

    def _current_tile(self) -> str:
        return self._tiles[self._current_y, self._current_x]

    def _start_index(self):
        return np.argwhere(self._tiles == 'S')[0]


def load_data(filename: str) -> Maze:
    with open(filename, 'r') as file:
        data = []
        for line in file:
            data.append([tile for tile in line.strip()])
    return Maze(np.array(data))


def get_result(maze):
    return int(maze.count_loop_tiles()/2 + 1)


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
