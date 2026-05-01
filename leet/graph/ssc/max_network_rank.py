# https://leetcode.com/problems/maximal-network-rank
from typing import List

class Solution:
    # improvement from bottom solution is that this only checks the possible pair sets that have the optimal answer, the solution below this one checks every pair which is redundant.
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        g = [set() for _ in range(n)]
        in_deg = [0] * n

        for f, t in roads:
            g[f].add(t)
            g[t].add(f)
            in_deg[t] += 1
            in_deg[f] += 1
        
        sorted_node_deg = sorted(in_deg)
        best_deg = sorted_node_deg[-1]
        second_best_deg = sorted_node_deg[-2]

        best_deg_set = set()
        for node in range(n):
            if in_deg[node] == best_deg:
                best_deg_set.add(node)

        if len(best_deg_set) > 1:
            # can find optimal pair with just this set
            for node1 in best_deg_set:
                for node2 in best_deg_set:
                    if node1 != node2 and node2 not in g[node1]:
                        # no mutual road, best solution
                        return best_deg * 2
            # next best is when 2 of these highest rank nodes share 1 road
            return (best_deg * 2) - 1

        second_best_deg_set = set()
        for node in range(n):
            if in_deg[node] == second_best_deg:
                second_best_deg_set.add(node)
        
        for node1 in best_deg_set:
            for node2 in second_best_deg_set:
                if node2 not in g[node1]:
                    # no mutual road
                    return in_deg[node1] + in_deg[node2]
        # next best is sharing 1 road with the best_deg_node
        second_best_node = second_best_deg_set.pop()
        return best_deg + in_deg[second_best_node] - 1

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        degree = [0] * n
        max_degree = 0
        edges_set = set()

        for _from, _to in roads:
            edges_set.add((_from, _to))
            degree[_from] += 1
            degree[_to] += 1

        for node in range(n):
            for nei in range(n):
                if node != nei:
                    if (node, nei) in edges_set or (nei, node) in edges_set:
                        max_degree = max(degree[node] + degree[nei] - 1, max_degree)
                    else:
                        max_degree = max(degree[node] + degree[nei], max_degree)

        return max_degree
