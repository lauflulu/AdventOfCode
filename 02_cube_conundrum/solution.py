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
    for draw in game:
        if draw['red'] > 12:
            return False
        if draw['green'] > 13:
            return False
        if draw['blue'] > 14:
            return False
    return True


def get_result(data: list[list[dict]]) -> int:
    result = 0
    for i, game in enumerate(data):
        if is_possible(game):
            result += i + 1
    return result


def main():
    data = load_data("data.txt")
    print(get_result(data))


if __name__ == '__main__':
    main()
