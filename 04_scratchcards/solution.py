class Card:

    def __init__(self, winning_numbers: tuple[int], scratch_numbers: tuple[int]):
        self.winning_numbers: tuple[int] = winning_numbers
        self.scratch_numbers: tuple[int] = scratch_numbers

    def value(self):
        pass


def load_data(filepath: str) -> list[Card]:
    with open(filepath, 'r') as file:
        return [_parse(line) for line in file]


def _parse(line: str):
    _, numbers = line.split(':')
    winning_numbers, scratch_numbers = numbers.split('|')
    winning_numbers = tuple([int(number.strip()) for number in winning_numbers.split(' ') if not number == ''])
    scratch_numbers = tuple([int(number.strip()) for number in scratch_numbers.split(' ') if not number == ''])
    return Card(winning_numbers, scratch_numbers)


def get_result(data) -> int:
    pass
