
class Platform:
    def __init__(self, platform):
        self.platform = platform
        self.rotate_right()

    def rotate_right(self):
        n_rows = len(self.platform)
        n_cols = len(self.platform[0])
        rotated_platform = ['' for _ in range(n_rows)]
        for r in reversed(range(n_rows)):
            for c in range(n_cols):
                rotated_platform[c] += self.platform[r][c]
        self.platform = rotated_platform

    def tilt(self):
        pass



def load_data(filename):
    with open(filename, 'r') as file:
        return Platform([row.strip() for row in file])


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
