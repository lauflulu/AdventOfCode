import random

import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_a_list_of_blocks(self):
        blocks = solution.load_data("example.txt")
        assert blocks[0].cubes == [[1, 0, 1], [1, 1, 1], [1, 2, 1]]
        assert blocks[6].cubes == [[1, 1, 8], [1, 1, 9]]

    def test_that_blocks_are_sorted_by_lowest_z(self):
        blocks = solution.load_data("example.txt")
        random.shuffle(blocks)
        environment = solution.Environment(blocks)
        environment.sort_by_lowest_z()
        assert [block.cubes[0][2] for block in blocks] == [1, 2, 3, 4, 5, 6, 8]

    def test_that_blocks_are_sorted_by_highest_z(self):
        blocks = solution.load_data("example.txt")
        random.shuffle(blocks)
        environment = solution.Environment(blocks)
        environment.sort_by_highest_z()
        assert [block.cubes[-1][2] for block in blocks] == [1, 2, 3, 4, 5, 6, 9]

    def test_that_bottom_block_does_not_fall_below_the_ground(self):
        blocks = solution.load_data("example.txt")
        environment = solution.Environment(blocks)
        environment.fall()
        assert blocks[0].cubes == [[1, 0, 1], [1, 1, 1], [1, 2, 1]]

    def test_that_top_block_falls_to_the_top_of_the_pile(self):
        blocks = solution.load_data("example.txt")
        environment = solution.Environment(blocks)
        environment.fall()
        assert blocks[6].cubes == [[1, 1, 5], [1, 1, 6]]

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 5


@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
