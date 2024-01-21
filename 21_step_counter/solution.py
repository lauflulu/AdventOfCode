import numpy as np


DIRECTION_TO_VECTOR = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0)
}

VECTOR_TO_DIRECTION = {value: key for key, value in DIRECTION_TO_VECTOR.items()}


class Gardener:
    def __init__(self, lines: list[str]):
        self.garden, self.start_yx = self._parse(lines)
        self._shape = self.garden.shape
        self.reachable_tiles = {self.start_yx}


    def _parse(self, lines: list[str]) -> tuple[np.array, tuple]:
        start_yx = (-1, -1)
        for i, line in enumerate(lines):
            j = line.find("S")
            if j > 0:
                start_yx = (i, j)
                break
        return np.array([[col for col in row.strip()] for row in lines]), start_yx

    def step(self, n=1):
        for _ in range(n):
            next_reachable_tiles = set()
            for yx in self.reachable_tiles:
                next_reachable_tiles.update(self._reachable_neighbors(yx))
            self.reachable_tiles = next_reachable_tiles

    def _reachable_neighbors(self, yx: tuple[int, int]) -> list[tuple[int, int]]:
        reachable_neighbors = []
        for direction, d_yx in DIRECTION_TO_VECTOR.items():
            _yx = tuple(np.array(yx) + np.array(d_yx))
            if self._within_bounds(_yx) and not self.garden[*_yx] == "#":
                reachable_neighbors.append(_yx)
        return reachable_neighbors

    def number_of_reachable_tiles(self):
        return len(self.reachable_tiles)

    def _within_bounds(self, yx: tuple[int, int]) -> bool:
        if not 0 <= yx[0] < self._shape[0] or not 0 <= yx[1] < self._shape[1]:
            return False
        return True


def load_data(filename) -> Gardener:
    with open(filename, "r") as file:
        return Gardener(file.readlines())


def get_result(gardener: Gardener) -> int:
    gardener.step(64)
    return gardener.number_of_reachable_tiles()


def get_result_2(gardener: Gardener) -> int:
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
