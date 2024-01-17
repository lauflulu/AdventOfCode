from abc import ABC, abstractmethod


HIGH = True
LOW = False
ON = True
OFF = False


class Pulse:
    def __init__(self, sender_id, level, receiver_id):
        self.sender_id = sender_id
        self.level = level
        self.receiver_id = receiver_id

class Module(ABC):
    def __init__(self, destination_modules: list[str]):
        self.destinations = destination_modules
        self.inputs = []

    def register_inputs(self, self_id, modules: dict):
        for key, module in modules.items():
            if self_id in module.destinations:
                self.inputs.append(key)

    @abstractmethod
    def receive(self, pulse: bool):
        pass

    @abstractmethod
    def send(self) -> list:
        pass


class FlipFlopModule(Module):
    def __init__(self, destination_modules: list[str]):
        super().__init__(destination_modules)
        self.state = OFF
        self._last_received = None

    def receive(self, pulse: bool):
        self._last_received = pulse
        if pulse is LOW:
            self.state = not self.state

    def send(self) -> list:
        if self._last_received is HIGH:
            return []
        if self.state is ON:
            out_pulse  = HIGH
        else:
           out_pulse = LOW
        return [(destination, out_pulse) for destination in self.destinations]


class ConjunctionModule(Module):
    def __init__(self, destination_modules: list[str]):
        super().__init__(destination_modules)
        self.state = {}

    def register_inputs(self, self_id, modules: dict):
        super().register_inputs(self_id, modules)
        self.state = {key: LOW for key in self.inputs}

    def receive(self, pulse: bool):
        pass

    def send(self) -> list:
        pass


class BroadcasterModule(Module):

    def receive(self, pulse: bool):
        pass

    def send(self) -> list:
        pass


class TheButton:
    def __init__(self, modules):
        self.modules = modules
        self.pulses = []


def load_data(filename):
    modules = {}
    with open(filename, "r") as file:
        for line in file:
            description, destinations = line.split(" -> ")
            destinations = [destination.strip() for destination in destinations.split(",")]
            if description == "broadcaster":
                modules[description] = BroadcasterModule(destinations)
            elif description[0] == "%":
                modules[description[1:]] = FlipFlopModule(destinations)
            elif description[0] == "&":
                modules[description[1:]] = ConjunctionModule(destinations)
    for key, module in modules.items():
        module.register_inputs(key, modules)
    return modules


def get_result(data):
    pass


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
