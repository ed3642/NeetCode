# https://leetcode.com/problems/maximum-candies-allocated-to-k-children

from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def can_split(n):
            total_same_piles = 0
            for pile in candies:
                total_same_piles += pile // n
            return total_same_piles >= k

        total = sum(candies)
        if total < k:
            return 0
        if total == k:
            return 1
        
        l = 0
        r = max(candies) + 1 # +1 since maybe we can split into max(candies) but were finding the first that doesnt work, so we need to check the +1

        while l < r:
            m = (l + r) // 2
            if can_split(m):
                l = m + 1
            else:
                r = m
        
        return l - 1 # l is the first size we cant split into
