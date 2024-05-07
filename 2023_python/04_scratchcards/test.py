import pytest
import solution


class TestPart1:
    def test_that_loaded_example_data_is_a_list_of_cards(self):
        cards = solution.load_data("example.txt")
        assert isinstance(cards[0], solution.Card)
        assert cards[0].scratch_numbers == (83, 86, 6, 31, 17, 9, 48, 53)
        assert cards[3].index == 3

    @pytest.mark.parametrize("card_index, value", [(0, 8), (1, 2), (2, 2), (3, 1), (4, 0), (5, 0)])
    def test_that_the_card_value_is_correct_for_example_data(self, card_index, value):
        data = solution.load_data("example.txt")
        assert data[card_index].value() == value

    def test_that_result_is_correct_for_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 13


class TestPart2:
    def test_that_fully_processed_card_stack_contains_the_correct_count_of_cards(self):
        cards = solution.load_data("example.txt")
        card_stack = solution.CardStack(cards)
        assert card_stack.counts() == [1, 2, 4, 8, 14, 1]

    def test_that_result_is_correct_for_example_data(self):
        cards = solution.load_data("example.txt")
        card_stack = solution.CardStack(cards)
        assert card_stack.total_count() == 30

