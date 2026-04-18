# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        _max = -float('inf')
        _min = float('inf')

        _sum = 0
        for num in nums:
            _sum += num
            if _sum < 0:
                _sum = 0
            _max = max(_sum, _max)
        
        _sum = 0
        for num in nums:
            _sum += num
            if _sum > 0:
                _sum = 0
            _min = min(_sum, _min)

        return max(abs(_min), _max)