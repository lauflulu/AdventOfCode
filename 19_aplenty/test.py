import pytest

import solution


class TestPart1:
    def test_that_loaded_data_contains_list_of_parts(self):
        _, parts = solution.load_data("example.txt")
        assert isinstance(parts[0], solution.Part)

    def test_that_loaded_data_contains_dict_of_workflows(self):
        workflows, _ = solution.load_data("example.txt")
        assert isinstance(workflows["in"], solution.Workflow)

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 19114

@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0