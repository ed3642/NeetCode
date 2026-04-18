# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        # bisect left
        N = len(nums)
        l = 0
        r = N
        while l < r:
            m = (l + r) // 2
            if nums[m] < 0:
                l = m + 1
            else:
                r = m
        
        first_non_neg = l
        num_non_neg = N - first_non_neg # including 0s
        num_negative = N - num_non_neg

        # bisect right
        l = 0
        r = N
        while l < r:
            m = (l + r) // 2
            if nums[m] <= 0:
                l = m + 1
            else:
                r = m
        
        first_positive = l
        num_positive = N - first_positive

        return max(num_negative, num_positive)