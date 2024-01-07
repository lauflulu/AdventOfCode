import numpy as np


DIRECTION_TO_VECTOR = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0)}


VECTOR_TO_DIRECTION = {value: key for key, value in DIRECTION_TO_VECTOR.items()}


class Graph:
    def __init__(self, lines: list[str]):
        self._values = self._lines_to_array(lines)
        self.ny, self.nx = self._values.shape
        self.graph = self._parse_input()

    def get_result(self):
        dist, path = self._dominance()
        self._visualize_shortest(path)
        return dist

    def _visualize_shortest(self, _path):
        path = np.char.add(np.zeros(self._values.shape, dtype='U1'), '.')
        node = np.array((0, 0))
        path[*node] = '#'
        for direction in _path:
            node += np.array(DIRECTION_TO_VECTOR[direction])
            path[*node] = '#'
        print()
        print(path)

    def _dominance(self):
        def remove_dominated(node, path):
            min_distance_to_node = min(dist[node].values())
            dist[node] = {path: d for path, d in dist[node].items() if d <= min_distance_to_node + 18}


        def step_valid(_current_path, _direction):
            if len(_current_path) == 0:
                return True
            _current_vector = np.array(DIRECTION_TO_VECTOR[_current_path[-1]])
            _dicection_vector = np.array(DIRECTION_TO_VECTOR[_direction])
            if np.all(_current_vector == - _dicection_vector):
                return False
            if len(_current_path) <= 3:
                return True
            if _current_path[-3:] == _direction * 3:
                return False
            return True

        def get_node(_path):
            node = np.array((0, 0))
            for _direction in _path:
                node += np.array(DIRECTION_TO_VECTOR[_direction])
            return tuple(node)

        queue = {"": self.graph[(0, 0)]}
        dist = {node: {} for node in self.graph}
        dist[(0, 0)] = {"": self.graph[(0, 0)]}
        while queue:
            current_path = min(queue, key=queue.get)
            current_node = get_node(current_path)
            queue.pop(current_path)
            #print(current_path, current_node)
            #print(len(queue))
            #print(current_node, len(dist[current_node]), dist[current_node])
            if current_node == (self.ny-1, self.nx-1):
                break

            # check node for dominance
            remove_dominated(current_node, current_path)
            if current_path not in dist[current_node]:
                continue

            # add neighbors
            for next_node, direction in self.neighbors(*current_node):
                weight = self._values[*next_node]
                if not step_valid(current_path, direction):
                    continue

                new_dist = dist[current_node][current_path] + weight
                new_path = current_path + direction

                queue[new_path] = new_dist
                dist[next_node][new_path] = new_dist
        print(len(dist[(self.ny-1, self.nx-1)]))
        min_path = min(dist[(self.ny-1, self.nx-1)], key=dist[(self.ny-1, self.nx-1)].get)
        min_dist = dist[(self.ny-1, self.nx-1)][min_path]
        return min_dist, min_path

    def _parse_input(self) -> dict[tuple, int]:
        return {(y, x): int(self._values[y, x]) for y in range(self.ny) for x in range(self.nx)}

    def neighbors(self, y, x):
        neighbors = []
        for direction in DIRECTION_TO_VECTOR:
            dy, dx = DIRECTION_TO_VECTOR[direction]
            if not 0<= y+dy < self.ny or not 0 <= x+dx< self.nx:
                continue
            neighbors.append(((y+dy, x+dx), direction))
        return neighbors

    def _lines_to_array(self, lines):
        data = []
        for row in lines:
            data.append([col for col in row.strip()])
        return np.array(data, dtype="i8")

def load_data(filename):
    with open(filename, "r") as file:
        return Graph([line.strip() for line in file])


def get_result(graph):
    return graph.get_result()


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
