import numpy as np
import pytest

import solution


class TestPart1:
    def test_that_data_is_loaded_as_adjacency_matrix(self):
        graph, _ = solution.load_data("example.txt")
        assert graph.shape == (15, 15)

    def test_that_data_is_loaded_with_list_of_nodes(self):
        _, nodes = solution.load_data("example.txt")
        assert nodes == [
            'jqt', 'rhn', 'xhk', 'nvd', 'rsh', 'frs', 'pzl', 'lsr', 'hfx', 'cmg', 'qnr', 'lhk', 'bvb', 'ntq', 'rzs'
        ]

    def test_that_diagonal_of_adjacency_matrix_is_zero(self):
        graph, _ = solution.load_data("example.txt")
        assert np.all(graph.diagonal() == 0)

    def test_that_adjacency_matrix_is_symmetric(self):
        graph, _ = solution.load_data("example.txt")
        assert np.all(graph == graph.T)

    def test_that_adjacency_matrix_only_contains_ones_and_zeros(self):
        graph, _ = solution.load_data("example.txt")
        assert np.all(np.logical_or(graph == 0, graph == 1))

    @pytest.mark.skip(reason="Not implemented yet")
    def test_that_result_is_correct_for_example(self):
        matrix, nodes = solution.load_data("example.txt")
        assert solution.get_result(matrix, nodes) == 54


@pytest.fixture
def simple_graph():
    return solution.StoerWagner(np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), ["a", "b", "c"])


class TestStoerWagner:
    def test_merge_nodes(self, simple_graph):
        simple_graph.merge_nodes("a", "b")
        assert simple_graph.matrix.tolist() == [[0, 2], [2, 0]]
        assert simple_graph.nodes == {"a": 2, "c": 1}
        assert simple_graph.index == ["a", "c"]

    def test_weight(self, simple_graph):
        assert simple_graph.weight("a", ["b", "c"]) == 2
        assert simple_graph.weight("b", ["a", "c"]) == 2
        assert simple_graph.weight("c", ["a"]) == 1


@pytest.mark.skip(reason="Not implemented yet")
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
