# https://leetcode.com/problems/left-and-right-sum-differences

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        lsum = 0
        rsum = sum(nums)

        for i in range(len(nums)):
            curr_num = nums[i]
            rsum -= curr_num
            nums[i] = abs(lsum-rsum)
            lsum += curr_num
        
        return nums