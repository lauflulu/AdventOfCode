import re


def read_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def _find_all_digits(line: str):
    return re.findall(r'[0-9]', line)


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
