import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_adjacency_matrix(self):
        graph = solution.load_data("example.txt")
        assert graph.shape == (15, 15)

    @pytest.mark.skip(reason="Not implemented yet")
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 54


@pytest.mark.skip(reason="Not implemented yet")
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
