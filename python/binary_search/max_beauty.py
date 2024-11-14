# https://leetcode.com/problems/most-beautiful-item-for-each-query
import bisect
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        N = len(items)
        items.sort(key=lambda x: x[0])

        max_beauty_to_left = [0] * N
        max_beauty_to_left[0] = items[0][1]
        for i in range(1, N):
            max_beauty_to_left[i] = max(items[i][1], max_beauty_to_left[i - 1])
        
        res = [0] * len(queries)
        for i, price in enumerate(queries):
            price_index = bisect.bisect_right(items, price, key=lambda x: x[0]) - 1 # -1 since we  want lt or eq to the price were searching
            if price_index == -1: 
                res[i] = 0
            else:
                res[i] = max_beauty_to_left[price_index]

        return res
