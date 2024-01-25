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
        assert [block.lowest_z() for block in blocks] == [1, 2, 3, 4, 5, 6, 8]

    def test_that_blocks_are_sorted_by_highest_z(self):
        blocks = solution.load_data("example.txt")
        random.shuffle(blocks)
        environment = solution.Environment(blocks)
        environment.sort_by_highest_z()
        assert [block.highest_z() for block in blocks] == [1, 2, 3, 4, 5, 6, 9]

    def test_that_bottom_block_does_not_fall_below_the_ground(self):
        blocks = solution.load_data("example.txt")
        environment = solution.Environment(blocks)
        environment.settle()
        assert blocks[0].cubes == [[1, 0, 1], [1, 1, 1], [1, 2, 1]]

    def test_that_top_block_falls_to_the_top_of_the_pile(self):
        blocks = solution.load_data("example.txt")
        environment = solution.Environment(blocks)
        environment.settle()
        assert blocks[6].cubes == [[1, 1, 5], [1, 1, 6]]

    def test_that_supporting_blocks_are_correctly_identified(self):
        blocks = solution.load_data("example.txt")
        environment = solution.Environment(blocks)
        environment.settle()
        environment.identify_supports()
        assert blocks[0].supported_by == []
        assert blocks[1].supported_by == [blocks[0]]
        assert blocks[3].supported_by == [blocks[2], blocks[1]]

    def test_that_removable_blocks_are_correctly_identified(self):
        blocks = solution.load_data("example.txt")
        environment = solution.Environment(blocks)
        environment.settle()
        environment.identify_supports()
        assert blocks[0].removable == False
        assert blocks[1].removable == True
        assert blocks[2].removable == True
        assert blocks[3].removable == True
        assert blocks[4].removable == True
        assert blocks[5].removable == False
        assert blocks[6].removable == True

    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 5

    def test_that_result_is_correct_for_data(self):
        data = solution.load_data("data.txt")
        assert solution.get_result(data) == 416


class TestPart2:
    def test_that_settle_returns_count_of_blocks_that_fall(self):
        blocks = solution.load_data("example.txt")
        environment = solution.Environment(blocks)
        assert environment.settle() == 5

    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 7
