# https://leetcode.com/problems/maximum-average-pass-ratio
import heapq
from typing import List

class RatioItem:
    def __init__(self, top, bot):
        self.top = top
        self.bot = bot
        self.ratio = top / bot
        self.potential_change = ((top + 1) / (bot + 1)) - top / bot

    def __lt__(self, other):
        return self.potential_change > other.potential_change # prio bigger change

class Solution:
    # using tuple, 950 ms. tuple is way faster than making an object
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        N = len(classes)
        _sum = 0
        heap = []
        for top, bot in classes:
            if top == bot:
                _sum += 1
            else:
                heapq.heappush(heap, (-(((top + 1) / (bot + 1)) - top / bot), top, bot))

        if not heap: # no improvement to be done
            return _sum / N

        for _ in range(extraStudents):
            _, top, bot = heapq.heappop(heap)
            top += 1
            bot += 1
            heapq.heappush(heap, (-(((top + 1) / (bot + 1)) - top / bot), top, bot))
        
        for _, top, bot in heap:
            _sum += top / bot

        return _sum / N
    
    # using object, 1900ms
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        N = len(classes)
        _sum = 0
        heap = []
        for top, bot in classes:
            if top == bot:
                _sum += 1
            else:
                heapq.heappush(heap, RatioItem(top, bot))

        if not heap: # no improvement to be done
            return _sum / N

        for _ in range(extraStudents):
            ratio_item = heapq.heappop(heap)
            top = ratio_item.top
            bot = ratio_item.bot
            heapq.heappush(heap, RatioItem(top + 1, bot + 1))
        
        for item in heap:
            _sum += item.ratio

        return _sum / N
