# https://leetcode.com/problems/find-champion-ii/
from collections import deque
from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        # Topological sort, must be 1 starting 0-degree node
        # notice we dont need to do the full sort just the set up

        in_degree = [0] * n

        for _from, _to in edges:
            in_degree[_to] += 1
        
        expected_winner = -1
        for node, degree in enumerate(in_degree):
            if degree == 0:
                if expected_winner != -1:
                    return -1
                else:
                    expected_winner = node
        
        return expected_winner 

    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        # Topological sort, must be 1 starting 0-degree node

        in_degree = [0] * n
        adj_list = [[] for _ in range(n)]

        for _from, _to in edges:
            in_degree[_to] += 1
            adj_list[_from].append(_to)
        
        q = deque()
        expected_winner = -1
        for node, degree in enumerate(in_degree):
            if degree == 0:
                q.append(node)
                if len(q) > 1:
                    return -1
                else:
                    expected_winner = node
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for nei in adj_list[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        q.append(nei)
        
        return expected_winner if len(q) == 0 else -1
