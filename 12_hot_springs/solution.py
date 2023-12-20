

class Record:

    def __init__(self, springs: str, groups: list[int]):
        self._folded_springs = self._pad(springs)
        self._folded_groups = groups

        self._springs = self._folded_springs
        self._groups = self._folded_groups
        self._forced_indices = self._get_forced_indices()

    def _fold(self):
        self._springs = self._folded_springs
        self._groups = self._folded_groups
        self._forced_indices = self._get_forced_indices()

    def _unfold(self, folds):
        self._springs = self._unfolded_springs(folds)
        self._groups = self._unfolded_groups(folds)
        self._forced_indices = self._get_forced_indices()

    def count_arrangements(self):
        self._fold()
        return self._count_arrangements()

    def count_unfolded_arrangements(self):
        locked, one_arrangements, left_arrangements = self._locked()
        if locked:
            return left_arrangements**4*one_arrangements
        return self._unfolded_arrangements()

    def _count_arrangements(self):
        pools = [self._fit_indices(n) for n in self._groups]

        result = [[]]
        for pool in pools:
            temp_result = []
            for x in result:
                for y in pool:
                    partial_product = x + [y]
                    if not self._groups_are_in_correct_order(partial_product):
                        continue
                    if not self._groups_do_not_overlap(partial_product):
                        continue
                    if not self._forced_indices_can_be_filled(partial_product):
                        continue
                    temp_result.append(partial_product)
            result = temp_result
        return len(result)

    def _groups_are_in_correct_order(self, partial_product):
        return partial_product == sorted(partial_product)

    def _forced_indices_can_be_filled(self, partial_product):
        already_filled_indices = [i for g, p in zip(self._groups, partial_product) for i in range(p, p+g)]
        forced_indices = self._forced_indices
        remaining_groups = self._groups[len(partial_product):]
        remaining_forced_indices = list(set(forced_indices) - set(already_filled_indices))
        if sum(remaining_groups) < len(remaining_forced_indices):
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

    def _get_forced_indices(self):
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

    def _unfolded_groups(self, folds):
        return self._folded_groups * folds

    def _unfolded_springs(self, folds):
        springs = self._folded_springs[1:-1]
        return self._pad((springs + '?') * (folds - 1) + springs)

    def _unfolded_left_spring(self):
        springs = self._folded_springs[1:-1]
        return self._pad(springs + '?')

    def _unfolded_right_spring(self):
        springs = self._folded_springs[1:-1]
        return self._pad('?' + springs)

    def _unfolded_arrangements(self, folds: int = 5):
        self._unfold(folds)
        return self._count_arrangements()

    def _locked(self):
        one_fold_arrangements = self.count_arrangements()
        two_fold_arrangements = self._unfolded_arrangements(2)
        self._springs = self._unfolded_left_spring()
        self._groups = self._folded_groups
        self._forced_indices = self._get_forced_indices()
        left_fold_arrangements = self._count_arrangements()
        print(one_fold_arrangements, left_fold_arrangements, two_fold_arrangements)
        if one_fold_arrangements*left_fold_arrangements == two_fold_arrangements:
            return True, one_fold_arrangements, left_fold_arrangements
        self._springs = self._unfolded_right_spring()
        self._groups = self._folded_groups
        self._forced_indices = self._get_forced_indices()
        right_fold_arrangements = self._count_arrangements()
        print(one_fold_arrangements, right_fold_arrangements, two_fold_arrangements)
        if one_fold_arrangements * right_fold_arrangements == two_fold_arrangements:
            return True, one_fold_arrangements, right_fold_arrangements

        return False, None, None


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
        c = record.count_unfolded_arrangements()
        count += c
        print(i + 1, c)
    return count


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
