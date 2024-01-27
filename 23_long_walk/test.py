import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_a_walk(self):
        walk = solution.load_data("example.txt")
        assert isinstance(walk, solution.Walk)


    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 94


@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0