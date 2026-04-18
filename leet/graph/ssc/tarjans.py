# example code for tarjans algo to gen SSCs
def tarjan_scc(adj_list):

    indexes = {}
    low_link = {}
    in_stack = set()
    stack = []
    curr_index = 0
    sccs = []

    def find_sscs():
        for node in adj_list:
            if node not in indexes:
                dfs(node)

    def dfs(node):
        nonlocal curr_index
        stack.append(node)
        in_stack.add(node)
        indexes[node] = curr_index
        low_link[node] = curr_index
        curr_index += 1

        for nei in adj_list[node]:
            if nei not in indexes:
                dfs(nei)
            if nei in in_stack: # propapage LL through SCC
                low_link[node] = min(low_link[nei], low_link[node])
        
        if indexes[node] == low_link[node]: # found root of SCC
            scc = []
            while True:
                popped_node = stack.pop()
                in_stack.remove(popped_node)
                scc.append(popped_node)
                if popped_node == node:
                    break
            sccs.append(scc)

    find_sscs()
    return sccs

# TESTS
import unittest

class TestTarjanSCC(unittest.TestCase):

    def test_single_node(self):
        graph = {0: []}
        result = tarjan_scc(graph)
        expected_sccs = [{0}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_two_nodes_no_edges(self):
        graph = {0: [], 1: []}
        result = tarjan_scc(graph)
        expected_sccs = [{0}, {1}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_two_nodes_one_edge(self):
        graph = {0: [1], 1: []}
        result = tarjan_scc(graph)
        expected_sccs = [{0}, {1}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_two_nodes_cycle(self):
        graph = {0: [1], 1: [0]}
        result = tarjan_scc(graph)
        expected_sccs = [{0, 1}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_three_nodes_cycle(self):
        graph = {0: [1], 1: [2], 2: [0]}
        result = tarjan_scc(graph)
        expected_sccs = [{0, 1, 2}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_complex_graph(self):
        graph = {
            0: [1],
            1: [2, 3],
            2: [0, 4],
            3: [4],
            4: []
        }
        result = tarjan_scc(graph)
        expected_sccs = [{0, 1, 2}, {3}, {4}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_disconnected_graph(self):
        graph = {
            0: [1],
            1: [2],
            2: [0],
            3: [4],
            4: [5],
            5: [3]
        }
        result = tarjan_scc(graph)
        expected_sccs = [{0, 1, 2}, {3, 4, 5}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_tree_structure(self):
        graph = {
            0: [1, 2],
            1: [3, 4],
            2: [5, 6],
            3: [],
            4: [],
            5: [],
            6: []
        }
        result = tarjan_scc(graph)
        expected_sccs = [{0}, {1}, {2}, {3}, {4}, {5}, {6}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_bidirectional_edges(self):
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
        result = tarjan_scc(graph)
        expected_sccs = [{0, 1, 2, 3}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_single_node_self_loop(self):
        graph = {0: [0]}
        result = tarjan_scc(graph)
        expected_sccs = [{0}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_large_complicated_graph(self):
        graph = {
            0: [1],
            1: [2, 3],
            2: [0, 4],
            3: [4, 5],
            4: [6],
            5: [6, 7],
            6: [4],
            7: [8],
            8: [5, 9],
            9: [10],
            10: [11, 12],
            11: [9],
            12: [13],
            13: [14],
            14: [12]
        }
        result = tarjan_scc(graph)
        expected_sccs = [{4, 6}, {12, 13, 14}, {9, 10, 11}, {8, 5, 7}, {3}, {0, 1, 2}]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

    def test_new_graph_sccs(self):
        graph = {
            0: [1, 2],
            1: [3],
            2: [3, 4],
            3: [0, 5],
            4: [5, 6],
            5: [6],
            6: [4, 7],
            7: [8],
            8: [9],
            9: [7]
        }
        result = tarjan_scc(graph)
        expected_sccs = [
            {0, 1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        ]
        result_sccs = [set(scc) for scc in result]
        self.assertEqual(set(map(frozenset, result_sccs)), set(map(frozenset, expected_sccs)))

if __name__ == '__main__':
    unittest.main()