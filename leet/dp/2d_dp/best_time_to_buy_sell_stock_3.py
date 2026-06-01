# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # there is a way cleaner solution but this uses all the dp principles nicely
        # 1 transaction is buy and sell not just one, count it on the buy
        
        n = len(prices)
        NINF = float('-inf')
        OPEN = 0
        HOLD = 1
        max_transactions = 2
        # dp[t][transactions][holding] max unrealised profit at time t with transactions and holding state
        dp = [[[0, NINF] for _ in range(max_transactions + 1)] for _ in range(n)]
        dp[0][1][HOLD] = -prices[0]

        for t in range(1, n):
            for num_trans in range(max_transactions + 1):
                dp[t][num_trans][OPEN] = max(
                    dp[t-1][num_trans][HOLD] + prices[t],
                    dp[t-1][num_trans][OPEN]
                )
                if num_trans < max_transactions:
                    dp[t][num_trans + 1][HOLD] = max(dp[t-1][num_trans][OPEN] - prices[t], dp[t][num_trans + 1][HOLD]) # buy
                dp[t][num_trans][HOLD] = max(
                    dp[t-1][num_trans][HOLD],
                    dp[t][num_trans][HOLD]
                )

        return max(dp[n-1][0][OPEN], dp[n-1][1][OPEN], dp[n-1][2][OPEN])