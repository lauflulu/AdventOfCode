import re


def read_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def _find_all_digits(code_line: str):
    return re.findall(r'[0-9]', code_line)


def extract_two_digits(code_line: str):
    all_digits = _find_all_digits(code_line)
    return int(all_digits[0] + all_digits[-1])


def answer(lines):
    two_digits = [extract_two_digits(line) for line in lines]
    return sum(two_digits)
