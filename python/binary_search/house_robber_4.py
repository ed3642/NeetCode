# https://leetcode.com/problems/house-robber-iv

from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        # [0,1,2,3,5,9]
        # can greedily choose the next lower val we see

        def is_possible(cap_i):
            val = sorted_nums[cap_i]
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= val:
                    count += 1
                    if count == k:
                        return True
                    i += 2
                else:
                    i += 1
            return False
        
        if k == 1:
            return min(nums)
        
        sorted_nums = sorted(nums)

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if is_possible(m):
                r = m
            else:
                l = m + 1
        
        return sorted_nums[l]
