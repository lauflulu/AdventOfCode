class Block:
    def __init__(self, line: str):
        self.cubes = self._parse_line(line)

    def _parse_line(self, line: str) -> list:
        ends = line.strip().split("~")
        xyz_1 = ends[0].split(",")
        xyz_2 = ends[1].split(",")
        return [[x, y, z] for x in range(int(xyz_1[0]), int(xyz_2[0]) + 1)
                for y in range(int(xyz_1[1]), int(xyz_2[1]) + 1)
                for z in range(int(xyz_1[2]), int(xyz_2[2]) + 1)]

class Environment:
    def __init__(self, blocks: list[Block]):
        self.blocks = blocks



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
