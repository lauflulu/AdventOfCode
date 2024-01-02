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


class TestPart2:

    def test_that_lens_is_added_in_empty_box(self):
        boxes = solution.Boxes()
        boxes.process("rn=1")
        assert boxes.get_box(0) == [("rn", 1)]

    def test_that_lens_is_appended_to_existing_box(self):
        boxes = solution.Boxes()
        boxes.process("rn=1")
        boxes.process("cm=2")
        assert boxes.get_box(0) == [("rn", 1), ("cm", 2)]

    def test_that_lens_is_removed_from_box(self):
        boxes = solution.Boxes()
        boxes.process("rn=1")
        boxes.process("rn-")
        assert boxes.get_box(0) == []

    def test_that_lens_is_replaced_in_box(self):
        boxes = solution.Boxes()
        boxes.process("rn=1")
        boxes.process("rn=2")
        assert boxes.get_box(0) == [("rn", 2)]

    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 145