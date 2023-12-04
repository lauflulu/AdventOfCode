import re

import numpy as np


def _has_neighbor(data: np.array, x: int, y: int) -> bool:
    """Determine if there is a symbol in the 8-neighborhood of a given position."""
    padded_data = np.pad(data, 1, mode='constant', constant_values='.')
    neighboring_data = padded_data[y:y+3, x:x+3]  # has to shift by one due to padding
    return bool(np.any(np.char.find(neighboring_data, '*') != -1))


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



def get_result():
    pass


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
