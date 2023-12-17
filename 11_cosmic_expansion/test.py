import solution


class TestPart1:
    def test_that_data_is_loaded_as_numpy_array(self):
        universe = solution.load_data("example.txt")
        print(universe)

    def test_that_the_example_universe_is_expanded(self):
        universe = solution.load_data("example.txt")
        print(universe.expand())

    def test_that_galaxy_indices_are_complete_for_example(self):
        universe = solution.load_data("example.txt")
        print(universe.galaxy_indices())

    def test_that_shortest_paths_are_correct_for_example(self):
        universe = solution.load_data("example.txt")
        print(universe.lengths_of_shortest_paths())

    def test_that_the_result_is_correct_for_example(self):
        universe = solution.load_data("example.txt")
        print(solution.get_result(universe))

