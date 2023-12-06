import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # calc distances
        # put points based on distances in max_heap
        # pop k elems from max_heap
        def calc_distance(p1, p2):
            return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** (1 / 2)

        distances = list(map(lambda p: calc_distance([0,0], p), points))
        min_heap = list(zip(distances, points))
        heapq.heapify(min_heap)

        closests = []
        for i in range(k):
            closests.append(heapq.heappop(min_heap)[1])
        
        return closests
    
    def kClosest2(self, points: list[list[int]], k: int) -> list[list[int]]:
        # stream heap
        heap = [] # min_heap

        for x, y in points:
            heapq.heappush(heap, (-((x * x) + (y * y)), (x, y)))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [list(p) for dist, p in heap]