# https://leetcode.com/problems/find-missing-observations/description/
from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        def max_to_assign(target, missing_left):
            reserved = missing_left - 1 # save 1 for all the remaining slots
            available = target - reserved
            return min(available, 6) # take 6 or less


        m = len(rolls)
        N = n + m
        target = (mean * N) - sum(rolls)
        
        # check if there is enough space to find sol
        MAX_POSSIBLE = n * 6
        if MAX_POSSIBLE < target:
            return []
        MIN_POSSIBLE = n
        if MIN_POSSIBLE > target:
            return []

        # greedily assign values
        missing = [0] * n 
        for i in range(n):
            assigning = max_to_assign(target, n - i)
            missing[i] = assigning
            target -= assigning

        return missing
