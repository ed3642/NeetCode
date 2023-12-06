import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        min_heap = list(map(lambda x: -x, stones))
        heapq.heapify(min_heap)

        while len(min_heap) > 1:
            y = heapq.heappop(min_heap) * -1 # last stone
            x = heapq.heappop(min_heap) * -1 # second last stone
            remaining_stone = y - x

            if remaining_stone:
                heapq.heappush(min_heap, -remaining_stone)
        
        return -min_heap[0] if min_heap else 0