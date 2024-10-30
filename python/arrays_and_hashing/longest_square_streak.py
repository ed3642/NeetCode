# https://leetcode.com/problems/longest-square-streak-in-an-array/
from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # [4,3,6,16,8,2]
        # [2,3,4,6,8,16]
        nums = sorted(set(nums))
        looking = {} # <next_num, len)
        best = -1
        for num in nums:
            if num not in looking:
                looking[num * num] = 1
            else:
                next_square = num * num
                looking[next_square] = looking[num] + 1
                best = max(looking[next_square], best)
        
        return best