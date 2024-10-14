# https://leetcode.com/problems/maximal-score-after-applying-k-operations/
import math
from typing import List
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        heap = nums
        heap = list(map(lambda x: -x, heap))
        heapq.heapify(heap)
        score = 0

        for _ in range(k):
            best = -heapq.heappop(heap)
            score += best
            processed = math.ceil(best / 3)
            heapq.heappush(heap, -processed)
        
        return score