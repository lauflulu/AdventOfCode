import pytest

import solution


@pytest.fixture
def beam():
    return solution.load_data("example.txt")


class TestPart1:
    def test_that_data_is_loaded(self, beam):
        assert beam.contraption.shape == (10, 10)

    def test_that_energy_is_computed(self, beam):
        assert solution.get_result(beam) == 46
