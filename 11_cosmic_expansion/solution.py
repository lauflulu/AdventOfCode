import numpy as np


class Universe:
    def __init__(self, map_of_the_universe: np.array):
        self._map = map_of_the_universe
        self._expansion_factor = 2

    def _expand(self):
        expanded_rows = []
        for row in range(self._map.shape[0]):
            expanded_rows.append(self._map[row, :])
            if np.all(self._map[row, :] == '.'):
                for _ in range(self._expansion_factor-1):
                    expanded_rows.append(self._map[row, :])
        expanded_rows = np.array(expanded_rows)
        expanded_cols = []
        for col in range(expanded_rows.shape[1]):
            expanded_cols.append(expanded_rows[:, col])
            if np.all(expanded_rows[:, col] == '.'):
                for _ in range(self._expansion_factor-1):
                    expanded_cols.append(expanded_rows[:, col])
        return np.array(expanded_cols).T

    def _galaxy_coordinates(self) -> list[tuple]:
        return [tuple(yx) for yx in np.argwhere(self._expand() == '#')]

    def _galaxy_distances(self) -> list[int]:
        paths = []
        galaxies = self._galaxy_coordinates()
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                distance = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
                paths.append(distance)
        return paths

    def total_distance(self, expansion_factor: int = 2) -> int:
        self._expansion_factor = expansion_factor
        return sum(self._galaxy_distances())


class VirtualUniverse:
    def __init__(self, map_of_the_universe: np.array):
        self._map = map_of_the_universe
        self._expansion_factor = 2

    def _expanded_rows(self) -> list[int]:
        row_indicess = []
        for row in range(self._map.shape[0]):
            if np.all(self._map[row, :] == '.'):
                row_indicess.append(row)
        return row_indicess

    def _expanded_cols(self) -> list[int]:
        col_indices = []
        for col in range(self._map.shape[1]):
            if np.all(self._map[:, col] == '.'):
                col_indices.append(col)
        return col_indices

    def _galaxy_coordinates(self) -> list[tuple]:
        return [tuple(yx) for yx in np.argwhere(self._map == '#')]

    def _galaxy_distances(self) -> list[int]:
        distances = []
        galaxies = self._galaxy_coordinates()
        expanded_rows = self._expanded_rows()
        expanded_cols = self._expanded_cols()
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                if galaxies[i][0] < galaxies[j][0]:
                    row_min = galaxies[i][0]
                    row_max = galaxies[j][0]
                else:
                    row_min = galaxies[j][0]
                    row_max = galaxies[i][0]
                if galaxies[i][1] < galaxies[j][1]:
                    col_min = galaxies[i][1]
                    col_max = galaxies[j][1]
                else:
                    col_min = galaxies[j][1]
                    col_max = galaxies[i][1]
                expanded_rows_between = len([row for row in expanded_rows if row_min < row < row_max])
                expanded_cols_between = len([col for col in expanded_cols if col_min < col < col_max])
                distance = (abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
                            + (self._expansion_factor - 1) * (expanded_rows_between + expanded_cols_between))
                distances.append(distance)
        return distances

    def total_distance(self, expansion_factor: int = 2) -> int:
        self._expansion_factor = expansion_factor
        return sum(self._galaxy_distances())


def load_data(filename):
    with open(filename, 'r') as file:
        data = []
        for row in file:
            data.append([col for col in row.strip()])
    return np.array(data)


def get_result(universe):
    return universe.total_distance()


def get_result_2(universe, expansion_factor):
    return universe.total_distance(expansion_factor)


def main():
    data = load_data("data.txt")
    universe = Universe(data)
    print(get_result(universe))
    virtual_universe = VirtualUniverse(data)
    print(get_result_2(virtual_universe, 1_000_000))


if __name__ == '__main__':
    main()
