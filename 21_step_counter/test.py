import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded(self):
        gardener = solution.load_data("example.txt")
        assert gardener.garden.shape == (11, 11)
        assert gardener.start_yx == (5, 5)

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        gardener = solution.load_data("example.txt")
        gardener.step(6)
        assert solution.get_result(gardener) == 16


@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        gardener = solution.load_data("example.txt")
        assert solution.get_result_2(gardener) == 0