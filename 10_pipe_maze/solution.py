from timeit import timeit

import numpy as np

TILES = {
    '-': ("left", "right"),
    '|': ("up", "down"),
    'F': ("down", "right"),
    'L': ("up", "right"),
    'J': ("up", "left"),
    '7': ("down", "left"),
}

DIRECTION_TO_YX = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
YX_TO_DIRECTION = {value: key for key, value in DIRECTION_TO_YX.items()}


class Maze:

    def __init__(self, tiles: np.array):
        self._tiles = tiles
        self._current_y, self._current_x = self._start_index()
        self._last_direction = None

        self._main_loop_tiles = self._find_main_loop_tiles()

    def count_loop_tiles(self) -> int:
        c = 0
        symbols = ['S', *list(TILES.keys())]
        for symbol in symbols:
            c += np.count_nonzero(self._main_loop_tiles == symbol.encode())
        return c

    def _find_main_loop_tiles(self):
        """Walk through the main loop."""
        _main_loop_tiles = np.zeros(self._tiles.shape, dtype='S1')
        self._move_from_start()
        _main_loop_tiles[self._current_y, self._current_x] = self._current_tile()
        while not all((self._current_y, self._current_x) == self._start_index()):
            self._move_to_next_tile()
            _main_loop_tiles[self._current_y, self._current_x] = self._current_tile()
        return _main_loop_tiles

    def _move_to_next_tile(self):
        _in_direction = tuple(- np.array(self._last_direction))
        _out_direction = [direction for direction in TILES[self._current_tile()]
                          if direction != YX_TO_DIRECTION[_in_direction]][0]
        _y, _x = DIRECTION_TO_YX[_out_direction]
        self._update_position(_y, _x)

    def _update_position(self, _y, _x):
        self._current_y += _y
        self._current_x += _x
        self._last_direction = (_y, _x)

    def _neighboring_tile(self, _y, _x):
        return self._tiles[self._current_y + _y, self._current_x + _x]

    def _current_tile(self) -> str:
        return self._tiles[self._current_y, self._current_x]

    def _start_index(self):
        return np.argwhere(self._tiles == 'S')[0]

    def _move_from_start(self):
        for _y, _x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if not 0 <= self._current_y + _y < self._tiles.shape[0]:
                continue
            if not 0 <= self._current_x + _x < self._tiles.shape[1]:
                continue
            if _y == 1 and self._neighboring_tile(_y, _x) in ['|', 'J', 'L']:
                self._update_position(_y, _x)
                return
            if _x == 1 and self._neighboring_tile(_y, _x) in ['-', 'J', '7']:
                self._update_position(_y, _x)
                return
            if _y == -1 and self._neighboring_tile(_y, _x) in ['|', '7', 'F']:
                self._update_position(_y, _x)
                return
            if _x == -1 and self._neighboring_tile(_y, _x) in ['-', 'F', 'L']:
                self._update_position(_y, _x)
                return


def load_data(filename: str) -> Maze:
    with open(filename, 'r') as file:
        data = []
        for line in file:
            data.append([tile for tile in line.strip()])
    return Maze(np.array(data))


def get_result(maze):
    return int(maze.count_loop_tiles() / 2)


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    print(timeit(main, number=1))
