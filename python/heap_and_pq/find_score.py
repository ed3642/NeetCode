# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements
import heapq
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        N = len(nums)
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        
        marked = [False] * N
        _sum = 0
        while heap:
            num, i = heapq.heappop(heap)
            if marked[i]:
                continue
            marked[i] = True
            if i > 0:
                marked[i - 1] = True
            if i < N - 1:
                marked[i + 1] = True
            
            _sum += num

        return _sum
