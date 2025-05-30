# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array

from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        count = 0

        for i in range(N - 1):
            for j in range(i + 1, N):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        
        return count