import re


class Map:
    def __init__(self, right, left):
        self.right = right
        self.left = left


def load_data(filename):
    with open(filename, 'r') as file:
        instructions = file.readline().strip()
        file.readline()
        maps = {}
        for line in file.readlines():
            start, left, right = re.findall(r'[A-Z]{3}', line)
            maps[start] = Map(right, left)
        return instructions, maps


def get_result(instructions, maps):
    pass


def get_result_2(instructions, maps):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
