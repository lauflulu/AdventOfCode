import numpy as np


class Beam:
    def __init__(self, contraption: list[str]):
        self.contraption = self._set_contraption(contraption)
        self.beam_tips = [(0,0, ">")]

    def _set_contraption(self, contraption) -> np.array:
        data = []
        for row in contraption:
            data.append([col for col in row.strip()])
        return np.array(data)


def load_data(filename) -> Beam:
    with open(filename, 'r') as file:
        return Beam(file.readlines())


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
