import numpy as np


DIRECTIONS_TO_VECTOR = {
    "^": np.array((-1, 0)),
    "v": np.array((1, 0)),
    ">": np.array((0, 1)),
    "<": np.array((0, -1)),
}


class Walk:
    def __init__(self, lines: list[str]):
        self.trail_map = self._parse(lines)
        self.trail_graph = {(0, 1): {}}
        self._tip_queue = [((0, 1), "v")]

    @staticmethod
    def _parse(lines: list[str]) -> np.ndarray:
        return np.array([[tile for tile in line.strip()] for line in lines])

    def explore(self):
        while self._tip_queue:
            current_node, direction = self._pop_queue()
            distance, new_node, out_directions = self._explore_from(current_node, direction)
            if new_node is None:
                continue
            self._update_graph(current_node, distance, new_node)
            self._append_queue(new_node, out_directions)

    def _append_queue(self, new_node, out_directions):
        for tip in out_directions:
            if new_node not in self.trail_graph:
                self._tip_queue.append((new_node, tip))

    def _pop_queue(self):
        return self._tip_queue.pop(0)

    def _update_graph(self, current_node, length, new_node):
        if current_node not in self.trail_graph:
            self.trail_graph[current_node] = {new_node: length}
        else:
            self.trail_graph[current_node][new_node] = length

    def _explore_from(self, node: tuple, direction: str) -> tuple[int, tuple[int, int] | None, list[str]]:
        distance = 0
        yx = np.array(node)
        possible_directions = [direction]
        while len(possible_directions) == 1:
            direction = possible_directions[0]
            yx += DIRECTIONS_TO_VECTOR[direction]
            if self._is_uphill(yx, direction):
                return distance, None, []
            possible_directions = self.possible_directions(yx, last_direction=direction)
            distance += 1
        return distance, (int(yx[0]), int(yx[1])), possible_directions

    def possible_directions(self, yx, last_direction):
        directions = []
        for d, d_yx in DIRECTIONS_TO_VECTOR.items():
            if np.all(d_yx == - DIRECTIONS_TO_VECTOR[last_direction]):
                continue
            _yx = yx + np.array(d_yx)
            if not 0 <= _yx[0] < self.trail_map.shape[0] or not 0 <= _yx[1] < self.trail_map.shape[1]:
                continue
            if self.trail_map[tuple(_yx)] in [".", "^", "v", "<", ">"]:
                directions.append(d)
        return directions

    def _is_uphill(self, yx, direction):
        tile = self.trail_map[tuple(yx)]
        if tile not in DIRECTIONS_TO_VECTOR:
            return False
        return np.all(DIRECTIONS_TO_VECTOR[tile] == -DIRECTIONS_TO_VECTOR[direction])

    def longest_path(self) -> int:
        self.explore()
        start = (0, 1)
        finish = (self.trail_map.shape[0]-1, self.trail_map.shape[1] - 2)
        tips = [(start, 0)]
        max_distance = 0
        while tips:
            node, length = tips.pop(0)
            max_distance = max(max_distance, length)
            if node == finish:
                continue
            for out_node, out_length in self.trail_graph[node].items():
                tips.append((out_node, length + out_length))
        return max_distance


def load_data(filename) -> Walk:
    with open(filename, "r") as f:
        return Walk(f.readlines())


def get_result(walk: Walk) -> int:
    return walk.longest_path()


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
