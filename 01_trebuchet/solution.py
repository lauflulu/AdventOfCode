import re


def _find_all_digits(code_line: str):
    return re.findall(r'[0-9]', code_line)


def extract_two_digits(code_line: str):
    all_digits = _find_all_digits(code_line)
    return int(all_digits[0] + all_digits[-1])
