import numpy as np
import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_a_list_of_hailstones(self):
        hailstones = solution.load_data("example.txt")
        assert isinstance(hailstones, list)
        assert isinstance(hailstones[0], solution.Hailstone)

    def test_that_hailstone_parses_line_correctly(self):
        hailstones = solution.load_data("example.txt")
        assert np.all(hailstones[0].start_position == np.array([19, 13, 30]))
        assert np.all(hailstones[0].velocity == np.array([-2, 1, -2]))

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 0


@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0