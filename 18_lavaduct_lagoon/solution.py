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
        perimeter = self.polygon_perimeter()
        n_edges = len(self._instructions)
        perimeter_area = (perimeter - n_edges) / 2 + ((3 -1) * self.convex_edges() + n_edges) / 4
        return self.polygon_area() + int(perimeter_area)

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
        n_instructions = len(self._instructions)
        for i in range(n_instructions):
            distance = self._instructions[i].distance
            for d in range(distance):
                self._grid[*self._yx] = "#"
                in_direction = self._instructions[i].direction if d > 0 else self._instructions[i-1].direction
                out_direction = self._instructions[i].direction
                self._mark_inner(in_direction, out_direction)
                self._yx += self._instructions[i].direction

    def _mark_inner(self, in_direction, out_direction):
        side = 'I' if self.rotation < 0 else 'O'
        directions_clockwise = ['U', 'R', 'D', 'L']
        start_index = directions_clockwise.index(VECTOR_TO_DIRECTION[tuple(-in_direction)])
        for i in range(4):
            direction = directions_clockwise[(i + start_index) % 4]
            _yx = self._yx + DIRECTION_TO_VECTOR[direction]
            if self._outside_bounds(*_yx):
                continue

            if direction == VECTOR_TO_DIRECTION[tuple(out_direction)]:
                side = 'O' if self.rotation < 0 else 'I'

            if self._grid[*_yx] == '.':
                self._grid[*_yx] = side

    def _outside_bounds(self, y, x):
        return not 0 <= y < self.shape[0] or not 0 <= x < self.shape[1]

    def dig_inner(self):
        ny, nx = self.shape
        for y in range(ny):
            for x in range(nx):
                if self._grid[y, x] == '.':
                    self._update_tile_based_on_neighbors(y, x)
        self._grid[self._grid == "I"] = "#"

    def _update_tile_based_on_neighbors(self, y, x):
        for direction in VECTOR_TO_DIRECTION:
            _yx = np.array((y, x)) + np.array(direction)
            if self._outside_bounds(*_yx):
                continue
            neighboring_tile = self._grid[*_yx]
            if neighboring_tile == 'I':
                self._grid[y, x] = neighboring_tile
                return

    def volume(self) -> int:
        return np.count_nonzero(self._grid == '#')

    def vertices(self) -> list[np.array]:
        self._yx = np.zeros(2)
        vertices = [np.zeros(2)]
        for instruction in self._instructions:
            self._yx += instruction.distance * instruction.direction
            vertices.append(self._yx.copy())
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


def get_result(instructions):
    return Lagoon(instructions).get_result()


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
