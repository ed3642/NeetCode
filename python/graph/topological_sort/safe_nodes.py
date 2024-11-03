# https://leetcode.com/problems/find-eventual-safe-states
# NOTE: this can also be solved with topo sorting
from functools import lru_cache
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        @lru_cache(maxsize=None)
        def dfs(node):
            if node_state[node] != UNVISITED:
                return node_state[node] == SAFE

            node_state[node] = INSTACK

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            node_state[node] = SAFE
            return True

        N = len(graph)
        UNVISITED = 0
        INSTACK = 1
        SAFE = 2
        node_state = [UNVISITED] * N
        safe_nodes = []

        for node in range(N):
            if dfs(node):
                safe_nodes.append(node)
        
        return safe_nodes