from abc import ABC, abstractmethod


HIGH = True
LOW = False
ON = True
OFF = False


class Module(ABC):
    def __init__(self, destination_modules: list[str]):
        self.destinations = destination_modules

    @abstractmethod
    def receive(self, pulse: bool):
        pass

    @abstractmethod
    def send(self):
        pass


class FlipFlopModule(Module):
    def __init__(self, destination_modules: list[str]):
        super().__init__(destination_modules)
        self.state = OFF


    def receive(self, pulse: bool):
        pass

    def send(self):
        pass


class ConjunctionModule(Module):

    def receive(self, pulse: bool):
        pass

    def send(self):
        pass


class BroadcasterModule(Module):

    def receive(self, pulse: bool):
        pass

    def send(self):
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
