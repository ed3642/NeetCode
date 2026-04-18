from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # edge list to adj list
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        queue = deque([source])
        visited = [False] * n
        visited[source] = True 
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        
        return False
