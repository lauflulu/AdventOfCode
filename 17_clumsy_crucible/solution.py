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
            new_dist_node = {}
            node_distances = dist[node].values()
            if node_distances:
                min_distance_to_node = min(node_distances)
                for p, d in dist[node].items():
                    if d > min_distance_to_node + 18:
                        continue
                    if d > min_distance_to_target:
                        continue
                    if len(set(path[-4:])) == 4:  # small 4-node loops can be discarded
                        continue
                    if self._best_case_score(d, node) > minimum_score:
                        continue
                    new_dist_node[p] = d
            dist[node] = new_dist_node

        def get_node(_path):
            node = np.array((0, 0))
            for _direction in _path:
                node += np.array(DIRECTION_TO_VECTOR[_direction])
            return tuple(node)

        queue = {"": 5}  # path: score
        dist = {node: {} for node in self.graph}
        dist[(0, 0)] = {"": self.graph[(0, 0)]}
        min_distance_to_target = 9 * (self.nx + self.ny)  # worst case scenario
        minimum_score = 9
        while queue:
            current_path = min(queue, key=queue.get)
            current_node = get_node(current_path)
            queue.pop(current_path)
            print(len(queue))

            if current_node == (self.ny-1, self.nx-1):
                min_distance_to_target = min(dist[current_node].values())
                minimum_score = self._worst_case_score(min_distance_to_target, current_node)
                _queue = {}
                for p in queue:
                    _node = get_node(p)
                    if p not in dist[_node]:
                        continue
                    _dist = dist[_node][p]
                    s = self._best_case_score(_dist, _node)
                    print(minimum_score, s)
                    if s <= minimum_score:
                        _queue[p] = self._worst_case_score(_dist, _node)
                queue = _queue

            # check node for dominance
            remove_dominated(current_node, current_path)
            if current_path not in dist[current_node]:
                continue

            # add neighbors
            for next_node, direction in self.valid_neighbors(*current_node, current_path):
                new_dist = dist[current_node][current_path] + self._values[*next_node]
                new_path = current_path + direction

                queue[new_path] = self._worst_case_score(new_dist, next_node)
                dist[next_node][new_path] = new_dist

        min_path = min(dist[(self.ny-1, self.nx-1)], key=dist[(self.ny-1, self.nx-1)].get)
        return min_distance_to_target, min_path

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
