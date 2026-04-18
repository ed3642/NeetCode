# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        # [1,1,2,3,7,10]
        # [0,0,1,1,2]
        # [1,2,3,8,11,12]

        def is_valid(diff):
            i = 1
            pairs = 0
            while i < len(nums):
                if nums[i] - nums[i - 1] <= diff:
                    pairs += 1
                    if pairs >= p:
                        return True
                    i += 1
                i += 1
            return pairs >= p
        
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        
        return l

