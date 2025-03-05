# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii
import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heap = nums
        heapq.heapify(heap)
        operations = 0

        while heap[0] < k:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            new_num = min(x, y) * 2 + max(x, y)
            heapq.heappush(heap, new_num)
            operations += 1
        
        return operations
