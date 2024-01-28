import numpy as np


class Hailstone:
    def __init__(self, line: str):
        self.start_position, self.velocity = self._parse(line)

    @staticmethod
    def _parse(line: str):
        position, velocity = line.split("@")
        position = np.array([int(x.strip()) for x in position.split(",")])
        velocity = np.array([int(x.strip()) for x in velocity.split(",")])
        return position, velocity
    
    
class Intersection:
    def __init__(self, a: Hailstone, b: Hailstone, limits: tuple[int, int]):
        self._hailstone_a = a
        self._hailstone_b = b
        self._limits = limits
        self.x, self.y, self._tx, self._ty = self._find_intersection()
        self.forward = self._is_forward()
        self.in_box = self._is_in_box()

    def _find_intersection(self):
        a, b = self._hailstone_a, self._hailstone_b
        v = np.array([a.velocity[:2], -b.velocity[:2]]).T
        p = b.start_position[:2] - a.start_position[:2]
        t = np.linalg.solve(v, p)
        intersect = a.start_position[:2] + a.velocity[:2] * t[0]
        return intersect[0], intersect[1], t[0], t[1]

    def _is_forward(self) -> bool:
        return bool(self._tx > 0 and self._ty > 0)

    def _is_in_box(self):
        return bool(
            self._limits[0] <= self.x <= self._limits[1]
            and self._limits[0] <= self.y <= self._limits[1]
        )


def load_data(filename: str) -> list[Hailstone]:
    with open(filename) as f:
        return [Hailstone(line) for line in f]


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
