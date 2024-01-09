import numpy as np


DIRECTION_TO_VECTOR = {
    "U": np.array((-1, 0)),
    "R": np.array((0, 1)),
    "D": np.array((1, 0)),
    "L": np.array((0, -1)),
}

VECTOR_TO_DIRECTION = {tuple(value): key for key, value in DIRECTION_TO_VECTOR.items()}

class Instruction:
    def __init__(self, line: str):
        self.direction, self.distance, self.color = self._parse(line)

    def _parse(self, line: str) -> tuple[np.array, int, str]:
        direction, distance, color = line.split(" ")
        return DIRECTION_TO_VECTOR[direction], int(distance), color[1:-1]


class Instruction2:
    def __init__(self, line: str):
        self.direction = self._parse_direction(line)
        self.distance = self._parse_distance(line)

    def _parse_direction(self, line: str) -> np.array:
        direction = int(line.split(" ")[2][-2])
        _map = {0: "R",1: "D", 2: "L", 3: "U"}
        return DIRECTION_TO_VECTOR[_map[direction]]

    def _parse_distance(self, line):
        distance = line.split(" ")[2][2:-2]
        return int(distance, 16)


class Lagoon:
    def __init__(self, instructions: list[Instruction]):
        self._instructions = instructions

    def get_result(self) -> int:
        perimeter = self.polygon_perimeter()
        n_edges = len(self._instructions)
        straight_edges = perimeter - n_edges
        convex_edges = self.convex_edges()
        concave_edges = n_edges - convex_edges
        perimeter_area = 1 / 2 * straight_edges  + 3 / 4 * convex_edges + 1/ 4 * concave_edges
        return self.polygon_area() + int(perimeter_area)


    def _angle(self, v1, v2):
        """Return +/-1 for right/left turns."""
        _in = (*v1, 0)
        _out = (*v2, 0)
        return np.cross(_in, _out)[2]

    def vertices(self) -> list[np.array]:
        _yx = np.zeros(2)
        vertices = [np.zeros(2)]
        for instruction in self._instructions:
            _yx += instruction.distance * instruction.direction
            vertices.append(_yx.copy())
        return vertices

    def polygon_perimeter(self) -> int:
        return sum([instruction.distance for instruction in self._instructions])

    def polygon_area(self) -> int:
        points = self.vertices()
        n_points = len(points)
        p0 = points[0]
        area = 0
        for i in range(n_points - 1):
            v1 = points[i] - p0
            v2 = points[i+1] - p0
            cross = v1[0] * v2[1] - v1[1] * v2[0]
            area += cross
        return int(abs(area)/2)

    def convex_edges(self):
        left_edges = 0
        right_edges = 0
        rotation = 0
        n_instructions = len(self._instructions)
        for i in range(n_instructions):
            direction = self._instructions[i].direction
            previous_direction = self._instructions[i-1].direction
            angle = self._angle(direction, previous_direction)
            rotation += angle
            left_edges += angle < 0
            right_edges += angle > 0
        return left_edges if rotation < 0 else right_edges


def load_data(filename):
    with open(filename, "r") as file:
        return [Instruction(line.strip()) for line in file]


def load_data_2(filename):
    with open(filename, "r") as file:
        return [Instruction2(line.strip()) for line in file]


def get_result(instructions):
    return Lagoon(instructions).get_result()


def get_result_2(instructions):
    return Lagoon(instructions).get_result()


def main():
    print(get_result(load_data("data.txt")))
    print(get_result_2(load_data_2("data.txt")))


if __name__ == '__main__':
    main()
