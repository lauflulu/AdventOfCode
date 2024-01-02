import re


class Boxes:
    def __init__(self):
        self._boxes = {i: {} for i in range(256)}

    def process(self, instruction):
        label = re.findall(r'[a-z]+', instruction)[0]
        box_index = evaluate(label)
        print(box_index)
        if "=" in instruction:
            focal_length = int(instruction[-1])
            self._boxes[box_index][label] = focal_length
        if "-" in instruction:
            if label in self._boxes[box_index].keys():
                self._boxes[box_index].pop(label)


    def get_box(self, index):
        return self._boxes[index]

    def focusing_power_sum(self):
        return sum([self._focusing_power(i, box) for i, box in self._boxes.items()])

    def _focusing_power(self, i, box):
        if box == {}:
            return 0
        box_power = 0
        for slot, focal_length in enumerate(box.values()):
            box_power += (i + 1) * (slot + 1) * focal_length
        return box_power


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
    boxes = Boxes()
    for instruction in data:
        boxes.process(instruction)
    return boxes.focusing_power_sum()


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
