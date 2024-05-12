from functools import lru_cache

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        
        max_nums = max(nums)
        total_worth = [0 for _ in range(max_nums + 1)]
        dp = [0] * len(total_worth)

        for num in nums:
            total_worth[num] += num

        dp[0] = total_worth[0]
        dp[1] = max(total_worth[0], total_worth[1])

        for i in range(2, len(total_worth)):
            dp[i] = max(dp[i - 1], dp[i - 2] + total_worth[i])

        return dp[len(total_worth) - 1]