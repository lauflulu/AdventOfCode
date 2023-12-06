import re


class Card:

    def __init__(self, index: int, winning_numbers: tuple[int], scratch_numbers: tuple[int]):
        self.index = index
        self.winning_numbers: tuple[int] = winning_numbers
        self.scratch_numbers: tuple[int] = scratch_numbers

    def value(self):
        matches = self.matches()
        if matches == 0:
            return 0
        return 2**(matches - 1)

    def matches(self):
        matches = 0
        for number in self.scratch_numbers:
            if number in self.winning_numbers:
                matches += 1
        return matches


class CardStack:
    def __init__(self, cards: list[Card]):
        self._processed = {i: [] for i in range(len(cards))}
        self._unprocessed = {i: [card] for i, card in enumerate(cards)}

    def counts(self) -> list[int]:
        return [len(card_instance) for card_instance in self._processed.values()]

    def total_count(self) -> int:
        return sum(self.counts())


def load_data(filepath: str) -> list[Card]:
    with open(filepath, 'r') as file:
        return [_parse(line) for line in file]


def _parse(line: str):
    index, numbers = line.split(':')
    index = int(re.findall(r'[0-9]+', index)[0]) - 1
    winning_numbers, scratch_numbers = numbers.split('|')
    return Card(index, _parse_numbers(winning_numbers), _parse_numbers(scratch_numbers))


def _parse_numbers(numbers: str):
    return tuple([int(number.strip()) for number in numbers.split(' ') if not number == ''])


def get_result(cards: list[Card]) -> int:
    return sum([card.value() for card in cards])


def get_result_2(cards: list[Card]) -> int:
    return CardStack(cards).total_count()


def main():
    cards = load_data("data.txt")
    print(get_result(cards))
    print(get_result_2(cards))


if __name__ == '__main__':
    main()
