# https://leetcode.com/problems/path-existence-queries-in-a-graph-i

from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        # expansion on each num forms a reachable group since nums its sorted
        
        N = len(nums)
        res = [False] * len(queries)
        group = [0] * N

        for i in range(1, N):
            if nums[i]-nums[i-1] <= maxDiff:
                group[i] = group[i-1] # propagate same group
            else:
                group[i] = group[i-1]+1 # start next group
        
        for i, (f, t) in enumerate(queries):
            res[i] = group[f] == group[t]
        
        return res