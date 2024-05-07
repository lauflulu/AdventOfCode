import numpy as np


class Terrain:
    def __init__(self, pattern: np.array):
        self.pattern = pattern

    def mirror_indices(self) -> tuple[int, int]:
        column_mirror_index = self._mirror_index(self.pattern, np.all)
        row_mirror_index = self._mirror_index(self.pattern.T, np.all)
        return row_mirror_index, column_mirror_index

    def _mirror_index(self, pattern, condition_func) -> int:
        n_rows, n_columns = pattern.shape
        for c in range(1, n_columns):
            min_width = min([c, n_columns-c])
            left_pattern = pattern[: ,c-min_width:c]
            right_pattern = pattern[:, c:c+min_width]
            if condition_func(left_pattern[:, ::-1] == right_pattern):
                return c
        return 0

    def result(self):
        mirror_indices = self.mirror_indices()
        return mirror_indices[0] * 100 + mirror_indices[1]

    def result_2(self):
        mirror_indices = self.smudge_mirror_indices()
        return mirror_indices[0] * 100 + mirror_indices[1]

    def smudge_mirror_indices(self):
        def one_field_does_not_match(bool_array: np.array):
            return np.count_nonzero(bool_array == False) == 1
        column_mirror_index = self._mirror_index(self.pattern, one_field_does_not_match)
        row_mirror_index = self._mirror_index(self.pattern.T, one_field_does_not_match)
        return row_mirror_index, column_mirror_index


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

def get_result(terrains):
    return sum([terrain.result() for terrain in terrains])


def get_result_2(terrains):
    return sum([terrain.result_2() for terrain in terrains])


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
