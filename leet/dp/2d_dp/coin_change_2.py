# https://leetcode.com/problems/coin-change-ii/

from functools import lru_cache
from typing import List

class Solution:
    
    def change(self, amount: int, coins: List[int]) -> int:
        
        # ways to make amount 
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for val in range(1, amount + 1):
                if val-coin >= 0:
                    dp[val] += dp[val - coin]

        return dp[amount]

    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        ways = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            ways[i][0] = 1

        for i in range(n - 1, -1, -1):
            for curr_amount in range(1, amount + 1):
                if coins[i] <= curr_amount:
                    ways[i][curr_amount] = (
                        ways[i][curr_amount - coins[i]] +
                        ways[i + 1][curr_amount]
                    )
                else:
                    ways[i][curr_amount] = ways[i + 1][curr_amount]


        return ways[0][amount]

    def change(self, amount: int, coins: list[int]) -> int:
        
        @lru_cache(maxsize=None)
        def ways(i, this_amount):
            if this_amount < 0 or i >= len(coins):
                return 0
            if this_amount == 0:
                return 1
            
            return (
                ways(i, this_amount - coins[i]) + # use this coin, and stay on this index
                ways(i + 1, this_amount) # move onto the next coin
            )

        return ways(0, amount)
    