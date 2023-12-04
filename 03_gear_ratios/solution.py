import re

import numpy as np


def _has_neighbor(x: int, y: int):
    """Determine if there is a symbol in the 8-neighborhood of a given position."""
    pass


def get_part_numbers():
    pass


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
