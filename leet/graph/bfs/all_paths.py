from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        queue = deque([[0]])
        paths = []
        n = len(graph)

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == n - 1:
                paths.append(path)

            for neighbor in graph[node]:
                queue.append(path + [neighbor])

        return paths