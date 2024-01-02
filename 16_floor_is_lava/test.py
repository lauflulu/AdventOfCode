import solution


class TestPart1:
    def test_that_data_is_loaded(self):
        beam = solution.load_data("example.txt")
        assert beam.contraption.shape == (10, 10)

    def test_that_energy_is_computed(self):
        beam = solution.load_data("example.txt")
        assert solution.get_result(beam) == 46
