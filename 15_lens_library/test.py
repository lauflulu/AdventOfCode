import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_list_of_strings(self):
        data = solution.load_data("example.txt")
        assert data[0] == "rn=1"

    @pytest.mark.parametrize("instruction, result", [
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47)
    ])
    def test_that_result_are_correct_for_each_instruction(self, instruction, result):
        assert solution.evaluate(instruction) == result

    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 1320