import solution


class TestPart1:
    def test_that_loaded_data_is_list_of_tuples(self):
        data = solution.load_data("example.txt")
        assert data == [(7, 9), (15, 40), (30, 200)]

    def test_that_possible_distances_are_computed(self):
        assert solution.possible_distances(7) == [0, 6, 10, 12, 12, 10, 6, 0]

    def test_that_number_of_winning_times_is_correct_for_example(self):
        assert solution.number_of_winning_times([(7, 9)]) == 4

    def test_that_result_is_correct_for_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 288


class TestPart2:
    def test_roots_for_part_2(self):
        print(solution.find_roots(71530, 940200))

