import solution


class TestPart1:
    def test_that_data_is_loaded_as_list_of_strings_column_wise(self):
        data = solution.load_data("example.txt").platform
        assert data[0] == "##..O.O.OO"
        assert len(data) == 10
        assert len((data[0])) == 10

    def test_that_data_is_tilted_correctly(self):
        data = solution.load_data("example.txt")
        data.tilt()
        expected_data = solution.load_data("example_tilted.txt")
        for d, t in zip(data.platform, expected_data.platform):
            assert d == t

    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 136
