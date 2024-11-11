# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        # its a tree.
        
        def dfs(node):
            nonlocal flips 

            visited[node] = True

            for nei, type in adj_list[node]:
                if not visited[nei]:
                    if type == ORIGINAL:
                        flips += 1
                    dfs(nei)

        ORIGINAL = 0
        REVERSED = 1
        adj_list = [[] for _ in range(n)]
        for _from, _to in connections:
            adj_list[_from].append((_to, ORIGINAL))
            adj_list[_to].append((_from, REVERSED))
        
        visited = [False] * n
        flips = 0
        
        dfs(0)

        return flips

    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # tree structure
        # all cities are connected by 1 or 2 single direction edge
        # double connect each pair and label the edges that we didnt need to fabricate
        
        def dfs(node):
            visited.add(node)

            for neighbor_node, label in adj_list[node]:
                if neighbor_node not in visited:
                    if label == 1:
                        self.count += 1
                    dfs(neighbor_node)

        adj_list = defaultdict(list)
        visited = set()
        self.count = 0

        for _from, to in connections:
            adj_list[_from].append((to, 1)) # real connection
            adj_list[to].append((_from, 0)) # fabricated connection

        dfs(0)
        return self.count
