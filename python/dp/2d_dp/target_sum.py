from functools import lru_cache

class Solution:

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def num_ways(i, _sum):
            if i >= len(nums):
                if _sum == target:
                    return 1
                return 0

            return num_ways(i + 1, _sum + nums[i]) + num_ways(i + 1, _sum + (nums[i] * -1))
            
        return num_ways(0, 0)
    