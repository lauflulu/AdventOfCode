import re


def load_data(filename: str):
    with open(filename, 'r') as file:
        return [_parse_line(line) for line in file]


def _parse_line(line: str) -> list[dict]:
    draw_strings = line.split(':')[1].split(';')
    draw_dicts = [_parse_rgb(draw_string) for draw_string in draw_strings]
    return draw_dicts


def _parse_rgb(rgb_string: str) -> dict:
    rgbs = rgb_string.split(',')
    rgb_dict = {'red': 0, 'green': 0, 'blue': 0}
    for rgb in rgbs:
        for color in rgb_dict.keys():
            if color in rgb:
                rgb_dict[color] = int(re.findall(r'[0-9]+', rgb)[0])
    return rgb_dict


def is_possible(game: list[dict]) -> bool:
    # 12 red cubes, 13 green cubes, and 14 blue cubes.
    pass
