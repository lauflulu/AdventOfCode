import pytest
import solution
import numpy as np


class TestExampleData:
    def test_that_loaded_example_data_has_the_correct_shape(self):
        loaded_data = solution.load_data("example.txt")
        assert loaded_data.shape == (10, 10)

    def test_that_loaded_data_only_contains_allowed_symbols(self):
        loaded_data = solution._replace_symbols(solution.load_data("example.txt"))
        assert np.all(np.isin(loaded_data, ['*', '.'] + [str(n) for n in range(10)]))

    def test_that_only_part_numbers_are_found_in_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_part_numbers(data) == [467, 35, 633, 617, 592, 755, 664, 598]

    def test_that_the_answer_is_correct_for_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 4361


class TestKernel:
    @pytest.mark.parametrize(" x, y, has_neighbor_", [
        (0, 0, False),  # corner top left
        (2, 0, True),  # symbol diagonal
        (3, 2, True),  # symbol above
        (9, 9, False),  # corner bottom right
        (2, 4, True),  # symbol right
        (8, 5, False)  # no neighbor
    ])
    def test_that_neighboring_symbols_are_detected_in_example_data_at_position(self, x, y, has_neighbor_):
        data = solution.load_data("example.txt")
        assert solution._has_neighbor(data, x, y) is has_neighbor_

    def test_that_sliced_data_has_correct_shape(self):
        data = solution.load_data("example.txt")
        assert solution._slice_neighbors(data, 2, 2).shape == (3, 3)

    @pytest.mark.parametrize(" x, y", [(1, 1), (2, 2), (3, 1)])
    def test_that_sliced_data_is_centered(self, x, y):
        data = solution.load_data("example.txt")
        center_of_slice = solution._slice_neighbors(data, x, y)[1, 1]
        assert center_of_slice == data[y, x]


class TestPart2:
    def test_that_the_gear_ratios_are_found_in_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_gear_ratios(data) == [16345, 755 * 598]

    def test_that_the_result_is_correct_for_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 467835

    def test_that_only_non_adjacent_digits_are_considered_as_parts(self):
        neighbors = np.array([[False, False, False], [False, True, True], [True, True, False]])
        assert solution._non_adjacent_part_indices(neighbors) == [(1, 1), (2, 0)]
