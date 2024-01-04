import numpy as np


class Graph:
    def __init__(self, lines: list[str]):
        self._values = self._lines_to_array(lines)
        self.graph = self._parse_input()

    def _parse_input(self) -> dict[tuple, dict]:
        ny, nx = self._values.shape
        graph = {}
        for y in range(ny):
            for x in range(nx):
                node = (y, x)
                graph[node] = self._neighbors(*node)
        return graph

    def _neighbors(self, y, x):
        ny, nx = self._values.shape
        neighbors = {}
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if not 0<= y+dy < ny or not 0 <= x+dx< nx:
                continue
            neighbors[(y+dy, x+dx)] = self._values[y, x] + self._values[y+dy, x+dx]
        return neighbors

    def _lines_to_array(self, lines):
        data = []
        for row in lines:
            data.append([col for col in row.strip()])
        return np.array(data, dtype="i8")

def load_data(filename):
    with open(filename, "r") as file:
        return Graph([line.strip() for line in file])


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
