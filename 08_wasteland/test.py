import pytest

import solution


class TestPart1:
    def test_that_load_data_returns_the_correct_types(self):
        instructions, maps = solution.load_data("example.txt")
        assert instructions == 'RL'
        assert maps['AAA'].left == 'BBB'
        assert maps['AAA'].right == 'CCC'
        assert 'ZZZ' in maps

    @pytest.mark.parametrize("filename, result", [("example.txt", 2), ("example_2.txt", 6)])
    def test_that_result_is_correct_for_example(self, filename, result):
        instructions, maps = solution.load_data(filename)
        assert solution.get_result(instructions, maps) == result
