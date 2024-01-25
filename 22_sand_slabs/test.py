import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_a_list_of_blocks(self):
        blocks = solution.load_data("example.txt")
        assert blocks[0].cubes == [[1, 0, 1], [1, 1, 1], [1, 2, 1]]
        assert blocks[6].cubes == [[1, 1, 8], [1, 1, 9]]

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 5


@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
