import pytest

import solution


@pytest.fixture
def beam():
    return solution.load_data("example.txt")


class TestPart1:
    def test_that_data_is_loaded(self, beam):
        assert beam.contraption.shape == (10, 10)

    def test_that_beam_enters_from_one_direction(self, beam):
        assert len(beam.beam_tips) == 1

    def test_that_beam_marks_tile_with_its_direction_when_passing(self):
        beam = solution.load_data("example_3x3_empty.txt")
        beam.beam_tips = [(1, 1, ">")]
        beam._process_tips()
        assert beam.contraption[1, 1] == "." + ">"

    def test_that_energy_is_computed(self, beam):
        assert solution.get_result(beam) == 46
