import pytest

import solution


@pytest.fixture
def beam():
    return solution.load_data("example.txt")


class TestPart1:
    def test_that_data_is_loaded(self, beam):
        assert beam.contraption.shape == (10, 10)

    def test_that_beam_enters_from_one_direction(self, beam):
        assert len(beam.tips) == 1

    def test_that_beam_marks_tile_with_its_direction_when_passing(self):
        beam = solution.load_data("example_3x3_empty.txt")
        beam.tips = [(1, 1, ">")]
        beam.process_tips()
        assert beam.contraption[1, 1] == "." + ">"

    def test_that_tip_moves_to_next_tile_in_direction(self):
        beam = solution.load_data("example_3x3_empty.txt")
        beam.tips = [(1, 1, ">")]
        beam.process_tips()
        assert beam.tips[0] == (1, 2, ">")

    @pytest.mark.parametrize("in_tip, out_tip", [
        ((1, 4, ">"), (2, 4, "v")),
        ((1, 4, "<"), (0, 4, "^")),
        ((1, 4, "^"), (1, 3, "<")),
        ((1, 4, "v"), (1, 5, ">")),
        ((6, 4, ">"), (5, 4, "^")),
        ((6, 4, "<"), (7, 4, "v")),
        ((6, 4, "^"), (6, 5, ">")),
        ((6, 4, "v"), (6, 3, "<")),
    ])
    def test_that_mirrors_reflect_direction(self, beam, in_tip, out_tip):
        beam.tips = [in_tip]
        beam.process_tips()
        assert beam.tips[0] == out_tip

    @pytest.mark.parametrize("in_tip", [
        (1, 2, "^"),
        (1, 2, "v"),
        (2, 5, "<"),
        (2, 5, ">"),
    ])
    def test_that_splitters_split_beam_when_orthogonal(self, beam, in_tip):
        beam.tips = [in_tip]
        beam.process_tips()
        assert len(beam.tips) == 2

    @pytest.mark.parametrize("in_tip", [
        (1, 2, "<"),
        (1, 2, ">"),
        (2, 5, "^"),
        (2, 5, "v"),
    ])
    def test_that_splitters_do_nothing_when_beam_parallel(self, beam, in_tip):
        beam.tips = [in_tip]
        beam.process_tips()
        assert len(beam.tips) == 1

    @pytest.mark.parametrize("in_tip", [
        (0, 0, "<"),
        (0, 5, "<"),
        (3, 9, ">"),
    ])
    def test_that_beam_terminates_at_boundary(self, beam, in_tip):
        beam.tips = [in_tip]
        beam.process_tips()
        assert len(beam.tips) == 0

    def test_that_energy_is_computed(self, beam):
        assert solution.get_result(beam) == 46


class TestPart2:
    def test_that_maximum_energy_is_found(self, beam):
        assert solution.get_result_2(beam) == 51