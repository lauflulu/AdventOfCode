
class Graph:
    def __init__(self, lines: list[str]):
        self.graph = self._parse_input(lines)

    def _parse_input(self, lines) -> dict[dict]:
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
