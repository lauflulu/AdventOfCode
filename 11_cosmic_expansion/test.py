import numpy as np
import pytest

import solution


@pytest.fixture
def universe():
    yield solution.load_data("example.txt")


class TestPart1:
    def test_that_data_is_loaded_as_numpy_array(self, universe):
        assert universe._map.shape == (10, 10)

    def test_that_the_example_universe_is_expanded(self, universe):
        expanded_universe = solution.load_data("example_expanded.txt")
        assert np.all(universe._expand() == expanded_universe._map)

    def test_that_galaxy_coordinates_are_complete_for_example(self, universe):
        assert len(universe._galaxy_coordinates()) == 9

    def test_that_galaxy_coordinates_are_found_for_example(self, universe):
        assert (0, 4) in universe._galaxy_coordinates()
        assert (11, 5) in universe._galaxy_coordinates()

    def test_that_shortest_paths_are_correct_for_example(self, universe):
        assert len(universe._galaxy_distances()) == 36

    def test_that_the_result_is_correct_for_example(self, universe):
        assert solution.get_result(universe) == 374


class TestPart2:
    @pytest.mark.parametrize("expansion_factor, result", [(10, 1030), (100, 8410)])
    def test_that_the_result_is_correct_for_example_with_expansion_factor(self, expansion_factor, result, universe):
        assert solution.get_result_2(universe) == result
