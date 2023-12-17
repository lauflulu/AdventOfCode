import itertools


class Record:

    def __init__(self, springs: str, groups: list[int]):
        self._springs = self._pad(springs)
        self._n_springs = len(springs)
        self._groups = groups

    def number_of_arrangements(self):
        # compute potential _boxes(self._springs)
        # check if self._groups fits in boxes
        fit_indices = [self._fit_indices(n) for n in self._groups]
        count = 0
        for permutation in list(set(list(itertools.product(*fit_indices)))):
            valid = True
            for i in range(len(permutation) - 1):
                if not permutation[i + 1] > permutation[i] + self._groups[i]:
                    valid = False
            count += int(valid)
        return count

    def _fit_indices(self, n):
        indices = []
        for i in range(len(self._springs) - n):
            if self._matches(n, i):
                indices.append(i)
        return indices

    def _matches(self, n, i):
        group = self._spring_group(n)
        sub_springs = self._springs[i:i + len(group)]
        for j in range(len(group)):
            if not (sub_springs[j] == '?' or sub_springs[j] == group[j]):
                return False
        return True

    def _spring_group(self, n) -> str:
        return self._pad('#' * n)

    def _pad(self, springs: str) -> str:
        return '.' + springs + '.'


def load_data(filename):
    with open(filename, 'r') as file:
        records = []
        for line in file:
            springs, groups = line.strip().split(' ')
            groups = [int(i) for i in groups.split(',')]
            records.append(Record(springs, groups))
        return records


def get_result(records):

    return sum([record.number_of_arrangements() for record in records])


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()