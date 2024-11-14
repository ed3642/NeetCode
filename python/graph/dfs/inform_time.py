# https://leetcode.com/problems/time-needed-to-inform-all-employees
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        # get the longest path weight from head to a leaf

        def dfs(node):

            longest_time = 0
            for nei in adj_list[node]:
                longest_time = max(dfs(nei), longest_time)

            return longest_time + informTime[node]

        adj_list = [[] for _ in range(n)]

        for _to in range(n):
            _from  = manager[_to]
            if _from == -1:
                continue
            adj_list[_from].append(_to)
        
        return dfs(headID)
        