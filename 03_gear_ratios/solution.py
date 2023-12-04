import re
import numpy as np


def _has_neighbor(data: np.array, x: int, y: int) -> bool:
    """Determine if there is a symbol in the 8-neighborhood of a given position."""
    padded_data = np.pad(data, 1, mode='constant', constant_values='.')
    neighboring_data = _slice_neighbors(padded_data, x+1, y+1)  # has to shift by +1 due to padding
    return bool(np.any(np.char.find(neighboring_data, '*') != -1))


def _slice_neighbors(padded_data, x, y):
    return padded_data[y-1:y + 2, x-1:x + 2]


def get_part_numbers(data: np.array) -> list:
    part_numbers = []
    previous_value = '.'
    part_number = ''
    neighbor_found = False
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            value = data[y, x]

            if re.match(r'[0-9]', value) and not re.match(r'[0-9]', previous_value):
                part_number = value
                neighbor_found = _has_neighbor(data, x, y)
            if re.match(r'[0-9]', value) and re.match(r'[0-9]', previous_value):
                part_number += value
                neighbor_found = neighbor_found or _has_neighbor(data, x, y)
            if not re.match(r'[0-9]', value) and re.match(r'[0-9]', previous_value) and neighbor_found:
                part_numbers.append(part_number)

            previous_value = value

    return [int(n) for n in part_numbers]


def get_result(data: np.array) -> int:
    return sum(get_part_numbers(data))


def load_data(filename: str):
    with open(filename, 'r') as file:
        matrix = []
        for row in file:
            matrix.append(_replace_symbols(row))
        return np.array(matrix)


def _replace_symbols(row):
    columns = []
    for col in row.strip():
        if not re.match(r'[.0-9]', col):
            col = '*'
        columns.append(col)
    return columns


def main():
    data = load_data("data.txt")
    print(get_result(data))


if __name__ == '__main__':
    main()
