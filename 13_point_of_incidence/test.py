import solution


class TestPart1:
    def test_that_data_is_loaded_as_list_of_terrains_containing_numpy_arrays(self):
        data = solution.load_data("example.txt")
        assert len(data) == 2
        assert data[0].pattern.shape == (7, 9)
        assert data[1].pattern.shape == (7, 9)

    def test_that_correct_mirror_indices_are_found_for_example_data(self):
        data = solution.load_data("example.txt")
        assert data[0].mirror_indices == (0, 5)
        assert data[1].mirror_indices == (4, 0)

    def test_that_result_is_correct_for_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 405
