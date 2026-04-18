# https://leetcode.com/problems/all-paths-from-source-to-target
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, path: list):

            if node == N - 1:
                paths.append(path.copy())

            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
            
        N = len(graph)
        paths = []
        dfs(0, [0])

        return paths
    
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def dfs(node, builder):
            if node == self.n - 1:
                paths.append(builder)
                return

            for n in graph[node]:
                dfs(n, builder + [n])
            
        self.n = len(graph)
        paths = []
        dfs(0, [0])
        return paths
