import re
import numpy as np


def _has_neighbor(data: np.array, x: int, y: int, symbols: list[str] = '*') -> bool:
    """Determine if there is a symbol in the 8-neighborhood of a given position."""
    return bool(np.any(_find_neighbors(data, symbols, x, y)))


def _find_neighbors(data, symbols, x, y):
    neighboring_data = _slice_neighbors(_dot_pad_data(data), x + 1, y + 1)  # has to shift by +1 due to padding
    return np.isin(neighboring_data, symbols)


def _dot_pad_data(data):
    return np.pad(data, 1, mode='constant', constant_values='.')


def _slice_neighbors(padded_data, x, y):
    return padded_data[y - 1:y + 2, x - 1:x + 2]


def get_part_numbers(data: np.array) -> list:
    data = _dot_pad_data(_replace_symbols(data))
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
        return np.array([[col for col in row.strip()] for row in file])


def _replace_symbols(data: np.array):
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            if not re.match(r'[.0-9]', data[y, x]):
                data[y, x] = '*'
    return data


def get_gear_ratios(data: np.array):
    data = _dot_pad_data(data)
    gear_ratios = []
    for y, x in _find_gears(data):
        neighbors = _find_neighbors(data=data, symbols=[str(i) for i in range(10)], x=x, y=y)
        if not neighbors.sum() >= 2:
            continue
        parts = _find_parts_next_to_gear(data, neighbors, x, y)
        if len(parts) == 2:
            gear_ratios.append(parts[0] * parts[1])
    return gear_ratios


def _find_parts_next_to_gear(data, neighbors, x, y):
    parts = []
    for dy, dx in _non_adjacent_part_indices(neighbors):
        parts.append(_get_part_number_at_index(data, y - 1 + dy, x - 1 + dx))
    return [int(part) for part in parts]


def _get_part_number_at_index(data, y, x):
    part_number = data[y, x]
    digit_chars = [str(i) for i in range(10)]
    if part_number not in digit_chars:
        return None
    # go left until not digit
    dx = 1
    while data[y, x - dx] in digit_chars:
        part_number = data[y, x - dx] + part_number
        dx += 1
    # go right until not digit
    dx = 1
    while data[y, x + dx] in digit_chars:
        part_number += data[y, x + dx]
        dx += 1
    return part_number


def _non_adjacent_part_indices(neighbors):
    indices = []

    for y in range(neighbors.shape[0]):
        previous_is_neighbor = False
        for x in range(neighbors.shape[1]):
            if neighbors[y, x] and not previous_is_neighbor:
                indices.append((y, x))
            previous_is_neighbor = neighbors[y, x]
    return indices


def _find_gears(data):
    return np.argwhere(data == '*')


def get_result_2(data):
    return sum(get_gear_ratios(data))


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
