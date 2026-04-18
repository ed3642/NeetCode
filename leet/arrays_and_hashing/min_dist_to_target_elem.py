# https://leetcode.com/problems/minimum-distance-to-the-target-element

from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        n = len(nums)
        min_dist = float('inf')

        for i in range(start, n):
            if nums[i] == target:
                min_dist = i - start
                break
        for i in range(start - 1, -1, -1):
            if nums[i] == target:
                min_dist = min(start - i, min_dist)
                break
        
        return min_dist