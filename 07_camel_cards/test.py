import solution


class TestPart1:
    def test_that_hands_are_loaded_from_example_data(self):
        hands = solution.load_data("example.txt")
        assert hands[0].cards == '32T3K'
        assert hands[0].bid == 765

