# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i

from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        # 1 2 4 8 16
        # node 1 is the root by problem statement

        def dfs(node, d):
            nonlocal max_depth

            max_depth = max(d, max_depth)

            for nei in g[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei, d+1)
            

        n = len(edges)+1
        g = [[] for _ in range(n+1)]

        for f, t in edges:
            g[f].append(t)
            g[t].append(f)

        visited = [False] * (n+1)
        visited[1] = True
        max_depth = 0
        dfs(1, 0)

        return pow(2, (max_depth - 1), (10 ** 9 + 7))