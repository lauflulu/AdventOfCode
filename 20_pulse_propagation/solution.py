from abc import ABC, abstractmethod


class Module(ABC):
    def __init__(self, destination_modules: list[str]):
        self._destination_modules = destination_modules

    @abstractmethod
    def receive(self, pulse: bool):
        pass

    @abstractmethod
    def send(self):
        pass


class FlipFlopModule(Module):

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


def load_data(filename):
    pass


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
