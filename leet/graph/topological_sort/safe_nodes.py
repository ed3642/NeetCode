# https://leetcode.com/problems/find-eventual-safe-states

from collections import defaultdict, deque
from functools import lru_cache
from typing import List

class Solution:
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # reverse edges
        n = len(graph)
        al = [[] for _ in range(n)]
        in_deg = [0] * n
        for f in range(n):
            for t in graph[f]:
                al[t].append(f)
                in_deg[f] += 1
        
        res = []
        q = deque()
        for node in range(n):
            if in_deg[node] == 0:
                q.append(node)
                res.append(node)
        
        while q:
            node = q.popleft()
            
            for nei in al[node]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    res.append(nei)
                    q.append(nei)
        
        return sorted(res)
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # good example of recursion. says if all neis are safe -> this node is safe
        
        def is_safe(node):
            if node_state[node] == SAFE:
                return True
            elif node_state[node] == VISITED:
                return False

            node_state[node] = VISITED
            
            for nei in graph[node]:
                if not is_safe(nei):
                    return False
            
            node_state[node] = SAFE
            return True
        
        n = len(graph)
        res = []
        UNVISITED = 0
        VISITED = 1
        SAFE = 2
        node_state = [UNVISITED] * n

        for node in range(n):
            if is_safe(node):
                res.append(node)
        
        return res

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