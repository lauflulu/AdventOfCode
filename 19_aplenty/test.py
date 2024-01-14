import pytest

import solution
from solution import Rule, Part, Workflow


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

    @pytest.mark.parametrize("workflow, part, expected", [
        (Workflow("s<1351:px,qqz"), Part("{x=787,m=2655,a=1222,s=2876}"), "qqz"),
        (Workflow("s>2770:qs,m<1801:hdj,R"), Part("{x=787,m=2655,a=1222,s=2876}"), "qs"),
        (Workflow("s>3448:A,lnx"), Part("{x=787,m=2655,a=1222,s=2876}"), "lnx"),
        (Workflow("m>1548:A,A"), Part("{x=787,m=2655,a=1222,s=2876}"), "A"),
    ])
    def test_given_a_part_a_workflow_is_evaluated_correctly(self, workflow, part, expected):
        assert workflow.evaluate(part) == expected

    @pytest.mark.skip
    @pytest.mark.parametrize("part, expected", [
        (Part("{x=787,m=2655,a=1222,s=2876}"), 7540),
        (Part("{x=1679,m=44,a=2067,s=496}"), 0),
        (Part("{x=2036,m=264,a=79,s=2244}"), 4623),
        (Part("{x=2461,m=1339,a=466,s=291}"), 0),
        (Part("{x=2127,m=1623,a=2188,s=1013}"), 6951),
    ])
    def test_given_all_workflows_a_part_is_rated_correctly(self, part, expected):
        pass

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 19114

@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0