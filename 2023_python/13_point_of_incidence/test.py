import pytest
import solution


class TestPart1:
    def test_that_data_is_loaded_as_list_of_terrains_containing_numpy_arrays(self):
        data = solution.load_data("example.txt")
        assert len(data) == 2
        assert data[0].pattern.shape == (7, 9)
        assert data[1].pattern.shape == (7, 9)

    @pytest.mark.parametrize("terrain_index, mirror_indices", [
        (0, (0, 5)),
        (1, (4, 0)),
    ])
    def test_that_correct_mirror_indices_are_found_for_example_data(self, terrain_index, mirror_indices):
        data = solution.load_data("example.txt")
        assert data[terrain_index].mirror_indices() == mirror_indices

    def test_that_result_is_correct_for_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 405


class TestPart2:
    @pytest.mark.parametrize("terrain_index, mirror_indices", [
        (0, (3, 0)),
        (1, (1, 0)),
    ])
    def test_that_correct_mirror_indices_are_found_for_example_data(self, terrain_index, mirror_indices):
        data = solution.load_data("example.txt")
        assert data[terrain_index].smudge_mirror_indices() == mirror_indices

    def test_that_result_is_correct_for_example_data(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 400
