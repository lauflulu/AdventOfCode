import numpy as np


def load_data(filename):
    with open(filename, 'r') as file:
        histories = []
        for line in file:
            history = line.split(' ')
            histories.append(np.array([int(point.strip()) for point in history]))
        return histories


def _get_next_value(history):
    current_diff = history
    sum_of_last_value = 0
    while not np.all(current_diff == 0):
        sum_of_last_value += current_diff[-1]
        current_diff = np.diff(current_diff)
    return sum_of_last_value


def _get_previous_value(history):
    return None


def get_result(histories):
    next_values = [_get_next_value(history) for history in histories]
    return sum(next_values)


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()

