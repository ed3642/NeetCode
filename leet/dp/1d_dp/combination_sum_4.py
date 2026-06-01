# https://leetcode.com/problems/combination-sum-iv

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # permutations of sum?

        n = target
        # dp[s] = ways to make sum s with the nums 
        dp = [0] * (n+1)
        dp[0] = 1

        for s in range(n + 1):
            for num in nums:
                next_s = s + num
                if next_s <= target:
                    dp[next_s] += dp[s]
        
        return dp[target]