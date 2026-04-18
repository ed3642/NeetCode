from functools import lru_cache
from enum import Enum

class State(Enum):
    CAN_BUY = 1
    CAN_SELL = 2
    # MUST_WAIT = 3, since we must wait 1 day each time we can just skip the next day when we buy and not have to worry about this state

class Solution:

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
