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
        assert records[row_index].count_arrangements() == number_of_arrangements

    @pytest.mark.parametrize("springs, groups, number", [
        ('.?#??#??.???????', [1, 1, 1, 1, 3], 7),  # first two indices need to be forced
        ('.##?##???.???', [2, 2, 2], 3)  # consecutive forced indices
    ])
    def test_number_of_arrangements_for_additional_examples(self, springs, groups, number):
        record = Record(springs, groups)
        assert record.count_arrangements() == number

    def test_forced_indices(self):
        record = Record('.?#??#??.???????', [1, 1, 1, 1, 3])
        assert record._forced_indices() == [2, 5]

    def test_that_result_is_correct_for_example(self):
        records = solution.load_data("example.txt")
        assert solution.get_result(records) == 21


class TestPart2:
    @pytest.mark.parametrize("springs, groups, unfolded_springs, unfolded_groups", [
        (".#", [1], "..#?.#?.#?.#?.#.", [1, 1, 1, 1, 1]),
        ("???.###", [1, 1, 3], ".???.###????.###????.###????.###????.###.", [1, 1, 3] * 5)
    ])
    def test_that_springs_and_groups_unfold_and_are_padded(self, springs, groups, unfolded_springs, unfolded_groups):
        record = Record(springs, groups)
        assert record._unfolded_springs() == unfolded_springs
        assert record._unfolded_groups() == unfolded_groups

    def test_that_correct_number_of_combinations_is_computed_for_unfolded_springs_for_simple_example(self):
        record = Record(".??", [1])
        assert record.unfolded_arrangements() == 534

    @pytest.mark.parametrize("row_index, unfolded_arrangements", [
        (0, 1),
        (1, 16384),
        # (2, 1),
        (3, 16),
        (4, 2500),
        # (5, 506250)
    ])
    def test_that_correct_number_of_combinations_is_computed_for_unfolded_springs(
            self, row_index, unfolded_arrangements):
        records = solution.load_data("example.txt")
        assert records[row_index].unfolded_arrangements() == unfolded_arrangements
