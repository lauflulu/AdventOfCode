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
        for permutation in itertools.product(*fit_indices):
            valid = True
            for i in range(len(permutation) - 1):
                if not permutation[i + 1] > permutation[i] + self._groups[i]:
                    valid = False
            if valid:
                permutation_indices = []
                for i, g in zip(permutation, self._groups):
                    permutation_indices += list(range(i, i + g) )
                if not all([i in permutation_indices for i in self._forced_indices()]):
                    valid = False
            if valid:
                count += int(valid)
        return count

    def _fit_indices(self, n):
        indices = []
        for i in range(len(self._springs) - n):
            if self._matches(n, i):
                indices.append(i)
        return indices

    def _forced_indices(self):
        return [i-1 for i in range(len(self._springs)) if self._springs[i] == '#']

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

    def _unfolded_groups(self):
        return self._groups * 5

    def _unfolded_springs(self):
        springs = self._springs[1:-1]
        return self._pad((springs + '?') * 4 + springs)

    def unfolded_arrangements(self):
        return 1


def load_data(filename):
    with open(filename, 'r') as file:
        records = []
        for line in file:
            springs, groups = line.strip().split(' ')
            groups = [int(i) for i in groups.split(',')]
            records.append(Record(springs, groups))
        return records


def get_result(records):
    count = 0
    for i, record in enumerate(records):
        c = record.number_of_arrangements()
        count += c
        print(i+1, c)
    return count


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
