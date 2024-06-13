class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for curr_amount in range(amount + 1):
            for coin in coins:
                prev_amount = curr_amount - coin
                if prev_amount >= 0:
                    dp[curr_amount] = min(dp[prev_amount] + 1, dp[curr_amount])

        return dp[amount] if dp[amount] != float('inf') else -1