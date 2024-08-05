from collections import defaultdict

class Solution:
    # https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
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
