class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid


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
