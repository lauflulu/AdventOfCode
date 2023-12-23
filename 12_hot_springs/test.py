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
        assert record._get_forced_indices() == [2, 5]

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
        assert record._unfolded_springs(5) == unfolded_springs
        assert record._unfolded_groups(5) == unfolded_groups

    def test_that_correct_number_of_combinations_is_computed_fast_enough_when_order_matters(self):
        record = Record(".??", [1])
        assert record._unfolded_arrangements() == 534

    @pytest.mark.parametrize("partial_indices, result", [
        ([1], True), ([1, 3], False), ([1, 9], True)])
    def test_that_forced_indices_condition_can_be_fulfilled(self, partial_indices, result):
        record = Record(".#?????", [1])
        record._unfold(5)
        assert record._forced_indices_can_be_filled([1, 3]) is False

    def test_that_correct_number_of_combinations_is_computed_fast_enough_when_forced_indices_matter(self):
        record = Record(".#?????", [1])
        assert record._unfolded_arrangements() == 1

    @pytest.mark.parametrize("springs, groups, locked", [
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], True),
        ("?###????????", [3, 2, 1], True),
        ("?#??????????", [3, 2, 1], False),
        # left: ?.??...??#? = 2, right: ??.??...??# = 2, two: ?.??...??#??.??...??#
        ("?.??...??#", [2, 3], False),
        ("?????????#?#", [1, 1, 7], False)
        # ????????? #7#7777 ?1?1? 7#7#777 ?1?1? 77#7#77 ?1?1? 777#7#
    ])
    def test_that_locked_determines_whether_folds_are_locked(self, springs, groups, locked):
        record = Record(springs, groups)
        assert record._locked()[0] is locked

    @pytest.mark.parametrize("springs, groups, unfolded_arrangements", [
        ("???.###", [1, 1, 3], 1),  # 41 ms
        (".??..??...?##.", [1, 1, 3], 16384),  # 2.7 s, if locking condition: first_fold*second_fold**4=4*8**4
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),  # 2:40 min, locked: 1*1**4
        ("????.#...#...", [4, 1, 1], 16),  # 650 ms
        ("????.######..#####.", [1, 6, 5], 2500),  # 450 ms
        ("?###????????", [3, 2, 1], 506250),  # 4:40 min 15**4*10
        ("?.??...??#", [2, 3], 81),
    ])
    def test_that_correct_number_of_combinations_is_computed_for_unfolded_springs(
            self, springs, groups, unfolded_arrangements):
        record = Record(springs, groups)
        assert record.count_unfolded_arrangements() == unfolded_arrangements

    def test_another_slow_case_from_data(self):
        record = Record("?????????#?#", [1, 1, 7])
        print(record._locked()[0])
