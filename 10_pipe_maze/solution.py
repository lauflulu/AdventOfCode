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
DIRECTIONS_TO_TILE = {value: key for key, value in TILES.items()}

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
        self._loop_direction = 0

        self._main_loop_tiles = self._find_main_loop_tiles()

        self._inner_outer_tiles = self._main_loop_tiles.copy()
        self._mark_inner_outer_tiles()
        self._fill_areas()

    def count_loop_tiles(self) -> int:
        c = 0
        symbols = ['S', *list(TILES.keys())]
        for symbol in symbols:
            c += np.count_nonzero(self._main_loop_tiles == symbol)
        return c

    def count_inner_tiles(self) -> int:
        return np.count_nonzero(self._inner_outer_tiles == 'I')

    def _mark_inner_outer_tiles(self):
        self._current_y, self._current_x = self._start_index()
        self._mark_neighbors()
        self._last_direction = [DIRECTION_TO_YX[direction] for direction in TILES[self._current_tile()]
                                if direction != YX_TO_DIRECTION[self._start_direction()]][0]
        self._move_to_next_tile()
        while not all((self._current_y, self._current_x) == self._start_index()):
            self._mark_neighbors()
            self._move_to_next_tile()

    def _fill_areas(self):
        for y in range(self._tiles.shape[0]):
            for x in range(self._tiles.shape[1]):
                if self._inner_outer_tiles[y, x] == '.':
                    self._update_tile_based_on_neighbors(y, x)

    def _update_tile_based_on_neighbors(self, y, x):
        directions = ['left', 'up', 'right', 'down']
        for direction in directions:
            _y, _x = DIRECTION_TO_YX[direction]
            neighboring_tile = self._inner_outer_tiles[y + _y, x + _x]
            if neighboring_tile in ['I', 'O']:
                self._inner_outer_tiles[y, x] = neighboring_tile
                return

    def _mark_neighbors(self):
        if self._loop_direction < 0:
            side = 'I'
        else:
            side = 'O'
        start_direction = YX_TO_DIRECTION[self._current_in_direction()]
        out_direction = self._current_out_direction()
        directions_clockwise = ['up', 'right', 'down', 'left']
        start_index = directions_clockwise.index(start_direction)
        for i in range(4):
            direction = directions_clockwise[(i + start_index) % 4]
            _y, _x = DIRECTION_TO_YX[direction]
            if direction == out_direction:
                if self._loop_direction < 0:
                    side = 'O'
                else:
                    side = 'I'
            if self._get_inner_outer_tile(self._current_y + _y, self._current_x + _x) == '.':
                self._set_inner_outer_tile(self._current_y + _y, self._current_x + _x, side)

    def _set_inner_outer_tile(self, y, x, side):
        if self._index_outside_bounds(x, y):
            return
        self._inner_outer_tiles[y, x] = side

    def _get_inner_outer_tile(self, y, x):
        if self._index_outside_bounds(x, y):
            return
        return self._inner_outer_tiles[y, x]

    def _index_outside_bounds(self, x, y):
        return not 0 <= y < self._tiles.shape[0] or not 0 <= x < self._tiles.shape[1]

    def _find_main_loop_tiles(self):
        """Walk through the main loop."""
        _main_loop_tiles = np.char.add(np.zeros(self._tiles.shape, dtype='<U1'), '.')
        self._last_direction = [DIRECTION_TO_YX[direction] for direction in TILES[self._current_tile()]
                                if direction != YX_TO_DIRECTION[self._start_direction()]][0]
        self._move_to_next_tile()
        _main_loop_tiles[self._current_y, self._current_x] = self._current_tile()
        while not all((self._current_y, self._current_x) == self._start_index()):
            self._move_to_next_tile()
            _main_loop_tiles[self._current_y, self._current_x] = self._current_tile()
        return _main_loop_tiles

    def _move_to_next_tile(self):
        _in_direction = self._current_in_direction()
        _out_direction = DIRECTION_TO_YX[self._current_out_direction()]
        self._loop_direction += self._angle_score(_in_direction, _out_direction)
        _y, _x = _out_direction
        self._update_position(_y, _x)

    def _angle_score(self, _in_direction, _out_direction):
        _in = (*_in_direction, 0)
        _out = (*_out_direction, 0)
        return np.cross(_in, _out)[2]

    def _current_out_direction(self):
        return [direction for direction in TILES[self._current_tile()]
                if direction != YX_TO_DIRECTION[self._current_in_direction()]][0]

    def _current_in_direction(self):
        return tuple(- np.array(self._last_direction))

    def _update_position(self, _y, _x):
        self._current_y += _y
        self._current_x += _x
        self._last_direction = (_y, _x)

    def _neighboring_tile(self, _y, _x):
        return self._tiles[self._current_y + _y, self._current_x + _x]

    def _current_tile(self) -> str:
        tile = self._tiles[self._current_y, self._current_x]
        if tile == 'S':
            tile = self._identify_start_tile()
        return tile

    def _start_index(self):
        return np.argwhere(self._tiles == 'S')[0]

    def _start_direction(self):
        for _y, _x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if _y == 1 and self._neighboring_tile(_y, _x) in ['|', 'J', 'L']:
                return _y, _x
            if _x == 1 and self._neighboring_tile(_y, _x) in ['-', 'J', '7']:
                return _y, _x
            if _y == -1 and self._neighboring_tile(_y, _x) in ['|', '7', 'F']:
                return _y, _x
            if _x == -1 and self._neighboring_tile(_y, _x) in ['-', 'F', 'L']:
                return _y, _x

    def _identify_start_tile(self):
        directions = []
        for direction, _yx in DIRECTION_TO_YX.items():
            neighboring_tile = self._neighboring_tile(*_yx)
            if neighboring_tile not in TILES:
                continue
            if direction == 'down' and 'up' in TILES[neighboring_tile]:
                directions.append('down')
            if direction == 'up' and 'down' in TILES[neighboring_tile]:
                directions.append('up')
            if direction == 'left' and 'right' in TILES[neighboring_tile]:
                directions.append('left')
            if direction == 'right' and 'left' in TILES[neighboring_tile]:
                directions.append('right')
        return DIRECTIONS_TO_TILE[tuple(directions)]


def load_data(filename: str) -> Maze:
    with open(filename, 'r') as file:
        data = []
        for line in file:
            data.append([tile for tile in line.strip()])
    return Maze(np.array(data))


def get_result(maze):
    return int(maze.count_loop_tiles() / 2)


def get_result_2(maze):
    return maze.count_inner_tiles()


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    print(timeit(main, number=1))
