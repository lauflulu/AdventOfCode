import numpy as np


class Beam:
    def __init__(self, contraption: list[str]):
        self.contraption = self._set_contraption(contraption)
        self.beam_tips = [(0,0, ">")]

    def _set_contraption(self, contraption) -> np.array:
        data = []
        for row in contraption:
            data.append([col for col in row.strip()])
        return np.array(data, dtype="U8")

    def _process_tips(self):
        new_tips = []
        for tip in self.beam_tips:
            new_tips.append(self._walk(tip))
        self.beam_tips = new_tips

    def _walk(self, tip):
        y = tip[0]
        x = tip[1]
        direction = tip[2]
        if direction in self.contraption[y, x]:
            return
        self.contraption[y, x] += direction


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
