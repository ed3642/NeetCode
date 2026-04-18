import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif heap[0] < num:
                heapq.heapreplace(heap, num)
        
        return heap[0]