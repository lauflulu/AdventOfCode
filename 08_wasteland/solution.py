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
            start, left, right = re.findall(r'[A-Z0-9]{3}', line)
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
    current_locations = [location for location in maps if location.endswith('A')]
    count = 0
    while not _all_end_with_z(current_locations):
        for i in instructions:
            for x, location in enumerate(current_locations):
                if i == 'R':
                    current_locations[x] = maps[current_locations[x]].right
                else:
                    current_locations[x] = maps[current_locations[x]].left
            count += 1
            if _all_end_with_z(current_locations):
                break
    return count


def _all_end_with_z(current_locations):
    return all([location.endswith('Z') for location in current_locations])


def main():
    instructions, maps = load_data("data.txt")
    print(get_result(instructions, maps))
    print(get_result_2(instructions, maps))


if __name__ == '__main__':
    main()
