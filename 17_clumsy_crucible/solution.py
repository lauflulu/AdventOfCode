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

        # for algorithm
        self._distances = {node: {} for node in self.graph}
        self._distances[(0, 0)] = {"": self.graph[(0, 0)]}
        self._best_score = 9
        self._queue = {"": 5}
        self.path_to_node = {"": (0, 0)}


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

        min_distance_to_target = 9 * (self.nx + self.ny)  # worst case scenario

        while self._queue:
            current_path = min(self._queue, key=self._queue.get)
            current_node = self.path_to_node[current_path]
            self._queue.pop(current_path)

            if current_node == (self.ny-1, self.nx-1):
                min_distance_to_target = min(self._distances[current_node].values())
                self._best_score = self._score(min_distance_to_target, current_node)
                print(min_distance_to_target)
                _queue = {}
                for p in self._queue:
                    _node = self.path_to_node[p]
                    if p not in self._distances[_node]:
                        continue
                    _dist = self._distances[_node][p]
                    s = self._best_case_score(_dist, _node)
                    if s <= self._best_score:
                        _queue[p] = self._worst_case_score(_dist, _node)
                self._queue = _queue

            # add neighbors
            for next_node, direction in self.valid_neighbors(*current_node, current_path):
                new_dist = self._distances[current_node][current_path] + self._values[*next_node]
                new_path = current_path + direction

                self._distances[next_node][new_path] = new_dist
                self._remove_dominated(next_node, new_path, new_dist)

        min_path = min(self._distances[(self.ny - 1, self.nx - 1)], key=self._distances[(self.ny - 1, self.nx - 1)].get)
        return min_distance_to_target, min_path

    def _remove_dominated(self, node, new_path, new_dist):
        new_dist_node = {}
        node_distances = self._distances[node].values()
        if not node_distances:
            return
        min_distance_to_node = min(node_distances)
        for p, d in self._distances[node].items():
            dominated = False
            if d > min_distance_to_node + 18:
                dominated = True
            if len(set(p[-4:])) == 4:  # small 4-node loops can be discarded
                dominated = True
            if self._best_case_score(d, node) > self._best_score:
                dominated = True
            if dominated:
                if p in self._queue:
                    self._queue.pop(p)
            else:
                if p == new_path and new_path not in self.path_to_node:
                    print(self._best_score, len(self.path_to_node), len(self._queue))
                    self._queue[new_path] = self._worst_case_score(new_dist, node)
                    self.path_to_node[new_path] = node
                new_dist_node[p] = d
            self._distances[node] = new_dist_node

    def _score(self, _distance, _node):
        return _distance / sum(_node)

    def _best_case_score(self, _distance, _node):
        smallest_possible_distance = _distance + self.ny - 1 - _node[0] + self.nx - 1 - _node[1]
        return self._score(smallest_possible_distance, (self.ny - 1, self.nx - 1))

    def _worst_case_score(self, _distance, _node):
        largest_possible_distance = _distance + 9 * (self.ny - 1 - _node[0] + self.nx - 1 - _node[1])
        return self._score(largest_possible_distance, (self.ny - 1, self.nx - 1))

    def _parse_input(self) -> dict[tuple, int]:
        return {(y, x): int(self._values[y, x]) for y in range(self.ny) for x in range(self.nx)}

    def valid_neighbors(self, y, x, path):
        def valid(_current_path, _direction):
            if not 0 <= y + dy < self.ny or not 0 <= x + dx < self.nx:
                return False
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

        neighbors = []
        for direction in DIRECTION_TO_VECTOR:
            dy, dx = DIRECTION_TO_VECTOR[direction]
            if valid(path, direction):
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
    data = load_data("example.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
