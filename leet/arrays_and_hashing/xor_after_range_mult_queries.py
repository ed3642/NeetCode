# https://leetcode.com/problems/xor-after-range-multiplication-queries-i

from functools import reduce
import operator
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7

        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        
        return reduce(operator.xor, nums)