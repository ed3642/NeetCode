# https://leetcode.com/problems/maximum-xor-for-each-query
from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        N = len(nums)
        cumulative = 0
        for num in nums:
            cumulative ^= num
        
        max_num = (2 ** maximumBit) - 1
        res = [0] * N
        for i in range(N - 1, 0, -1):
            best = cumulative ^ max_num
            res[N - 1 - i] = best
            cumulative ^= nums[i] # remove the last num each query
        best = cumulative ^ max_num
        res[-1] = best

        return res