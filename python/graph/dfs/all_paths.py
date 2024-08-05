class Solution:
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
