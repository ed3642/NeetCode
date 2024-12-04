# https://leetcode.com/problems/maximal-network-rank
from typing import List

class Solution:
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
