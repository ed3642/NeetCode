# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph
from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # topological sort
        # add all ancestors of "node" since we should have recorded all of the ancestors before "node" since we topologically sorted

        def dfs(node, ancestors):
            if not node:
                return
            
            ancestors.append(node)

            for neighbor_node in adj_list[node]:
                dfs(neighbor_node)


        adj_list = [[] for _ in range(n)]
        rev_adj_list = [[] for _ in range(n)] # so we can see the parents of each node
        ancestors = [[] for _ in range(n)]
        indegree = [0] * n

        for _from, _to in edges:
            adj_list[_from].append(_to)
            rev_adj_list[_to].append(_from)
            indegree[_to] += 1
        
        # start with degree 0's
        queue = deque()
        for node, d in enumerate(indegree):
            if d == 0:
                queue.append(node)
        
        # topological sort
        while queue:
            node = queue.popleft()

            # append the ancestors, plus the ancestor itself
            ancestor_set = set()
            for ancestor_node in rev_adj_list[node]:
                ancestor_set.add(ancestor_node)
                for temp in ancestors[ancestor_node]:
                    ancestor_set.add(temp)
            ancestors[node] = sorted(ancestor_set)

            for neighbor_node in adj_list[node]:
                indegree[neighbor_node] -= 1
                if indegree[neighbor_node] == 0:
                    queue.append(neighbor_node)

        return ancestors
