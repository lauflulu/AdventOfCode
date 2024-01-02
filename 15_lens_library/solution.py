
def evaluate(instruction):
    return None


def load_data(filename):
    with open(filename, "r") as file:
        return file.readline().strip().split(",")


def get_result(data):
    pass


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
