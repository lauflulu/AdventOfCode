import pytest

import solution


@pytest.fixture
def graph():
    return solution.load_data("example.txt")


class TestPart1:
    def test_that_data_is_loaded_as_graph(self, graph):
        assert isinstance(graph, solution.Graph)

    def test_that_nodes_have_weight(self, graph):
        assert graph.graph[(0, 1)] == 4

    @pytest.mark.parametrize("node, n_neighbors", [
        ((0, 0), 2),
        ((0, 1), 3),
        ((1, 1), 4),
    ])
    def test_that_node_has_correct_number_of_neighbors(self, graph, node, n_neighbors):
        assert len(graph.neighbors(*node)) == n_neighbors

    @pytest.mark.parametrize("_graph, min_length", [
        #(solution.load_data("example.txt"), 102),
        #(solution.load_data("example_minimal.txt"), 8),
        (solution.load_data("example_simple.txt"), 19),
        (solution.load_data("example_rule3.txt"), 31)
    ])
    def test_that_result_is_correct_for_example(self, _graph, min_length):
        assert solution.get_result(_graph) == min_length

    @pytest.mark.parametrize("_graph, min_length", [
        # (solution.load_data("example.txt"), 102),
        (solution.load_data("example_minimal.txt"), 8),
        (solution.load_data("example_simple.txt"), 19),
        #(solution.load_data("example_rule3.txt"), 31)
    ])
    def test_dominance(self, _graph, min_length):
        assert _graph._dominance() == min_length


class TestPart2:
    def test_that_result_is_correct_for_example(self, graph):
        assert solution.get_result_2(graph) == 0