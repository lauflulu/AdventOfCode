import pytest

import solution
from solution import HandTypes


class TestPart1:
    def test_that_hands_are_loaded_from_example_data(self):
        hands = solution.load_data("example.txt")
        assert hands[0].cards == '32T3K'
        assert hands[0].bid == 765

    @pytest.mark.parametrize("cards, type_", [
        ('AAAAA', HandTypes.FIVE),
        ('AA8AA', HandTypes.FOUR),
        ('23332', HandTypes.FULL_HOUSE),
        ('TTT98', HandTypes.THREE),
        ('23432', HandTypes.TWO_PAIR),
        ('A23A4', HandTypes.ONE_PAIR),
        ('23456', HandTypes.HIGH_CARD),
    ])
    def test_that_types_are_correct_for_examples(self, cards, type_):
        assert solution.Hand(cards, 1).type() == type_

    @pytest.mark.parametrize("cards, values", [
        ('AAAAA', [0, 0, 0, 0, 0]),
        ('TTT98', [4, 4, 4, 5, 6]),
        ('23432', [12, 11, 10, 11, 12]),
    ])
    def test_that_cards_are_valued_correctly(self, cards, values):
        assert solution.Hand(cards, 1).values() == values
