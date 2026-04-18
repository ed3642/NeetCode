# https://leetcode.com/problems/number-of-operations-to-make-network-connected

from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        def dfs(node):
            if visited[node]:
                return
            
            visited[node] = True

            for nei in adj_list[node]:
                dfs(nei)

        if len(connections) < n - 1:
            return -1

        adj_list = [[] for _ in range(n)]

        for _from, _to in connections:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)
        
        groups = 0
        visited = [False] * n

        for node in range(n):
            if not visited[node]:
                dfs(node)
                groups += 1

        return groups - 1