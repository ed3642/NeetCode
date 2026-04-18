# https://leetcode.com/problems/count-the-number-of-fair-pairs/

import bisect
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        # [0,1,4,4,5,7]

        N = len(nums)
        nums.sort()
        count = 0

        for i in range(N):
            # find smallest and largest nums to match with nums[i] with bs
            # only search indexes after i
            smallest_i = bisect.bisect_left(nums, lower - nums[i], i + 1)
            largest_i = bisect.bisect_right(nums, upper - nums[i], i + 1) - 1
            if smallest_i <= largest_i:
                count += largest_i - smallest_i + 1
            
        return count
            