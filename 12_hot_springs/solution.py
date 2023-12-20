

class Record:

    def __init__(self, springs: str, groups: list[int]):
        self._folded_springs = self._pad(springs)
        self._folded_groups = groups

        self._springs = self._folded_springs
        self._groups = self._folded_groups

    def _fold(self):
        self._springs = self._folded_springs
        self._groups = self._folded_groups

    def _unfold(self):
        self._springs = self._unfolded_springs()
        self._groups = self._unfolded_groups()

    def count_arrangements(self):
        self._fold()
        return self._count_arrangements()

    def _count_arrangements(self):

        def product(pools):
            result = [[]]

            for pool in pools:
                temp_result = []
                for x in result:
                    for y in pool:
                        branch_up_to_current_depth = x + [y]
                        if not branch_up_to_current_depth == sorted(branch_up_to_current_depth):
                            continue
                        if not self._groups_do_not_overlap(branch_up_to_current_depth):
                            continue
                        temp_result.append(branch_up_to_current_depth)
                result = temp_result
            print(len(result))

            for prod in result:
                yield tuple(prod)

        fit_indices = [self._fit_indices(n) for n in self._groups]
        count = 0

        for permutation in product(fit_indices):
            if self._forced_indices_are_included(permutation):
                count += 1
        return count

    def _forced_indices_are_included(self, permutation):
        permutation_indices = []
        for i, g in zip(permutation, self._groups):
            permutation_indices += list(range(i, i + g))
        if not all([i in permutation_indices for i in self._forced_indices()]):
            return False
        return True

    def _groups_do_not_overlap(self, permutation):
        for i in range(len(permutation) - 1):
            if not permutation[i + 1] > permutation[i] + self._groups[i]:
                return False
        return True

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
        self._unfold()
        return self._count_arrangements()


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
        c = record.count_arrangements()
        count += c
        print(i+1, c)
    return count


def get_result_2(records):
    count = 0
    for i, record in enumerate(records):
        c = record.unfolded_arrangements()
        count += c
        print(i + 1, c)
    return count


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
