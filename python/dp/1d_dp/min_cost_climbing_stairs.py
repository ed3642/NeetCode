# https://leetcode.com/problems/min-cost-climbing-stairs

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        N = len(cost)
        cost.append(0) # to reach this

        for i in range(2, N + 1):
            cost[i] += min(cost[i - 2], cost[i - 1])

        return cost[N]
    
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = cost

        for i in range(n - 3, -1, -1):
            dp[i] += min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])

    def minCostClimbingStairs2(self, cost: list[int]) -> int:
        n = len(cost)
        b = cost[n - 1]
        a = cost[n - 2]

        for i in range(n - 3, -1, -1):
            a, b = cost[i] + min(a, b), a
        
        return min(a, b)