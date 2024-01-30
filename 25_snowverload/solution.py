import numpy as np


class StoerWagner:
    def __init__(self, matrix, nodes):
        self.matrix = matrix
        self.index = nodes
        self.nodes = {node: 1 for node in nodes}
        self.n_nodes = len(nodes)

    def get_result(self):
        minimum_partition = self.minimum_cut()
        return minimum_partition * (self.n_nodes - minimum_partition)

    def minimum_cut(self):
        w_min = np.inf
        min_partition = []
        i = 0
        while len(self.index) > 2 and i < 10:
            i += 1
            t, w = self.minimum_cut_phase()
            if w < w_min:
                w_min = w
                min_partition = self.nodes[t]
        return min_partition

    def minimum_cut_phase(self):
        node_a = self.index[0]
        A = [node_a]
        while len(A) != len(self.index):
            A.append(self.node_most_tightly_connected_with(A))
        s, t = A[-2], A[-1]
        self.merge_nodes(s, t)
        return s, self.sum_of_weights(s)

    def node_most_tightly_connected_with(self, A):
        max_connected_node = ""
        max_weight = 0
        for node in self.index:
            if node not in A:
                node_weight = self.weight_of_connections_between(node, A)
                if node_weight > max_weight:
                    max_weight = node_weight
                    max_connected_node = node
        return max_connected_node

    def weight_of_connections_between(self, node, A):
        return sum(self.matrix[self.index.index(node), self.index.index(a)] for a in A)

    def merge_nodes(self, s, t):
        self.matrix[self.index.index(s), :] += self.matrix[self.index.index(t), :]
        self.matrix[:, self.index.index(s)] += self.matrix[:, self.index.index(t)]
        self.matrix = np.delete(self.matrix, self.index.index(t), 0)
        self.matrix = np.delete(self.matrix, self.index.index(t), 1)
        for i in range(len(self.index) - 1):
            self.matrix[i, i] = 0

        self.nodes[s] += self.nodes[t]
        self.index.remove(t)
        self.nodes.pop(t)

    def sum_of_weights(self, s):
        return sum(self.matrix[self.index.index(s), :])


def load_data(filename) -> tuple[np.ndarray, list[str]]:
    with open(filename, "r") as f:
        nodes = []
        for line in f:
            neighbors, node = _parse(line)
            for n in [node] + neighbors:
                if n not in nodes:
                    nodes.append(n)
        adjacency_matrix = np.zeros((len(nodes), len(nodes)))
        for line in open(filename, "r"):
            neighbors, node = _parse(line)
            for n in neighbors:
                adjacency_matrix[nodes.index(node), nodes.index(n)] = 1
    return adjacency_matrix + adjacency_matrix.T, nodes


def _parse(line):
    node, neighbors = line.split(":")
    node = node.strip()
    neighbors = [n.strip() for n in neighbors.strip().split(" ")]
    return neighbors, node


def get_result(matrix, nodes):
    return StoerWagner(matrix, nodes).get_result()


def get_result_2(matrix, nodes):
    pass


def main():
    matrix, nodes = load_data("data.txt")
    print(get_result(matrix, nodes))
    print(get_result_2(matrix, nodes))


if __name__ == '__main__':
    main()
