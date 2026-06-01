# https://leetcode.com/problems/coin-change

from functools import lru_cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort(reverse=True)

        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0
        
        for val in range(1, amount + 1):
            min_coins = INF
            for coin in coins:
                if val - coin >= 0:
                    min_coins = min(dp[val - coin], min_coins)
            dp[val] = min_coins + 1
        
        return dp[amount] if dp[amount] != INF else -1

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