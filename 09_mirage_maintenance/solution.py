import numpy as np


def load_data(filename):
    with open(filename, 'r') as file:
        histories = []
        for line in file:
            history = line.split(' ')
            histories.append(np.array([int(point.strip()) for point in history]))
        return histories


def _get_difference_to_next_value(history):
    return None


def _get_next_value(history):
    return None


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
