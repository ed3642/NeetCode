from collections import defaultdict

class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        
        def dfs(node):
            visited.add(node)
            children_counts = []
            for nei in adj_list[node]:
                if nei not in visited:
                    children_counts.append(dfs(nei) + 1)

            # all same size or leaf
            if len(set(children_counts)) == 1 or len(children_counts) == 0:
                self.count += 1

            return sum(children_counts)
            
        adj_list = defaultdict(list)
        visited = set()

        for _from, _to in edges:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)
        
        self.count = 0

        dfs(0)

        return self.count