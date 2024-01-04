import numpy as np


class Graph:
    def __init__(self, lines: list[str]):
        self._values = self._lines_to_array(lines)
        self.graph = self._parse_input()

    def get_result(self):
        ny, nx = self._values.shape
        dist, prev = self._dijkstra()
        min_length = (dist[(ny - 1, nx - 1)] + self._values[0, 0] + self._values[ny - 1, nx - 1]) / 2
        return int(min_length)

    def _dijkstra(self) -> tuple[dict[tuple, int], dict[tuple, tuple]]:
        queue = {node: 2**31 for node in self.graph}
        dist = {node: 2**31 for node in self.graph}
        dist[(0, 0)] = 0
        prev = {}
        c = 0
        while queue:
            c+= 1
            min_queued_node = min(queue, key=queue.get)
            queue.pop(min_queued_node)

            for neighbor, weight in self.graph[min_queued_node].items():
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
