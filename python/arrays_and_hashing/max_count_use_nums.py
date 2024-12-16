# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i
from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        # greedily choose the smallest number available
        banned = set(banned)
        _sum = 0
        count = 0
        for num in range(1, n + 1):
            if num in banned:
                continue
            _sum += num
            if _sum > maxSum:
                return count
            count += 1

        return count