from functools import lru_cache
from enum import Enum
from typing import List

class State(Enum):
    CAN_BUY = 1
    CAN_SELL = 2
    # MUST_WAIT = 3, since we must wait 1 day each time we can just skip the next day when we buy and not have to worry about this state

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # can also not max states with self if we do the solution below
        # but this is more general
        
        n = len(prices)
        NINF = float('-inf')
        OPEN = 0
        HOLD = 1
        dp = [[0, NINF] for _ in range(n)] # starts all HOLD states with NINF
        dp[0][HOLD] = -prices[0]

        for i in range(1, n):
            # sell or keep open
            dp[i][OPEN] = max(dp[i-1][HOLD] + prices[i], dp[i-1][OPEN], dp[i][OPEN]) 

            # buy or keep holding
            last_valid_open = i-2 if i > 2 else 0
            dp[i][HOLD] = max(dp[last_valid_open][OPEN] - prices[i], dp[i-1][HOLD], dp[i][HOLD]) 

        return dp[n-1][OPEN]

    # O(n)
    def maxProfit(self, prices: List[int]) -> int:
        # interesting insight is that for this state machine you dont max states with themselves as that leads to invalid states. 
        # It can be like buying a stock for free.
        # can also make it so you max with self if you initialize all HOLD states with NINF
        
        n = len(prices)
        # dp[i][state] = max profit realized at i and if were holding or open
        OPEN = 0
        HOLD = 1
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][HOLD] = -prices[0]

        for i in range(1, n):
            # sell or keep open
            dp[i][OPEN] = max(dp[i-1][HOLD] + prices[i], dp[i-1][OPEN]) 

            # buy or keep holding
            last_valid_open = i-2 if i > 2 else 0
            dp[i][HOLD] = max(dp[last_valid_open][OPEN] - prices[i], dp[i-1][HOLD]) 

        return dp[n-1][OPEN]

    def maxProfit(self, prices: List[int]) -> int:
        # works but O(n^2) there are alot of optimizations to do
        # O(n) is possible
        
        n = len(prices)
        # dp[i][holding] = max profit at i and if were holding, cd or open 
        OPEN = 0
        HOLD = 1
        CD = 2
        dp = [[0 for _ in range(3)] for _ in range(n)]

        for r in range(n):
            for l in range(r):
                dp[r][HOLD] = max(dp[l][OPEN], dp[r][HOLD])
                dp[r][OPEN] = max(dp[l][CD], dp[r][OPEN])
                dp[r][CD] = max(dp[l][HOLD] + prices[r] - prices[l], dp[r][CD])

        return max(dp[n - 1])

    def maxProfit(self, prices: list[int]) -> int:
        # some pruning implemented
        
        @lru_cache(maxsize=None)
        def max_profit(i, state):
            
            if i >= len(prices) - 1:
                if state == State.CAN_SELL: # sell on last day
                    return prices[i]
                return 0

            if state == State.CAN_BUY:
                # if the price is dropping, buy at the next bottom peak
                if prices[i] > prices[i + 1]:
                    npb = i + 1 # Next Peak Bottom
                    while npb + 1 < len(prices) - 1 and prices[npb] > prices[npb + 1]:
                        npb += 1
                    return max_profit(npb, State.CAN_BUY)
                # if there is no future day with a higher price, wait to buy
                if prices[i] > best_future_price[i + 1]:
                    npd = i + 1 # Next Profitable Day
                    while npd + 1 < len(prices) - 1 and prices[npd] > best_future_price[npd + 1]:
                        npd += 1
                    return max_profit(npd, State.CAN_BUY)
                return max(
                    max_profit(i + 1, State.CAN_SELL) - prices[i], # buy
                    max_profit(i + 1, State.CAN_BUY) # do nothing
                )
            elif state == State.CAN_SELL:
                return max(
                    # +2 when selling since the 1 day cooldown after selling
                    max_profit(i + 2, State.CAN_BUY) + prices[i], # sell
                    max_profit(i + 1, State.CAN_SELL) # do nothing
                )

            return -float('inf') # this should never happen
        
        best_future_price = [0] * len(prices) # mono_inc from right
        best_future_price[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            best_future_price[i] = max(prices[i], best_future_price[i + 1])
    
        return max_profit(0, State.CAN_BUY)
