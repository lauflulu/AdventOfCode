import re

import numpy as np


def load_data(filename):
    with open(filename, 'r') as file:
        times = re.findall(r'[0-9]+', file.readline())
        distances = re.findall(r'[0-9]+', file.readline())
    return [(int(time), int(distance)) for time, distance in zip(times, distances)]


def number_of_winning_times(data):
    return [np.where(np.array(possible_distances(time)) > distance)[0].shape[0] for time, distance in data]


def possible_distances(total_time):
    return [(total_time - waiting_time) * waiting_time for waiting_time in range(total_time + 1)]


def find_roots(total_time, distance):
    coeffs = [-1, total_time, - distance]
    roots = np.roots(coeffs)
    return int(roots[0]) - int(roots[1])


def get_result(data):
    result = 1
    for n in number_of_winning_times(data):
        result *= n
    return result


def get_result_2(data):
    total_time, total_distance = ('', '')
    for time, distance in data:
        total_time += str(time)
        total_distance += str(distance)
    return find_roots(int(total_time), int(total_distance))


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
