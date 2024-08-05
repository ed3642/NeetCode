from collections import defaultdict

class Solution:
    # recursive
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        def dfs(node):
            if visited[node]:
                return 
            visited[node] = True
            if node == destination:
                return True
            for v in adj[node]:
                if dfs(v):
                    return True
            return False

        adj = defaultdict(list)
        visited = [False] * n

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        return dfs(source)
    
    # iterative
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if [source, destination] in edges or [destination, source] in edges:
            # in the given test cases this is really efficient but not generally
            return True
        adj = defaultdict(list)
        visited = [False] * n
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        stack = [source]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            if node == destination:
                return True
            
            for v in adj[node]:
                stack.append(v)
        return False