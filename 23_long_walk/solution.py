import numpy as np


class Walk:
    def __init__(self, lines: list[str]):
        self.trail_map = self._parse(lines)
        self.trail_graph = {(0, 1): []}

    @staticmethod
    def _parse(lines: list[str]) -> np.ndarray:
        return np.array([[tile for tile in line.strip()] for line in lines])

    def explore(self):
        pass


def load_data(filename) -> Walk:
    with open(filename, "r") as f:
        return Walk(f.readlines())


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
