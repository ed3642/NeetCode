# https://leetcode.com/problems/valid-arrangement-of-pairs/
from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # NOTE: in this problem we can always form a eulerian path or circuit guarantee
        # so we dont have to check if its possible
        # in a eulerian path there are exactly 2 nodes with odd degree
        # in a eulerian circuit there are 0 odd degreed nodes

        def dfs(node):
            # visit all neighbors then append when exhausted
            # this will order it by the end of the path, by starting from the leafs of the dfs
            while adj_list[node]:
                dfs(adj_list[node].pop())
            reversed_order.append(node)

        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        adj_list = defaultdict(list)
        for _from, _to in pairs:
            out_degree[_from] += 1
            in_degree[_to] += 1
            adj_list[_from].append(_to)

        start_node = pairs[0][0] # arbitrary node initially
        for node in out_degree:
            # if we find 1 odd degree node the problem guarantees that there will be exactly 2
            # need to start with the one that has exactly 1 extra out degree 
            # there is exactly one node with this property in a eulerian circuit
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break

        reversed_order = []
        dfs(start_node)

        # format output
        res = []
        for i in range(len(reversed_order) - 2, -1, -1):
            res.append([reversed_order[i + 1], reversed_order[i]])
        return res

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
