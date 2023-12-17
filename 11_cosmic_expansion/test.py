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
        assert np.all(universe._map_expanded == expanded_universe._map)

    def test_that_galaxy_coordinates_are_complete_for_example(self, universe):
        assert len(universe._galaxy_coordinates()) == 9

    def test_that_galaxy_coordinates_are_found_for_example(self, universe):
        assert (0, 4) in universe._galaxy_coordinates()
        assert (11, 5) in universe._galaxy_coordinates()

    def test_that_shortest_paths_are_correct_for_example(self, universe):
        print(universe.lengths_of_shortest_paths())

    def test_that_the_result_is_correct_for_example(self, universe):
        print(solution.get_result(universe))

