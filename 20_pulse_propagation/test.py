import pytest

import solution
from solution import Module, FlipFlopModule, BroadcasterModule, ConjunctionModule
from solution import HIGH, LOW, ON, OFF, Pulse


def is_pulse(pulse_1: Pulse, pulse_2: Pulse):
    return (pulse_1.sender_id == pulse_2.sender_id
            and pulse_1.level == pulse_2.level
            and pulse_1.receiver_id == pulse_2.receiver_id)


class TestLoadData:
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


class TestFlipFlopModule:
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
        assert is_pulse(modules["a"].send()[0], Pulse("a", HIGH, "b"))

    def test_that_flip_flop_sends_low_pulse_when_on_and_receiving_low_pulse(self):
        modules = solution.load_data("example.txt")
        modules["a"].state = ON
        modules["a"].receive(Pulse("broadcaster", LOW, "a"))
        assert is_pulse(modules["a"].send()[0], Pulse("a", LOW, "b"))

class TestConjunctionModule:
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

    def test_that_conjunction_modules_sends_high_pulse_if_all_inputs_are_high(self):
        module = ConjunctionModule(module_id="x", destination_modules=["a", "b"])
        module.inputs = ["c", "d"]
        module.state = {key: HIGH for key in module.inputs}
        out_pulses = module.send()
        assert [out_pulse.level is HIGH for out_pulse in out_pulses]

    def test_that_conjunction_module_sends_low_pulse_if_at_least_one_input_is_low(self):
        module = ConjunctionModule(module_id="x", destination_modules=["a", "b"])
        module.inputs = ["c", "d"]
        module.state = {key: HIGH for key in module.inputs}
        module.receive(Pulse("c", LOW, "x"))
        out_pulses = module.send()
        assert [out_pulse.level is HIGH for out_pulse in out_pulses]


class TestBroadcasterModule:
    @pytest.mark.parametrize("level", [HIGH, LOW])
    def test_that_broadcaster_sends_a_received_pulse_to_its_destinations(self, level):
        module = BroadcasterModule(module_id="broadcaster", destination_modules=["a", "b", "c"])
        module.receive(Pulse("x", level, "broadcaster"))
        pulses = module.send()
        assert [pulse.level == level for pulse in pulses]

class TestPart1:
    @pytest.mark.skip
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 0

@pytest.mark.skip
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
