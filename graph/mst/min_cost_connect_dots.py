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
    # no heap
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        def cost(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)
        ds = UnionFind(n)

        # generate edges
        possible_edges = [] # cost, p1, p2
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                possible_edges.append((cost(points[i1], points[i2]), i1, i2))
        
        possible_edges.sort(reverse=True)

        min_connection_cost = 0
        max_edges = n - 1 # max edges in MST
        edges_count = 0

        while edges_count < max_edges and possible_edges:
            edge_cost, a, b = possible_edges.pop()
            if not ds.connected(a, b):
                ds.union(a, b)
                min_connection_cost += edge_cost
        
        return min_connection_cost
    
    # heap
    # if you want list sorted, its better to build it with a heap then sort as array
    # generally this is true in practice
    def minCostConnectPoints2(self, points: list[list[int]]) -> int:
        def cost(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)
        ds = UnionFind(n)

        # generate edges
        heap_edges = [] # cost, p1, p2
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                heap_edges.append((cost(points[i1], points[i2]), i1, i2))
        
        heapq.heapify(heap_edges)
        
        min_connection_cost = 0
        max_edges = n - 1 # max edges in MST
        edges_count = 0

        while edges_count < max_edges and heap_edges:
            edge_cost, a, b = heapq.heappop(heap_edges)
            if not ds.connected(a, b):
                ds.union(a, b)
                min_connection_cost += edge_cost
        
        return min_connection_cost




