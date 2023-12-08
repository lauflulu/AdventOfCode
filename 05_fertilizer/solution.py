class Map:

    def __init__(self):
        self.source = ''
        self.destination = ''
        self.ranges: list[Range] = []

    def map(self, source_number):
        for range_ in self.ranges:
            destination_number = range_.destination(source_number)
            if destination_number is not None:
                return destination_number
        return source_number


class Range:
    def __init__(self):
        self.source_start = 0
        self.destination_start = 0
        self.length = 0

    def destination(self, source_number) -> int | None:
        if self.source_start <= source_number <= self.source_start + self.length:
            return self.source_start - source_number + self.destination_start


def load_data(filename) -> tuple[list[int], list[Map]]:
    pass


def map_categories(number, source, destination):
    pass
