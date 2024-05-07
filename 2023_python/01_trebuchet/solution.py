import re


map_literal_digits = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def read_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def _find_all_digits(line: str) -> list[str]:
    literal_digits = _find_all_digits_including_literals(line)
    return _replace_literal_digits(literal_digits)


def _replace_literal_digits(literal_digits):
    int_digits = []
    for digit in literal_digits:
        if digit in map_literal_digits.keys():
            int_digits.append(map_literal_digits[digit])
        else:
            int_digits.append(digit)
    return int_digits


def _find_all_digits_including_literals(line):
    matches = re.finditer(r'(?=([0-9]|zero|one|two|three|four|five|six|seven|eight|nine))', line)
    return [match.group(1) for match in matches]


def _extract_two_digits(line: str):
    all_digits = _find_all_digits(line)
    return int(all_digits[0] + all_digits[-1])


def compute_total_sum(lines):
    two_digits = [_extract_two_digits(line) for line in lines]
    return sum(two_digits)


def main():
    lines = read_data("material.txt")
    print(compute_total_sum(lines))


if __name__ == '__main__':
    main()
