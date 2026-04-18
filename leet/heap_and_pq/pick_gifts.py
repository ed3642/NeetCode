# https://leetcode.com/problems/take-gifts-from-the-richest-pile
import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts = list(map(lambda x: -x, gifts))
        heapq.heapify(gifts)

        for _ in range(k):
            highest = -heapq.heappop(gifts)
            leaving = math.floor(math.sqrt(highest))
            heapq.heappush(gifts, -leaving)
        
        return -sum(gifts)
