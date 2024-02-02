import cProfile

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

    def test_that_result_is_correct_for_example(self):
        matrix, nodes = solution.load_data("example.txt")
        assert solution.get_result(matrix, nodes) == 54


@pytest.fixture
def simple_graph():
    return solution.StoerWagner(np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), ["a", "b", "c"])

@pytest.fixture
def simple_graph_2():
    return solution.StoerWagner(np.array([[0, 1, 2], [1, 0, 1], [2, 1, 0]]), ["a", "b", "c"])


class TestStoerWagner:
    def test_merge_nodes(self, simple_graph):
        simple_graph.merge_nodes("a", "b")
        assert simple_graph.matrix.tolist() == [[0, 2], [2, 0]]
        assert simple_graph.nodes == {"a": 2, "c": 1}
        assert simple_graph.index == ["a", "c"]

    def test_that_weight_of_connections_between_node_and_set_of_nodes_is_correct(self, simple_graph):
        assert simple_graph.weight_of_connections_between("a", ["b", "c"]) == 2
        assert simple_graph.weight_of_connections_between("b", ["a", "c"]) == 2
        assert simple_graph.weight_of_connections_between("c", ["a"]) == 1

    def test_that_sum_of_weights_is_correct(self, simple_graph):
        assert simple_graph.sum_of_weights("a") == 2
        assert simple_graph.sum_of_weights("b") == 2
        assert simple_graph.sum_of_weights("c") == 2

    def test_node_most_tightly_connected_with(self, simple_graph):
        assert simple_graph.node_most_tightly_connected_with(["a", "c"]) == "b"
        assert simple_graph.node_most_tightly_connected_with(["b", "c"]) == "a"
        assert simple_graph.node_most_tightly_connected_with(["a"]) == "b"

    def test_node_most_tightly_connected_with_2(self, simple_graph_2):
        assert simple_graph_2.node_most_tightly_connected_with(["a"]) == "c"

    def test_minimum_cut_phase(self, simple_graph):
        assert simple_graph.minimum_cut_phase() == ("b", 2)
        assert simple_graph.matrix.tolist() == [[0, 2], [2, 0]]
        assert simple_graph.nodes == {"a": 1, "b": 2}
        assert simple_graph.index == ["a", "b"]

    def test_minimum_cut_returns_length_of_one_minimum_partition(self, simple_graph):
        assert simple_graph.minimum_cut() == 2

    def test_minimum_cut_returns_length_of_one_minimum_partition_2(self, simple_graph_2):
        assert simple_graph_2.minimum_cut() == 2


class TestPerformance:
    def test_complete_algorithm(self):

        with cProfile.Profile() as pr:
            pr.enable()
            for _ in range(100):
                matrix, nodes = solution.load_data("example.txt")
                solution.get_result(matrix, nodes)
            pr.disable()
        pr.print_stats()

@pytest.mark.skip(reason="Not implemented yet")
class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0
