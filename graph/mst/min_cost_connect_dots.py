import heapq

# Kruskals

class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

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
    
    def areConnected(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b

class Kruskals:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        
        def calcCost(a, b):
            x1, y1 = a
            x2, y2 = b
            return abs(x2 - x1) + abs(y2 - y1)

        n = len(points)
        ds = UnionFind(n)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((calcCost(points[i], points[j]), i, j))

        heapq.heapify(edges)
        max_edges = n - 1
        edges_count = 0
        total_cost = 0

        while edges and edges_count < max_edges:
            cost, p1, p2 = heapq.heappop(edges)

            if not ds.areConnected(p1, p2):
                ds.union(p1, p2)
                total_cost += cost
                edges_count += 1
        
        return total_cost

# Prims

class Prims:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        def calcCost(a, b):
            x1, y1 = a
            x2, y2 = b
            return abs(x2 - x1) + abs(y2 - y1)
        
        n = len(points)
        heap = []
        visited = [False] * n

        # edges from points[0]
        for i in range(1, n):
            heap.append((calcCost(points[0], points[i]), 0, i))

        heapq.heapify(heap)
        visited[0] = True
        max_edges = n - 1
        edges_count = 0
        total_cost = 0

        while heap and edges_count < max_edges:
            cost, p1, p2 = heapq.heappop(heap)

            if not visited[p2]:
                visited[p2] = True
                total_cost += cost
                edges_count += 1
                for i in range(1, n):
                    if not visited[i]:
                        heapq.heappush(heap, (calcCost(points[p2], points[i]), p2, i))
        
        return total_cost