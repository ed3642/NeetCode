class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        n = len(prices)
        l = 0
        r = 1

        while r < n:
            if prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        
        return max_profit
    
    def maxProfit2(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = 999999999

        for p in prices:
            min_price = min(p, min_price)
            profit = p - min_price
            max_profit = max(profit, max_profit)

        return max_profit
    
s = Solution()

nums = [7, 6, 4, 3, 1]

print(s.maxProfit(nums))