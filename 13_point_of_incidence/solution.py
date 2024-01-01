import numpy as np


class Terrain:
    def __init__(self, pattern: np.array):
        self.pattern = pattern

    def mirror_indices(self) -> tuple[int, int]:
        pass


def load_data(filename):
    pass


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
