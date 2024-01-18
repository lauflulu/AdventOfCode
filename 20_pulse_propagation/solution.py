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
    def __init__(self, module_id, destination_modules: list[str]):
        self.id = module_id
        self.destinations = destination_modules
        self.inputs = []

    def register_inputs(self, self_id, modules: dict):
        for key, module in modules.items():
            if self_id in module.destinations:
                self.inputs.append(key)

    @abstractmethod
    def receive(self, pulse: Pulse, n_push=0):
        pass

    @abstractmethod
    def send(self) -> list:
        pass


class FlipFlopModule(Module):
    def __init__(self, module_id, destination_modules: list[str]):
        super().__init__(module_id, destination_modules)
        self.state = OFF
        self._last_received = None

    def receive(self, pulse: Pulse, n_push=0):
        self._last_received = pulse.level
        if pulse.level is LOW:
            self.state = not self.state

    def send(self) -> list:
        if self._last_received is HIGH:
            return []
        if self.state is ON:
            return [Pulse(self.id, HIGH, destination) for destination in self.destinations]
        return [Pulse(self.id, LOW, destination) for destination in self.destinations]



class ConjunctionModule(Module):
    def __init__(self, module_id, destination_modules: list[str]):
        super().__init__(module_id, destination_modules)
        self.state = {}

    def register_inputs(self, self_id, modules: dict):
        super().register_inputs(self_id, modules)
        self.state = {key: LOW for key in self.inputs}

    def receive(self, pulse: Pulse, n_push=0):
        self.state[pulse.sender_id] = pulse.level

    def send(self) -> list:
        if all([level is HIGH for level in self.state.values()]):
            return [Pulse(self.id, LOW, destination) for destination in self.destinations]
        return [Pulse(self.id, HIGH, destination) for destination in self.destinations]


class OutputConjunctionModule(ConjunctionModule):
    def receive(self, pulse: Pulse, n_push=0):
        super().receive(pulse)
        print(n_push, ["1" if s is HIGH else "0" for key, s in self.state.items()])


class BroadcasterModule(Module):
    def __init__(self, module_id, destination_modules: list[str]):
        super().__init__(module_id, destination_modules)
        self._last_received = None

    def receive(self, pulse: Pulse, n_push=0):
        self._last_received = pulse.level

    def send(self) -> list:
        return [Pulse(self.id, self._last_received, destination) for destination in self.destinations]


class TheButton:
    def __init__(self, modules: dict[str, Module]):
        self.low_count = 0
        self.high_count = 0
        self.modules = modules
        self.pulses: list[Pulse] = []

    def push(self, n=1):
        for i in range(n):
            self.pulses = [Pulse("button", LOW, "broadcaster")]
            # print()
            self.process_pulses(i)

    def process_pulses(self, n_push: int):
        while self.pulses:
            pulse = self.pulses.pop(0)

            if pulse.level == LOW:
                self.low_count += 1
            if pulse.level == HIGH:
                self.high_count += 1

            # print(pulse.sender_id, "-high->" if pulse.level else "-low->", pulse.receiver_id)
            if pulse.receiver_id not in self.modules:
                continue
            self.modules[pulse.receiver_id].receive(pulse, n_push)
            for p in self.modules[pulse.receiver_id].send():
                self.pulses.append(p)


def load_data(filename):
    modules = {}
    with open(filename, "r") as file:
        for line in file:
            description, destinations = line.split(" -> ")
            destinations = [destination.strip() for destination in destinations.split(",")]
            if description == "broadcaster":
                modules[description] = BroadcasterModule(description, destinations)
            elif description in ("&ns", "&con"):
                modules[description[1:]] = OutputConjunctionModule(description[1:], destinations)
            elif description[0] == "%":
                modules[description[1:]] = FlipFlopModule(description[1:], destinations)
            elif description[0] == "&":
                modules[description[1:]] = ConjunctionModule(description[1:], destinations)
    for key, module in modules.items():
        module.register_inputs(key, modules)
    return modules


def get_result(modules):
    button = TheButton(modules)
    button.push(1000)
    return button.low_count * button.high_count


def get_result_2(modules):
    button = TheButton(modules)
    button.push(3000)


def main():
    modules = load_data("data.txt")
    print(get_result(modules))
    print(get_result_2(modules))


if __name__ == '__main__':
    main()
