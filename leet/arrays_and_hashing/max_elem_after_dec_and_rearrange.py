# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging

from typing import Counter, List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        f = Counter(arr)
        curr = 1
        sorted_nums = sorted(f)
        f[sorted_nums[0]] -= 1

        for num in sorted_nums:
            curr = min(f[num]+curr, num)
        
        return curr
