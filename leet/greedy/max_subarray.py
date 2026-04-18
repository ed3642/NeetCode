# https://leetcode.com/problems/maximum-subarray
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # kadanes
        max_sum = -float('inf')
        _sum = 0
        for num in nums:
            _sum += num
            max_sum = max(_sum, max_sum)
            if _sum < 0:
                _sum = 0
        
        return max_sum
    
    def maxSubArray(self, nums: List[int]) -> int:
        # kadanes
        curr_max = -float('inf')
        global_max = -float('inf')

        for num in nums:
            curr_max = max(curr_max + num, num)
            global_max = max(curr_max, global_max)
        
        return global_max
    
    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer

        def max_sum(l, r):
            if l > r:
                return -float('inf')
            if l == r:
                return nums[l]
            
            m = (l + r) // 2
            
            return max(
                max_sum(l, m),
                max_sum(m + 1, r), 
                prefix_max_sum[m] + suffix_max_sum[m + 1]
            )

        N = len(nums)
        prefix_max_sum = nums.copy()
        suffix_max_sum = nums.copy()
        for i in range(1, N):
            prefix_max_sum[i] += max(0, prefix_max_sum[i - 1])
        for i in range(N - 2, -1, -1):
            suffix_max_sum[i] += max(0, suffix_max_sum[i + 1])
        
        return max_sum(0, N - 1)
    
