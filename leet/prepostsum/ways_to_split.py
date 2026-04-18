# https://leetcode.com/problems/number-of-ways-to-split-array
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        N = len(nums)
        left = 0
        right = sum(nums)
        count = 0
        for i in range(N - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                count += 1
            
        return count

    def waysToSplitArray(self, nums: List[int]) -> int:
        
        def range_sum(l, r):
            left_sum = 0
            if l > 0:
                left_sum = pf_sum[l - 1]
            return pf_sum[r] - left_sum

        N = len(nums)
        pf_sum = nums
        for i in range(1, N):
            pf_sum[i] += pf_sum[i - 1]

        count = 0
        for i in range(N - 1):
            left = range_sum(0, i)
            right = range_sum(i + 1, N - 1)
            if left >= right:
                count += 1
        
        return count