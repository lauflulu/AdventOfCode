import pytest

import solution
from solution import Module, FlipFlopModule, BroadcasterModule, ConjunctionModule
from solution import HIGH, LOW, ON, OFF, Pulse


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
        modules["a"].receive(Pulse("broadcaster", HIGH, "a"))
        assert modules["a"].state is OFF
        assert modules["a"].send() == []

    def test_that_flip_flop_changes_state_when_receiving_low_pulse(self):
        modules = solution.load_data("example.txt")
        assert modules["a"].state is OFF
        modules["a"].receive(Pulse("broadcaster", LOW, "a"))
        assert modules["a"].state is ON
        modules["a"].receive(Pulse("broadcaster", LOW, "a"))
        assert modules["a"].state is OFF

    def test_that_flip_flop_sends_high_pulse_when_off_and_receiving_low_pulse(self):
        modules = solution.load_data("example.txt")
        modules["a"].receive(Pulse("broadcaster", LOW, "a"))
        assert modules["a"].send() == [("b", HIGH)]

    def test_that_flip_flop_sends_low_pulse_when_on_and_receiving_low_pulse(self):
        modules = solution.load_data("example.txt")
        modules["a"].state = ON
        modules["a"].receive(Pulse("broadcaster", LOW, "a"))
        assert modules["a"].send() == [("b", LOW)]

    def test_that_conjunction_modules_know_their_input_module(self):
        modules = solution.load_data("example.txt")
        assert modules["inv"].inputs == ["c"]

    def test_that_conjunction_modules_know_their_input_modules(self):
        modules = solution.load_data("data.txt")
        assert modules["nl"].inputs == ["tg", "pr", "hd", "rh", "pf", "rl", "qz"]

    def test_that_state_of_conjunction_modules_is_initialized_to_low(self):
        modules = solution.load_data("data.txt")
        assert [state is LOW for state in modules["nl"].state.values()]

    def test_that_conjunction_modules_remember_last_received_pulse_for_each_input(self):
        modules = solution.load_data("example.txt")
        modules["inv"].receive(Pulse("c", HIGH, "inv"))
        assert modules["inv"].state["c"] == HIGH

    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 0

@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
