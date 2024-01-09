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

    def test_that_loop_rotation_is_precalculated(self, lagoon):
        assert lagoon.rotation > 0

    def test_that_the_outline_ends_where_it_starts(self, lagoon):
        lagoon.dig_outline()
        assert np.all(lagoon._yx == np.array((0, 0)))

    def test_that_the_outline_has_correct_volume(self, lagoon):
        lagoon.dig_outline()
        assert lagoon.volume() == 38

    def test_that_the_inside_is_digged_out(self, lagoon):
        lagoon.dig_outline()
        lagoon.dig_inner()
        assert lagoon.volume() == 62

    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 62


class TestPart2:
    def test_that_vertices_are_found_correctly(self, lagoon):
        assert np.all(lagoon.vertices()[0] == np.array((0, 0)))
        assert np.all(lagoon.vertices()[1] == np.array((0, 6)))
        assert np.all(lagoon.vertices()[2] == np.array((5, 6)))
        assert np.all(lagoon.vertices()[3] == np.array((5, 4)))
        assert np.all(lagoon.vertices()[-1] == np.array((0, 0)))

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 952408144115