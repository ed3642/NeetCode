# https://leetcode.com/problems/find-eventual-safe-states

from collections import deque
from functools import lru_cache
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        N = len(graph)
        reversed_g = [[] for _ in range(N)]
        in_degrees = [0] * N

        for node in range(N):
            for nei in graph[node]:
                reversed_g[nei].append(node)
                in_degrees[node] += 1
        
        q = []
        for node in range(N):
            if in_degrees[node] == 0:
                q.append(node)
        
        terminal_nodes = [] # topo sort doesnt need a queue
        while q:
            node = q.pop()
            terminal_nodes.append(node)

            for nei in reversed_g[node]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    q.append(nei)
        
        return sorted(terminal_nodes)
    
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