import pytest

import solution
import numpy as np

HISTORIES = [
    np.array([0, 3, 6, 9, 12, 15]),
    np.array([1, 3, 6, 10, 15, 21]),
    np.array([10, 13, 16, 21, 30, 45])
]


class TestPart1:
    def test_that_loaded_histories_is_list_of_numpy_arrays(self):
        histories = solution.load_data("example.txt")
        assert histories == HISTORIES

    @pytest.mark.parametrize("history, diff_to_next", [(HISTORIES[0], 3), (HISTORIES[1], 7), (HISTORIES[2], 23)])
    def test_that_get_difference_to_next_value_is_correct(self, history, diff_to_next):
        assert solution._get_difference_to_next_value(history) == diff_to_next

    @pytest.mark.parametrize("history, diff_to_next", [(HISTORIES[0], 18), (HISTORIES[1], 28), (HISTORIES[2], 68)])
    def test_that_get_next_value_is_correct(self, history, diff_to_next):
        assert solution._get_next_value(history) == diff_to_next

    def test_that_result_for_example_data_is_correct(self):
        assert solution.get_result(HISTORIES) == 114
