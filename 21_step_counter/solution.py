import numpy as np


class Gardener:
    def __init__(self, lines: list[str]):
        self.garden, self.start_yx = self._parse(lines)

    def _parse(self, lines: list[str]) -> tuple[np.array, tuple]:
        start_yx = (-1, -1)
        for i, line in enumerate(lines):
            j = line.find("S")
            if j > 0:
                start_yx = (i, j)
                break
        return np.array([[col for col in row.strip()] for row in lines]), start_yx


    def step(self, n=1):
        pass


def load_data(filename) -> Gardener:
    with open(filename, "r") as file:
        return Gardener(file.readlines())


def get_result(gardener: Gardener) -> int:
    pass


def get_result_2(gardener: Gardener) -> int:
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
