# https://leetcode.com/problems/maximum-total-subarray-value-ii

from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ...
        # segment tree solution is correct but TLE, needed sparse table