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
    current_location = 'AAA'
    count = 0
    while not current_location == 'ZZZ':
        for i in instructions:
            if i == 'R':
                current_location = maps[current_location].right
            else:
                current_location = maps[current_location].left
            count += 1
            if current_location == 'ZZZ':
                break
    return count


def get_result_2(instructions, maps):
    pass


def main():
    instructions, maps = load_data("data.txt")
    print(get_result(instructions, maps))
    print(get_result_2(instructions, maps))


if __name__ == '__main__':
    main()
