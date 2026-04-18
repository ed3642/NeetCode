import heapq

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
    
    def connected(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        def calcCost(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x2 - x1) + abs(y2 - y1)

        n = len(points)
        ds = UnionFind(n)
        total_cost = 0

        # generate edge combinations
        edges_heap = []
        for p1 in range(n):
            for p2 in range(p1 + 1, n):
                edges_heap.append([calcCost(points[p1], points[p2]), p1, p2])
        
        heapq.heapify(edges_heap)

        # get MST
        max_edges = n - 1
        edges_count = 0

        while edges_heap and edges_count < max_edges:
            cost, p1, p2 = heapq.heappop(edges_heap)
            if not ds.connected(p1, p2):
                ds.union(p1, p2)
                total_cost += cost
                edges_count += 1
        
        return total_cost