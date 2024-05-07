import math
import re
from sympy import primefactors


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
    return _count_steps_until('AAA', 'ZZZ', instructions, maps)


def _count_steps_until(start_location, abort_condition, instructions, maps):
    current_location = start_location
    count = 0
    while not current_location.endswith(abort_condition):
        for i in instructions:
            if i == 'R':
                current_location = maps[current_location].right
            else:
                current_location = maps[current_location].left
            count += 1
            if current_location.endswith(abort_condition):
                return count


def get_result_2(instructions, maps):
    current_locations = [location for location in maps if location.endswith('A')]
    counts = [_count_steps_until(start_location, 'Z', instructions, maps) for start_location in current_locations]
    prime_factors = set([prime for count in counts for prime in primefactors(count)])
    return math.prod(prime_factors)


def _all_end_with_z(current_locations):
    return all([location.endswith('Z') for location in current_locations])


def main():
    instructions, maps = load_data("data.txt")
    print(get_result(instructions, maps))
    print(get_result_2(instructions, maps))


if __name__ == '__main__':
    main()
