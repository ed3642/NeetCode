from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # works but O(n^2) there are alot of optimizations to do
        # O(n) is possible
        
        n = len(prices)
        # dp[i][holding] = max profit at i and if were holding, cd or open 
        OPEN = 0
        HOLD = 1
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        for r in range(n - 1):
            for l in range(r):
                dp[r][HOLD] = max(dp[l][OPEN], dp[r][HOLD])
                dp[r][OPEN] = max(dp[l][HOLD] + prices[r] - prices[l], dp[r][OPEN])

        return max(dp[n - 1])