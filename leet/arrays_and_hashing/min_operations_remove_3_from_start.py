# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct

from collections import Counter
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        N = len(nums)
        counts = Counter(nums)
        operations = 0
        last_i = 0

        for i in range(0, N - 2, 3):
            if counts[nums[i]] > 1 or counts[nums[i + 1]] > 1 or counts[nums[i + 2]] > 1:
                counts[nums[i]] -= 1
                counts[nums[i + 1]] -= 1
                counts[nums[i + 2]] -= 1
                operations += ((i - last_i) // 3) + 1
                last_i = i + 3

        # remaining counts
        if N % 3 != 0:
            i = N - 2
            if (i < N and counts[nums[i]] > 1) or (i + 1 < N and counts[nums[i + 1]] > 1):
                operations += ((i - last_i) // 3) + 1

        return operations