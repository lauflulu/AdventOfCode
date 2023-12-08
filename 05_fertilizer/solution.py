import re


class Map:

    def __init__(self, source, destination, ranges):
        self.source = source
        self.destination = destination
        self.ranges: list[Range] = ranges

    def map(self, source_number):
        for range_ in self.ranges:
            destination_number = range_.destination(source_number)
            if destination_number is not None:
                return destination_number
        return source_number


class Range:
    def __init__(self, destination_start: int, source_start: int, length: int):
        self.source_start = source_start
        self.destination_start = destination_start
        self.length = length

    def destination(self, source_number) -> int | None:
        if self.source_start <= source_number < self.source_start + self.length:
            return source_number - self.source_start + self.destination_start


def load_data(filename) -> tuple[list[int], list[Map]]:
    maps = []
    with open(filename, 'r') as file:
        seeds = [int(seed.strip()) for seed in file.readline().split(' ')[1:]]

        lines = file.readlines()[1:]
        source = ''
        destination = ''
        ranges = []
        for line in lines:
            if "map" in line:
                source, _, destination = line.split(' ')[0].split('-')
            elif re.match(r'[0-9]+ [0-9]+ [0-9]+', line):
                ranges.append(Range(*[int(n.strip()) for n in line.split(' ')]))
            else:
                maps.append(Map(source, destination, ranges))
                source = ''
                destination = ''
                ranges = []
        maps.append(Map(source, destination, ranges))
    return seeds, maps


def map_categories(maps, number, source, destination) -> int:
    n = number
    for map_ in maps:
        if map_.source == source:
            n = map_.map(n)
            source = map_.destination
            if map_.destination == destination:
                return n
    raise ValueError
