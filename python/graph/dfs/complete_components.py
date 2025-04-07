# https://leetcode.com/problems/count-the-number-of-complete-components

from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node, group):
            if visited[node]:
                return
            
            visited[node] = True
            group.add(node)

            for nei in adj_list[node]:
                dfs(nei, group)
            return group
        
        def is_valid_group(group):
            for node in group:
                if len(adj_list[node]) != len(group) - 1:
                    return False
            return True
        
        # group them
        # each node in group size n should have n - 1 connections

        adj_list = [[] for _ in range(n)]
        for _from, _to in edges:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)

        connected_groups = 0
        visited = [False] * n

        for node in range(n):
            if not visited[node]:
                group = dfs(node, set())
                if is_valid_group(group):
                    connected_groups += 1
        
        return connected_groups

