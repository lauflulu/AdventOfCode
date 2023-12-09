import pytest

import solution


class TestLoading:
    def test_that_loaded_data_has_seeds_and_maps(self):
        seeds, maps = solution.load_data("example.txt")
        assert isinstance(seeds, list)
        assert isinstance(maps, list)
        assert isinstance(seeds[0], int)
        assert isinstance(maps[0], solution.Map)

    def test_that_loaded_seeds_are_correct_for_example(self):
        seeds, maps = solution.load_data("example.txt")
        assert seeds == [79, 14, 55, 13]

    def test_that_loaded_maps_are_correct_for_example(self):
        seeds, maps = solution.load_data("example.txt")
        assert maps[0].source == "seed"
        assert maps[0].destination == "soil"
        assert len(maps[0].ranges) == 2

    def test_that_loaded_ranges_are_correct_for_example(self):
        seeds, maps = solution.load_data("example.txt")
        range_ = maps[0].ranges[0]
        assert range_.length == 2
        assert range_.source_start == 98
        assert range_.destination_start == 50


class TestMapping:
    @pytest.mark.parametrize("seed, soil", [(79, 81), (14, 14), (55, 57), (13, 13), (97, 99), (98, 50), (49, 49)])
    def test_that_example_seeds_are_mapped_to_correct_soil(self, seed, soil):
        _, maps = solution.load_data("example.txt")
        assert solution.map_categories(maps, number=seed, source="seed", destination="soil") == soil

    @pytest.mark.parametrize("seed, location", [(79, 82), (14, 43), (55, 86), (13, 35)])
    def test_that_example_seeds_are_mapped_to_correct_location(self, seed, location):
        _, maps = solution.load_data("example.txt")
        assert solution.map_categories(maps, number=seed, source="seed", destination="location") == location


class TestResult1:
    def test_that_the_result_is_correct_for_example(self):
        seeds, maps = solution.load_data("example.txt")
        assert solution.get_result(seeds, maps) == 35


class TestResult2:
    def test_that_seeds_are_loaded_correctly_if_interpreted_as_ranges(self):
        seeds, maps = solution.load_data("example.txt")
        seed_ranges = solution.convert_seeds(seeds)
        assert len(seed_ranges) == sum(seeds[1::2])

    def test_that_the_result_is_correct_for_example(self):
        seeds, maps = solution.load_data("example.txt")
        seed_ranges = solution.convert_seeds(seeds)
        assert solution.get_result(seed_ranges, maps) == 46

    @pytest.mark.parametrize("seed, soil", [(79, 81), (14, 14), (55, 57), (13, 13), (97, 99), (98, 50), (49, 49)])
    def test_inverse_mapping_one_category_for_example(self, seed, soil):
        _, maps = solution.load_data("example.txt")
        assert solution.map_categories_inverse(maps, number=soil, source="seed", destination="soil") == seed

    @pytest.mark.parametrize("seed, location", [(79, 82), (14, 43), (55, 86), (13, 35)])
    def test_inverse_mapping_for_example(self, seed, location):
        _, maps = solution.load_data("example.txt")
        assert solution.map_categories_inverse(maps, number=location, source="seed", destination="location") == seed
