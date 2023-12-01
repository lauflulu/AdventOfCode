import pytest

import solution


EXAMPLE_DATA = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"


@pytest.mark.parametrize("code_line, expected_result", [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
])
def test_that_first_and_last_digits_are_extracted(code_line, expected_result):
    result = solution.extract_two_digits(code_line)
    assert result == expected_result


def test_that_the_correct_sum_is_computed_for_example_data():
    assert solution.answer(EXAMPLE_DATA) == 142
