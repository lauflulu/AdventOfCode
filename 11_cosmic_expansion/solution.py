import numpy as np


class Universe:
    def __init__(self, map_of_the_universe: np.array):
        self._map = map_of_the_universe

    def expand(self):
        pass

    def galaxy_indices(self):
        pass

    def lengths_of_shortest_paths(self):
        pass


def load_data(filename):
    with open(filename, 'r') as file:
        data = []
        for row in file:
            data.append([col for col in row.strip()])
    return Universe(np.array(data))


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
