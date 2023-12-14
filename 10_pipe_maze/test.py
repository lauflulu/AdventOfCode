import pytest
import solution


class TestPart1:
    def test_load_data_returns_maze(self):
        maze = solution.load_data("example.txt")
        assert maze._tiles.shape == (5, 5)

    @pytest.mark.parametrize("filename, x, y", [("example.txt", 1, 1), ("example_2.txt", 0, 2)])
    def test_that_start_position_is_found(self, filename, x, y):
        maze = solution.load_data(filename)
        assert maze._current_x == x
        assert maze._current_y == y

    @pytest.mark.parametrize("filename, result", [("example.txt", 4), ("example_2.txt", 8)])
    def test_that_result_is_correct_for_example_data(self, filename, result):
        maze = solution.load_data(filename)
        assert solution.get_result(maze) == result
