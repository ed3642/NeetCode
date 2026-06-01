# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # same as best time to buy and sell stock but with just a flat fee
        # weird thing on this problem is they say fee per transaction but only apply it on one of the transactions, either buy or sell but not both.

        n = len(prices)
        NINF = float('-inf')
        OPEN = 0
        HOLD = 1
        # dp[t][state] = max unrealised profit at i and what state were on
        dp = [[0, NINF] for _ in range(n)]
        dp[0][HOLD] = -prices[0] - fee

        for t in range(1, n):
            dp[t][OPEN] = max(dp[t-1][HOLD] + prices[t], dp[t-1][OPEN])
            dp[t][HOLD] = max(dp[t-1][OPEN] - prices[t] - fee, dp[t-1][HOLD])
        
        return dp[n-1][OPEN]