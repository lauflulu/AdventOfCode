import pytest

import solution
from solution import Module, FlipFlopModule, BroadcasterModule, ConjunctionModule


class TestPart1:
    def test_that_data_is_loaded_as_a_dict_of_modules(self):
        modules = solution.load_data("example.txt")
        assert isinstance(modules["a"], Module)
        assert isinstance(modules["a"], FlipFlopModule)
        assert isinstance(modules["inv"], ConjunctionModule)
        assert isinstance(modules["broadcaster"], BroadcasterModule)

    def test_that_loaded_modules_have_destinations(self):
        modules = solution.load_data("example.txt")
        assert modules["a"].destinations == ["b"]
        assert modules["broadcaster"].destinations == ["a", "b", "c"]

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 0

@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
