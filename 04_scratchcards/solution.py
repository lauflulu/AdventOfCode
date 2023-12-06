class Card:

    def __init__(self, winning_numbers, scratch_numbers):
        self.winning_numbers: tuple = winning_numbers
        self.scratch_numbers: tuple = scratch_numbers

    def value(self):
        pass


def load_data(filepath) -> list[Card]:
    pass


def get_result(data) -> int:
    pass
