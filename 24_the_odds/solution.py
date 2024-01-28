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
    def __init__(self, a: Hailstone, b: Hailstone):
        self._hailstone_a = a
        self._hailstone_b = b
        self.x, self.y, self._tx, self._ty = self._find_intersection()
        self.forward = self._is_forward()
        self.in_box = self._is_in_box()

    def _find_intersection(self):
        pass

    def _is_forward(self):
        pass

    def _is_in_box(self):
        pass


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
