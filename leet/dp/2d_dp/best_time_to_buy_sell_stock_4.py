from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # solution can be a lot cleaner
        n = len(prices)
        NINF = float('-inf')
        OPEN = 0
        HOLD = 1
        max_transactions = k
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

        best = NINF
        for i in range(max_transactions + 1):
            best = max(dp[n-1][i][OPEN], best)
        return best