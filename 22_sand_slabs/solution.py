class Block:
    def __init__(self, line: str):
        self.cubes = self._parse_line(line)

    def _parse_line(self, line: str) -> list:
        pass


def load_data(filename) -> list[Block]:
    with open(filename) as f:
        return list(map(Block, f.readlines()))


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
