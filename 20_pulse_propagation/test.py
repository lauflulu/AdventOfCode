import pytest

import solution
from solution import Module, FlipFlopModule, BroadcasterModule, ConjunctionModule
from solution import HIGH, LOW, ON, OFF


class TestPart1:
    def test_that_data_is_loaded_as_a_dict_of_modules(self):
        modules = solution.load_data("example.txt")
        assert isinstance(modules["a"], Module)
        assert isinstance(modules["a"], FlipFlopModule)
        assert isinstance(modules["inv"], ConjunctionModule)
        assert isinstance(modules["broadcaster"], BroadcasterModule)

    def test_that_loaded_modules_have_destinations(self):
        modules = solution.load_data("example.txt")
        assert modules["a"].destinations == ["b"]
        assert modules["broadcaster"].destinations == ["a", "b", "c"]

    def test_that_flip_flop_does_nothing_when_receiving_high_pulse(self):
        modules = solution.load_data("example.txt")
        assert modules["a"].state is OFF
        modules["a"].receive(HIGH)
        assert modules["a"].state is OFF
        assert modules["a"].send() == []

    def test_that_flip_flop_changes_state_when_receiving_low_pulse(self):
        modules = solution.load_data("example.txt")
        assert modules["a"].state is OFF
        modules["a"].receive(LOW)
        assert modules["a"].state is ON
        modules["a"].receive(LOW)
        assert modules["a"].state is OFF

    def test_that_flip_flop_sends_high_pulse_when_off_and_receiving_low_pulse(self):
        modules = solution.load_data("example.txt")
        modules["a"].receive(LOW)
        assert modules["a"].send() == [("b", HIGH)]

    def test_that_flip_flop_sends_low_pulse_when_on_and_receiving_low_pulse(self):
        modules = solution.load_data("example.txt")
        modules["a"].state = ON
        modules["a"].receive(LOW)
        assert modules["a"].send() == [("b", LOW)]

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 0

@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
