class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)] # m x m

        for i in range(m + 1):
            for j in range(m - i + 1):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + nums[i - 1] * multipliers[i + j - 1])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + nums[n - j] * multipliers[i + j - 1])
        
        max_res = 0
        for i in range(m + 1):
            max_res = max(max_res, dp[i][m - i])

        return max_res