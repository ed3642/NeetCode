class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # only buy if the derivative is positive
        # sell when der is neg
        if len(prices) == 1:
            return 0
        
        prices.append(-float('inf')) # stopper, always sell at the end
        n = len(prices)
        profit = 0
        buy_price = float('inf') # signify we dont hold anything
        i = 0
        while i < n - 1:
            while prices[i + 1] - prices[i] > 0: # increasing chain
                if buy_price == float('inf'): # only buy at the start
                    buy_price = prices[i]
                i += 1
            if buy_price != float('inf'): # price drops
                profit += prices[i] - buy_price
                buy_price = float('inf')
            i += 1
        
        return profit
    