class Instruction:
    def __init__(self, line: str):
        self.direction, self.distance, self.color = self._parse(line)

    def _parse(self, line: str) -> tuple[str, int, str]:
        pass


class Lagoon:
    def __init__(self, instructions: list[Instruction]):
        self._instructions = instructions
        self.y, self.x = (0, 0)

    def get_result(self) -> int:
        pass

    def precalculate_shape(self) -> tuple[int, int]:
        pass

    def dig_outline(self):
        pass

    def volume(self) -> int:
        pass


def load_data(filename):
    pass


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
