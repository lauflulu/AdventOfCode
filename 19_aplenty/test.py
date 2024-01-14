import pytest

import solution
from solution import Rule, Part


class TestPart1:
    def test_that_loaded_data_contains_list_of_parts(self):
        _, parts = solution.load_data("example.txt")
        assert isinstance(parts[0], solution.Part)

    def test_that_parts_are_loaded_with_correct_ratings(self):
        _, parts = solution.load_data("example.txt")
        assert parts[0].ratings == {"x": 787, "m": 2655, "a": 1222, "s": 2876}

    def test_that_loaded_data_contains_dict_of_workflows(self):
        workflows, _ = solution.load_data("example.txt")
        assert isinstance(workflows["in"], solution.Workflow)

    def test_that_workflows_are_loaded_with_correct_rules(self):
        workflows, _ = solution.load_data("example.txt")
        assert workflows["in"].rules[0]._condition == ('s', '<', 1351)
        assert workflows["in"].rules[0]._return == "px"
        assert workflows["in"].rules[1]._condition == ('x', '>', -1)
        assert workflows["in"].rules[1]._return == "qqz"

    @pytest.mark.parametrize("rule, part, expected", [
        (Rule("s>2770:qs"), Part("{x=787,m=2655,a=1222,s=2876}"), "qs"),
        (Rule("s<2770:qs"), Part("{x=787,m=2655,a=1222,s=2876}"), ""),
        (Rule("A"), Part("{x=787,m=2655,a=1222,s=2876}"), "A")
    ])
    def test_given_a_part_a_rule_is_evaluated_correctly(self, rule, part, expected):
        assert rule.evaluate(part) == expected


    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 19114

@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0