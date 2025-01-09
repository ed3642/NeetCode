# https://leetcode.com/problems/target-sum
from functools import lru_cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # BT or DP?

        @lru_cache(maxsize=None)
        def ways(i, _sum):
            if i >= len(nums):
                return 1 if _sum == target else 0

            return ways(i + 1, _sum + nums[i]) + ways(i + 1, _sum - nums[i])

        return ways(0, 0)
    
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def num_ways(i, _sum):
            if i >= len(nums):
                if _sum == target:
                    return 1
                return 0

            return num_ways(i + 1, _sum + nums[i]) + num_ways(i + 1, _sum + (nums[i] * -1))
            
        return num_ways(0, 0)
    