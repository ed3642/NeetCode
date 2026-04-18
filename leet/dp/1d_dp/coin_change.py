from functools import lru_cache


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
    
    def coinChange(self, coins: list[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def min_coins(this_amount):
            if this_amount < 0:
                return float('inf')
            if this_amount == 0:
                return 0
            
            best = float('inf')
            for coin in coins:
                if coin <= this_amount:
                    prev_amount = this_amount - coin
                    best = min(min_coins(prev_amount) + 1, best)
            
            return best
        
        res = min_coins(amount)
        return res if res != float('inf') else -1