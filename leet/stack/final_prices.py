# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
from typing import List

class Solution:
    # O(n)
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        # [0,1,2,3,4]
        # [8,4,6,2,3]
        # [(1,4),(2,6)]
        # [4,]
        
        N = len(prices)
        stack = []

        for i in range(N):
            while stack and prices[stack[-1]] >= prices[i]:
                discounted_i = stack.pop()
                prices[discounted_i] -= prices[i]
            stack.append(i)
        
        return prices

    # O(n ^ 2)
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        N = len(prices)

        for i in range(N):
            price = prices[i]
            for j in range(i + 1, N):
                if prices[j] <= price:
                    prices[i] = price - prices[j]
                    break
        
        return prices
    