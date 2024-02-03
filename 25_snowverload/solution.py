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
        while len(self.index) > 2:
            t, w = self.minimum_cut_phase()
            if w < w_min:
                w_min = w
                min_partition = self.nodes[t]
        return min_partition

    def minimum_cut_phase(self):
        processed_nodes = [False for _ in range(len(self.index))]
        processed_nodes[0] = True
        while sum(processed_nodes) != len(self.index) - 2:
            processed_nodes[self.index.index(self.node_most_tightly_connected_with(processed_nodes))] = True
        s = self.node_most_tightly_connected_with(processed_nodes)
        processed_nodes[self.index.index(self.node_most_tightly_connected_with(processed_nodes))] = True
        t = self.node_most_tightly_connected_with(processed_nodes)
        self.merge_nodes(s, t)
        return s, self.sum_of_weights(s)

    def node_most_tightly_connected_with(self, processed_nodes):
        node_weights = self.weight_of_connections(processed_nodes)

        unprocessed_labels = [node for node, processed in zip(self.index, processed_nodes) if not processed]
        max_weight_index = np.argmax(node_weights)
        return unprocessed_labels[max_weight_index]

    def weight_of_connections(self, processed_nodes):
        unprocessed_nodes = np.invert(processed_nodes)
        sliced = self.matrix[unprocessed_nodes, :][:, processed_nodes]
        return np.sum(sliced, axis=1)

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
