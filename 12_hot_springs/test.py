import pytest

import solution
from solution import Record


class TestPart1:
    def test_load_data_returns_list_of_records(self):
        records = solution.load_data("example.txt")
        assert isinstance(records[0], Record)
        assert records[0]._springs == ".???.###."
        assert records[2]._groups == [1, 3, 1, 6]

    def test_matches(self):
        record = Record(".??..??...?##.", [1, 1, 3])
        assert record._matches(1, 0) is False
        assert record._matches(1, 1) is True
        assert record._matches(1, 2) is True
        assert record._matches(1, 3) is False
        assert record._matches(1, 10) is False
        assert record._matches(3, 10) is True
        assert record._matches(3, 1) is False

    def test_fit_indices(self):
        record = Record(".??..??...?##.", [1, 1, 3])
        assert record._fit_indices(1) == [1, 2, 5, 6]

    @pytest.mark.parametrize("row_index, number_of_arrangements", enumerate([1, 4, 1, 1, 4, 10]))
    def test_that_correct_number_of_combinations_is_computed_for_each_row(self, row_index, number_of_arrangements):
        records = solution.load_data("example.txt")
        assert records[row_index]._number_of_arrangements() == number_of_arrangements

    def test_that_result_is_correct_for_example(self):
        records = solution.load_data("example.txt")
        assert solution.get_result(records) == 21
