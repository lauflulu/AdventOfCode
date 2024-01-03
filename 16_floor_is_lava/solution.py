import numpy as np


DIRECTION_TO_VECTOR = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0)}


VECTOR_TO_DIRECTION = {value: key for key, value in DIRECTION_TO_VECTOR.items()}


class Beam:
    def __init__(self, contraption: list[str]):
        self.contraption = self._set_contraption(contraption)
        self.tips = [(0, 0, ">")]
        self.energized = np.char.add(np.zeros(self.contraption.shape, dtype='U1'), '.')

    def compute_energy(self):
        while self.tips:
            self.process_tips()
        return np.count_nonzero(self.energized == "#")

    def _set_contraption(self, contraption) -> np.array:
        data = []
        for row in contraption:
            data.append([col for col in row.strip()])
        return np.array(data, dtype="U8")

    def process_tips(self):
        ny, nx = self.contraption.shape
        new_tips = []
        for tip in self.tips:
            for _new_tip in  self._walk(tip):
                if 0 <= _new_tip[0] < ny and 0 <= _new_tip[1] < nx:
                    new_tips.append(_new_tip)
        self.tips = new_tips

    def _walk(self, tip) -> list:
        y, x, direction = tip
        self.energized[y, x] = "#"
        current_tile = self.contraption[y, x]
        if direction in current_tile:
            return []
        if current_tile == "/":
            if direction == "<":
                out_direction = "v"
            if direction == ">":
                out_direction =  "^"
            if direction == "^":
                out_direction =  ">"
            if direction == "v":
                out_direction =  "<"
            dy, dx = DIRECTION_TO_VECTOR[out_direction]
            return [(y + dy, x + dx, out_direction)]
        if current_tile == "\\":
            if direction == "<":
                out_direction = "^"
            if direction == ">":
                out_direction = "v"
            if direction == "^":
                out_direction = "<"
            if direction == "v":
                out_direction = ">"
            dy, dx = DIRECTION_TO_VECTOR[out_direction]
            return [(y + dy, x + dx, out_direction)]
        if current_tile == "-" and direction in ["^", "v"]:
            return [(y, x + 1, ">"), (y, x - 1, "<")]
        if current_tile == "|" and direction in ["<", ">"]:
            return [(y - 1, x, "^"), (y + 1, x, "v")]
        if "." in current_tile:
            self.contraption[y, x] += direction
        return [(y + DIRECTION_TO_VECTOR[direction][0], x + DIRECTION_TO_VECTOR[direction][1], direction)]


def load_data(filename) -> Beam:
    with open(filename, 'r') as file:
        return Beam(file.readlines())


def get_result(beam):
    return beam.compute_energy()


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
