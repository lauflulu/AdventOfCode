class Block:
    def __init__(self, line: str):
        self.cubes = self._parse_line(line)
        self.removable = True
        self.supported_by = []

    def _parse_line(self, line: str) -> list:
        ends = line.strip().split("~")
        xyz_1 = ends[0].split(",")
        xyz_2 = ends[1].split(",")
        return [[x, y, z] for x in range(int(xyz_1[0]), int(xyz_2[0]) + 1)
                for y in range(int(xyz_1[1]), int(xyz_2[1]) + 1)
                for z in range(int(xyz_1[2]), int(xyz_2[2]) + 1)]

    def fall(self, to_z):
        min_current_z = min([cube[2] for cube in self.cubes])
        for cube in self.cubes:
            cube[2] += to_z - min_current_z

    def set_supports(self, blocks):
        self.supported_by = blocks
        if len(blocks) == 1:
            blocks[0].removable = False

    def lowest_z(self):
        return self.cubes[0][2]

    def highest_z(self):
        return self.cubes[-1][2]


class Environment:
    def __init__(self, blocks: list[Block]):
        self.blocks = blocks

    def n_removable_blocks(self):
        self.settle()
        self.identify_supports()
        return len([block for block in self.blocks if block.removable])

    def settle(self):
        self.sort_by_lowest_z()
        tops_of_fallen_blocks = {}
        for block in self.blocks:
            xys = [(cube[0], cube[1]) for cube in block.cubes]
            highest_z_below = max([tops_of_fallen_blocks[xy] for xy in xys if xy in tops_of_fallen_blocks] or [0])
            block.fall(highest_z_below  + 1)
            tops_of_fallen_blocks.update({(cube[0], cube[1]): cube[2] for cube in block.cubes})

    def identify_supports(self):
        self.sort_by_highest_z()
        for i, block in enumerate(self.blocks):
            supporting_blocks = []
            for j in reversed(range(0, i)):
                block_below = self.blocks[j]
                if block_below.highest_z() < block.lowest_z() - 1:
                    break
                xys = [(cube[0], cube[1]) for cube in block.cubes]
                below_xys = [(cube[0], cube[1]) for cube in block_below.cubes]
                if any(xy in below_xys for xy in xys):
                    supporting_blocks.append(block_below)
            block.set_supports(supporting_blocks)

    def sort_by_lowest_z(self):
        self.blocks.sort(key=lambda block: block.lowest_z())

    def sort_by_highest_z(self):
        self.blocks.sort(key=lambda block: block.highest_z())


def load_data(filename) -> list[Block]:
    with open(filename) as f:
        return list(map(Block, f.readlines()))


def get_result(blocks: list[Block]) -> int:
    return Environment(blocks).n_removable_blocks()


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
