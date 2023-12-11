

class Instruction:
    def __init__(self, right, left):
        self.right = right
        self.left = left


def load_data(filename):
    pass


def get_result(instructions, maps):
    pass


def get_result_2(instructions, maps):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
