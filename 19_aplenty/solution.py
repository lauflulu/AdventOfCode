class Part:
    def __init__(self, line):
        pass


class Workflow:
    def __init__(self, line):
        pass


def load_data(filename):
    workflows = {}
    parts = []
    workflows_read = False
    with open(filename, "r") as file:
        for line in file:
            if line == "\n":
                workflows_read = True
            if not workflows_read:
                name, rules = line.strip().split("{")
                workflows[name] = Workflow(rules[:-1])
            else:
                line = file.readline()
                parts.append(Part(line[1:-1]))
    return workflows, parts


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
