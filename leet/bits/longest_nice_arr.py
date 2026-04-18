# https://leetcode.com/problems/longest-nice-subarray

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # record the occurences of 1
        # if nums[l] & nums[r] overlap then move l up

        # 01
        # 11
        # 3  000011
        # 8  001000
        # 48 110000
        
        curr = 0
        longest = 1
        l = 0

        for r, num in enumerate(nums):
            while l < r and curr & nums[r] != 0:
                curr ^= nums[l]
                l += 1

            curr ^= num
            longest = max(r - l + 1, longest)

        return longest
