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


def is_possible(game: list[dict], cube_set: dict = None) -> bool:
    cube_set = cube_set or {'red': 12, 'green': 13, 'blue': 14}
    for draw in game:
        if draw['red'] > cube_set['red']:
            return False
        if draw['green'] > cube_set['green']:
            return False
        if draw['blue'] > cube_set['blue']:
            return False
    return True


def get_result(data: list[list[dict]]) -> int:
    result = 0
    for i, game in enumerate(data):
        if is_possible(game):
            result += i + 1
    return result


def minimum_set(game: list[dict]) -> dict:
    min_set = {'red': 0, 'green': 0, 'blue': 0}
    for set_ in game:
        for color in min_set.keys():
            if set_[color] > min_set[color]:
                min_set[color] = set_[color]
    return min_set


def power_of(set_: dict) -> int:
    p = 1
    for number in set_.values():
        p *= number
    return p


def get_result_2(data: list[list[dict]]) -> int:
    power_sum = 0
    for game in data:
        power_sum += power_of(minimum_set(game))
    return power_sum


def main():
    data = load_data("data.txt")
    print(f"Result: {get_result(data)}")
    print(f"Result 2: {get_result_2(data)}")


if __name__ == '__main__':
    main()
