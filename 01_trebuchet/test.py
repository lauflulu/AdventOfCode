import pytest

import solution


class TestPartOne:
    def test_that_read_example_data_is_the_correct_list(self):
        assert solution.read_data("example_data.txt") == ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

    @pytest.mark.parametrize("code_line, expected_result", [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ])
    def test_that_first_and_last_digits_are_extracted(self, code_line, expected_result):
        result = solution._extract_two_digits(code_line)
        assert result == expected_result

    def test_that_the_correct_sum_is_computed_for_example_data(self):
        example_data = solution.read_data("example_data.txt")
        assert solution.compute_total_sum(example_data) == 142


class TestPartTwo:
    pass