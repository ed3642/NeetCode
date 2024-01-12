import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        
        def calcCost(a, b):
            x1, y1 = a
            x2, y2 = b
            return abs(x2 - x1) + abs(y2 - y1)
        
        if not points or len(points) == 0:
            return 0
        
        heap = []
        n = len(points)
        visited = [False] * n
        total_cost = 0

        # generate edges from points[0] to all other points
        for j in range(1, n):
            heap.append((calcCost(points[0], points[j]), 0, j))
        
        heapq.heapify(heap)
        visited[0] = True

        edges_count = 0 # edges needed to form MST
        max_edges = n - 1

        while heap and edges_count < max_edges:
            cost, p1, p2 = heapq.heappop(heap)

            if not visited[p2]:
                total_cost += cost
                visited[p2] = True
                edges_count += 1
                print(edges_count, p1, p2)
                # generate all edges from p2 to all other non-visited points
                for j in range(n):
                    if not visited[j]:
                        heapq.heappush(heap, (calcCost(points[p2], points[j]), p2, j))
        
        return total_cost