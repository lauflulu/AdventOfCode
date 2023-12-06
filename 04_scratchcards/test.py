import pytest
import solution


def test_that_loaded_example_data_is_a_list_of_cards():
    assert isinstance(solution.load_data("example.txt")[0], solution.Card)
    assert solution.load_data("example.txt")[0].scratch_numbers == (83, 86,  6, 31, 17,  9, 48, 53)


@pytest.mark.parametrize("card_index, value", [(0, 8), (1, 2), (2, 2), (3, 1), (4, 0), (5, 0)])
def test_that_the_card_value_is_correct_for_example_data(card_index, value):
    data = solution.load_data("example.txt")
    assert data[card_index].value() == value


def test_that_result_is_correct_for_example_data():
    data = solution.load_data("example.txt")
    assert solution.get_result(data) == 13
