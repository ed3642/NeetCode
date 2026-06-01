# https://leetcode.com/problems/minimum-cost-for-tickets

from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        INF = float('inf')
        n = 365
        # dp[d] = least cost to cover all days up to d
        travel_days = set(days)
        dp = [INF for _ in range(n + 1)]
        dp[0] = 0

        for d in range(1, 366):
            if d in travel_days:
                dp[d] = min(dp[d-1] + costs[0],
                            (dp[d-7] if d-7 > 0 else 0) + costs[1],
                            (dp[d-30] if d-30 > 0 else 0) + costs[2])
            else:
                dp[d] = min(dp[d-1], dp[d])
        
        return dp[days[-1]]