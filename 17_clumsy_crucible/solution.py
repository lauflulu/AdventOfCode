import numpy as np


class Graph:
    def __init__(self, lines: list[str]):
        self._values = self._lines_to_array(lines)
        self.graph = self._parse_input()

    def get_result(self):
        ny, nx = self._values.shape
        dist, prev = self._dijkstra()
        self._visualize_shortest_path(prev)
        min_length = dist[(ny - 1, nx - 1)]
        return int(min_length)

    def _visualize_shortest_path(self, prev):
        path = np.char.add(np.zeros(self._values.shape, dtype='U1'), '.')
        ny, nx = self._values.shape
        source_reached = False
        node = (ny - 1, nx - 1)
        path[*node] = '#'
        while not source_reached:
            node = prev[node]
            path[*node] = '#'
            if node == (0, 0):
                source_reached = True
        print()
        print(path)

    def _dominance(self):
        queue = {node: 2 ** 31 for node in self.graph}
        dist = {node: {"rlud": 2**31} for node in self.graph}

    def _dijkstra(self) -> tuple[dict[tuple, int], dict[tuple, tuple]]:
        queue = {node: 2**31 for node in self.graph}
        dist = {node: 2**31 for node in self.graph}
        dist[(0, 0)] = self.graph[(0, 0)]
        prev = {}
        while queue:
            min_queued_node = min(queue, key=queue.get)
            queue.pop(min_queued_node)

            for neighbor in self._neighbors(*min_queued_node):
                weight = self._values[*neighbor]
                if neighbor not in queue:
                    continue
                if self._last_three_moves_were_straight(min_queued_node, neighbor, prev):
                    continue
                new_dist = dist[min_queued_node] + weight
                if new_dist < dist[neighbor]:
                    queue[neighbor] = new_dist
                    dist[neighbor] = new_dist
                    prev[neighbor] = min_queued_node
        return dist, prev

    def _last_three_moves_were_straight(self, min_queued_node, neighbor, prev):
        try:
            vector_to_prev3 = np.array(prev[prev[prev[min_queued_node]]]) - np.array(neighbor)
            distance_to_prev3 = int(np.dot(vector_to_prev3, vector_to_prev3)**0.5)
            return distance_to_prev3 == 4
        except KeyError:
            return False

    def _parse_input(self) -> dict[tuple, int]:
        ny, nx = self._values.shape
        return {(y, x): int(self._values[y, x]) for y in range(ny) for x in range(nx)}

    def _neighbors(self, y, x):
        ny, nx = self._values.shape
        neighbors = []
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if not 0<= y+dy < ny or not 0 <= x+dx< nx:
                continue
            neighbors.append((y+dy, x+dx))
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
