import numpy as np


class Gardener:
    def __init__(self, lines: list[str]):
        self.garden, self.start = self._parse(lines)

    def _parse(self, lines: list[str]) -> tuple[np.array, tuple]:
        pass

    def step(self, n=1):
        pass




def load_data(filename) -> Gardener:
    pass


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
