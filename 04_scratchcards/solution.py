class Card:

    def __init__(self, winning_numbers: tuple[int], scratch_numbers: tuple[int]):
        self.winning_numbers: tuple[int] = winning_numbers
        self.scratch_numbers: tuple[int] = scratch_numbers

    def value(self):
        matches = 0
        for number in self.scratch_numbers:
            if number in self.winning_numbers:
                matches += 1
        if matches == 0:
            return 0
        return 2**(matches - 1)


def load_data(filepath: str) -> list[Card]:
    with open(filepath, 'r') as file:
        return [_parse(line) for line in file]


def _parse(line: str):
    _, numbers = line.split(':')
    winning_numbers, scratch_numbers = numbers.split('|')
    return Card(_parse_numbers(winning_numbers), _parse_numbers(scratch_numbers))


def _parse_numbers(numbers: str):
    return tuple([int(number.strip()) for number in numbers.split(' ') if not number == ''])


def get_result(cards: list[Card]) -> int:
    return sum([card.value() for card in cards])


def main():
    cards = load_data("data.txt")
    print(get_result(cards))


if __name__ == '__main__':
    main()