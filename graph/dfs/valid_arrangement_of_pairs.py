from collections import defaultdict

class Solution:
    # https://leetcode.com/problems/valid-arrangement-of-pairs/description/
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        # hierholzers algo
        # hard part if finding starting node
        # eulerian path

        # hierholzers algo
        def dfs(prev, node):
            while adj_list[node]:
                dfs(node, adj_list[node].pop())
            path.append([prev, node])

        # make G
        adj_list = defaultdict(list)
        out_degrees = defaultdict(int)
        in_degrees = defaultdict(int)
        for _from, to in pairs:
            adj_list[_from].append(to)
            out_degrees[_from] += 1
            in_degrees[to] += 1
        
        # find the starting node in directed graph
        starting_node = pairs[0][0] # if it turns out its not a path, but a circuit, we start anywhere
        for node, out_degree in out_degrees.items():
            # if its a eulerian path there is exactly 1 node that meets this condition, this is the start of the path
            # NOTE: there is also a node in-degree - out-degree == 1, this is the end of the path
            # there are always 0 or 2 nodes with odd degrees in a eulerian path.
            if out_degree - in_degrees[node] == 1:
                starting_node = node
                break

        path = []
        dfs(None, starting_node)
        path.pop() # remove the initial edge (None, starting_node)
        return path[::-1]
