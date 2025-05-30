# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii

from collections import deque
from typing import List

class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # each tree is split into 2 groups, evens and odds
        # just see which is best group to take for tree 2
        # and see which group each node in tree 1 belongs to

        def find_evens(node, adj_list, num_nodes):
            q = deque([node])
            visited = [False] * num_nodes
            visited[node] = True
            parity = 1
            evens = set([node])

            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    for nei in adj_list[node]:
                        if not visited[nei]:
                            if parity == 0:
                                evens.add(nei)
                            visited[nei] = True
                            q.append(nei)
                parity = (parity + 1) % 2
            return evens
        
        # find node with best score in tree2
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        adj_list_1 = [[] for _ in range(n1)]
        adj_list_2 = [[] for _ in range(n2)]

        for _from, _to in edges1:
            adj_list_1[_from].append(_to)
            adj_list_1[_to].append(_from)
        for _from, _to in edges2:
            adj_list_2[_from].append(_to)
            adj_list_2[_to].append(_from)

        # tree will have 2 possible reaches for each node
        # just find the two options and pick the bigger one
        best_tree_2 = 0
        evens = find_evens(0, adj_list_2, n2)
        num_evens = len(evens)
        num_odds = n2 - num_evens
        best_tree_2 = max(num_evens, num_odds)

        # see reach of each node in tree 1
        res = [best_tree_2] * n1

        evens = find_evens(0, adj_list_1, n1)
        num_evens = len(evens)
        num_odds = n1 - num_evens

        for node in range(n1):
            res[node] += num_evens if node in evens else num_odds

        return res
    