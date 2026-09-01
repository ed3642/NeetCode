# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        N = len(nums)
        s = nums[0] # Sum
        i = 1
        while i < N and nums[i] == nums[i-1]+1:
            s += nums[i]
            i += 1

        A = set(nums)

        while s in A:
            s += 1

        return s