# https://leetcode.com/problems/sum-of-all-subset-xor-totals

from functools import reduce
import operator
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def bt(start, builder: int):
            nonlocal total
            total += builder

            for i in range(start, len(nums)):
                builder ^= nums[i]
                bt(i + 1, builder)
                builder ^= nums[i]
        
        total = 0
        bt(0, 0)

        return total

    def subsetXORSum(self, nums: List[int]) -> int:
        
        def bt(start, builder: list):
            if builder:
                subsets.append(builder.copy())

            for i in range(start, len(nums)):
                builder.append(nums[i])
                bt(i + 1, builder)
                builder.pop()
        
        subsets = []
        bt(0, [])

        total = 0
        for arr in subsets:
            total += reduce(operator.xor, arr)

        return total