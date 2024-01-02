
def evaluate(instruction: str):
    current_value = 0
    for char in instruction:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def load_data(filename):
    with open(filename, "r") as file:
        return file.readline().strip().split(",")


def get_result(data):
    return sum([evaluate(instruction) for instruction in data])



def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
