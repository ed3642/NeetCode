# https://leetcode.com/problems/partition-equal-subset-sum

from functools import lru_cache
from typing import List

class Solution:

    def canPartition(self, nums: List[int]) -> bool:

        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        
        half = _sum // 2
        can_split = [False] * (half + 1)
        can_split[0] = True

        for num in nums:
            for curr_sum in range(half, num - 1, -1):
                if can_split[half]:
                    return True
                can_split[curr_sum] = can_split[curr_sum] or can_split[curr_sum - num]

        return can_split[half]

    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(maxsize=None)
        def can_split(i, rem):
            if i >= len(nums) or rem < 0:
                return False
            if rem == 0:
                return True

            return can_split(i + 1, rem - nums[i]) or can_split(i + 1, rem)

        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        
        nums.sort(reverse=True)

        return can_split(0, _sum // 2)