import numpy as np


DIRECTIONS_TO_VECTOR = {
    "n": np.array((-1, 0)),
    "s": np.array((1, 0)),
    "e": np.array((0, 1)),
    "w": np.array((0, -1)),
}


class Walk:
    def __init__(self, lines: list[str]):
        self.trail_map = self._parse(lines)
        self.trail_graph = {(0, 1): {}}
        self._tip_queue = [((0, 1), "s")]

    @staticmethod
    def _parse(lines: list[str]) -> np.ndarray:
        return np.array([[tile for tile in line.strip()] for line in lines])

    def explore(self):
        while self._tip_queue:
            current_node, direction = self._tip_queue.pop(0)
            print(current_node, direction)
            length, new_node, out_directions = self._explore_from(current_node, direction)
            self._update_graph(current_node, length, new_node)
            for tip in out_directions:
                if new_node not in self.trail_graph:
                    self._tip_queue.append((new_node, tip))

    def _update_graph(self, current_node, length, new_node):
        if current_node not in self.trail_graph:
            self.trail_graph[current_node] = {new_node: length}
        else:
            self.trail_graph[current_node][new_node] = length

    def _explore_from(self, node: tuple, direction: str) -> tuple[int, tuple[int, int], list[str]]:
        distance = 0
        yx = np.array(node)
        possible_directions = [direction]
        while len(possible_directions) == 1:
            yx += DIRECTIONS_TO_VECTOR[possible_directions[0]]
            possible_directions = self.possible_directions(yx, last_direction=possible_directions[0])
            distance += 1
        return distance, (int(yx[0]), int(yx[1])), possible_directions

    def possible_directions(self, yx, last_direction):
        directions = []
        for d in "nsew":
            if np.all(DIRECTIONS_TO_VECTOR[d] == - DIRECTIONS_TO_VECTOR[last_direction]):
                continue
            _yx = yx + np.array(DIRECTIONS_TO_VECTOR[d])
            if not 0 <= _yx[0] < self.trail_map.shape[0] or not 0 <= _yx[1] < self.trail_map.shape[1]:
                continue
            if self.trail_map[tuple(_yx)] in [".", "^", "v", "<", ">"]:
                directions.append(d)
        return directions


def load_data(filename) -> Walk:
    with open(filename, "r") as f:
        return Walk(f.readlines())


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
