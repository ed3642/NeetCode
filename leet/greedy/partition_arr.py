# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k

from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        # [1,2,3,5,6]

        n = len(nums)
        nums.sort()
        parts = 0

        i = 0
        while i < n:
            j = i
            while j < n and nums[j] - nums[i] <= k:
                j += 1
            i = j
            parts += 1
        
        return parts