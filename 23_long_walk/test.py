import numpy as np
import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_a_walk(self):
        walk = solution.load_data("example.txt")
        assert isinstance(walk, solution.Walk)

    def test_that_walk_has_trail_map_of_correct_shape(self):
        walk = solution.load_data("example.txt")
        assert walk.trail_map.shape == (23, 23)

    def test_that_start_is_marked_as_node(self):
        walk = solution.load_data("example.txt")
        assert (0, 1) in walk.trail_graph

    def test_that_intersections_are_marked_as_nodes(self):
        walk = solution.load_data("example.txt")
        walk.explore()
        assert (5, 3) in walk.trail_graph

    @pytest.mark.parametrize("yx, last_direction, expected", [
        (np.array((1, 1)), "s", ["e"]),
        (np.array((5, 3)), "s", ["s", "e"]),
        (np.array((3, 4)), "w", ["w"]),
    ])
    def test_that_possible_directions_are_found(self, yx, last_direction, expected):
        walk = solution.load_data("example.txt")
        assert walk.possible_directions(yx, last_direction) == expected

    def test_that_first_segment_has_the_correct_distance(self):
        walk = solution.load_data("example.txt")
        walk.explore()
        assert walk.trail_graph[(0, 1)][(5, 3)] == 15

    def test_that_finish_is_marked_as_out_node(self):
        walk = solution.load_data("example.txt")
        walk.explore()
        assert any((22, 21) in out_nodes for out_nodes in walk.trail_graph.values())

    def test_that_uphill_segments_are_not_explored(self):
        walk = solution.load_data("example.txt")
        walk.explore()
        assert (19, 13) not in walk.trail_graph[(19, 19)]
        assert (11, 21) not in walk.trail_graph[(19, 19)]

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 94


@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0