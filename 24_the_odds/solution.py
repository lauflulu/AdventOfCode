import itertools

import numpy as np
from scipy.optimize import fsolve


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
        try:
            t = np.linalg.solve(v, p)
        except np.linalg.LinAlgError:
            return None, None, None, None
        intersect = a.start_position[:2] + a.velocity[:2] * t[0]
        return intersect[0], intersect[1], t[0], t[1]

    def _is_forward(self) -> bool:
        if self._tx is None or self._ty is None:
            return False
        return bool(self._tx > 0 and self._ty > 0)

    def _is_in_box(self):
        if self.x is None or self.y is None:
            return False
        return bool(
            self._limits[0] <= self.x <= self._limits[1]
            and self._limits[0] <= self.y <= self._limits[1]
        )


def load_data(filename: str) -> list[Hailstone]:
    with open(filename) as f:
        return [Hailstone(line) for line in f]


def solve_initial_position(hailstones: list[Hailstone]) -> tuple[int, int, int]:
    x_1, y_1, z_1 = hailstones[0].start_position
    x_2, y_2, z_2 = hailstones[1].start_position
    x_3, y_3, z_3 = hailstones[2].start_position
    u_1, v_1, w_1 = hailstones[0].velocity
    u_2, v_2, w_2 = hailstones[1].velocity
    u_3, v_3, w_3 = hailstones[2].velocity

    def nonlinear_equations(p):
        x, y, z, u, v, w, t_1, t_2, t_3 = p
        return [
            x_1 + u_1 * t_1 - x - u * t_1,
            y_1 + v_1 * t_1 - y - v * t_1,
            z_1 + w_1 * t_1 - z - w * t_1,
            x_2 + u_2 * t_2 - x - u * t_2,
            y_2 + v_2 * t_2 - y - v * t_2,
            z_2 + w_2 * t_2 - z - w * t_2,
            x_3 + u_3 * t_3 - x - u * t_3,
            y_3 + v_3 * t_3 - y - v * t_3,
            z_3 + w_3 * t_3 - z - w * t_3,
        ]
    root = fsolve(nonlinear_equations, np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))
    x, y, z = root[:3]
    return round(x), round(y), round(z)


def get_result(hailstones: list[Hailstone], limits: tuple[int, int]) -> int:
    cross_count = 0
    for a, b in itertools.combinations(hailstones, 2):
        intersection = Intersection(a, b, limits=limits)
        if intersection.forward and intersection.in_box:
            cross_count += 1
    return cross_count


def get_result_2(hailstones: list[Hailstone]) -> int:
    return sum(solve_initial_position(hailstones[:3]))


def main():
    hailstones = load_data("data.txt")
    print(get_result(hailstones, limits=(200000000000000, 400000000000000)))
    print(get_result_2(hailstones))


if __name__ == '__main__':
    main()
