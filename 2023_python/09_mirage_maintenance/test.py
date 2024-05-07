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
        for i in range(len(histories)):
            assert np.all(histories[0] == HISTORIES[0])

    @pytest.mark.parametrize("history, next_value", [(HISTORIES[0], 18), (HISTORIES[1], 28), (HISTORIES[2], 68)])
    def test_that_get_next_value_is_correct(self, history, next_value):
        assert solution._get_next_value(history) == next_value

    def test_that_result_for_example_data_is_correct(self):
        assert solution.get_result(HISTORIES) == 114


class TestPart2:
    @pytest.mark.parametrize("history, previous_value", [(HISTORIES[0], -3), (HISTORIES[1], 0), (HISTORIES[2], 5)])
    def test_that_get_previous_value_is_correct(self, history, previous_value):
        assert solution._get_previous_value(history) == previous_value

    def test_that_result_for_example_data_is_correct(self):
        assert solution.get_result_2(HISTORIES) == 2
