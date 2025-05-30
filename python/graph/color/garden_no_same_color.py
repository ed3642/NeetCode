# https://leetcode.com/problems/flower-planting-with-no-adjacent/description/?envType=problem-list-v2&envId=2s0bp6s1
from collections import deque
from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # for this problem we have 4 colors and at max 3 edges
        # so we can greedily choose any color thats not already used to find a solution
        
        res = [0] * n
        adj_list = [[] for _ in range(n + 1)]

        for _from, _to in paths:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)
        
        q = deque([1])
        not_visited = set([node for node in range(1, n + 1)])

        while not_visited or q:
            if not q:
                q.append(not_visited.pop()) # make sure we visit all components
            node = q.popleft()
            open_colors = set([1, 2, 3, 4])

            for nei in adj_list[node]:
                if nei in not_visited:
                    not_visited.remove(nei)
                    q.append(nei)
                else:
                    open_colors.discard(res[nei - 1])

            # check available colors
            res[node - 1] = open_colors.pop()
        
        return res