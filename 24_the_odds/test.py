import numpy as np
import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_a_list_of_hailstones(self):
        hailstones = solution.load_data("example.txt")
        assert isinstance(hailstones, list)
        assert isinstance(hailstones[0], solution.Hailstone)

    def test_that_hailstone_parses_line_correctly(self):
        hailstones = solution.load_data("example.txt")
        assert np.all(hailstones[0].start_position == np.array([19, 13, 30]))
        assert np.all(hailstones[0].velocity == np.array([-2, 1, -2]))

    def test_that_intersections_are_found_correctly(self):
        hailstones = solution.load_data("example.txt")
        intersection = solution.Intersection(a=hailstones[0], b=hailstones[1], limits=(7, 27))
        assert pytest.approx(14.333, abs=0.1) == intersection.x
        assert pytest.approx(15.333, abs=0.1) == intersection.y
        assert intersection.forward is True
        assert intersection.in_box is True

    def test_that_parallel_trajectories_are_not_intersecting(self):
        hailstones = solution.load_data("example.txt")
        intersection = solution.Intersection(a=hailstones[1], b=hailstones[2], limits=(7, 27))
        assert intersection.forward is False
        assert intersection.in_box is False

    def test_that_result_is_correct_for_example(self):
        hailstones = solution.load_data("example.txt")
        assert solution.get_result(hailstones, limits=(7, 27)) == 2


class TestPart2:
    def test_that_initial_position_is_found_by_solving_nonlinear_equations_given_three_hailstones(self):
        hailstones = solution.load_data("example.txt")
        assert solution.solve_initial_position(hailstones[:3]) == (24, 13, 10)

    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 47
