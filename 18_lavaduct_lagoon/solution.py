import numpy as np


DIRECTION_TO_VECTOR = {
    "L": np.array((0, -1)),
    "R": np.array((0, 1)),
    "U": np.array((-1, 0)),
    "D": np.array((1, 0))}


class Instruction:
    def __init__(self, line: str):
        self.direction, self.distance, self.color = self._parse(line)

    def _parse(self, line: str) -> tuple[np.array, int, str]:
        direction, distance, color = line.split(" ")
        return DIRECTION_TO_VECTOR[direction], int(distance), color[1:-1]



class Lagoon:
    def __init__(self, instructions: list[Instruction]):
        self._instructions = instructions
        self.shape = (0, 0)
        self.start = (0, 0)
        self.rotation = 0
        self._yx = np.array((0, 0))
        self._precalculate_grid()

        self._grid = np.char.add(np.zeros(self.shape, dtype='U1'), '.')

    def get_result(self) -> int:
        self.dig_outline()
        self.dig_inner()
        return self.volume()

    def _precalculate_grid(self):
        min_y, min_x, max_y, max_x = (0, 0, 0, 0)
        _previous_direction = np.zeros(2)
        for instruction in self._instructions:
            self._yx += instruction.distance * instruction.direction
            min_y = min(min_y, int(self._yx[0]))
            min_x = min(min_x, int(self._yx[1]))
            max_y = max(max_y, int(self._yx[0]))
            max_x = max(max_x, int(self._yx[1]))
            self.rotation += self._angle(instruction.direction, _previous_direction)
            _previous_direction = instruction.direction
        self.shape = (max_y - min_y + 1, max_x - min_x + 1)
        self.start = (-min_y, -min_x)

    def _angle(self, v1, v2):
        """Return +/-1 for right/left turns."""
        _in = (*v1, 0)
        _out = (*v2, 0)
        return np.cross(_in, _out)[2]

    def dig_outline(self):
        self._yx = np.array(self.start)
        for instruction in self._instructions:
            for _ in range(instruction.distance):
                self._yx += instruction.direction
                self._grid[*self._yx] = "#"

    def volume(self) -> int:
        return np.count_nonzero(self._grid == '#')


def load_data(filename):
    with open(filename, "r") as file:
        return [Instruction(line.strip()) for line in file]


def get_result(data):
    pass


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
