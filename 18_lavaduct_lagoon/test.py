import numpy as np
import pytest

import solution


@pytest.fixture
def lagoon():
    instructions = solution.load_data("example.txt")
    return solution.Lagoon(instructions)


class TestPart1:
    def test_that_instructions_are_loaded(self):
        instructions = solution.load_data("example.txt")
        assert np.all(instructions[0].direction == np.array((0, 1)))
        assert instructions[0].distance == 6
        assert instructions[0].color == '#70c710'

    def test_that_shape_can_be_pre_calculated(self, lagoon):
        assert lagoon.shape == (10, 7)

    def test_that_start_coordinates_can_be_precalculated(self, lagoon):
        assert lagoon.start == (0, 0)

    def test_that_the_outline_ends_where_it_starts(self, lagoon):
        lagoon.dig_outline()
        assert np.all(lagoon._yx == np.array((0, 0)))

    def test_that_the_outline_has_correct_volume(self, lagoon):
        lagoon.dig_outline()
        assert lagoon.volume() == 38

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 62

@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0