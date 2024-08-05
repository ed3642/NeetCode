import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        
        while len(stones) > 1:
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)
            
            if heaviest != second_heaviest:
                heaviest -= second_heaviest
                heapq.heappush(stones, -heaviest)
        
        return -stones[0] if stones else 0