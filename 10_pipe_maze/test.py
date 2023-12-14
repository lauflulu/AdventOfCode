import pytest
import solution


class TestPart1:
    @pytest.mark.parametrize("filename, result", [("example.txt", 4), ("example_2.txt", 8)])
    def test_that_result_is_correct_for_example_data(self, filename, result):
        maze = solution.load_data(filename)
        assert solution.get_result(maze) == result
