from functools import lru_cache
# https://leetcode.com/problems/coin-change-ii/
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        @lru_cache(maxsize=None)
        def ways(i, this_amount):
            if this_amount < 0 or i >= len(coins):
                return 0
            if this_amount == 0:
                return 1
            
            return (
                ways(i, this_amount - coins[i]) + # take this coin as much as we can
                ways(i + 1, this_amount) # move onto the next coin
            )
        
        return ways(0, amount)