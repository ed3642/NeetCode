# https://leetcode.com/problems/count-elements-with-maximum-frequency

from typing import Counter, List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freqs = Counter(nums)
        total = 0
        max_f = -float('inf')

        for f in freqs.values():
            if f == max_f:
                total += f
            elif f > max_f:
                total = f
                max_f = f

        return total