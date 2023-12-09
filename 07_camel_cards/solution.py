from enum import IntEnum


class HandTypes(IntEnum):
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
        card_count = [self.cards.count(i) for i in set(self.cards)]
        card_count.sort(reverse=True)
        if card_count == [5]:
            return HandTypes.FIVE
        if card_count == [4, 1]:
            return HandTypes.FOUR
        if card_count == [3, 2]:
            return HandTypes.FULL_HOUSE
        if card_count == [3, 1, 1]:
            return HandTypes.THREE
        if card_count == [2, 2, 1]:
            return HandTypes.TWO_PAIR
        if card_count == [2, 1, 1, 1]:
            return HandTypes.ONE_PAIR
        return HandTypes.HIGH_CARD

    def values(self):
        return [CARD_STRENGTHS.index(card) for card in self.cards]

    def score(self):
        return [int(self.type())] + self.values()


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
