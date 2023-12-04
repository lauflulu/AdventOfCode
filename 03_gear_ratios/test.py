import pytest
import solution
import numpy as np


class TestExampleData:
    def test_that_loaded_example_data_has_the_correct_shape(self):
        loaded_data = solution.load_data("example.txt")
        assert loaded_data.shape == (10, 10)

    def test_that_loaded_data_only_contains_allowed_symbols(self):
        loaded_data = solution.load_data("example.txt")
        assert np.all(np.isin(loaded_data, ['*', '.'] + [str(n) for n in range(10)]))

    def test_that_only_part_numbers_are_found_in_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_part_numbers(data) == [467, 35, 633, 617, 592, 755, 664, 598]

    def test_that_the_answer_is_correct_for_example_data(self):
        assert solution.get_result() == 4361


class TestKernel:
    @pytest.mark.parametrize(" x, y, has_neighbor_", [
        (0, 0, False),  # corner top left
        (2, 0, True),  # symbol diagonal
        (3, 2, True),  # symbol above
        (9, 9, False),  # corner bottom right
        (2, 4, True),  # symbol right
    ])
    def test_that_neighboring_symbols_are_detected_in_example_data_at_position(self, x, y, has_neighbor_):
        data = solution.load_data("example.txt")
        assert solution._has_neighbor(data, x, y) is has_neighbor_
