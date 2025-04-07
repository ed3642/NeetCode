# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-is

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        max_i = nums[0]
        max_diff = 0
        max_score = 0
        
        for k in range(1, N):
            max_score = max(max_diff * nums[k], max_score)
            max_i = max(nums[k], max_i)
            max_diff = max(max_i - nums[k], max_diff)
        
        return max_score

    def maximumTripletValue2(self, nums: List[int]) -> int:
        
        max_val = 0
        N = len(nums)

        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    max_val = max((nums[i] - nums[j]) * nums[k], max_val)
        
        return max_val
    