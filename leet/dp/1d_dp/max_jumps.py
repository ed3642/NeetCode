# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index

from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        NINF = float('-inf')

        n = len(nums)
        # max steps to get to i
        dp = [NINF for _ in range(n + 1)]
        dp[n - 1] = 0

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if dp[j] == NINF: # skip is not yet reached
                    continue
                if -target <= nums[j] - nums[i] <= target:
                    dp[i] = max(dp[j] + 1, dp[i])

        return dp[0] if dp[0] != NINF else -1