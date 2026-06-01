# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discout

from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        min_cost = 0
        cost.sort()

        i = len(cost)-1
        while i >= 2:
            min_cost += cost[i]
            min_cost += cost[i-1] if i > 0 else 0
            i -= 3
        
        if i == 1:
            min_cost += cost[1]+cost[0]
        elif i == 0:
            min_cost += cost[0]

        return min_cost