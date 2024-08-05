import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)

        heap = []

        for num in counter:
            heapq.heappush(heap, (-counter[num], num))

        res = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)
        
        return res