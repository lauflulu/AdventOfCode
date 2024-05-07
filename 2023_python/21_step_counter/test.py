import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded(self):
        gardener = solution.load_data("example.txt")
        assert gardener.garden.shape == (11, 11)
        assert gardener.start_yx == (5, 5)

    @pytest.mark.parametrize("n_steps, n_tiles", [(1, 2), (2, 4), (3, 6), (6, 16)])
    def test_that_number_of_reachable_tiles_after_n_steps_is_correct(self, n_steps, n_tiles):
        gardener = solution.load_data("example.txt")
        gardener.step(n_steps)
        assert gardener.number_of_reachable_tiles() == n_tiles

    def test_that_result_is_correct_for_example(self):
        gardener = solution.load_data("example.txt")
        assert solution.get_result(gardener) == 42


@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        gardener = solution.load_data("example.txt")
        assert solution.get_result_2(gardener) == 0