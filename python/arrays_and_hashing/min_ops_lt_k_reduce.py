# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        _set = set(nums)
        _min = min(_set)

        if k > _min:
            return -1

        res = len(_set) - 1
        if k < _min:
            res += 1
        return res