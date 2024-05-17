from functools import lru_cache

class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, profit):

            pass
        
        self.max_profit = 0
        dp(0, 0)
        return self.max_profit
