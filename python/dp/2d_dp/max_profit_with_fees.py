from functools import lru_cache

class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)

        @lru_cache(maxsize=None)
        def dp(i: int, hold: int) -> int:
            if i == n:
                return 0
            
            if hold:
                return max(
                    dp(i + 1, 0) + prices[i] - fee, # sell
                    dp(i + 1, 1)) # keep holding
            else:
                return max(
                    dp(i + 1, 0), # still dont buy
                    dp(i + 1, 1) + prices[i]) # buy

        return dp(0, 0)
    
    # iterative solution
    def maxProfit2(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0] * n, [0] * n
        
        # In order to hold a stock on day 0, we have no other choice but to buy it for prices[0].
        hold[0] = -prices[0]
        
        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
        
        return free[-1]