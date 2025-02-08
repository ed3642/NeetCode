from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        N = len(nums)

        max_sum = nums[0]
        _sum = nums[0]
        for i in range(1, N):
            if nums[i - 1] < nums[i]:
                _sum += nums[i]
                max_sum = max(_sum, max_sum)
            else:
                _sum = nums[i]
        
        return max_sum