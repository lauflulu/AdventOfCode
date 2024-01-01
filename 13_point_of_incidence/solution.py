import numpy as np


class Terrain:
    def __init__(self, pattern: np.array):
        self.pattern = pattern

    def mirror_indices(self) -> tuple[int, int]:
        pass


def load_data(filename):
    with open(filename, 'r') as file:
        terrains = []
        current_terrain = []
        for line in file:
            if line == '\n':
                terrains.append(Terrain(np.array(current_terrain)))
                current_terrain = []
                continue
            current_terrain.append([x for x in line.strip()])
    terrains.append(Terrain(np.array(current_terrain)))
    return terrains

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
