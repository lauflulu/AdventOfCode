import pytest

import solution


class TestPart1:
    def test_load_data_returns_list_of_records(self):
        records = solution.load_data("example.txt")
        assert isinstance(records[0], solution.Record)

    @pytest.mark.parametrize("row_index, number_of_arrangements", enumerate([1, 4, 1, 1, 4, 10]))
    def test_that_correct_number_of_combinations_is_computed_for_each_row(self, row_index, number_of_arrangements):
        records = solution.load_data("example.txt")
        assert records[row_index]._number_of_arrangements() == number_of_arrangements

    def test_that_result_is_correct_for_example(self):
        records = solution.load_data("example.txt")
        assert solution.get_result(records) == 21
