import numpy as np
import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_a_walk(self):
        walk = solution.load_data("example.txt")
        assert isinstance(walk, solution.Walk)

    def test_that_walk_has_trail_map_of_correct_shape(self):
        walk = solution.load_data("example.txt")
        assert walk.trail_map.shape == (23, 23)


    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 94


@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0