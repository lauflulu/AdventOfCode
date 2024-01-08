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
        self.shape = (None, None)
        self.start = (None, None)
        self._yx = np.array((0, 0))
        self._precalculate_grid()


    def get_result(self) -> int:
        pass

    def _precalculate_grid(self):
        min_y, min_x, max_y, max_x = (0, 0, 0, 0)
        for instruction in self._instructions:
            self._yx += instruction.distance * instruction.direction
            min_y = min(min_y, int(self._yx[0]))
            min_x = min(min_x, int(self._yx[1]))
            max_y = max(max_y, int(self._yx[0]))
            max_x = max(max_x, int(self._yx[1]))
        self.shape = (max_y - min_y + 1, max_x - min_x + 1)
        self.start = (-min_y, -min_x)

    def dig_outline(self):
        pass

    def volume(self) -> int:
        pass


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
