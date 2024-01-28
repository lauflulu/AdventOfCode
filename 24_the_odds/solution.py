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
