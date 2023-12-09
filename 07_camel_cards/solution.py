from enum import Enum


class HandTypes(Enum):
    FIVE = 0
    FOUR = 1
    FULL_HOUSE = 2
    THREE = 3
    TWO_PAIR = 4
    ONE_PAIR = 5
    HIGH_CARD = 6


CARD_STRENGTHS = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

    def type(self):
        pass

    def values(self):
        return [CARD_STRENGTHS.index(card) for card in self.cards]


def load_data(filename):
    with open(filename, 'r') as file:
        hands = []
        for line in file:
            cards, bid = line.split(' ')
            hands.append(Hand(cards.strip(), int(bid.strip())))
        return hands


def get_result(data):
    pass


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
